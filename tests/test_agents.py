import unittest
from src.agents.ai_agent import AIAgent

class TestAIAgent(unittest.TestCase):
    def test_run(self):
        agent = AIAgent()
        self.assertIsNone(agent.run())

if __name__ == '__main__':
    unittest.main()