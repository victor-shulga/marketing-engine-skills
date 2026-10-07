# marketing-engine

Marketing skills for B2B service companies: where clients come from, what to charge, what to say on the site and how to measure it. One pack inside the GTM-system skill stack by [Victor Shulga](https://victorshulga.com) (Fractional CRO), routed by Max (`npx skills add victor-shulga/max`, then `/max`).

Full catalog of the stack: https://github.com/victor-shulga/max/blob/main/CATALOG.md

## Install

```bash
npx skills add victor-shulga/marketing-engine-skills
```

or in Claude Code:

```
/plugin marketplace add victor-shulga/marketing-engine-skills
/plugin install marketing-engine@marketing-engine-skills
```

Restart your Claude Code session after install — skills load at session start.

## Skills included

**Clients and market**

- `referrals` — a referral or partner program: who to ask, what to ask for, how to track intros
- `customer-research` — client interviews, reviews and the words clients use for their problem
- `competitor-profiling` — a profile per competitor: offer, prices, proof, weak spots

**Offer and plan**

- `pricing` — prices, packages and how to present them
- `marketing-plan` — a marketing plan by quarter
- `revops` — the sales process, pipeline data and handoffs between marketing and sales
- `analytics` — site analytics and event tracking

**Site and content**

- `copywriting` — page copy
- `cro` — why a page or form does not convert and what to change
- `seo-audit` — technical and on-page SEO audit
- `ai-seo` — visibility in ChatGPT, Perplexity and other AI search
- `content-strategy` — what to publish and why
- `lead-magnets` — lead magnets
- `free-tools` — a free tool as a lead channel
- `website-copy-reframe` — audit a service company's site messaging (0–100 scorecard), rewrite the homepage or one service page

**Nurture (leads that are not ready yet)**

- `nurture-architect` — the whole nurture program: fit × engagement scoring, tracks by entry source, branching, re-engagement and sunset, renewal drips
- `nurture-value-factory` — what value to give at a given touch, whether an asset is needed at all, the asset spec and which skill builds it

## Requirements & integrations

| Integration | Used for | Required? | Auth / setup |
|---|---|---|---|
| Claude Code or Claude.ai | runs the skills | yes | — |
| Web search / fetch | competitor and SEO research | recommended | built into Claude |
| Analytics, CRM, SEO tools | real numbers instead of estimates in `analytics`, `revops`, `seo-audit` | optional | the skills ask what you have connected |

## Source and license

14 of the 17 skills are copies of skills from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) by Corey Haines, MIT License. Each folder keeps the original `LICENSE` and a `NOTICE.md` with the source commit and the changes made (links to the upstream tool registry turned into plain text; descriptions rewritten as plain YAML). Packaging in this repo: MIT.

`website-copy-reframe`, `nurture-architect` and `nurture-value-factory` are written by Victor Shulga (MIT). Borrowed ideas are credited inside each `SKILL.md`: the copy canvas and homepage questions come from Anthony Pierri and Robert Kaminski (Fletch PMM), the awareness levels from Eugene Schwartz.
