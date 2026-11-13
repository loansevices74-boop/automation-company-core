from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class SocialDraft:
    id: str
    platform: str
    text: str
    status: str
    created_at: str


def create_draft(platform: str, text: str) -> SocialDraft:
    if platform not in {"linkedin", "mastodon", "x", "facebook", "instagram"}:
        raise ValueError("Unsupported platform")
    text = text.strip()
    if not text or len(text) > 5000:
        raise ValueError("Post text must contain 1 to 5000 characters")
    return SocialDraft(f"draft_{uuid4().hex}", platform, text, "pending_review", datetime.now(timezone.utc).isoformat())


def approve_draft(draft: SocialDraft, administrator: str) -> SocialDraft:
    if not administrator.strip() or draft.status != "pending_review":
        raise ValueError("A pending draft and administrator identity are required")
    return SocialDraft(draft.id, draft.platform, draft.text, "approved", draft.created_at)
