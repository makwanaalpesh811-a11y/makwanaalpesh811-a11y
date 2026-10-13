# Skill Inventory

**Date:** 2026-10-13
**Total skills:** 118 across 27 local repos (29 total on GitHub)

---

## Status Breakdown

| Status | Count | Description |
|--------|-------|-------------|
| **executable** | 89 | Has `scripts/` dir with executable `.py`/`.sh`/`.js` + code blocks |
| **partially executable** | 8 | Code blocks with commands but no `scripts/` dir |
| **documentation-only** | 21 | Prose/references only, no executable code |

**Total: 118 SKILL.md files**

---

## Skills by Repository

### Content & Social Media (35 skills)

**youtube-agent-skill (15)** — `skills/youtube-*/SKILL.md`
- youtube-full-access (executable)
- youtube-content (executable)
- youtube-strategy-analysis (partially executable)
- youtube-trading (documentation-only)
- youtube-trading-strategy (documentation-only)
- youtube-trading-workflow (documentation-only)
- yt-chapters (executable)
- yt-comment (executable)
- yt-edit (executable)
- yt-package (executable)
- yt-plan (executable)
- yt-retention (executable)
- yt-shorts (executable)
- yt-viral (executable)
- yt-transcript (executable)

**instagram-agent-skill (16)** — `skills/ig-*/SKILL.md`
- ig-audit, ig-caption, ig-carousel, ig-comment, ig-dm, ig-hashtag-strategist, ig-hook-extractor, ig-human, ig-plan, ig-profile, ig-reel, ig-reply, ig-repurpose, ig-story, ig-viral (executable)

**x-agent-skill (1)** — `skills/xurl/SKILL.md` (partially executable)
**reddit-agent-skill (1)** — `skills/reddit-reading/SKILL.md` (partially executable)

### Trading (15 skills)

**delta-trading-skill (15)** — `skills/{delta-*,signal-bot-*,paper-trade-*,tredalgo-*,ema200-*,strategy-backtest-verify}/SKILL.md`
- delta-market-analysis, delta-live-order-execution, delta-market-refresh-rules, delta-mcp-india-readonly (documentation-only — read-only mode), ema200-trendline-signal, hermes-crypto-grid-backtest, paper-trade-simulator, signal-bot-matplotlib, strategy-backtest-verify, tredalgo-signal-bot (executable)

**youtube-trading-skill (3)** — documentation-only

### AI Agents & Dev (17 skills)

**hermes-agent-skill (4)** — computer-use, hermes-agent, hermes-agent-skill-authoring, port-external-skills
**claude-code-skill (1)** — claude-code
**codex-skill (1)** — codex
**opencode-skill (1)** — opencode
**github-skill (10)** — github, codebase-inspection, dogfood, hermes-agent-skill-authoring, inspecting-hermes-desktop-dom, node-inspect-debugger, python-debugpy, requesting-code-review, simplify-code, spike, systematic-debugging, test-driven-development

### Tools & DevOps (13 skills)

**aws-free-tier-skill (3)** — aws-free-ai-access, aws-free-tier, aws-bedrock-free-tier
**telegram-bot-skill (2)** — telegram-gateway-setup, telegram-standalone-bot
**video-localization-skill (4)** — hindi-video-dub, video-localization, + subs
**document-tools-skill (9)** — docx, pdf, xlsx, excel-author, airtable, box, notion-related
**research-skill (6)** — arxiv, competitor-news-monitor, grounded-citations, hermes-crypto-grid-backtest, llm-wiki, pdf-read-ocr, rss-feeds
**apple-skill (4)** — apple-*, + subs
**maps-skill (1)** — maps (executable)
**google-workspace-skill (1)** — google-workspace (executable)
**notion-skill (1)** — notion (executable)
**obsidian-skill (1)** — obsidian
**email-skill (2)** — email-inbox-triage, himalaya
**education-skill (1)** — teacher-mode

### Creative & Media (13 skills)

**creative-design-skill (10)** — architecture-diagram, ascii-video, baoyu-infographic, claude-design, design-md, humanizer, manim-video, p5js, popular-web-designs, songwriting-and-ai-music
**ai-image-gen-skill (4)** — ai-image-gen-termux, gif-search, image-search-mcp, mobile-ai-via-colab
**audio-tools-skill (1)** — songsee

---

## Documentation-Only Skills (21)

These skills provide guidance only, with no executable code:

- delta-mcp-india-readonly (read-only mode — no actions)
- youtube-trading, youtube-trading-strategy, youtube-trading-workflow
- education-skill (teacher-mode)
- aws-free-tier-skill (guidance on free tiers)
- hermes-agent-skill-authoring (docs for writing skills)
- port-external-skills (porting guide)
- strategy-backtest-verify (workflow guide)
- + others

**Labelled clearly in this inventory as documentation-only.** They should not be described as "tested executable features."

---

## Verification Command

```bash
find ~/hermes-repos -name SKILL.md -not -path "*/_audit_tmp/*" 2>/dev/null | wc -l
# → 118
```
