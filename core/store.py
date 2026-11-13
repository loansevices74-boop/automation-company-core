"""Small SQLite persistence layer for the Phase 1 operations console."""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Iterator


@dataclass(frozen=True)
class Lead:
    name: str
    email: str
    company: str = ""
    source: str = "manual"
    status: str = "new"


class LeadStore:
    def __init__(self, path: str | None = None) -> None:
        self.path = path or os.getenv("AUTOMATION_DB_PATH", "automation_company.db")
        self._initialise()

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def _initialise(self) -> None:
        with self._connection() as connection:
            connection.execute(
                """CREATE TABLE IF NOT EXISTS leads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    company TEXT NOT NULL DEFAULT '',
                    source TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )"""
            )

    def add(self, lead: Lead) -> int:
        if not lead.name.strip() or "@" not in lead.email:
            raise ValueError("A lead requires a name and a valid email address.")
        with self._connection() as connection:
            cursor = connection.execute(
                "INSERT INTO leads(name,email,company,source,status,created_at) VALUES(?,?,?,?,?,?)",
                (*asdict(lead).values(), datetime.now(timezone.utc).isoformat()),
            )
            return int(cursor.lastrowid)

    def list(self) -> list[dict[str, object]]:
        with self._connection() as connection:
            rows = connection.execute("SELECT * FROM leads ORDER BY id DESC").fetchall()
            return [dict(row) for row in rows]
