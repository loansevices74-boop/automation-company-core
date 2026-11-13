from datetime import date, timedelta


def build_content_calendar(start: date, days: int = 7) -> list[dict[str, str]]:
    if days < 1 or days > 31:
        raise ValueError("days must be between 1 and 31")
    themes = [
        "Problem: inconsistent follow-up loses qualified leads.",
        "Education: automate capture, qualification, and routing.",
        "Proof: measure response time and conversion rate.",
        "Offer: book a workflow review.",
    ]
    return [
        {
            "channel": ("linkedin", "mastodon", "website", "email")[index % 4],
            "body": themes[index % len(themes)],
            "status": "pending_review",
            "scheduled_for": str(start + timedelta(days=index)),
        }
        for index in range(days)
    ]


def campaign_metrics(leads: int, qualified: int, customers: int, revenue: int) -> dict[str, float]:
    if min(leads, qualified, customers, revenue) < 0:
        raise ValueError("metrics cannot be negative")
    return {
        "qualification_rate": round(qualified / leads * 100, 2) if leads else 0.0,
        "close_rate": round(customers / qualified * 100, 2) if qualified else 0.0,
        "target_gap": float(max(0, 5000 - revenue)),
    }
