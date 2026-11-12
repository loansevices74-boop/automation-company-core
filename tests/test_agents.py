import unittest

from agents.ai_agent import AIAgent


class TestAIAgent(unittest.TestCase):
    def test_run_returns_complete_logs_without_delay(self):
        agent = AIAgent(sleep_fn=self.fail)

        logs = agent.run()

        self.assertEqual(len(logs), 4)
        self.assertEqual(logs[0], "[Automation Agent] Agent started.")
        self.assertEqual(logs[-1], "[Automation Agent] Automation complete.")

    def test_run_clears_previous_logs(self):
        agent = AIAgent()

        first_run = agent.run()
        second_run = agent.run()

        self.assertEqual(first_run, second_run)
        self.assertEqual(len(second_run), 4)


if __name__ == "__main__":
    unittest.main()
