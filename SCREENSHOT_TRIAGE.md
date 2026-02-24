# Screenshot Triage (example-4 PNGs)

Source reviewed:

- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_1.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_2.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_3.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_4.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_5.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_6.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_7.png`
- `documentation/product/global-cargo-tracker/examples/example-4/example_4_image_8.png`

## Decision Summary

Recommendation for public HR case-study:

- Do **not** use these screenshots as-is.
- Prefer synthetic screenshots generated from the public demo / local MVP with synthetic data.
- If one is needed for "research workflow" illustration, use a heavily cropped and redacted variant of `example_4_image_1.png` or `example_4_image_3.png` only.

Approved replacement (recommended):

- `Synthetic transport route screenshot` from local MVP page rendered with `?demo_route=1`
  - status: `APPROVED`
  - rationale: real UI, synthetic company identity, synthetic route geometry, no visible PII, strong domain signal

## Per-Image Triage

### `example_4_image_1.png`

Content:

- OpenCorporates search page with "0 companies found"
- search query contains a real surname
- full browser chrome/tabs/bookmarks and desktop taskbar visible

Risk:

- personal name in query
- unrelated browser tabs / account context leakage
- low signal-to-noise for HR

Decision:

- `USE ONLY AFTER HEAVY CROP + REDACTION` (low priority)

Safer alternative:

- recreate a synthetic "no match" search screenshot using your public demo or a mocked UI snippet

### `example_4_image_2.png`

Content:

- Excel sheet with many rows of names, addresses, company strings

Risk:

- clear PII / identifying data
- addresses and names visible at scale

Decision:

- `DO NOT USE`

### `example_4_image_3.png`

Content:

- OpenCorporates search page similar to image 1
- query appears in Cyrillic (real surname)
- browser/desktop chrome visible

Risk:

- personal name in query
- noisy desktop/browser context

Decision:

- `USE ONLY AFTER HEAVY CROP + REDACTION` (low priority)

### `example_4_image_4.png`

Content:

- OpenCorporates search results page with found companies/person-like entries
- visible names and jurisdiction/status details

Risk:

- personal names and identifiable records

Decision:

- `DO NOT USE`

### `example_4_image_5.png`

Content:

- OpenCorporates entity/company page with identifiable personal/company details

Risk:

- direct identifiable entity information

Decision:

- `DO NOT USE`

### `example_4_image_6.png`

Content:

- Google search results page with a real surname and multiple identifiable results

Risk:

- personal name query
- third-party search results with unrelated/sensitive content
- browser/desktop noise

Decision:

- `DO NOT USE`

### `example_4_image_7.png`

Content:

- Russian business directory page for an individual entrepreneur
- visible personal name and identifiers (INN / OGRNIP-like values)

Risk:

- high PII exposure

Decision:

- `DO NOT USE`

### `example_4_image_8.png`

Content:

- appears to be the same page as image 7 (duplicate/near-duplicate)

Risk:

- same high PII exposure

Decision:

- `DO NOT USE`

## What To Use Instead (Recommended)

For the public case-study, use these visual artifacts instead:

1. Mermaid diagrams exported/rendered in GitHub:
   - `docs/architecture.md`
   - `docs/data-model.md`

2. Synthetic demo screenshots:
   - terminal output of `demo/demo_cli.py` (cropped)
   - synthetic "search result" and "verification summary" JSON blocks from the CLI output

3. Optional local MVP screenshots (best option if available):
   - run local app against synthetic data
   - capture only the app viewport (no browser tabs/bookmarks/taskbar)
   - use synthetic company names/IDs only

Current approved visual from this track:

- Local MVP transport page screenshot with synthetic route:
  - `Bogota -> Panama -> Cadiz`
  - synthetic company label: `Synthetic Export Co`
  - captured from `.../transport?demo_route=1`

## Minimal Visual Pack (Safe and Sufficient)

Recommended first public release can ship with just:

- 1 architecture diagram (Mermaid)
- 1 data model diagram (Mermaid ER)
- 1 screenshot of synthetic demo output (cropped terminal) OR
- 1 screenshot of synthetic local transport route page (approved)

This is enough for HR/tech lead review without privacy risk.
