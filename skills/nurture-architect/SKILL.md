---
name: nurture-architect
description: >-
  Designs a complete lead-nurture (lead-warming, "догрів") program for a B2B service company
  and ships it as one readable document: two-axis lead scoring (fit + engagement), nurture
  tracks keyed to how the lead entered (Researcher, Evaluator, "not now" reply), behavioural
  branching, re-engagement and sunset rules, and, for retainer businesses, renewal drips and a
  churn early-warning model. Use when the user says "build a nurture program", "lead nurture",
  "what do we do with leads that are not ready", "the lead said not now, what next",
  "re-engagement", "win-back", "renewal campaign", "побудуй нурчур", "трек догріву", "прогрів
  лідів", "реактивація бази", "догрів пропоузалів що злили", or hands over not-ready leads,
  "not now" replies or a dormant base. Not for one reply (use reply-objection-handler), not
  for a cold sequence (use sequence-writer), not for analysing a batch of replies (use
  reply-audit).
---

# Nurture Architect

You design the lifecycle and nurture layer for a B2B service company: agencies and outsourcing
firms selling engineering, design, software, data or consulting work. These are **high-value,
long-cycle deals**. A services buyer often spends 3-12 months evaluating, with a buying committee.

Most leads are not a "no". They are a "not yet". Nurture is the system that keeps the company in
the buyer's mind through that window and turns not-ready leads into pipeline, instead of sending
everything to sales and hoping. Your job: design the full architecture and ship it as one readable
program document.

**This is not SaaS product-lifecycle nurture.** There is no product telemetry, no seat usage, no
in-app activation moment. The signals are: how a lead entered (content, site, a "not now" reply),
how they respond to follow-ups, and, for existing retainer clients, the health of the delivery
relationship. Adapt every borrowed SaaS idea to that reality.

## Language and voice

- **Answer the user and write the program document in the user's language.** If it is Ukrainian,
  use plain words and avoid anglicisms (догрів / прогрів, оцінка лідів, дозбір даних, стоп-фільтр,
  ОПР). Tool names stay in Latin script.
- **Email and DM copy inside the sequences is written in the prospect's language** (often
  English). Label it clearly.
- Edit the prose for AI tells before delivering. If installed, use `anticopywriting-ai` (pack
  `gtm-skills`).

## Hard rules (they override any borrowed template)

1. **Interest-based CTAs only.** Nurture sequences never ask for a call, a meeting or a time slot.
   If installed, load `cta-interest-based` (pack `outbound-engine-skills`) and use its CTA bank.
   The first soft CTA appears no earlier than the touch set for each track below.
2. **Every email or message ends with a question** (the soft CTA).
3. **80/20.** 80% educational, 20% about the company. A drip that pitches in every email gets
   unsubscribed. The first harder CTA comes around touch 5 of a track, not touch 1.
4. **Never invent client data.** If ICP tiers, entry sources or offers are unknown, write
   "to confirm on discovery, not invented" and design around the gap.
5. **The program document is the deliverable.** It is a readable narrative, never a dump of rows.
   If a scoring matrix or tracker is needed, it lives in a separate table or database and the
   document links to it.
6. **Confidentiality.** Anything that could end up in a public asset stays generic: no client
   names, no third-party vendor names.

---

## Step 0: Gather inputs (do not invent)

Load what exists: the company's ICP document, any GTM audit, offers, previous sequences, and the
user's brief. You need:

| Input | Where it usually lives | If missing |
| :-- | :-- | :-- |
| ICP tiers and personas (titles, verticals) | ICP document | flag "to confirm on discovery" |
| Offers / services and any lead magnets | website, design system, proposals | list what exists, note gaps |
| Entry sources actually in use | outreach platform, content, forms, website | design only for real sources |
| Available channels | email platform, LinkedIn tool, ads | design for what they run |
| Retainer or new-logo motion? | the user's brief | decides whether Step 6 applies |

Confirm in one line what you loaded. If the user handed over a concrete batch of not-ready leads or
"not now" replies, that batch decides which tracks come first.

**Read `references/nurture-library.md` now.** It holds the cadences, scoring weights and
re-engagement structures you will assemble. This file is the workflow; the library is the parts.

---

## Step 1: Two-axis lead scoring (the foundation)

Never one threshold. Build two independent axes so fit and interest cannot be confused (a director
who opened one email is not the same lead as a junior who booked a call).

- **Fit 0-50**: match with the ICP. Decision-maker title, company size, vertical.
- **Engagement 0-50**: behaviour. Content pulled, pages viewed, a curious reply, a webinar
  attended, a visit to the services or pricing page, a question asked back.

Starting thresholds (tune per company): **total above 40 → nurture (MQL)**, **above 70 → sales
(SQL)**. Weights and the full signal table are in the library. Engineering and technical buyers
rarely download content but reveal fit through tenders, permits and hiring. If the company has no
content funnel, weight engagement on reply behaviour and site visits, not downloads.

Output a scoring table with the company's real titles and verticals filled in, or flagged.

---

## Step 2: Map entry sources to tracks

The most common nurture mistake is one drip for everyone. Design **at least three tracks**, keyed
to how the lead entered, because the entry point shows intent. Default mapping (adapt to the
company's real sources):

| Track | Entry signal | Intent | First soft CTA at |
| :-- | :-- | :-- | :-- |
| Researcher | pulled a lead magnet or educational content | early, learning | touch 5 (about week 8) |
| Evaluator | visited services, pricing or comparison pages, or asked "how much / compared to whom" | middle, comparing | touch 4 (about week 4) |
| Reply / event | replied "not now / not this quarter", or attended a webinar | interested, wrong timing | touch 3-4 |

For service companies the **"not now" reply track is usually worth the most**: these are outbound
leads who engaged but were mistimed. Prioritise it. Week-by-week cadences are in the library; fill
them with the company's real proof.

---

## Step 3: Design each track's cadence

For each track in scope, write the actual sequence: each touch gets a day or week, a channel, a
content theme and the copy angle (in the prospect's language). When a touch calls for a produced
value asset (lead magnet, template, SOP, mini-audit, calculator), hand that touch to
**`nurture-value-factory`** (pack `marketing-engine-skills`, if installed). It decides whether an
asset is warranted, picks the type by stage and objection, and routes the build. Apply:

- **80/20.** Touches 1-4 give value (a template, an industry case, a benchmark, an insight). Around
  touch 5 comes the first soft interest CTA.
- **Layer channels** where the company has them: email first; a LinkedIn connection and engagement
  for scored MQLs; retargeting by stage if they run ads; a physical gift only for truly strategic
  accounts (never during an active negotiation, and check public-sector gift policies).
- **Openers that reference the source.** "Since you looked at [X]..." beats a generic intro.
- Every message ends on a question. CTAs come from the interest-based bank only.

---

## Step 4: Behavioural branching rules

Static drips waste sends and damage sender reputation. Specify the routing:

- Clicked **services or pricing** → move to the **Evaluator** track.
- **No opens for 30 days** → move to **re-engagement**.
- Replied with real interest → **leave nurture, hand to sales**, log as SQL.
- Never send touch 4 to someone who never opened touch 1. Progression is gated on engagement.

Write these as if-then rules a RevOps person can implement in the company's CRM or sending tool
(for example Clay, Instantly, HubSpot).

---

## Step 5: Re-engagement and sunset

Dormant leads and lost proposals are the cheapest pipeline: they already know the company.
**Rule one: never "we miss you".** Open with what changed since they last engaged: a new service, a
fresh industry case, new proof. Before any re-engagement send, build a **"What's new" inventory**
(3 improvements, 2 new services or capabilities, 1-2 relevant cases).

- **Dormant lead: 3 touches over 14 days**, ending with a polite close-the-file message.
- **Lost proposal or churned client: 3 touches over 21 days**, with a concrete reason to come back
  on touch 3.
- **Segment by recency:** cold 3-6 months (full series), frozen 6-12 months (shortened series),
  dead 12+ months (one email, then suppress).
- **Sunset and hygiene:** 6 months without engagement → re-engagement; 12 months → suppress from
  all nurture; clean the list every quarter to protect deliverability. Endless nurture destroys
  sender reputation.

Full sequences and the "what changed" framing are in the library.

---

## Step 6: Renewal and churn early warning (retainer businesses only)

Skip this for a pure new-logo motion. For companies on retainers, nurture extends into retention:

- **Renewal drip at 90, 60, 30, 14 and 7 days before renewal.** 90 days: a summary of the value
  delivered this year (not a discount). 60 days: what is new. 30 days: a check-in. 14 days: the
  renewal offer. 7 days: what they would lose. Starting at 30 days is too late.
- **Churn early warning, 60-90 days out.** The champion leaving (visible on LinkedIn) is the
  strongest single signal that a retainer will end. Others: less work routed to the company, the
  client going quiet, a missed review. Score it (weights in the library). Red means intervene
  within hours, not at renewal. For a service company this measures the health of the delivery
  relationship, not product usage.

---

## Step 7: Measurement

Specify what to track so the program can be improved:

- Per track: opens, replies, MQL to SQL conversion, opportunities, pipeline influenced.
- Stage conversion and median time in stage (where do leads stall or leak?).
- Exit rules firing correctly (nobody stuck in nurture forever).
- An A/B test plan for at least one element per track (subject, timing or content format).

---

## Step 8: Ship the program document

Output format:
- a **Notion page** under the company's workspace, if a Notion connector is available;
- otherwise a **markdown document** (or .docx via the docx skill, if the user prefers).

Use this skeleton (headings in the user's language; Ukrainian version shown):

```
# Догрів лідів: [Компанія]
> Головна думка (2-3 речення: хто в догріві, скільки треків, головний важіль)

## 1. Оцінка лідів (дві осі)
   таблиця Fit 0-50 / Engagement 0-50 + пороги MQL > 40 / SQL > 70

## 2. Треки за точкою входу
   таблиця треків, для кого, перший м'який CTA

## 3. Каданси по треках
   по кожному треку: дотики (день, канал, тема, кут копії мовою проспекта)

## 4. Поведінкове розгалуження
   правила «якщо, то»

## 5. Реактивація і стоп-політика
   серії для сплячих лідів і програних пропозицій, сегменти за давниною, гігієна бази

## 6. Продовження і рання діагностика відтоку   [лише для ретейнерів]
   90/60/30/14/7 + ранні сигнали відтоку зі скорингом

## 7. Вимірювання
   показники по треках, конверсія між етапами, план A/B-тестів

## 8. Дії (відповідальний + дата)
   що впровадити цього тижня, хто і коли; прогалини даних = «уточнити на discovery»
```

Data-quality warnings (unknown ICP, no content funnel, missing entry sources) go **near the top**,
not buried at the end. If a scoring or tracking matrix is needed, keep it in a separate table and
link it.

After shipping, give the user the link or file path and a three-bullet recap: the priority track,
the biggest data gap, and the one thing to ship this week.

---

## Common pitfalls this skill prevents

1. **One drip for everyone.** No entry-source tracks. Build at least three.
2. **Pitch-heavy drips.** Every email asks for a call. Enforce 80/20 and interest-only CTAs.
3. **No branching.** Leads get touch 4 after ignoring touch 1. Gate on engagement.
4. **"We miss you" re-engagement.** Lead with what changed.
5. **Endless nurture.** No sunset. Use 6- and 12-month exits and quarterly hygiene.
6. **SaaS-shaped copy.** Product-usage language aimed at a services buyer. Reframe to delivery,
   capacity and how they evaluate vendors.
7. **Invented ICP or sources.** Flag "to confirm on discovery" instead.

## Related skills (optional, if installed)

- `nurture-value-factory` (pack `marketing-engine-skills`): picks and builds the value asset for a
  touch.
- `cta-interest-based`, `sequence-writer`, `reply-objection-handler`, `reply-audit`, `icp-builder`
  (pack `outbound-engine-skills`).
- `content-run` and the rest of pack `content-engine-skills`, or `linkedin-post-writing`
  (standalone repo): produce the content the nurture touches link to.

## Credits

Built by Victor Shulga for B2B service companies. The content-by-awareness menu in the library
uses Eugene Schwartz's five levels of customer awareness from *Breakthrough Advertising* (1966).
