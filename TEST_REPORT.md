# Test Report

**Date:** 2026-10-13
**Source of truth:** Actual test execution output, not claims.

---

## Summary

| Check | Passed | Failed | Skipped | Type |
|-------|--------|--------|---------|------|
| Python syntax (81 scripts) | 81 | 0 | 0 | static (ast.parse) |
| SKILL.md YAML frontmatter (118) | 118 | 0 | 0 | static (regex) |
| Priority unit tests (8 repos) | 73 | 0 | 0 | runtime (mocks) |
| Pre-existing docx/pdf/pptx/xlsx tests (4) | 0 | 4 | 0 | runtime (missing deps) |
| Secret scan | 0 real | 2 examples | 0 | static (regex) |
| Dangerous commands | 46 documented | 0 real | 0 | static (regex) |

---

## Tests Executed — Priority Suite (73 tests, all pass)

**Command per repo:**
```bash
cd ~/hermes-repos/<repo>
python3 -m unittest discover -s tests -v
```

| # | Repository | Tests | Pass | Fail | Type |
|---|-----------|-------|------|------|------|
| 1 | delta-trading-skill | 10 | 10 | 0 | runtime (mocks) |
| 2 | algotest-backtester-mcp | 9 | 9 | 0 | runtime (mocks) |
| 3 | document-tools-skill | 9 | 9 | 0 | runtime (mocks) |
| 4 | github-skill | 9 | 9 | 0 | runtime (mocks) |
| 5 | youtube-agent-skill | 9 | 9 | 0 | runtime (mocks) |
| 6 | instagram-agent-skill | 9 | 9 | 0 | runtime (mocks) |
| 7 | research-skill | 9 | 9 | 0 | runtime (mocks) |
| 8 | creative-design-skill | 9 | 9 | 0 | runtime (mocks) |
| **Total** | **8 repos** | **73** | **73** | **0** | **all mock-based** |

**All 73 tests use `unittest` with mocks only — no live APIs, no real credentials, no side effects.**

### Test Categories per Priority Repo

- Happy path (mock result)
- Invalid input rejection
- Missing credentials
- Timeout handling
- Dry-run / mock mode (no side effects)
- Placeholder key rejection (`your_key`, `ghp_xxxxxx`, `sk_live_xxxxxx`)
- Copy-paste usage example (no real keys)
- Error handling (malformed config / API errors)
- Trading-specific: invalid symbols, invalid prices, duplicate orders, testnet default

### Safety Guarantees Verified

1. **No real API keys** — all tests run with placeholders removed from env
2. **No live orders** — all trading tests use `dry_run=True` default
3. **No side effects** — dry-run tests verify no files/orders created
4. **Placeholder keys rejected** — `your_key`, `ghp_xxxxxx`, `sk_live_xxxxxx` all detected
5. **Timeout handling** — `TimeoutError` raised, not silent failure
6. **Testnet default** — `DELTA_MCP_MODE` defaults to `read`, never `trade`

---

## Tests Executed — Pre-existing Skill Tests (0 pass, 4 fail)

**Location:** `document-tools-skill/skills/{docx,pdf,powerpoint,xlsx}/tests/test_*.py`

These are 4 pre-existing test files that were present before this audit. They fail on Termux due to missing native dependencies (`python-docx`, `pdfplumber`, `python-pptx`, `openpyxl` — none of which install on Termux aarch64 without wheels).

**Command:**
```bash
cd ~/hermes-repos/document-tools-skill/skills/docx/tests
python3 -m unittest discover -s . -v
```

**Result:** 4 test files, each with 1 test, all fail with `ModuleNotFoundError` for their respective libraries.

**Note:** These failures are not counted in the priority test pass rate. They document what would need to run on a full Python environment.

---

## Static Validation

### 1. Python Syntax Check
```
OK: 81  FAIL: 0
```
All 81 Python scripts pass `ast.parse()` — including 71 skill scripts + 12 test scripts + 2 top-level tools.

### 2. SKILL.md YAML Frontmatter
```
OK: 118  FAIL: 0
```
All 118 SKILL.md files have valid YAML frontmatter with required `name` and `description` fields.

### 3. Secret Scan
```
Real findings: 0
Documentation examples: 2
```

Both matches are documentation examples:
- `telegram-bot-skill/skills/telegram-standalone-bot/SKILL.md` — `1234567890:***` (BotFather masked token example)
- `PHASE6_SECURITY.json` — the JSON record of the above

### 4. Dangerous Command Review
```
Total matches: 46
All documented:
- curl | bash: 34 (all official installers — hermes-agent, notion, xurl, etc.)
- os.system(): 11 (documented in code-review skill as anti-pattern to detect)
- shell=True: 1 (mentioned in code-review skill)
```

All flagged commands are **documented examples of what to review**, not actual dangerous code.

---

## File Counts Verified

| Category | Count | Command |
|----------|-------|---------|
| Total .py files | 81 | `find -name '*.py' \| wc -l` |
| Skill scripts (in skills/) | 71 | `find -path '*/skills/*' -name '*.py' \| wc -l` |
| Test scripts (in tests/) | 12 | `find -path '*/tests/*' -name '*.py' \| wc -l` |
| Top-level tools | 2 | `find -maxdepth 3 -name '*.py' -not -path '*/skills/*' -not -path '*/tests/*' \| wc -l` |
| SKILL.md files | 118 | `find -name SKILL.md \| wc -l` |
| Test files (test_*.py) | 12 | `find -name 'test_*.py' \| wc -l` |
| Priority tests executed | 73 | Sum of unittest test methods in 8 priority repos |

### Why "72 vs 81" discrepancy

Earlier reports said "72 Python scripts". The exact verified count is:
- **71** skill scripts (in `skills/*/scripts/`)
- **12** test scripts (in `tests/`)
- **2** top-level tools (`run_tests.py` + 1 audit tool)
- **81** total

The "72" was likely "71 skill scripts + 1 top-level tool" (or "71 skill + run_tests.py") before the priority tests were added.

---

## Tests NOT Counted as Pass

- The 4 pre-existing docx/pdf/pptx/xlsx skill tests (fail on Termux)
- Any test that hasn't been actually executed
- Any "planned" or "copied" test that hasn't been run
- Any test that only verifies a string pattern without asserting behavior

---

## Files Added by Phase 7C

- `delta-trading-skill/tests/test_priority.py` (10 tests)
- `algotest-backtester-mcp/tests/test_priority.py` (9 tests)
- `document-tools-skill/tests/test_priority.py` (9 tests)
- `github-skill/tests/test_priority.py` (9 tests)
- `youtube-agent-skill/tests/test_priority.py` (9 tests)
- `instagram-agent-skill/tests/test_priority.py` (9 tests)
- `research-skill/tests/test_priority.py` (9 tests)
- `creative-design-skill/tests/test_priority.py` (9 tests)
