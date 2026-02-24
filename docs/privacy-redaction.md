# Privacy and Redaction Scope (Draft)

## Why the Original Repository Is Private

The original project repository contains:

- private source code
- legacy datasets and SQL data scripts with real records
- credentials/secrets in historical materials (to be treated as compromised and non-public)
- operational/internal artifacts not suitable for public distribution

## Public Packaging Rules

This public case study includes only:

- rewritten narrative
- simplified diagrams
- synthetic demo data
- selected redacted visuals (after review)

It excludes:

- raw DB dumps
- migration/data scripts with real inserted records
- credentials / tokens / password databases
- source-specific integration details

## Redaction Principles

- Prefer re-authoring examples over editing real extracts
- Replace all identifiers/contact fields with synthetic placeholders
- Keep structural relationships, remove real-world traceability to actual parties
- Document what is hidden and why (privacy / IP / operational security)

