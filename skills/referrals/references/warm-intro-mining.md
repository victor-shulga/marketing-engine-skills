# Warm Intro Mining: Find the Right People in a Connector's Network

Most B2B service firms already live on referrals, yet the referrals arrive by accident. The client mentions you over dinner, a business club member passes your name on. Nobody chooses who gets introduced, nobody tracks it, nobody asks twice.

This flow turns that into a process. You look at the LinkedIn network of someone who already trusts you, pick the few people who match your ICP, and ask for those specific introductions. "Do you know anyone?" usually gets "I'll think about it". A named shortlist gets introductions.

## When to Use

- The company says "clients already recommend us", but nobody can show where the intros come from or how many arrive per month
- Customer interviews show that buyers find vendors through people they know: business clubs, peers, former colleagues
- After a client hits a result (first result delivered, launch, a fixed incident, project end). That is when the ask lands best
- When an open deal stalls: someone who knows the buyer can tell you who decides now

## Who Counts as a Connector

| Connector | Why they help | Ask when |
|---|---|---|
| Happy client (owner or project lead) | trusts your work, knows peers with the same problem | right after a result with a number |
| Person who referred a past deal | already referred you once, so the next ask is easy | when that deal closes or stalls |
| Advisor, investor, business-club organizer | large network of owners | quarterly, with a fresh case study |
| Former client employee who moved to another company | knows you and the new company's problems | 1–3 months after the move |

Do not ask a client who has an open complaint or an unpaid invoice. Fix the relationship first.

## Step 1: Get the Network (Legitimately)

There are two clean routes. Use the first one whenever possible.

**Route A: the connector shares their own export.** LinkedIn > Settings > Data privacy > Get a copy of your data > Connections. The file arrives within minutes as `Connections.csv` (name, profile URL, company, position, connection date, and email only if the person allowed it). Frame the ask around the connector's control: "Send us your connections file. We'll pick 3–5 people who might need us, and you decide whether to introduce any of them."

**Route B: your own account, if the connector is your 1st-degree connection.** LinkedIn search > People > filter "Connections of" > the connector, plus title and industry filters. Sales Navigator has the same filter. It works only if the connector has not hidden their connection list. Copy the matches by hand into a CSV with the same columns.

**Do not** scrape someone else's connections with browser automation or session cookies. It breaks LinkedIn's terms, puts your account at risk, and the connector never agreed to it. An intro that starts with a privacy violation tends to go nowhere anyway.

## Step 2: Score Against the ICP

Run the bundled script. It uses the standard library only and needs no API keys:

```bash
python3 scripts/score_connections.py \
  --connections Connections.csv \
  --icp icp.json \
  --exclude exclude.csv \
  --top 15 \
  --out shortlist.csv
```

- `icp.json` holds the user's ICP as regular-expression rules: titles (who decides), companies (what business), markets, stop-words, points for a recent connection and for having 2+ contacts at one company. Start from `references/icp-example.json` and replace every rule. Never run the example ICP on a real network.
- `exclude.csv` lists current clients, open deals, competitors and the connector's own company (columns `company` and/or `url`).
- The output keeps the top N rows with a `why` column and two empty columns for the connector: `connector_knows` and `intro_ok`.

The score is a triage of title plus company name. The export has no headcount, revenue or website. Before anything goes to the connector:

1. Read every row. Remove false positives: agencies with "store" in their name, HR people with "director" in their title, competitors.
2. For the top 10, check the company site and LinkedIn page: size, market, any visible trigger (hiring, new location, slow site, a stalled project).
3. Write one line per person: why this company might need you now. If you cannot write that line, drop the person.

If the ICP itself is not written down yet, stop and write it first. Without one, the shortlist turns into "everyone with CEO in the title".

## Step 3: Bring the Connector a Short List

Send 3–5 names. Each comes with one line on why you think they fit. Twenty names reads like a lead-generation request and gets ignored.

Template (adapt the language and tone to the relationship):

> [Name], thanks again for [result with a number]. We looked through your network and found a few people who might have the same problem you had: [person 1, company, one line why], [person 2, ...], [person 3, ...]. Do you know any of them well enough to introduce us? Totally fine if not.

Then let the connector mark each row: knows well / a bit / not really, and whether an intro is OK. Only "knows well + yes" moves forward. A cold intro from someone who barely knows the person hurts both of you.

## Step 4: Make the Intro Easy (Double Opt-In)

The connector asks the target first ("Can I connect you with the team that fixed our site?") and only then sends the intro. Give the connector a forwardable blurb written for the target:

> [Company] helped us [result with a number] in [time]. They work with [ICP type] that [problem]. Worth a 20-minute call if [trigger] sounds familiar.

Attach one case study link at most. No price list, no deck.

## Step 5: Handle the Intro

- Reply within one business day, thank the connector in the same thread, and move the connector to BCC
- Open a deal in the CRM: source = referral, referrer = connector name, connector type
- Tell the connector how it went, whether or not a deal closed. People who hear back refer again
- Reward per the program rules. For B2B owners, service credit (support hours, an extra module) usually works better than cash. Never mention a reward in the first ask

## Step 6: Measure Monthly

| Metric | Target to start with |
|---|---|
| Connectors asked | every client with a result this month |
| Shortlists sent | 1 per connector |
| Intros made per shortlist | ≥1 |
| Intro → call | ≥50% |
| Call → deal | same as or better than other channels |
| Share of new revenue from referrals | track the trend; set a target after 3 months |

Keep a simple log: connector, date asked, names shortlisted, intros made, calls, deals, revenue. The log shows which connectors produce, and those become candidates for a formal partner program (see `affiliate-programs.md`).

## Common Mistakes

| Mistake | Fix |
|---|---|
| "Know anyone who needs a website?" | a named shortlist with a reason per name |
| 20+ names in one ask | 3–5 names; the rest can wait for next quarter |
| Asking right after an invoice or a bug | ask right after a result with a number |
| Intro arrives, reply takes three days | same-day reply, connector thanked publicly |
| Connector never hears back | tell them the outcome every time |
| Scraping networks without consent | Route A or Route B only |
