# Value asset library

The parts bin for `nurture-value-factory`. SKILL.md is the workflow; this file holds the method,
the decision matrix, the asset-family crosswalk, the reuse rules, gating and the full routing map.
Built for a service-company buyer (high deal value, long cycle, buying committee, no product
telemetry), not a SaaS user.

---

## 0. The method (the backbone)

Victor Shulga's eight-step lead-magnet method. Everything below serves it.

### The eight steps (asset cheat sheet)

1. **Define the problem**: one sentence, what problem and for whom.
2. **Pick the type**: the three-type test below.
3. **Step by step**: list the roughly ten sequential steps of your own process. Each step is a
   candidate magnet. Choose which step(s) to give away.
4. **Define the impact**: the concrete outcome. No impact, no value. It is also the small contract:
   deliver the impact and you have earned the right to move the lead forward.
5. **Name it**: believable and led by the format. Test 3-5 names on your network (a poll also gets
   the asset seen).
6. **Delivery format**: the same content can exist in several formats (ebook, guide, step-by-step)
   to reach more people, but each individual asset has ONE format.
7. **Make it very good**: give away the method, sell the execution. Too much value is rarely the
   problem; too little is.
8. **CTA**: what to do next and why now (a deadline, limited places, or a named reason). The best
   next step is another asset that builds on this one.

### The three-type test

| Type | Best when | Service-company example |
| :-- | :-- | :-- |
| **1. Make the problem visible** | the audience does not feel the problem; it gets worse with delay | a self-audit of their business development or process, "when to switch vendors", a health check |
| **2. Sample and trial** | your solution is a *repeatable* fix for a *repeatable* problem | time-boxed free access, **a sample deliverable or a mini-audit of their asset** |
| **3. Step 1 of X, free** | the core offer is a multi-step process for a complex problem | one free step: a course module, a calculator, a ready template, one audit stage |

### Type checklist (yes / no)

- Do prospects realise they have the problem?
- Are they ready to act?
- Does the problem get worse the longer they wait? (be honest)
- Do you have a repeatable solution to a repeatable problem?
- Can you offer a free, time-boxed version?
- Would running that free version cost you a lot?
- Does the free version deliver real benefit?
- Does your solution solve several problems in sequence?
- Is there something in onboarding you would do for every client anyway, which you could do free?
- **Conclusion: type 1, 2 or 3?**

Hidden assets you may already have: a **network or community**; clear **domain expertise**;
whether that expertise is **documented**; a **best-practice guide or SOP** from delivery work.

### Quality bar

Adapted from Tim Keen's *The 2025 Agency Growth Bible* (see Credits in SKILL.md):
- Aim for something a buyer would plausibly pay for (his benchmark is "worth $100+").
- Share the **process you actually use** in the business, not theory.
- **Show the work**: annotated screenshots or visuals for each step.
- Include a **real case** with a before and after number and, with permission, a client quote.
- Open with **who you are and why you are qualified** to write it.
- **Split a big magnet into several focused ones**, one per pain point. This maps directly to the
  one-objection-per-asset rule.
- Use the **thank-you page**: confirm delivery, show a testimonial, offer one next step.

---

## 1. Decision matrix (stage × objection → asset)

Pick the **cheapest asset that removes the ONE blocking objection at THIS stage**: not the fanciest
format, the one that clears the block.

### Researcher (early, learning): entered through content or education

| Blocking objection | Asset | Why it fits | Effort |
| :-- | :-- | :-- | :-- |
| "I don't see that this is a problem" | industry benchmark or short report | shows the gap with data, asks for nothing | low-medium |
| "I don't see how big the risk is" | framework visual or "signs that..." checklist | names the pattern they are in | low |
| "I don't know where to start" | one-page checklist or step-by-step guide | quick win, high perceived value | low |
| "Is this relevant to my industry?" | an anonymised industry case | proof it applies to their world | low |

The first soft CTA comes late in this track (around touch 5). Assets here are pure education.

### Evaluator (comparing vendors): visited services or pricing, asked about price or alternatives

| Blocking objection | Asset | Why it fits | Effort |
| :-- | :-- | :-- | :-- |
| "What does it cost / what is the ROI?" | ROI or cost calculator (interactive) | a number they get themselves, no sales call | medium |
| "Are we even ready?" | readiness or maturity assessment | segments the lead and gives them a score | medium |
| "How do I choose a vendor, what should I look at?" | "how to choose a [service] partner" guide | sets the criteria on your terms | low-medium |
| "You vs the alternatives, or in-house" | comparison template (spreadsheet) | structures the evaluation around your strengths | low-medium |

Assessments and calculators **also qualify the lead**: the inputs reveal fit. Prefer them here.

### "Not now" / high engagement: mistimed reply, webinar attendee, near-SQL

| Blocking objection | Asset | Why it fits | Effort |
| :-- | :-- | :-- | :-- |
| "I can't see that YOU can do this" | **mini-audit or teardown of their own asset** | shows skill on *their* problem | high, one-to-one |
| "What would it look like in practice?" | **sample deliverable** (marked-up drawing, sample model, teardown document) | concrete proof of the work product | high, one-to-one |
| "We have no process for this" | SOP, instruction or ready-to-use template | gives them the process; they see the gap you fill | medium |
| "Remind me why we should come back" | "what changed" proof pack (new service, fresh case) | re-engagement value instead of "we miss you" | low |

This track is usually **the most valuable** for service companies. Spend one-to-one effort here,
not on cold names.

---

## 2. Asset families crosswalk

Six standard families plus one that only service companies have:

| Family | Contains | Best stage | Reusable? | Build with |
| :-- | :-- | :-- | :-- | :-- |
| **Guides and ebooks** | checklists, frameworks, SOPs, step-by-step guides | Researcher → Evaluator | yes | docx skill; a visual builder for the visual version |
| **Courses and masterclasses** | email courses, video series, live or recorded | Evaluator (nurture plus authority) | yes | an email drip via `nurture-architect`; a deck via `slide-deck-builder` |
| **Events and webinars** | webinars, workshops, Q&A | Evaluator → "not now" | partly | `slide-deck-builder` plus a promo asset |
| **Calculators** | ROI, cost estimators, readiness scores | Evaluator (also qualifies) | yes | `free-tools` |
| **Mini-tools** | browser extensions, self-assessments, simple utilities | Evaluator | yes | `free-tools` |
| **Reports and research** | trends, analytics, benchmarks, comparisons | Researcher → Evaluator | yes | a data pull, then a visual builder |
| **Sample of the work** (service companies only) | mini-audit, teardown, sample deliverable | "not now" / near-SQL | **no, one-to-one** | `website-copy-reframe`, `account-dossier`, a `gtm-audit` fragment |

Generic lead-magnet playbooks tend to miss the seventh row, and for a service company it is often
the strongest asset.

---

## 3. Reuse before rebuild: inventory checklist

Before commissioning anything, sweep what the company already has:

- **Website**: guides, resource pages, blog posts (repurpose into a checklist or a visual).
- **Design system**: does one exist? If not, and the asset is client-facing, run
  `design-system-generator` first.
- **Proposals and decks**: proof points, cases and frameworks already written.
- **Earlier sequences and magnets**: anything gated before that still holds up.
- **GTM audit**: findings that can become a benchmark or a "what changed" pack.

A repurpose (blog post → visual, proposal section → SOP) almost always beats a fresh build: it is
faster, already on brand and already approved. Log what you reused.

---

## 4. Gating

| Approach | When | Trade-off |
| :-- | :-- | :-- |
| **Ungated** | top-of-funnel education (Researcher), reach matters more than capture | maximum reach, no email |
| **Email-only gate** | most reusable magnets | best balance of capture and friction; the default |
| **Email plus company / role** | high-value assets (assessment, webinar), where the fields also qualify | more friction, better lead data |
| **No gate, delivered one-to-one** | a mini-audit or teardown sent to a named lead | already personal; a form would only add friction |

Rule: ask for the minimum. Every extra field costs sign-ups. For assessments and calculators the
inputs are the qualification, so a long form on top is unnecessary.

---

## 5. Full routing map (spec → build skill)

All build skills are optional; use what is installed, or brief a human.

| Asset spec | Route to | Notes |
| :-- | :-- | :-- |
| Checklist, framework, benchmark or comparison as a visual (LinkedIn-shaped, up to about 9 blocks) | a visual or infographic builder you have | client brand for client assets |
| Multi-slide visual sequence | a carousel or slide builder you have | |
| Guide, ebook, SOP, instruction, document template | the docx skill | multi-page, printable |
| Spreadsheet, comparison sheet, tracker template | the xlsx skill | |
| ROI or cost calculator, assessment, readiness score, quiz, mini-tool | `free-tools` (pack `marketing-engine-skills`) | host wherever the company hosts its web tools |
| Plan and distribute a reusable magnet | `lead-magnets` (pack `marketing-engine-skills`) | |
| Landing or thank-you page | `page-builder` (standalone repo) + `copywriting` (pack `marketing-engine-skills`) | |
| Case study | `case-study-writer` (pack `account-management-skills`) | needs client permission for names |
| Webinar or workshop | `slide-deck-builder` (pack `sales-engine-skills`) | plus a promo visual |
| Data-backed report | a data pull, then a visual builder | source the data first |
| Mini-audit or teardown of the lead's **website copy** | `website-copy-reframe` (pack `marketing-engine-skills`) | audit mode, then a short copy deck |
| Teardown of a named account or its market | `account-dossier` (pack `account-management-skills`) | |
| GTM-shaped mini-audit | `gtm-audit` (pack `gtm-strategy-skills`), one criterion only | never run the full audit as a magnet |
| Client brand kit missing | `design-system-generator` (standalone repo) | run FIRST for client-facing assets |
| The delivering value-first email or DM | `reply-objection-handler` (pack `outbound-engine-skills`) | one message, prospect's language, interest CTA |
| Near-deal, proposal-grade asset | `proposal-generator` (pack `sales-engine-skills`) | |

---

## 6. Worked examples (anonymised)

- **A BIM/MEP outsourcing firm. The lead replied "not this quarter" and opened three follow-ups.**
  High engagement, "not now" track. Objection: "I can't see that you can do this". Asset: a
  **one-to-one mini-audit of one of their MEP coordination drawings** (sample of the work, ungated,
  sent directly). Route: `account-dossier` for context plus a manual teardown. Logged to touch 3 of
  the reply track.
- **A GIS services firm. The lead visited pricing and asked how they compare.** Evaluator.
  Objection: "how do I choose / what does it cost". Asset: a **readiness assessment** (segments and
  scores them, email plus role gate). Route: `free-tools`. Reusable, added to the inventory.
- **A cold Researcher who pulled a checklist and has low engagement.** Early. Objection: "I don't
  see the size of the problem". Asset: an **industry benchmark visual**, ungated. Route: a visual
  builder. Reusable.
- **An engaged lead with one clear objection that does not repeat across other leads.** Step 1
  says NO asset. The value is a two-sentence personal insight in the email body plus an interest
  CTA. Route: `reply-objection-handler`. Sometimes the right answer is to build nothing.
