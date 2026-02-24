# Publish Checklist (Public Case Study)

Use this checklist before the first push to `global-cargo-tracker-case-study` (public).

## 1. Scope and Content Check

- [ ] Public repo contains only case-study materials (`README`, `docs`, `demo`, assets)
- [ ] No direct copies of private source code beyond intentionally curated/redacted snippets
- [ ] No raw SQL dumps or private migrations
- [ ] No `.db` files
- [ ] No notebooks copied from the private repo unless rewritten and reviewed

## 2. Secrets / Credentials Check

- [ ] Run a text scan for secrets/tokens/API keys
- [ ] Confirm no password stores / `.kdbx` / env files are included
- [ ] Confirm no hardcoded external credentials remain in demo scripts

Recommended scan:

```bash
rg -n "api[_-]?key|token|secret|password|passwd|Authorization|AIza|X-ACCESS-KEY|BEGIN PRIVATE KEY" .
```

## 3. PII / Real Data Check

- [ ] No real names, phones, emails, addresses, company identifiers from historical datasets
- [ ] Demo data is synthetic
- [ ] Screenshots (if any) are reviewed and redacted
- [ ] Example payloads/snippets are synthetic or fully rewritten

## 4. Public Narrative Quality Check (Hiring)

- [ ] README explains problem, constraints, solution, architecture
- [ ] README clearly states what is private and why
- [ ] README clearly states role and timeframe (`2020-2021`)
- [ ] Demo instructions work in 1 command
- [ ] Docs are linked from README

## 5. Technical Sanity Check

- [ ] `python3 demo/demo_cli.py` runs successfully
- [ ] Mermaid diagrams render correctly on GitHub (architecture/data-model)
- [ ] File tree is clean and intentional

## 6. Git Safety Check (Before First Push)

- [ ] Verify current repo is the new public repo (not the private repo)
- [ ] `git remote -v` points to `global-cargo-tracker-case-study`
- [ ] `git status` shows only intended files
- [ ] Review `git diff --staged` before commit

## 7. Final Publish Steps

- [ ] Commit with a clear initial message (e.g., `Initial public case study draft`)
- [ ] Push to public repo
- [ ] Open GitHub page and verify README rendering + Mermaid diagrams
- [ ] Update CV / LinkedIn link after final review

