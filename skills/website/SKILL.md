---
name: website
description: >-
  Master skill for the website of a B2B service company. Runs the flow: website-audit for a baseline →
  homepage-rewrite (positioning and proof on the home page) → page-builder (service, industry,
  case and blog pages from the same proof) → website-audit again after launch. Works out which
  step the site is on, runs it, holds the hand-off between steps and says what comes next. Use
  when the user says "fix our website", "rebuild the site", "where do we start
  with the site", "запусти website", "майстер-скіл сайту", "сайт з нуля", "переробка сайту", "що робити з
  сайтом", or asks how the website skills fit together. For a single job (only the homepage,
  only one page, only an audit) call that skill directly.
---

# Website: the master skill for a company site

A service company's homepage says what it does and proves it, and the inner pages go deep on
each offer. A page that breaks on a phone loses the visitor before either job starts. This flow
runs an audit for a baseline, then the homepage, then the pages, then the audit again,
and keeps one proof bank across all of it.

| Step | Skill | Output | When |
|---|---|---|---|
| 0 | `website-audit` | baseline report P0-P3, scores per area | before any rewrite, so there is a "before" to compare |
| 1 | `homepage-rewrite` | diagnosis (clarity /50, trust /12), new homepage copy, proof bank, canvas | once, then again after a repositioning |
| 2 | `page-builder` | one publish-ready page per run (service, industry, case, blog) | per page, in the order of the Site Blueprint |
| 3 | `website-audit` | the "after" column against the baseline | after launch and after every larger release |

Optional around the flow:
- `website-copy-reframe`, `seo-audit`, `ai-seo`: in this pack, installed with it (messaging
  score of the current site, search and AI-answer visibility).
- `design-system-generator`: separate install, `npx skills add victor-shulga/design-system-generator`
  (visual brand system before a redesign).

## Routing

1. Find out the company, its site URL and what the user wants done.
2. If the user named a step, run that skill.
3. Otherwise pick the next step from the files in the working folder:
   - baseline exists = `website-audit/<domain>/website-audit-<domain>-<date>.md`;
   - homepage rewritten = `<company>-homepage-rewrite-<date>.md` with Proof bank and Canvas
     sections;
   - Site Blueprint = a page inventory file the user points to (ask if unsure);
   - pages shipped = `page-builder` output files newer than the baseline audit whose URLs the
     user confirms are live (ask for the URLs).

   Then:
   - no baseline audit → step 0, `website-audit` on the live site with `--limit 10`;
   - baseline exists, homepage not rewritten → step 1, `homepage-rewrite`;
   - homepage rewritten, no Site Blueprint (page inventory, URL logic, internal links) → stop and
     ask for one or help draft it, because `page-builder` refuses to run without it;
   - blueprint exists → step 2, `page-builder`, next page in the blueprint order;
   - new pages shipped → step 3, `website-audit` with the same page limit as the baseline.
4. If a skill in the table is not installed, say which one, give its install line and
   wait until it is installed:
   - `npx skills add victor-shulga/website-audit/skills/website-audit`
   - `npx skills add victor-shulga/homepage-rewrite/skills/homepage-rewrite`
   - `npx skills add victor-shulga/page-builder/skills/page-builder`

## Hand-offs between steps

- **Audit → homepage.** P0 and P1 findings on the conversion path (no CTA in the first screen,
  contact more than two clicks away) go into the homepage diagnosis as known gaps.
- **Homepage → pages.** The proof bank and canvas sections of the `homepage-rewrite` file are
  inputs to every `page-builder` run. If the file lacks either, rerun Steps 2-3 of
  `homepage-rewrite` first. A page does not use a number the proof bank does not have.
- **Pages → audit.** Every page URL shipped goes into the next audit run, so the "after" report
  covers it.

## Invariants

- One proof bank per company, reused by every step; a claim missing from it stays off the site.
- The company's brand voice and design system outrank the style rules of any step.
- No step publishes to the live site by itself. Each one hands over files and a checklist.
- Every step ends with a short summary and the next step from the table above.
