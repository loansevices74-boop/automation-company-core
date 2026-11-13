"""Minimal base agent used by the administrator automation console."""
from __future__ import annotations


class AIAgent:
    def __init__(self, name: str = "Automation Agent") -> None:
        self.name = name
        self.logs: list[str] = []

    def run(self) -> list[str]:
        self.logs.clear()
        self._log("Agent started.")
        self._log("Collecting data...")
        self._log("Analyzing workflows...")
        self._log("Automation complete.")
        return list(self.logs)

    def _log(self, message: str) -> None:
        self.logs.append(f"[{self.name}] {message}")
