import unittest

from agents.ai_agent import AIAgent


class TestAIAgent(unittest.TestCase):
    def test_run_returns_logs(self):
        agent = AIAgent()
        logs = agent.run()
        self.assertIsInstance(logs, list)
        self.assertTrue(logs)


if __name__ == "__main__":
    unittest.main()
