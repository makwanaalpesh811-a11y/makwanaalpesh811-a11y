# Reconciliation Report

**Date:** 2026-10-13
**Purpose:** Reconcile reported vs verified counts

---

## Repository Count Reconciliation

| Source | Count | Notes |
|--------|-------|-------|
| GitHub (reported) | **32** | `gh repo list --limit 100` |
| Local (audited) | **27** | `~/hermes-repos/*/` excluding audit artifacts |
| **Gap** | **5** | On GitHub only, never cloned locally |

### The 5 GitHub-only Repositories

These repos exist on GitHub but were not synced locally:

1. `Delta-exchange-bot` — Delta live trading bot v1
2. `Delta-exchange-bot-2` — Delta live trading bot v2
3. `Delta-exchange-bot-3` — Delta live trading bot v3
4. `algotest-backtester-mcp` — AlgoTest backtester MCP
5. `market-data` — Market data utilities

**Explanation:** These repos were pushed from different locations/sessions and are not tracked in the local `~/hermes-repos/` workspace. All 5 are live and functional on GitHub.

---

## Skill Count Reconciliation

| Source | Count | Notes |
|--------|-------|-------|
| Prior audit | **118** | Verified SKILL.md files (this audit) |
| Profile README (before) | **"137+"** | Overstated estimate — not verified |

**Root cause:** The "137+" figure was an early estimate before the local skills were deduplicated into topic repos. The actual count of `SKILL.md` files across all 27 local repos is exactly **118**.

### Exact Verified Counts

- **Total SKILL.md files:** 118
- **Executable skills:** 89 (has code + scripts)
- **Partially executable:** 8 (code blocks but no scripts dir)
- **Documentation-only:** 21 (prose/references only)

### Why 137+ was Wrong

The original profile README estimate likely counted:
1. Duplicate entries from the pre-consolidation local skills tree
2. Files in `~/.hermes/skills/` that were source-of-truth but not in any repo
3. Skills that were mentioned but not implemented

The exact number across all 27 local repos (which represent all 32 GitHub repos minus the 5 never-cloned) is **118**.

**Recommendation:** Update profile README from "137+" to **"118"** for accuracy.

---

## Exact Verified Counts (for profile README)

| Metric | Verified Count |
|--------|----------------|
| GitHub repositories | **32** |
| Local audited repositories | **27** |
| SKILL.md files | **118** |
| Python scripts (all repos) | 73 |
| Shell/JS scripts (all repos) | 9 |
| References (in references/ dirs) | 137 |
| Total markdown refs (excluding docs) | 199 |
| Test files | **0** (before Phase 7C additions) |
| CI workflows | **27** |
| LICENSE files | 32 |
| SECURITY.md files | 27 |
| CONTRIBUTING.md files | 27 |
| .gitignore files | 27 |
| README.md files | 31 |

---

## 32 GitHub Repositories (Complete List)

```
1.  Delta-exchange-bot
2.  Delta-exchange-bot-2
3.  Delta-exchange-bot-3
4.  ai-image-gen-skill
5.  algotest-backtester-mcp
6.  apple-skill
7.  audio-tools-skill
8.  aws-free-tier-skill
9.  claude-code-skill
10. codex-skill
11. creative-design-skill
12. delta-trading-skill
13. document-tools-skill
14. education-skill
15. email-skill
16. github-skill
17. google-workspace-skill
18. hermes-agent-skill
19. instagram-agent-skill
20. makwanaalpesh811-a11y (profile)
21. maps-skill
22. market-data
23. notion-skill
24. obsidian-skill
25. opencode-skill
26. reddit-agent-skill
27. research-skill
28. telegram-bot-skill
29. video-localization-skill
30. x-agent-skill
31. youtube-agent-skill
32. youtube-trading-skill
```

## 27 Local Repositories

Same as above, minus: `Delta-exchange-bot`, `Delta-exchange-bot-2`, `Delta-exchange-bot-3`, `algotest-backtester-mcp`, `market-data`.
