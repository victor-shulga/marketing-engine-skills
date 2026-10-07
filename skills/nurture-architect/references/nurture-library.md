# Nurture library: cadences, weights, sequences

The parts bin for `nurture-architect`. Assemble these into the company's program and fill every
bracket with the company's real ICP, offers and proof, or flag the gap. Everything here is tuned
for a B2B service company (high deal value, long cycle, buying committee), not self-serve SaaS.
The point values and day counts are starting defaults to tune, not measured benchmarks.

## Contents
1. Two-axis scoring weights
2. Track cadences (Researcher, Evaluator, "not now" reply)
3. Behavioural branching rules
4. Re-engagement sequences (dormant lead, lost proposal)
5. Renewal drip (retainer businesses)
6. Churn early-warning model
7. Content-by-awareness menu
8. Anti-pattern cheat sheet

---

## 1. Two-axis scoring weights

Two independent axes, 0-50 each. Total above 40 = enter nurture (MQL); above 70 = hand to sales
(SQL).

**Fit 0-50** (who they are):
- Decision-maker title matches an ICP persona: 0-20
- Company size in the target range: 0-15
- Vertical on the target list: 0-15

**Engagement 0-50** (what they did):
- Content or lead magnet pulled: 5 each
- Site visit of more than 5 pages: 10
- Webinar or event attended: 15
- Services or pricing page viewed: 20
- Replied with a real question or curiosity: 20
- Explicit hand-raise (asked for samples, a call, a quote): 50, automatic SQL

**Service-company adjustment.** Engineering and technical buyers rarely download content. If the
company has no content funnel, move the engagement weight onto reply behaviour and site visits,
and lean harder on fit signals that are public: hiring for the role the company provides (for
example BIM coordinators, MEP engineers, GIS analysts), won public or infrastructure tenders,
building permits, visible capacity gaps. Put these into fit, or into a third "trigger" axis if the
company runs signal-led outbound.

---

## 2. Track cadences

Each touch = timing, channel, content theme, copy angle (in the prospect's language). The first
soft CTA (interest-based only) is marked. Educational to company content stays at 80/20.

### Track A: Researcher (pulled educational content)
Early stage, learning. Slow and dense with value.
- **Week 1**, email: "Since you grabbed [resource], here is a related template or checklist."
- **Week 2**, email: a case from the same industry (anonymised), and the problem it solved.
- **Week 4**, email: a webinar or teardown invite: "How [industry] teams handle [problem]."
- **Week 6**, email: a benchmark or data drop: "[Year] [industry] benchmarks."
- **Week 8**, email: **first soft interest CTA** ("Want the deeper version for your situation?").
- Every email ends with a question.

### Track B: Evaluator (visited services, pricing or comparison pages, or asked about price or alternatives)
Middle stage, comparing. Faster, heavier on proof and ROI.
- **Week 1**, email: buyer's-guide angle: "How [peer] evaluated [category] partners."
- **Week 2**, email: ROI framing plus a case with a real number (cost per deliverable saved,
  throughput change, saving against an in-house hire).
- **Week 3**, email: an honest comparison with the alternatives. Say where you are NOT the right
  fit; a nervous committee trusts a vendor that does.
- **Week 4**, email: **first soft interest CTA** ("Would a scoped look at your [project] help?").
- **Week 5**, email: "Still comparing? Here is a reference in your vertical" (interest CTA).

### Track C: "Not now" reply or event (usually the most valuable for service companies)
Engaged, wrong timing. Short, respectful, keeps the door open.
- **Day 1**, reply or email: acknowledge the timing, leave one useful asset. No ask.
- **Day 3**: a same-industry case or a recording.
- **Day 7**: "one thing most [role]s miss about [problem]".
- **Day 14**: **soft interest CTA** tied to the timing they gave ("When [quarter] gets closer,
  worth a look at [X]?").
- If they named a date to revisit, schedule the soft-CTA touch to land about two weeks before it.

**Every track:** copy stays generic on anything public; CTAs come from an interest-based bank; each
message ends on a question.

---

## 3. Behavioural branching rules

Write them as if-then rules for RevOps or the sending tool's automation:
- Clicked services or pricing → move to **Evaluator**.
- No opens for 30 days → move to **re-engagement**.
- Real-interest reply or hand-raise → **leave nurture**, log SQL, hand to sales.
- No open on touch 1 → hold; do not advance until there is an open. Never send touch 4 to a lead who
  ignored touch 1.
- Bounce or job change detected → suppress, or re-route to the new contact (job-change play).

---

## 4. Re-engagement sequences

**Rule one: never "we miss you".** Lead with what changed. Prerequisite: a **"What's new"
inventory** of 3 improvements, 2 new services or integrations, 1-2 cases in their vertical, and any
change in packaging that helps them.

### Dormant lead: 3 touches over 14 days
- **Day 1**: "Since you looked at [original topic], we have added [one new thing]." Plus a related
  asset.
- **Day 7**: a new insight or piece of research on their original interest.
- **Day 14**: close the file: "Closing your file for now. If [problem] is still live, [new thing]
  has been working well for teams like yours. Is it worth keeping on your radar?"

### Lost proposal or churned client: 3 touches over 21 days
- **Day 1**: "We have changed [the two things that mattered most to you] since we last spoke. Would
  a short walkthrough be useful?"
- **Day 10**: a case: a similar firm got [result] with what was added.
- **Day 21**: a concrete reason to return: a scoped pilot, waived onboarding, or the old terms kept.

### Segment by recency
- **Cold** 3-6 months → full series.
- **Frozen** 6-12 months → shortened series, "what changed" angle.
- **Dead** 12+ months → one email, then suppress if there is no reply.

### Sunset and hygiene
- 6 months without engagement → re-engagement track.
- 12 months without engagement → suppress from all nurture (keep in the database for reactivation
  only).
- Clean the list every quarter to protect sender reputation and sending costs.

---

## 5. Renewal drip (retainer businesses)

Fires at 90, 60, 30, 14 and 7 days before renewal. Value first, discount last.
- **90 days**: a summary of the year's value: deliverables shipped, cycle-time gains, cost against
  an in-house team, defects avoided. Not a discount.
- **60 days**: what is new, and capacity the company can add.
- **30 days**: a check-in: "Is this still giving you value? What could be better?"
- **14 days**: the renewal offer (locked terms, added scope).
- **7 days**: what they would lose (the thing they rely on most).

Starting at 30 days misses the window for building the case.

---

## 6. Churn early-warning model

Leading indicators 60-90 days before a retainer ends. Score 0-100 and act by band. The weights are
a starting point; recalibrate them on the company's own churned accounts.

| Signal | Points |
| :-- | :-- |
| Champion or sponsor left (job change visible on LinkedIn) | 40 |
| Work routed to you down by half or more | 35 |
| Silent for 30+ days (no replies to the account or project manager) | 30 |
| Missed a review or QBR | 20 |
| Payments 15+ days late | 15 |
| New stakeholders questioning scope, or build-vs-buy | 15 |

Bands: **Red 70+** → intervene within hours (senior and executive contact, root cause, a named
action plan). **Yellow 40-69** → project manager outreach this week plus value reinforcement.
**Green below 40** → monitor.

The champion leaving is the strongest single signal. Set up a job-change watch on every key client
contact.

---

## 7. Content-by-awareness menu (feeds the content behind nurture)

Uses Eugene Schwartz's five awareness levels. Each asset serves one level and carries one CTA.
- **Unaware** → educational posts, industry data → earn attention.
- **Problem-aware** → how-to guides, checklists → name the problem.
- **Solution-aware** → comparison pages, webinars → position the category.
- **Product-aware** (here: aware of the company's service) → cases, teardowns, a scoped pilot →
  convert.
- **Most aware** → clear pricing, ROI calculator → close.

Content production belongs to the content skills (for example pack `content-engine-skills`); this
menu only tells you which asset a nurture touch should link to.

---

## 8. Anti-pattern cheat sheet

- One track for everyone → build three or more tracks by entry source.
- Sales-heavy emails → 80/20, first harder CTA around touch 5.
- No behavioural branching → gate progression on engagement.
- "We miss you" → lead with what changed.
- Endless nurture → 6- and 12-month sunset plus quarterly hygiene.
- Discounting to win back recent churn → lead with what changed in the service, not with price.
- Treating a paying but quiet client as churned → that calls for a health intervention, not a
  win-back.
- A call-based CTA anywhere in a sequence → interest-based only.
- Invented ICP or entry sources → flag "to confirm on discovery".
