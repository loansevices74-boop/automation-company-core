import unittest
from datetime import date

from marketing.engine import build_content_calendar, campaign_metrics
from social_media.workflow import approve_draft, create_draft


class TestMarketing(unittest.TestCase):
    def test_calendar_creates_reviewable_drafts(self):
        drafts = build_content_calendar(date(2026, 11, 13), 4)
        self.assertEqual(len(drafts), 4)
        self.assertTrue(all(draft["status"] == "pending_review" for draft in drafts))

    def test_metrics_are_percentages(self):
        metrics = campaign_metrics(100, 20, 5, 3995)
        self.assertEqual(metrics["qualification_rate"], 20.0)
        self.assertEqual(metrics["close_rate"], 25.0)
        self.assertEqual(metrics["target_gap"], 1005.0)

    def test_social_draft_requires_approval(self):
        draft = create_draft("linkedin", "Automation insight")
        self.assertEqual(approve_draft(draft, "administrator").status, "approved")


if __name__ == "__main__":
    unittest.main()
