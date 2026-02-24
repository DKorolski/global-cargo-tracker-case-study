# Synthetic Demo (CLI)

This demo reproduces the core idea of the MVP on synthetic data:

- combine records from multiple sources
- normalize values
- detect contradictions
- produce a reconciled "factual picture"

## Scenario

Three synthetic sources describe the same shipment / trade event:

- customs declaration source
- carrier/transport source
- registry/company source

The records intentionally contain contradictions:

- company naming variation
- date mismatch
- container formatting mismatch
- route-level linkage via customs country pair (`RU -> CO`) and transport ports (`RULED -> COCTG`)

## Run

Prerequisites:

- Python `3.9+`
- no external dependencies

```bash
python3 demo/demo_cli.py
```

## What the Demo Prints

- source records (raw)
- normalized records
- detected contradictions
- reconciled result
- a simplified UI-like navigation path:
  - search -> company -> foreign_trade -> transport -> verification summary

## Expected Output (Excerpt)

Full short sample: `demo/expected_output.txt`

```text
Synthetic Demo: Global Cargo Tracker (Redacted Case Study)
Representative path: search -> company -> foreign_trade -> transport -> verification

1) Raw Source Records
[customs] declaration_no=RU-EXP-2021-0001, route_origin=RU, route_destination=CO
[transport] source_record_id=TR-7788, origin_port=RULED, destination_port=COCTG

2) Normalized Comparison (selected fields)
normalized shipper: NORTHCHEMEXPORT == NORTHCHEMEXPORT
normalized container: MSCU1234567 == MSCU1234567
transport_event_date_normalized: 2021-02-04

3) Detected Contradictions
- shipment_date: customs 2021-02-03 vs transport 2021/02/04
- container_no: MSCU1234567 vs MSCU-123456-7

4) Reconciled 'Factual Picture' (Synthetic)
entity_key_shipper=7701001001
route_origin=RU, route_destination=CO
origin_port=RULED, destination_port=COCTG
verification_status=resolved_with_contradictions
```

## Why CLI First

CLI is the fastest way to present the data quality / reconciliation logic without introducing extra UI code. It can later be wrapped in a notebook or mini web page if needed.
