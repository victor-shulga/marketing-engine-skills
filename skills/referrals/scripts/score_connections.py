#!/usr/bin/env python3
"""Score a LinkedIn Connections.csv export against an ICP and build an intro shortlist.

The connector (a happy client, a referrer, an advisor) exports their own connections
(LinkedIn > Settings > Data privacy > Get a copy of your data > Connections) and shares
the file. This script ranks those connections so you can bring the connector a short,
specific list instead of asking "do you know anyone?".

Standard library only. Usage:

    python3 score_connections.py --connections Connections.csv --icp icp.json \
        [--exclude exclude.csv] [--top 15] [--out shortlist.csv]

icp.json format: see references/icp-example.json.
exclude.csv: any CSV with a "company" and/or "url" column (current clients, open deals,
competitors, the connector's own company). Matching is case-insensitive.
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime


def read_connections(path):
    """LinkedIn puts a 'Notes:' preamble above the header; skip to the real header row."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        lines = f.read().splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("First Name,")), None)
    if start is None:
        sys.exit("No 'First Name,...' header found. Is this a LinkedIn Connections.csv export?")
    return list(csv.DictReader(lines[start:]))


def compile_rules(rules):
    return [(re.compile(r["pattern"], re.I), r["points"], r.get("label", r["pattern"])) for r in rules]


def best_match(text, rules):
    """Highest-scoring rule that matches; rules do not stack within one block."""
    hits = [(pts, label) for rx, pts, label in rules if rx.search(text or "")]
    return max(hits) if hits else (0, "")


def any_match(text, patterns):
    return any(re.search(p, text or "", re.I) for p in patterns)


def connected_year(value):
    for fmt in ("%d %b %Y", "%d-%b-%y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value.strip(), fmt).year
        except (ValueError, AttributeError):
            continue
    return None


def load_exclusions(path):
    companies, urls = set(), set()
    if not path:
        return companies, urls
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            row = {k.strip().lower(): (v or "").strip() for k, v in row.items() if k}
            if row.get("company"):
                companies.add(row["company"].lower())
            if row.get("url"):
                urls.add(row["url"].lower().rstrip("/"))
    return companies, urls


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--connections", required=True)
    ap.add_argument("--icp", required=True)
    ap.add_argument("--exclude")
    ap.add_argument("--top", type=int, default=15, help="shortlist size (keep it small: 3-5 asks per connector)")
    ap.add_argument("--out", default="shortlist.csv")
    args = ap.parse_args()

    icp = json.load(open(args.icp, encoding="utf-8"))
    title_rules = compile_rules(icp.get("titles", []))
    company_rules = compile_rules(icp.get("companies", []))
    market_rules = compile_rules(icp.get("markets", []))
    title_stop = icp.get("title_exclude", [])
    company_stop = icp.get("company_exclude", [])
    min_score = icp.get("min_score", 0)
    recency = icp.get("recency_points", {})  # {"2026": 2, "2025": 1}
    ex_companies, ex_urls = load_exclusions(args.exclude)

    rows = read_connections(args.connections)
    company_counts = Counter((r.get("Company") or "").strip().lower() for r in rows if r.get("Company"))

    scored, dropped = [], Counter()
    for r in rows:
        name = f"{r.get('First Name', '')} {r.get('Last Name', '')}".strip()
        company = (r.get("Company") or "").strip()
        position = (r.get("Position") or "").strip()
        url = (r.get("URL") or "").strip()
        if not company and not position:
            dropped["no data"] += 1
            continue
        if company.lower() in ex_companies or url.lower().rstrip("/") in ex_urls:
            dropped["excluded list"] += 1
            continue
        if any_match(position, title_stop):
            dropped["title stop-word"] += 1
            continue
        if any_match(company, company_stop):
            dropped["company stop-word"] += 1
            continue

        t_pts, t_label = best_match(position, title_rules)
        if t_pts == 0:
            dropped["title not in ICP"] += 1
            continue
        c_pts, c_label = best_match(f"{company} {position}", company_rules)
        m_pts, m_label = best_match(f"{name} {company} {position}", market_rules)
        year = connected_year(r.get("Connected On", ""))
        r_pts = recency.get(str(year), 0) if year else 0
        same_co = company_counts.get(company.lower(), 0)
        # 2+ people at one account = more than one door into the same company.
        multi_pts = icp.get("multi_contact_points", 0) if same_co >= 2 else 0
        score = t_pts + c_pts + m_pts + r_pts + multi_pts
        if score < min_score:
            dropped["below min_score"] += 1
            continue
        why = "; ".join(x for x in (t_label, c_label, m_label,
                                     f"connected {year}" if r_pts else "",
                                     f"{same_co} contacts at company" if multi_pts else "") if x)
        scored.append({"score": score, "name": name, "position": position, "company": company,
                       "url": url, "email": r.get("Email Address", ""), "connected_on": r.get("Connected On", ""),
                       "why": why, "connector_knows": "", "intro_ok": ""})

    scored.sort(key=lambda x: (-x["score"], x["company"].lower()))
    fields = ["score", "name", "position", "company", "url", "email", "connected_on", "why",
              "connector_knows", "intro_ok"]
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(scored[: args.top])

    print(f"connections read:   {len(rows)}")
    print(f"matched ICP:        {len(scored)}")
    for reason, n in dropped.most_common():
        print(f"dropped, {reason}: {n}")
    print(f"shortlist written:  {min(args.top, len(scored))} -> {args.out}")
    print("Next: the connector fills connector_knows (well / a bit / no) and intro_ok (yes / no).")


if __name__ == "__main__":
    main()
