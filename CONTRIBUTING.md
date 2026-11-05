# Contributing

This collection is written by LinkedIn Ads practitioners and maintained by DemandSense as part of [The B2B AI Standard for LinkedIn Ads](https://b2baistandard.com/collection). There are three ways to take part.

## Send a skill, a scenario or a rule

Run a check we don't have? Send it as you run it today; you don't need to write a `SKILL.md`. We package it, test it with you and publish it under your name, with your company and links.

Start here: [b2baistandard.com/contribute](https://b2baistandard.com/contribute).

## Tell us a skill gets something wrong

[Open an issue](https://github.com/demandsense-labs/linkedin-ads-skills/issues/new/choose) with the skill's folder name, what it said and what it should say. If testing shows you're right, the skill is fixed and you're credited as a contributor.

Please keep client names, account IDs and other private data out of issues: this repository is public.

## Fix something small

Pull requests are welcome for typos, broken links and install problems. For a change to what a skill tells people to do, open an issue instead, so it can be checked with the skill's author.

## How a skill is laid out

Each skill is one folder with a `SKILL.md`. Its frontmatter carries the `name`, a `description` that says when to use it, the `license` with the credit line, and `metadata.author`. Keep the `license` and `metadata` lines when you replace a `SKILL.md`: they are how the author's credit travels with the file. The plugin manifests live in `.claude-plugin/`, and both list every skill folder.

A check runs on every push and pull request: names, descriptions, credit lines, both manifests and every relative link. Run it yourself before you push:

```bash
python .github/scripts/validate_skills.py
```

## Behaviour

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md). Report a problem to [znak@demandsense.com](mailto:znak@demandsense.com).

## Licence

The text of the skills and scenarios is under [CC BY 4.0](LICENSE), and the code and manifests are under [MIT](LICENSE-MIT). By contributing you agree that your contribution is published under the same licence, credited to you as listed in [AUTHORS.md](AUTHORS.md).
