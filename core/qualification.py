"""Validated, approval-first lead workflow primitives."""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class LeadStatus(StrEnum):
    NEW = "new"
    QUALIFIED = "qualified"
    CONTACTED = "contacted"
    WON = "won"
    LOST = "lost"


@dataclass(frozen=True)
class Qualification:
    score: int
    rationale: str
    next_action: str


def qualify_lead(*, company: str, need: str, budget: int | None = None) -> Qualification:
    """Score a lead without contacting it or making a commercial commitment."""
    if not company.strip() or not need.strip():
        raise ValueError("Company and need are required.")

    score = 40
    if len(company.strip()) >= 3:
        score += 10
    if len(need.strip()) >= 20:
        score += 20
    if budget is not None:
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
        score += 30 if budget >= 799 else 15

    score = min(score, 100)
    return Qualification(
        score=score,
        rationale="Structured qualification only; human approval is required before outreach.",
        next_action="Review and approve a personalized draft" if score >= 60 else "Request additional qualification details",
    )
