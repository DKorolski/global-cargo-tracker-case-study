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

## Run

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

## Why CLI First

CLI is the fastest way to present the data quality / reconciliation logic without introducing extra UI code. It can later be wrapped in a notebook or mini web page if needed.

