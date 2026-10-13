# Improvement Plan

**Date:** 2026-10-13
**Purpose:** Document remaining work to raise score from 76 to 80+

---

## Current State

**Score: 76/100** (see SCORECARD.md)

Reaching 80+ requires improvements in **tests** (2 points) and **examples/usability** (2 points) at minimum.

---

## Short-Term Wins (1-3 hours each)

### A. Add real pytest tests to non-priority repos (worth +3-5 pts in tests)

Currently 73 tests cover 8 priority repos. Adding basic tests to:
- `hermes-agent-skill` (10 skills, complex — needs real tests)
- `aws-free-tier-skill` (has shell scripts)
- `document-tools-skill` (already has tests, could add more)
- `youtube-trading-skill` (documentation-only — can test structure only)

**Effort:** 3-5 hours total
**Risk:** Low — all mock-based

### B. Add `examples/` folders to priority repos (worth +3-4 pts in examples)

Currently no `examples/` folders exist. Adding:
- `delta-trading-skill/examples/` — sample grid backtest, trend signal
- `youtube-agent-skill/examples/` — sample upload script, plan output
- `instagram-agent-skill/examples/` — sample caption, hashtag output
- `github-skill/examples/` — sample PR review, CI check

**Effort:** 2-3 hours
**Risk:** Low — clear copy-paste examples

### C. Standardize SKILL.md sections (worth +2-3 pts in documentation)

Add missing sections to all 118 SKILL.md:
- `## Usage` (118 files missing)
- `## Examples` (118 files missing)
- `## Troubleshooting` (118 files missing)
- `## Limitations` (118 files missing)

**Effort:** 8-12 hours (bulk edit script)
**Risk:** Medium — could introduce errors in 118 files
**Alternative:** Add to only 30 most-used skills first

### D. Version frontmatter (worth +1 pt in maintenance)

Add `version: 1.0.0` to 32 skills missing it.

**Effort:** 30 min (bulk edit)
**Risk:** Low

---

## Medium-Term (1-2 days each)

### E. Live API integration tests (worth +3 pts in tests)

Add integration tests that:
- Test against mock servers (not real APIs)
- Test token-expiry handling
- Test rate-limit responses
- Test network timeouts

**Effort:** 1-2 days
**Risk:** Medium — need mock server setup

### F. Cross-repo integration tests (worth +2 pts in tests)

Add tests that verify:
- delta-trading-skill + market-data work together
- youtube-agent-skill + telegram-bot-skill share auth patterns
- github-skill + document-tools-skill share CI patterns

**Effort:** 1 day
**Risk:** Low

### G. Documentation consistency (worth +3 pts in docs)

- Add badges to every repo README
- Add `## Getting Started` section to all repos
- Add troubleshooting section to top-level docs
- Standardize `SECURITY.md` (already done) and add `CODE_OF_CONDUCT.md`

**Effort:** 4-6 hours
**Risk:** Low

---

## Long-Term (3+ days)

### H. Real user testing (worth +3 pts in usability)

- Get 3-5 external users to try priority skills
- Record feedback
- Iterate on common failure modes

**Effort:** 1 week+
**Risk:** High — needs coordination

### I. Versioning and releases (worth +2 pts in maintenance)

- Add semantic versioning to all repos
- Create GitHub releases with changelogs
- Add `CHANGELOG.md` to each repo
- Use git tags for releases

**Effort:** 2-3 days
**Risk:** Low

### J. Community contribution infrastructure (worth +2 pts in open-source)

- Add GitHub Discussions
- Add issue templates
- Add PR template
- Add CODEOWNERS
- Add branch protection rules

**Effort:** 1 day
**Risk:** Low

---

## Recommended Priority Order

1. **B. Add examples/ to priority repos** — highest impact per hour, +3-4 pts
2. **A. Add tests to non-priority repos** — solid +3-5 pts
3. **D. Version frontmatter** — quick win, +1 pt
4. **G. Documentation consistency** — +3 pts

**Estimated effort to reach 80+: 12-20 hours total**

---

## What NOT to Do

- ❌ Force-push to add history changes
- ❌ Delete skills to "clean up" (violates preservation rules)
- ❌ Add fake stars/forks/contributors
- ❌ Add fake test coverage claims
- ❌ Remove documentation-only skills (they're useful)
- ❌ Add fake users/issues/comments
- ❌ Merge repos to reduce count (violates preservation rules)

---

## How to Reach 85+

Beyond 80+, reaching 85+ requires:
- Real user feedback (H)
- Live integration tests (E)
- Versioning and releases (I)
- Community infrastructure (J)

**Total effort: 2-3 weeks**

---

## Verification

All claims in this plan are evidence-based — no invented capabilities, no fake success claims, no fabricated metrics.
