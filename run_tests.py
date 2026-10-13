#!/usr/bin/env python3
"""Phase 4 — Test runner for skills. Safe mode: no external API calls."""
import os, sys, re, ast, subprocess, importlib.util, json, shutil

BASE = os.environ.get("BASE", "/data/data/com.termux/files/home/hermes-repos")
PRIORITY = ["delta-trading-skill","algotest-backtester-mcp","document-tools-skill",
            "github-skill","youtube-agent-skill","instagram-agent-skill",
            "research-skill","creative-design-skill"]

results = {"syntax_ok":0,"syntax_fail":0,"syntax_errors":[],
           "frontmatter_ok":0,"frontmatter_fail":0,"frontmatter_errors":[],
           "link_ok":0,"link_fail":0,"link_errors":[],
           "secret_found":0,"secret_examples":[],
           "dangerous_cmds":0,"dangerous_examples":[],
           "scripts_tested":0,"scripts_failed":0,"script_errors":[]}

# 1. Python syntax check all .py
print("=== 1. Python syntax check ===")
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in {".git","node_modules",".venv","__pycache__"}]
    for f in files:
        if not f.endswith(".py"): continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, BASE)
        try:
            ast.parse(open(fp, errors="replace").read())
            results["syntax_ok"] += 1
        except SyntaxError as e:
            results["syntax_fail"] += 1
            results["syntax_errors"].append({"file": rel, "line": e.lineno, "err": str(e)})
            print(f"  FAIL {rel}:{e.lineno}: {e}")
print(f"  OK: {results['syntax_ok']}, FAIL: {results['syntax_fail']}")

# 2. YAML frontmatter validation
print("\n=== 2. SKILL.md frontmatter ===")
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in {".git","node_modules"}]
    for f in files:
        if f != "SKILL.md": continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, BASE)
        content = open(fp, errors="replace").read()
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            results["frontmatter_fail"] += 1
            results["frontmatter_errors"].append({"file": rel, "err": "no frontmatter"})
            continue
        # Simple YAML parse (avoid pyyaml dep)
        try:
            fm_lines = m.group(1).strip().split("\n")
            parsed = {}
            for line in fm_lines:
                if ":" in line and not line.startswith(" "):
                    k, v = line.split(":", 1)
                    parsed[k.strip()] = v.strip().strip('"')
            if "name" not in parsed or "description" not in parsed:
                results["frontmatter_fail"] += 1
                results["frontmatter_errors"].append({"file": rel, "err": f"missing name/desc, got {list(parsed.keys())}"})
                continue
            results["frontmatter_ok"] += 1
        except Exception as e:
            results["frontmatter_fail"] += 1
            results["frontmatter_errors"].append({"file": rel, "err": str(e)})
print(f"  OK: {results['frontmatter_ok']}, FAIL: {results['frontmatter_fail']}")

# 3. Markdown local link check
print("\n=== 3. Markdown link check ===")
link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in {".git","node_modules"}]
    for f in files:
        if not f.endswith(".md"): continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, BASE)
        content = open(fp, errors="replace").read()
        for text, link in link_re.findall(content):
            if link.startswith(("http","https","mailto","#")): continue
            lp = link.split("#")[0]
            if not lp: continue
            # Skip template placeholders
            if "<" in lp or lp.startswith("~"): continue
            resolved = os.path.normpath(os.path.join(root, lp))
            if not os.path.exists(resolved):
                results["link_fail"] += 1
                results["link_errors"].append({"file": rel, "link": link, "resolved": resolved})
            else:
                results["link_ok"] += 1
print(f"  OK: {results['link_ok']}, FAIL: {results['link_fail']}")

# 4. Secret scanning (regex patterns)
print("\n=== 4. Secret scan ===")
SECRET_PATTERNS = {
    "aws_akid": r"AKIA[0-9A-Z]{16}",
    "github_token": r"ghp_[A-Za-z0-9_]{36}",
    "github_pat": r"github_pat_[A-Za-z0-9_]{22,}",
    "private_key": r"-----BEGIN (RSA|OPENSSH|EC|DSA|PGP) PRIVATE KEY-----",
    "telegram_bot": r"\b[0-9]{8,10}:[A-Za-z0-9_-]{35}\b",
    "slack_token": r"xox[baprs]-[A-Za-z0-9-]{10,}-[A-Za-z0-9-]{20,}",
    "google_api": r"AIza[0-9A-Za-z\-_]{35}",
    "stripe_live": r"sk_live_[0-9a-zA-Z]{24}",
}
EXAMPLE_KEYWORDS = ["example","sample","your_key","your_token","dummy","placeholder","fake",
                    "test_","xxx","your-api","not a screenshot","your_secret","your_key_here",
                    "not your","redacted"]

for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in {".git","node_modules"}]
    for f in files:
        if not f.endswith((".md",".py",".sh",".js",".json",".yaml",".yml")): continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, BASE)
        content = open(fp, errors="replace").read()
        for pname, pat in SECRET_PATTERNS.items():
            for m in re.finditer(pat, content):
                line_no = content[:m.start()].count("\n") + 1
                line = content.split("\n")[line_no-1]
                is_example = any(k in line.lower() for k in EXAMPLE_KEYWORDS)
                results["secret_found"] += 1
                results["secret_examples"].append({
                    "file": rel, "line": line_no, "type": pname,
                    "context": line[:100], "example": is_example
                })
                if not is_example:
                    print(f"  WARN {rel}:{line_no} [{pname}]: {line[:80]}")
print(f"  Total matches: {results['secret_found']}")

# 5. Dangerous commands (informational)
print("\n=== 5. Dangerous command review ===")
DANGEROUS = {
    "curl_pipe_bash": r"curl\s+[^\n|]{0,200}\|\s*(sudo\s+)?(bash|sh)",
    "wget_pipe_sh": r"wget\s+[^\n|]{0,200}\|\s*(sudo\s+)?sh",
    "chmod_777": r"chmod\s+777",
    "eval_string": r"\beval\s+\"",
    "shell_true": r"shell\s*=\s*True",
    "rm_rf_root": r"rm\s+-rf\s+(/|~/Hermes|~/.hermes)",
    "os_system": r"os\.system\(",
}
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in {".git","node_modules"}]
    for f in files:
        if not f.endswith((".md",".py",".sh",".js")): continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, BASE)
        content = open(fp, errors="replace").read()
        for pname, pat in DANGEROUS.items():
            for m in re.finditer(pat, content):
                line_no = content[:m.start()].count("\n") + 1
                line = content.split("\n")[line_no-1]
                results["dangerous_cmds"] += 1
                results["dangerous_examples"].append({
                    "file": rel, "line": line_no, "type": pname, "context": line[:120]
                })
print(f"  Total matches: {results['dangerous_cmds']}")

# Save results
with open(os.path.join(BASE, "PHASE4_TESTS.json"), "w") as f:
    json.dump(results, f, indent=2, default=str)

# Summary
print("\n=== SUMMARY ===")
print(f"Python syntax:    {results['syntax_ok']} ok / {results['syntax_fail']} fail")
print(f"Frontmatter:      {results['frontmatter_ok']} ok / {results['frontmatter_fail']} fail")
print(f"Markdown links:   {results['link_ok']} ok / {results['link_fail']} fail")
print(f"Secret matches:   {results['secret_found']}")
print(f"Dangerous cmds:   {results['dangerous_cmds']}")
print(f"\nSaved: PHASE4_TESTS.json")
