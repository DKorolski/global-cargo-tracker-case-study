# Data Quality and Verification

## Core Problem

The MVP was built for a domain where records across sources can be:

- incomplete
- delayed
- formatted differently
- partially duplicated
- contradictory

The engineering goal was not to force a single "perfect" source, but to produce a reconciled view that preserves evidence and makes uncertainty explicit.

## Practical Strategy (MVP-Level)

The system design used a staged approach:

1. Parse source records into a consistent internal representation
2. Normalize keys/fields (identifiers, names, dates, codes)
3. Generate candidate links across sources
4. Evaluate contradictions and confidence
5. Build a reconciled view for UI consumption

## Normalization Rules (Examples)

Normalization was applied before matching so that formatting differences do not look like real contradictions.

- identifiers: trim spaces/punctuation, uppercase where applicable (for example container numbers)
- company names: normalize case, legal suffix variants, punctuation, and repeated whitespace
- dates: convert source-specific formats into a common format (for example `YYYY-MM-DD`)
- codes: normalize HS codes / country codes into canonical string forms
- ports and locations: preserve raw source values, plus canonical keys when available

Important principle:

- keep both `raw` and `normalized` values so analysts can inspect what changed during normalization

## Match Types (Linking Across Sources)

The MVP-style logic supports multiple match strengths. The synthetic CLI demo primarily shows `exact` and `normalized` matching, but the public case-study description also covers a `fuzzy` tier used for candidate generation/review.

- `exact`: source values match without transformation (for example same declaration number or tax ID)
- `normalized`: values differ in formatting but match after normalization (for example `MSCU1234567` vs `MSCU-123456-7`)
- `fuzzy`: values are similar enough to be a candidate (for example naming variants / transliteration / token reordering), but require lower confidence and often extra evidence

Typical usage:

- high-confidence linking starts with exact identifiers
- normalized matches resolve common formatting noise
- fuzzy matches are used as candidates, not as final truth without supporting signals

## Contradictions and How They Are Recorded

A contradiction is recorded when two linked records refer to the same event/entity but disagree on a field in a meaningful way.

Examples:

- same shipment, different event/declaration dates
- same container represented differently (may resolve after normalization)
- same participant with naming variation (resolved after normalization)
- same route inferred differently across customs vs carrier source

Each contradiction record should capture:

- `field` (what conflicts)
- source values (what each source said)
- resolution note (what rule was applied, or why it remains unresolved)
- confidence/priority context (optional but useful for downstream review)

This is important because the system should remain explainable: users need to see both the conflict and the reason for the chosen reconciled value.

## Reconciled View Selection (Rules / Priority / Confidence)

The reconciled view is the analyst-facing "best current picture" built from linked evidence records. It is not a destructive overwrite of source data.

Typical selection approach:

1. Keep all raw source records as evidence
2. For each reconciled field, apply a rule set (priority + normalization + conflict handling)
3. Store the chosen value plus evidence references and contradictions
4. Expose a verification summary in UI/CLI

Examples of field-level rules:

- shipment declaration number: prefer customs source when present
- transport event date (load event): prefer carrier event date for operational timing; keep customs declaration date separately
- container number: store normalized canonical form, preserve raw source variants in evidence
- entity keys: prefer strong identifiers (tax ID / registration IDs) over name-only matches

Confidence can be derived from signals such as:

- identifier strength (exact ID > normalized name > fuzzy name)
- number of corroborating sources
- contradiction severity (formatting mismatch vs material value mismatch)
- recency/completeness of the contributing record

## Typical Contradictions the Demo Illustrates

- entity naming variations
- date mismatches
- missing identifiers in one source
- different representations of the same route or participant

## Public Demo Principle

The synthetic demo focuses on explainability:

- show raw source records
- show normalization
- show matching / reconciliation result
- show final "factual picture" record

In the included CLI example, the reconciled output explicitly shows:

- normalized company/container matches
- a date contradiction with a documented resolution
- evidence record IDs that support the reconciled shipment
