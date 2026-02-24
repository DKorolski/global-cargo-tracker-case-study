#!/usr/bin/env python3
"""
Synthetic reconciliation demo for the public case study.

No external dependencies required.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).parent / "data"


def load_json(name: str) -> list[dict[str, Any]]:
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))


def norm_company_name(value: str | None) -> str | None:
    if not value:
        return value
    v = value.upper()
    v = v.replace("S.A.S.", "SAS").replace("S.A.S", "SAS")
    v = v.replace("LLC", "")
    v = re.sub(r"[^A-Z0-9 ]+", " ", v)
    v = re.sub(r"\s+", " ", v).strip()
    # Collapse spacing so "NORTHCHEM" and "NORTH CHEM" match in the demo.
    v = v.replace(" ", "")
    return v


def norm_date(value: str | None) -> str | None:
    if not value:
        return value
    return value.replace("/", "-")


def norm_container(value: str | None) -> str | None:
    if not value:
        return value
    return re.sub(r"[^A-Z0-9]", "", value.upper())


@dataclass
class ReconciledShipment:
    entity_key_shipper: str
    entity_key_buyer: str
    declaration_no: str
    hs_code: str
    shipment_date: str
    container_no: str
    route_origin: str
    route_destination: str
    origin_port: str
    destination_port: str
    gross_weight_kg: int
    invoice_amount_usd: int
    vessel_name: str
    evidence_records: list[str]
    contradictions: list[dict[str, str]]


def detect_contradictions(customs: dict[str, Any], transport: dict[str, Any]) -> list[dict[str, str]]:
    contradictions: list[dict[str, str]] = []

    if norm_company_name(customs.get("shipper_name")) != norm_company_name(transport.get("shipper_name")):
        contradictions.append(
            {
                "field": "shipper_name",
                "customs": str(customs.get("shipper_name")),
                "transport": str(transport.get("shipper_name")),
                "resolution": "same entity after normalization",
            }
        )

    if customs.get("decl_date") != norm_date(transport.get("event_date")):
        contradictions.append(
            {
                "field": "shipment_date",
                "customs": str(customs.get("decl_date")),
                "transport": str(transport.get("event_date")),
                "resolution": "accept transport event date as load event; keep customs date as declaration date",
            }
        )

    customs_container_raw = customs.get("container_no")
    transport_container_raw = transport.get("container_no")
    customs_container_norm = norm_container(customs_container_raw)
    transport_container_norm = norm_container(transport_container_raw)
    if (
        customs_container_raw != transport_container_raw
        and customs_container_norm == transport_container_norm
    ):
        contradictions.append(
            {
                "field": "container_no",
                "customs": str(customs_container_raw),
                "transport": str(transport_container_raw),
                "resolution": "same container after formatting normalization",
            }
        )

    return contradictions


def build_registry_index(registry_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for row in registry_rows:
        name_key = norm_company_name(row.get("company_name"))
        if name_key:
            index[name_key] = row
        tax_id = row.get("tax_id")
        if tax_id:
            index[f"TAX:{tax_id}"] = row
    return index


def reconcile() -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]], ReconciledShipment]:
    customs = load_json("source_customs.json")[0]
    transport = load_json("source_transport.json")[0]
    registry = load_json("source_registry.json")

    registry_index = build_registry_index(registry)

    shipper_registry = registry_index.get(f"TAX:{customs['shipper_tax_id']}") or registry_index.get(
        norm_company_name(customs["shipper_name"]) or ""
    )
    buyer_registry = registry_index.get(norm_company_name(customs["buyer_name"]) or "")

    contradictions = detect_contradictions(customs, transport)

    reconciled = ReconciledShipment(
        entity_key_shipper=shipper_registry.get("tax_id", "UNKNOWN") if shipper_registry else "UNKNOWN",
        entity_key_buyer=norm_company_name(buyer_registry.get("company_name")) if buyer_registry else "UNKNOWN",
        declaration_no=customs["declaration_no"],
        hs_code=customs["hs_code"],
        shipment_date=norm_date(transport["event_date"]) or customs["decl_date"],
        container_no=norm_container(customs["container_no"]) or "",
        route_origin=customs["route_origin"],
        route_destination=customs["route_destination"],
        origin_port=transport["origin_port"],
        destination_port=transport["destination_port"],
        gross_weight_kg=customs["gross_weight_kg"],
        invoice_amount_usd=customs["invoice_amount_usd"],
        vessel_name=transport["vessel_name"],
        evidence_records=[customs["source_record_id"], transport["source_record_id"]],
        contradictions=contradictions,
    )

    return customs, transport, registry, reconciled


def print_section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_json(obj: Any) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def main() -> None:
    customs, transport, registry, reconciled = reconcile()

    print_section("Synthetic Demo: Global Cargo Tracker (Redacted Case Study)")
    print("Representative path: search -> company -> foreign_trade -> transport -> verification")

    print_section("1) Raw Source Records")
    print("[customs]")
    print_json(customs)
    print("\n[transport]")
    print_json(transport)
    print("\n[registry]")
    print_json(registry)

    print_section("2) Normalized Comparison (selected fields)")
    normalized_view = {
        "shipper_name": {
            "customs_raw": customs["shipper_name"],
            "transport_raw": transport["shipper_name"],
            "normalized_customs": norm_company_name(customs["shipper_name"]),
            "normalized_transport": norm_company_name(transport["shipper_name"]),
        },
        "container_no": {
            "customs_raw": customs["container_no"],
            "transport_raw": transport["container_no"],
            "normalized_customs": norm_container(customs["container_no"]),
            "normalized_transport": norm_container(transport["container_no"]),
        },
        "date_fields": {
            "customs_decl_date": customs["decl_date"],
            "transport_event_date_raw": transport["event_date"],
            "transport_event_date_normalized": norm_date(transport["event_date"]),
        },
    }
    print_json(normalized_view)

    print_section("3) Detected Contradictions")
    if reconciled.contradictions:
        print_json(reconciled.contradictions)
    else:
        print("No contradictions detected.")

    print_section("4) Reconciled 'Factual Picture' (Synthetic)")
    print_json(asdict(reconciled))

    print_section("5) UI-like Views (Synthetic)")
    print("[search result]")
    print_json(
        {
            "query": "NorthChem / 2933694000 / MSCU1234567",
            "matches": [
                {"type": "company", "title": "North Chem Export LLC", "company_sk": 1001},
                {"type": "product", "hs_code": "2933694000", "label": "Synthetic product item"},
            ],
        }
    )
    print("\n[company/1001 -> foreign_trade]")
    print_json(
        {
            "company_sk": 1001,
            "company_name": "North Chem Export LLC",
            "foreign_trade_summary": {
                "declarations": 1,
                "destinations": ["CO"],
                "linked_transport_records": 1,
            },
        }
    )
    print("\n[transport detail -> verification summary]")
    print_json(
        {
            "transport_record_id": transport["source_record_id"],
            "declaration_no": customs["declaration_no"],
            "container_no_normalized": norm_container(customs["container_no"]),
            "verification_status": "resolved_with_contradictions",
            "contradictions_count": len(reconciled.contradictions),
        }
    )


if __name__ == "__main__":
    main()
