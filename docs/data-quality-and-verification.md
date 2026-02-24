# Data Quality and Verification (Draft)

## Core Problem

The MVP was built for a domain where records across sources can be:

- incomplete
- delayed
- formatted differently
- partially duplicated
- contradictory

## Practical Strategy (MVP-Level)

The system design used a staged approach:

1. Parse source records into a consistent internal representation
2. Normalize keys/fields (identifiers, names, dates, codes)
3. Generate candidate links across sources
4. Evaluate contradictions and confidence
5. Build a reconciled view for UI consumption

## Typical Contradictions the Demo Will Illustrate

- entity naming variations
- date mismatches
- missing identifiers in one source
- different representations of the same route or participant

## Public Demo Principle

The synthetic demo will focus on explainability:

- show raw source records
- show normalization
- show matching / reconciliation result
- show final "factual picture" record

