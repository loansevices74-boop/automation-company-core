"""Safe recurring job plan for GitHub Actions or an external scheduler."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    name: str
    cadence: str
    action: str
    approval_required: bool


DEFAULT_JOBS = (
    Job("refresh_lead_metrics", "hourly", "Recalculate pipeline metrics", False),
    Job("generate_content_calendar", "daily", "Create marketing drafts", False),
    Job("review_social_queue", "daily", "Show pending drafts to administrator", True),
    Job("send_approved_followups", "daily", "Send only approved messages through configured provider", True),
    Job("billing_reconciliation", "daily", "Reconcile provider webhooks", False),
    Job("weekly_growth_report", "weekly", "Prepare revenue and funnel report", False),
)


def jobs_requiring_approval() -> list[Job]:
    return [job for job in DEFAULT_JOBS if job.approval_required]
