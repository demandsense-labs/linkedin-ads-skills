# The B2B AI Standard for LinkedIn Ads

Skills and scenarios for running LinkedIn Ads with an AI assistant, written and tested by people who run LinkedIn Ads for a living. Each one reads your exports (or your account through the DemandSense MCP), applies the Standard's rules and tells you what to do. None of them changes anything in your ad account or CRM.

**Browse the collection, with examples and the rules behind each check:** [ds-b2b-ai-standards.vercel.app](https://ds-b2b-ai-standards.vercel.app/collection)

Maintained by [DemandSense](https://demandsense.com).

## Run one in a minute

Attach your exports to a chat with Claude (or any assistant that can read a web page) and paste:

```text
Load the Warm-lead handoff scenario from https://github.com/demandsense-labs/linkedin-ads-skills/tree/main/warm-lead-handoff and run it on the exports I've attached.
```

Swap the name and folder for any skill below. Each skill's page on the [collection](https://ds-b2b-ai-standards.vercel.app/collection) lists the exports it needs and gives the same prompt ready to copy.

## Install all of them in Claude Code

One command, inside Claude Code:

```text
/plugin install linkedin-ads-skills --marketplace demandsense-labs/linkedin-ads-skills
```

On Claude Code older than 2.1.275, add the marketplace first:

```text
/plugin marketplace add demandsense-labs/linkedin-ads-skills
/plugin install linkedin-ads-skills@linkedin-ads-skills
```

Then ask for what you need ("build this week's warm-lead handoff from these files") or call a skill by name, for example `/linkedin-ads-skills:account-health-check`.

**Just one skill, by hand:** copy its folder into `~/.claude/skills/` (on Windows, `C:\Users\<you>\.claude\skills\`), so the path ends in `account-health-check/SKILL.md`. In the Claude apps, zip the folder and upload it as a custom skill.

## Scenarios

A scenario does a whole job, start to finish, with skills inside. Each one is the routine its author runs on client accounts.

| Scenario | What you get | Author |
| --- | --- | --- |
| [Warm-lead handoff](warm-lead-handoff) | A short list of who sales should call this week, with one handoff line per account | [Justin Rowe](https://www.linkedin.com/in/justin-rowe-4043339b/), [Impactable](https://impactable.com/) |
| [Account audit by cadence](account-audit-by-cadence) | Eight account checks on a schedule: what to fix today, this week and this month | [Roman Slobodzianyk](https://www.linkedin.com/in/roman-slobodzianyk-b67549140/), [Impactable](https://impactable.com/) |
| [Targeting vs who actually buys](monthly-targeting-review) | Who each campaign paid to reach next to the people on your deals, and where to move budget | [George Coudounaris](https://www.linkedin.com/in/b2b-marketing-expert/), [The B2B Playbook](https://theb2bplaybook.com/) |
| [Company-level account routing](company-account-routing) | Which companies take most of the impressions, which are underserved, and which to move into their own audience | [Joshua Stout](https://www.linkedin.com/in/joshua-stout/), [Beyond The Funnel](https://www.beyondthefunnel.ai/) |

## Skills

A skill runs one check against one rule. All skills below are by [DemandSense](https://demandsense.com).

### From signal to sales

| Skill | What you get |
| --- | --- |
| [No-Deal Warm Leads Finder](no-deal-warm-leads-finder) | Engaged companies that are not customers and have no open deal, ranked in tiers |
| [Who's Looking at Your Buying Pages](whos-looking-at-your-buying-pages) | Recent visitors to pricing, demo, contact and trial pages, checked against the CRM |
| [Account Engagement](account-engagement) | Engaged companies tied to pipeline, and the ones missing from the CRM |
| [CRM Data Health Check](crm-data-health-check) | Whether your pipeline data can be trusted: gaps, deal hygiene, win rate by source |

### Reach and frequency

| Skill | What you get |
| --- | --- |
| [Silent Watchers Finder](silent-watchers-finder) | Companies that saw your ads for three months and never engaged |
| [Capping Recommendation](capping-recommendation) | Impression caps and an exclusion list to stop overexposure |
| [LinkedIn ABM Account Penetration](linkedin-abm-account-penetration) | Which target accounts engage, at what level, and which show nothing |

### Who the budget reaches

| Skill | What you get |
| --- | --- |
| [Waste Budget Detection](waste-budget-detection) | Campaigns that spent in the last 30 days without producing what they were built for |
| [LinkedIn Audience Demographics](linkedin-audience-demographics) | Who your ads reach and who responds, by seniority, function, title, industry, size, location |

### Ads and creative

| Skill | What you get |
| --- | --- |
| [LinkedIn Creative Performance](linkedin-creative-performance) | Ads ranked by the measure that fits their job, with pause candidates |
| [Creative Decay Watchlist](creative-decay-watchlist) | Ads whose CTR has slid for weeks, and whether the ad or the campaign is the cause |
| [Video Quality Check](video-quality-check) | Video campaigns ranked by completion and cost per completed view |
| [Pausing Low-Performing Ads](pausing-low-performing-ads) | The best ad in a campaign and the ones worth stopping, with the statistics behind each call |

### Building the account

| Skill | What you get |
| --- | --- |
| [Account Health Check](account-health-check) | A ranked list of what to fix first in the account |
| [LinkedIn Performance KPIs](linkedin-performance-kpis) | Spend, CTR, CPC, CPM and cost per lead against the previous period, with pacing |
| [Pacing Check Against Schedule](pacing-check-against-schedule) | Campaigns spending off their daily budget or schedule, and what to do |
| [Budget Re-allocation](budget-re-allocation) | A plan to move budget from ended or paused campaigns to the ones that earn it |
| [Campaign Group Scoreboard](campaign-group-scoreboard) | Campaign groups ranked by efficiency, with the two best campaigns in each |
| [Weekly Reporting](weekly-reporting) | A weekly breakdown across LinkedIn, Google Ads and Meta, with the main drivers |
| [Manager Monthly Report](manager-monthly-report) | A monthly report: what to optimise, what to stop, how you compare with the market |
| [Multichannel Performance Rollup](multichannel-performance-rollup) | Several ad platforms in one view, with what can and cannot be added together |
| [Traffic Analysis](traffic-analysis) | Where site traffic comes from, paid traffic by campaign, and a UTM tagging audit |
| [Ad-Hoc Query](ad-hoc-query) | Answers to open questions: what changed, trends, breakdowns, pacing, pipeline |
| [LinkedIn Benchmark Context](linkedin-benchmark-context) | Your results against your own history first, then market benchmarks |
| [Benchmark Comparison](benchmark-comparison) | One metric placed inside a published benchmark range for your peer group |
| [Market Benchmark Comparison](market-benchmark-comparison) | Campaign groups compared with a published market benchmark |

## Rules

Every skill and scenario applies the Standard's rules: what LinkedIn does by default, and what to do on top of it. There are 15, for example *Read frequency and penetration together* and *Report exposure, influence and attribution separately*. Read them all at [ds-b2b-ai-standards.vercel.app/rules](https://ds-b2b-ai-standards.vercel.app/rules).

## What each skill needs

Every skill works from the files you attach: Campaign Manager exports, a web analytics export, a CRM export. The skill tells you which files it needs and which checks it cannot run without them. If you use the [DemandSense MCP](https://demandsense.com/mcp-intelligence-hub), the skill can read the same data from your account instead of asking for exports.

## Contribute

Run a check we don't have? Send a skill, a scenario or a rule as you run it today. We package it, test it with you and publish it under your name, with your company and links: [ds-b2b-ai-standards.vercel.app/contribute](https://ds-b2b-ai-standards.vercel.app/contribute).

Think a skill gets something wrong? [Open an issue](https://github.com/demandsense-labs/linkedin-ads-skills/issues). If testing shows you're right, you're credited as a contributor.

## Licence

The text of every skill and scenario is under [CC BY 4.0](LICENSE): use it, adapt it, also commercially, as long as you credit the author by name, link to the source and the licence, and say what you changed. Each `SKILL.md` names its author, and [AUTHORS.md](AUTHORS.md) gives a ready credit line for each one, for example:

> Warm-lead handoff by Justin Rowe, Impactable, adapted by DemandSense, CC BY 4.0

The plugin manifest in `.claude-plugin/` is under the [MIT License](LICENSE-MIT).

The licence covers the text, not the names: DemandSense and LinkedIn are trademarks of their owners, and a credit line does not mean an author or DemandSense endorses a changed version.

---

LinkedIn is a registered trademark of LinkedIn Corporation or its affiliates. This resource is not sponsored or endorsed by LinkedIn.
