import tempfile
import unittest
from pathlib import Path

from core.qualification import qualify_lead
from core.store import Lead, LeadStore


class TestQualification(unittest.TestCase):
    def test_qualified_lead_gets_review_next_action(self):
        result = qualify_lead(
            company="Acme Services",
            need="Automate lead follow-up and monthly reporting",
            budget=799,
        )
        self.assertGreaterEqual(result.score, 60)
        self.assertIn("Review", result.next_action)

    def test_missing_company_is_rejected(self):
        with self.assertRaises(ValueError):
            qualify_lead(company="", need="Automate follow-up")


class TestLeadStore(unittest.TestCase):
    def test_add_and_list_lead(self):
        with tempfile.TemporaryDirectory() as directory:
            store = LeadStore(str(Path(directory) / "test.db"))
            lead_id = store.add(
                Lead(name="Ada Example", email="ada@example.com", company="Acme")
            )
            leads = store.list()

        self.assertEqual(lead_id, 1)
        self.assertEqual(leads[0]["email"], "ada@example.com")
        self.assertEqual(leads[0]["status"], "new")


if __name__ == "__main__":
    unittest.main()
