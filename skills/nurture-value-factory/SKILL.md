---
name: nurture-value-factory
description: >-
  Decides WHAT value to give a lead at a nurture touch or in one value-first message: whether
  a produced asset is needed at all, which type fits the buyer stage and the ONE blocking
  objection, writes the asset spec, and routes the build to an existing skill. Sits between
  nurture-architect (WHEN and which track) and the build skills (docs, sheets, calculators,
  landing pages, visuals, teardowns). It specs and dispatches; it does not hand-craft the
  asset. Use when the user asks "what value do we give here", "do we need a lead magnet",
  "what should this lead get at this touch", "what to offer instead of a call", "яку цінність
  тут дати", "чи треба лід-магніт", "що дати ліду на цьому дотику", "чим прогріти цього
  ліда", or when a nurture track says "give value here" and the asset must be chosen and
  built. Not for the whole nurture program (use nurture-architect), not for one reply (use
  reply-objection-handler), not for a cold sequence (use sequence-writer).
---

# Nurture Value Factory

You pick value assets for nurture and route their build. The nurture program (`nurture-architect`)
says *when* to give value and on *which track*. **This skill decides what that value is, whether it
needs to be a produced asset at all, and then dispatches the build to a skill that already
exists.**

The core point for a **service company** (as opposed to SaaS): the value that converts best is
rarely a generic PDF. It is **a sample of the real work**: a mini-audit of the lead's own asset, a
teardown, a marked-up drawing, a filled-in template. That is the service company's unfair
advantage. Reach for it whenever the lead is engaged enough to justify one-to-one effort.

## Language and voice

- **Answer the user and write specs in the user's language.** If it is Ukrainian, use plain words
  and avoid anglicisms (цінність, оцінка лідів, дозбір, ОПР, стоп-фільтр). Tool names stay in
  Latin script.
- **The asset's own copy is written in the prospect's language** (often English). Label it. Edit
  prose for AI tells before delivery; if installed, use `anticopywriting-ai` (pack `gtm-skills`).
- **Brand:** an asset for a client company uses that company's design system or brand kit. An
  asset for the user's own business uses the user's brand. Never ship off-brand.

## Hard rules (they override any borrowed template)

1. **An asset is not always the answer.** Often the value is a personal insight written straight
   into the email body: no download, no gate. Decide *whether* an asset is warranted before picking
   a type (Step 1).
2. **Interest-based CTAs only.** Neither the asset nor the message that delivers it asks for a
   call, a meeting or a slot. If installed, load `cta-interest-based` (pack
   `outbound-engine-skills`).
3. **Every delivering message ends with a question** (the soft CTA).
4. **80/20.** The asset teaches; it does not pitch. The company plug stays at 20% or less.
5. **Never invent client data.** No ICP tiers, offers or cases? Write "to confirm on discovery,
   not invented" and spec around the gap.
6. **Reuse before rebuild.** Inventory what the company already has (site, design system,
   proposals, earlier magnets, GTM audit) and repurpose before commissioning anything new. Log the
   reuse.
7. **Confidentiality.** Anything that could reach a public or shareable asset stays generic: no
   client names, no third-party vendor names.
8. **Give away the method, sell the execution.** The asset explains the *what* and the *why* in
   full and holds nothing back. The paid offer is doing it for them. An asset that makes clear how
   much time and effort the work takes is what earns the deal. If giving it away does not feel a
   little painful, it is probably not good enough.
9. **Every asset names its impact, like a small contract.** Before building, state the concrete
   outcome the lead gets from using it. No impact means no value: drop back to a body-copy insight.
   Delivering that impact is what earns the right to move the lead toward the offer. Most lead
   magnets fail at exactly this step.

---

## Step 0: Gather inputs (do not invent)

From the user's brief and the company's documents (ICP, GTM audit, offers, earlier sequences,
design system):

| Input | Why it matters | If missing |
| :-- | :-- | :-- |
| Persona and buyer stage | picks the asset type | flag "to confirm on discovery" |
| Entry source / nurture track | shows intent (Researcher / Evaluator / "not now") | ask which track this touch belongs to |
| The ONE blocking objection | the asset must remove this and nothing else | infer from the stage and state the assumption |
| Fit × engagement score, if scored | decides reusable vs one-to-one (Step 3) | treat as low engagement → reusable |
| Existing asset inventory | reuse before rebuild | list what you found and the gaps |
| Assets the company does not know it has | the cheapest magnet is often already in hand | ask the four questions below |
| Design system / brand kit | the asset must be on brand | flag it; do not ship off brand |

**Hidden-asset check** (run before commissioning anything new): Is there a **network or
community**? Clear **domain expertise**? An existing **best-practice guide, SOP or internal
process** document? Anything already **written down** from delivery work? A yes to any of these
usually beats building from scratch: faster, and already proven. Log it as the reuse candidate.

Confirm in one line what you loaded. If the call came from a `nurture-architect` touch, take the
track and touch theme as given and go straight to Step 1.

**Read `references/value-asset-library.md` now.** It holds the decision matrix, the asset-family
crosswalk, the reuse rules, gating, and the full routing map. This file is the workflow; the
library is the parts.

---

## Step 1: Decide WHETHER an asset is needed

An asset is justified only if **all** of these hold:

- The blocking objection is real and *repeats across many leads* (→ reusable asset), **or** the
  lead is valuable enough for one-to-one proof (→ personal asset).
- One well-aimed insight in the message body would not do the job better and faster.
- The company can produce it on brand without weeks of work, or it can be repurposed.

If an asset is **not** warranted, output the value as a body-copy brief (angle, the one proof
point, interest CTA) and stop. Say *why* there is no asset. This is a valid and common outcome.

---

## Step 2: Pick the asset TYPE

Two selectors used together: first the **three-type test** (by the shape of the solution), then
the **stage × objection matrix** (by where the lead sits). They usually agree; when they do not,
the objection wins.

### 2a. The three-type test (which kind of magnet fits the offer)

| Type | Use when | Example |
| :-- | :-- | :-- |
| 1. Make the problem visible | the lead does not feel the problem yet, and it gets worse with time | a site speed test, "when to switch vendors", a self-audit of their process |
| 2. Sample / trial | the offer is a *repeatable* fix for a *repeatable* problem; give a limited taste | time-boxed free access, a sample deliverable, a mini-audit of their asset |
| 3. Step 1 of X, free | the core offer is a multi-step process for a complex problem; give one real step | one module of a course, a calculator, a ready template, one stage of the audit |

If the type is not obvious, run the yes/no checklist in the library (§0). For an engaged lead of a
service company, **type 2 (a sample of the real work)** is almost always the strongest.

### 2b. Stage × objection matrix (the cheapest asset that clears the block)

Full matrix in the library. Short version:

| Stage / track | Typical blocking objection | Asset family (cheapest that removes it) |
| :-- | :-- | :-- |
| Researcher: early, learning | "I don't see the problem or its size" | checklist · benchmark or report · framework visual · industry case |
| Evaluator: comparing vendors | "How do I choose / what does it cost / are we ready?" | ROI or cost calculator · readiness assessment · "how to choose a vendor" guide · comparison template |
| "Not now" / high engagement | "I can't see that YOU can do this" | mini-audit of their asset · teardown · sample deliverable · SOP · ready-to-use template |

The library maps these to six asset families plus one service-company family. Pick **one** format:
mixing an ebook, a video and a spreadsheet in one asset lowers its perceived value. Prefer the
lowest-effort asset that still clears the objection.

---

## Step 3: Reusable or one-to-one

- **Reusable** (build once, send to many): the default for Researcher and Evaluator leads with low
  or medium engagement. It must be generic and gateable.
- **One-to-one proof** (a mini-audit or teardown of *their* thing): reserved for high-engagement or
  near-SQL leads where the payoff justifies the effort. This is a service company's strongest
  nurture asset; spend it where a deal is close, not on cold names.

State which mode and why, tied to the fit × engagement read.

---

## Step 4: Write the asset spec

A tight spec the build skill can execute. Fill every field, flag every gap, invent nothing:

1. **Problem → solution → for whom**: the problem in one sentence, the solution, the exact persona.
2. **Type**: 1, 2 or 3 from Step 2a.
3. **Step by step** (mostly type 3): the sequential steps of the process; mark which steps are
   given away and which stay in the paid offer.
4. **Impact (the small contract)**: the concrete outcome the lead gets. If you cannot name one,
   go back to Step 1. This field is not optional.
5. **Name**: specific, believable, led by the format ("template", "calculator", "checklist", never
   "lead magnet"). Offer 3-5 title options; a quick poll of the user's network is a cheap way to
   pick.
6. **Format and length**: ONE format (a one-page checklist, a six-block visual, a web calculator,
   a three-page SOP...).
7. **What is inside**: 3-5 concrete takeaways (real substance, not placeholders). Quality bar in
   the library §0: a real case with a number, visuals over prose, a credible introduction.
8. **CTA**: interest-only; the delivering message ends on a question. The best next step is
   another asset that builds on this one.

Plus the delivery envelope:
- **Gate yes/no and fields**: the minimum (email only unless the asset is high value); ungated for
  top-of-funnel reach. See the gating section in the library.
- **Delivery**: instant, by email, or on a thank-you page (add a testimonial and one next step
  there), and how it lands in the nurture touch.
- **Stage, track and objection** it serves.
- **Brand**: the client's design system, or the user's own brand for their own assets.

Quality sets the ceiling on engagement. Do not ship a nice-to-have. If there is no hidden asset to
build on, the effort is the price of a magnet that converts.

---

## Step 5: Route to the build skill and invoke it

Match the spec to a build skill (full map in the library), then **invoke that skill with the spec**
so the asset actually gets produced. The skills below are optional; use the ones installed.

| Asset | Build with |
| :-- | :-- |
| Checklist, framework, benchmark, comparison as a visual (LinkedIn-shaped) | a visual or infographic builder you have (or a designer brief) |
| Guide, ebook, SOP, instruction, multi-page template | the docx skill, if available |
| Spreadsheet template, comparison sheet, tracker | the xlsx skill, if available |
| Calculator, assessment, readiness score, quiz, any interactive mini-tool | `free-tools` (pack `marketing-engine-skills`) |
| Planning and distributing a reusable magnet | `lead-magnets` (pack `marketing-engine-skills`) |
| Landing page or thank-you page for the magnet | `page-builder` (standalone repo), copy via `copywriting` (pack `marketing-engine-skills`) |
| Case study as the asset | `case-study-writer` (pack `account-management-skills`) |
| Webinar or event | `slide-deck-builder` (pack `sales-engine-skills`) plus a promo asset |
| Mini-audit or teardown of the lead's website copy | `website-copy-reframe` (pack `marketing-engine-skills`) |
| Teardown of a named account or its market | `account-dossier` (pack `account-management-skills`) |
| GTM-shaped mini-audit (one criterion, not the full audit) | `gtm-audit` (pack `gtm-strategy-skills`) |
| Client brand kit missing | `design-system-generator` (standalone repo), first |
| Near-deal, proposal-grade asset | `proposal-generator` (pack `sales-engine-skills`) |
| The delivering email or DM itself | `reply-objection-handler` (pack `outbound-engine-skills`) or the nurture track's own copy step |

If the asset is for a client company and it has no design system yet, run
`design-system-generator` first. Tell the user which skill you are dispatching to and why, then
hand over the spec.

---

## Step 6: Log it back into the nurture program

- Attach the finished asset (or its spec and the build output) to the **specific nurture touch** in
  the `nurture-architect` program document: which track, which touch number, gated or not.
- If it is reusable, add it to the company's **asset inventory** so later touches reuse it (this
  feeds Step 0).
- Give the user a one-line recap: asset type, the objection it clears, the touch it fills, the
  build skill used, and any open data gap.

Where the program lives in Notion (connector available), update the page there; otherwise update
the markdown program document.

---

## Where this sits

```
nurture-architect      →   nurture-value-factory      →   build skills
  WHEN + which track        asset or not? which type?      produce the asset
                            spec + reuse check             (docx / free-tools / page-builder /
                            route to builder                website-copy-reframe / ...)
```

- Upstream: `nurture-architect` (program); `agency-signal-sourcer` (pack `gtm-skills`, what
  triggered the lead); `icp-builder` (pack `outbound-engine-skills`) or the company's ICP document.
- CTA rules: `cta-interest-based`. Voice: `anticopywriting-ai`.

## Common pitfalls this skill prevents

1. **Building a magnet when a sentence would do.** Step 1 gates it.
2. **A generic PDF for an engaged lead.** Misses the sample-of-real-work advantage.
3. **Rebuilding what exists.** Skipping the inventory wastes effort.
4. **Wrong-stage asset.** An ROI calculator for a Researcher who does not feel the problem yet.
5. **Format soup.** Ebook plus video plus sheet in one asset. Pick one.
6. **Over-gating top of funnel.** A long form on an awareness asset. Email only, or ungated.
7. **Pitch-heavy asset or call CTA.** Breaks 80/20 and the interest-only rule.
8. **Off-brand output.** A client asset in someone else's colours.

## Credits

Built by Victor Shulga for B2B service companies; the eight-step lead-magnet method, the
three-type test and the asset-family taxonomy are his. The quality bar in the library (§0) is
adapted from Tim Keen's *The 2025 Agency Growth Bible* (a free guide he distributes on
LinkedIn), restated here in our own words.
