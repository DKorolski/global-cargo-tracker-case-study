# Global Cargo Tracker - Redacted Case Study (2020-2021)

**Case Study / Redacted**

## One-Liner

A hiring-focused, public case study of a private MVP for supply-chain traceability and cross-border cargo intelligence.

**Private source code + real datasets are NOT included** (by design).

## Why This Exists

International trade and logistics data is fragmented across sources and often:

- incomplete, delayed, and inconsistent
- duplicated or partially conflicting
- stored in incompatible formats

The MVP goal was to validate that one system can reconstruct a more reliable "factual picture" of shipments/participants by:

1. ingesting heterogeneous sources
2. normalizing and linking records
3. detecting contradictions
4. producing an explainable reconciled view for analysts

## What Is Public vs. Private

### Public in This Repository

- architecture overview (redacted): `docs/architecture.md`
- simplified data model (redacted): `docs/data-model.md`
- data quality and reconciliation notes: `docs/data-quality-and-verification.md`
- privacy / redaction scope: `docs/privacy-redaction.md`
- limitations and roadmap: `docs/limitations-and-roadmap.md`
- synthetic CLI demo (runs locally): `demo/README.md`
- approved synthetic UI screenshot: `assets/screenshots/transport-route-synthetic.png`

### Private (Not Published)

- original MVP source code repository
- real/historical datasets, SQL dumps, and migrations with real records
- source-specific integrations, credentials, and operational details

## Architecture (High Level)

See: `docs/architecture.md`

In short:

- ingestion/parsers -> normalization/cleaning -> matching/linking -> verification/reconciliation
- storage + search/read models -> analyst-facing UI (private MVP)

## Synthetic Demo (CLI)

Prerequisites:

- Python `3.9+`
- no external dependencies

Run:

```bash
python3 demo/demo_cli.py
```

What you'll see:

- raw synthetic source records (multiple sources)
- normalized comparison
- detected contradictions
- reconciled "factual picture" result

Expected output example: `demo/expected_output.txt`

## What You Can Evaluate (Interview Review)

- system decomposition for messy real-world data
- reconciliation/verification approach (evidence + contradictions)
- domain modeling choices for trade/transport entities
- explainability-first output (not a "black box ETL")

## My Role (2020-2021)

I worked across the stack and product scope:

- backend
- data/ETL
- schema/migrations
- UI implementation
- tech lead responsibilities
- product responsibilities

Details: `ROLE.md`

## Security / Redaction Note

This is a redacted case study. Examples are rewritten/synthetic to avoid exposing private code, secrets, or real records.

- publishing checklist: `PUBLISH_CHECKLIST.md`
- safe transfer workflow: `TRANSFER_TO_PUBLIC_REPO.md`

## Visuals (Approved, Synthetic)

![Synthetic transport route (local MVP UI)](assets/screenshots/transport-route-synthetic.png)

## Suggested Portfolio Label

`Global Cargo Tracker (private code, public redacted case study) - Supply Chain Traceability MVP`

## GitHub About / Topics (Recommended)

Set repository description to something close to:

- `Redacted case study of a supply-chain traceability MVP with synthetic reconciliation demo`

Suggested topics:

- `data-quality`
- `etl`
- `reconciliation`
- `case-study`
- `supply-chain`
