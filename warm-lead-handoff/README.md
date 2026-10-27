# Warm-Lead Handoff: what to give the assistant

This skill turns your LinkedIn, website-visitor and CRM data into a short list of accounts that sales should contact, with one line a rep can say out loud. The assistant only reads what you give it, so this page explains which files to prepare. Everything except the account file is optional, but each missing file removes a check, and the assistant will say which.

## How to use it

1. Add `SKILL.md` to your assistant (a Claude skill, a custom GPT or Gem, or paste it as instructions).
2. Start a new chat and attach your files in the first message.
3. Ask, for example: `Build this month's warm-lead handoff for <client> from these files. The client settings are in config.json.`

If a file is capped or a source has gone dark, the assistant stops before ranking and asks whether to re-pull first or to continue with a list marked provisional. Reply "go" to continue.

The assistant gives recommendations only. It changes nothing in your ad account or CRM.

## The files

| File | Needed? | What it holds |
|---|---|---|
| `accounts.csv` | Yes | One row per company per month: LinkedIn and website signals |
| `config.json` | Strongly recommended | Your ICP and the lists used for cleaning |
| `crm.csv` | Recommended | Who is already a customer, has an open deal or lost a deal, and who owns it |
| `people.csv` | Optional | Named website visitors, so handoff lines can say who to call |
| `leads.csv` | Optional | Form fills, so genuine requests rank first |
| `manifest.json` | Optional | A log of how each file was pulled, so capped or stale data is caught |
| Previous handoff list | Optional | Last run's list, so the assistant can mark accounts as new, repeat, rising or quieter |

You do not need to build these exactly. The assistant accepts raw exports (LinkedIn Companies tab, your visitor tool, a CRM export) and will map the columns. The column names below are what the skill expects when you prepare the files yourself.

**Do not rely on JSON if you do not want to.** `config.json` and `manifest.json` can be a table or plain text typed in the chat. JSON is only a tidy way to keep the same settings between runs.

## accounts.csv

One row per company and month. Pull LinkedIn from Campaign Manager (Plan, then Companies; LinkedIn caps the export at 15,000 rows and offers 7, 30, 60, 90 and 180 day windows). Pull website data from your visitor identification tool.

| Column | Meaning |
|---|---|
| `company`, `domain` | Company name and website domain |
| `employee_size`, `industry` | As in LinkedIn or your visitor tool, for example `1001-5000` |
| `month` | `YYYY-MM` |
| `paid_impressions`, `paid_engagements`, `paid_clicks` | LinkedIn ads |
| `organic_engagements` | LinkedIn company page and posts |
| `site_sessions`, `sales_page_views` | Website visits by that company |
| `site_people` (optional) | Number of named people seen |
| `pages_read` (optional) | Pages read, separated by `;` |
| `top_ad` (optional) | The ad that company engaged with most |

## config.json

Your settings. Example:

```json
{
  "client": "Northwind Merch",
  "months": ["2026-08", "2026-09"],
  "window_label": "August 1 to September 30, 2026",
  "icp_sizes": ["501-1000", "1001-5000", "5001-10000", "10001+"],
  "buyer_functions": ["Human Resources", "Marketing", "Events", "Operations", "Executive"],
  "own_domains": ["northwindmerch.com"],
  "agency_domains": ["impactable.com"],
  "competitor_domains": ["rivalpromo.com"],
  "cluster_max_impressions": 10,
  "cluster_min_companies": 3,
  "stale_after_days": 7
}
```

| Key | Meaning |
|---|---|
| `client` | Whose handoff this is |
| `months` | The months in the data |
| `window_label` | Text shown in the answer |
| `icp_sizes` | Company sizes that count as a fit |
| `buyer_functions` | Departments that buy from you |
| `own_domains`, `agency_domains`, `competitor_domains` | Removed from the sales list; competitors and agencies also go on the ad exclusion list |
| `cluster_max_impressions`, `cluster_min_companies` | Shared-profile cluster test: this many companies or more with identical engagement on this many impressions or fewer are treated as one person counted at every company on their profile (defaults 10 and 3). Only identical counts of 5 or more on at least 1 impression qualify; small identical counts such as 3 or 4, and rows with no paid impressions, are never treated as a cluster |
| `stale_after_days` | A source with no data this many days before the end of the window is called dark (default 7) |

The ICP (`icp_sizes`, `buyer_functions`) and `own_domains` are required: if either is missing the assistant asks for it before ranking. The agency and competitor lists are optional.

## manifest.json (the pull log)

Records what each pull returned, so the assistant can tell when a file is cut off or out of date. Example:

```json
{
  "as_of": "2026-10-01",
  "sources": {
    "linkedin_company_monthly": {
      "rows": 60, "limit": 60,
      "returned_total": 801, "source_total": 1350,
      "last_data_date": "2026-09-30"
    },
    "website_sessions": {
      "rows": 40, "limit": 100,
      "last_data_date": "2026-09-12"
    }
  }
}
```

| Key | Meaning |
|---|---|
| `as_of` | The day you pulled the data |
| `rows` | Rows in the file |
| `limit` | The row limit you used or the tool applied. If `rows` equals `limit`, the file is cut off and the lowest-ranked companies are missing |
| `returned_total`, `source_total` | The main metric summed over the file, and over the whole source. The share tells the assistant how much of the real activity the file covers |
| `last_data_date` | The latest date with data. A date more than `stale_after_days` before the end of the window means the source went dark |

Without a manifest, the assistant checks row counts against round limits (1,000, 10,000, 15,000) and reads the dates in the files.

## crm.csv

One row per company, from HubSpot, Salesforce, Attio or similar.

| Column | Meaning |
|---|---|
| `domain` | Used to match accounts (exact domain first, then exact name) |
| `lifecycle` | For example `Customer`, `Opportunity`, `Lead` |
| `owner` | Who owns the account or deal |
| `open_deals`, `open_amount` | Open deals and their amount (say the currency in the chat, or the assistant will write "not stated") |
| `won_deals`, `lost_deals` | Lifetime counts |

Routing: customers go to their owner as expansion, open deals to the deal owner, closed-lost to the owner of the lost deal, and new accounts to the SDR queue.

## people.csv (optional)

| Column | Meaning |
|---|---|
| `person`, `job_title`, `seniority`, `department` | Who visited and what they do |
| `company`, `domain`, `employee_size` | Where they work |
| `linkedin_url` (optional) | Profile link from your visitor tool |
| `visits`, `last_visit` | Activity |

Personal names appear in the answer only if your own visitor tool supplied them and you ask for names in the handoff lines. Without this file, handoff lines lead with signals (sessions, pages, ad engagements) instead of people. Check your privacy policy and your visitor tool's terms before using person-level data.

## leads.csv (optional)

| Column | Meaning |
|---|---|
| `domain`, `email` | The company and the contact |
| `source`, `campaign`, `keyword` | Where the form fill came from |
| `create_date` | Date of the form fill |
| `genuine` | `yes` for a real request, `no` for a placeholder or a duplicate event |

## Company checks and web search

The assistant classifies each remaining company (ICP, customer, competitor, supplier, partner, agency and so on) from the files. If your assistant has web search and a company is still unclear, it may check that company only, cite the source and mark it "web-verified". It never looks people up. Without web search, it marks the company "unclear, please confirm". Either way you confirm every competitor, supplier or partner call.

## What you get back

A cleaning summary (what was removed and why), an Act now list with one handoff line per account, customers engaging (expansion), open deals the signals reached, closed-lost accounts to re-engage, an ad exclusion list, a comparison with the last run if you gave one, up to five recommendations, and what could not be checked. A full list can come as a CSV with a `Client decision` column for you to fill in.
