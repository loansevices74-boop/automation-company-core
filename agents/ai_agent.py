# agents/ai_agent.py

import time

class AIAgent:
    def __init__(self, name="Automation Agent"):
        self.name = name
        self.logs = []

    def run(self):
        # Simulate agent workflow
        self._log("Agent started.")
        time.sleep(1)
        self._log("Collecting data...")
        time.sleep(1)
        self._log("Analyzing workflows...")
        time.sleep(1)
        self._log("Automation complete.")
        return self.logs

    def _log(self, message):
        entry = f"[{self.name}] {message}"
        print(entry)
        self.logs.append(entry)