# Limitations and Roadmap

## Current Limitations (Public Case Study)

- The public repository does not include original source code
- The demo uses synthetic data instead of historical real data
- Some implementation details are intentionally abstracted
- Production deployment details are omitted

## Why This Is Still Useful for Technical Review

The case study still demonstrates:

- problem framing
- architecture decomposition
- data model design choices
- reconciliation/verification logic
- MVP delivery trade-offs

## What I'd Redesign Now (If Continuing the Project)

1. Stronger provenance model for field-level decisions
2. More explicit confidence scoring and review queues for fuzzy matches
3. Clearer domain separation between ingestion, reconciliation, and UI read models
4. Better observability for ETL runs (validation metrics, error buckets, source drift alerts)
5. Reproducible public demo harness (fixtures + snapshot tests for expected outputs)

## Near-Term Case-Study Improvements

1. Add one more synthetic scenario with a different contradiction pattern (for example unresolved buyer identifier)
2. Add a diagram showing evidence flow into the reconciled view
3. Add a lightweight web demo or notebook wrapper around the CLI reconciliation output
