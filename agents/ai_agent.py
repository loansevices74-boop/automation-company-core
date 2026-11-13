"""Core automation agent implementation."""

from __future__ import annotations

import os
import time
from collections.abc import Callable


class AIAgent:
    """Run the core automation workflow and return human-readable logs."""

    def __init__(
        self,
        name: str = "Automation Agent",
        sleep_fn: Callable[[float], None] = time.sleep,
    ) -> None:
        self.name = name
        self.logs: list[str] = []
        self._sleep = sleep_fn
        self.step_delay = max(0.0, float(os.getenv("AGENT_STEP_DELAY_SECONDS", "0")))

    def run(self) -> list[str]:
        """Execute the workflow and return its logs."""
        self.logs.clear()
        for message in (
            "Agent started.",
            "Collecting data...",
            "Analyzing workflows...",
            "Automation complete.",
        ):
            self._log(message)
            if self.step_delay:
                self._sleep(self.step_delay)
        return self.logs.copy()

    def _log(self, message: str) -> None:
        entry = f"[{self.name}] {message}"
        print(entry)
        self.logs.append(entry)
