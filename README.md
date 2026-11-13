# B2B Automation Company Core

Streamlit-based administrator console for a productized B2B automation service.

## Active application surface

- `app.py` — administrator dashboard
- `core/` — SQLite lead storage and qualification
- `marketing/engine.py` — marketing calendar and funnel metrics
- `social_media/workflow.py` — approval-first social drafts
- `orchestration/automation_plan.py` — recurring job definitions
- `tests/` — automated tests

The repository intentionally keeps live publishing, bulk outreach, payment processing, and production mutations behind explicit administrator approval and provider configuration.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
python -m unittest discover -s tests -p 'test_*.py'
```

Windows PowerShell activation:

```powershell
.venv\\Scripts\\Activate.ps1
```

Set `AUTOMATION_DB_PATH` to choose a different SQLite location. Local databases, credentials, logs, and generated output are ignored by Git.

## Commercial plans

- Starter: $299/month
- Growth: $799/month
- Managed: $1,499/month

These are pricing targets, not guaranteed revenue.

## Cleanup note

The active application no longer depends on the older pillar directories inherited from the original scaffold. They should be removed in a repository maintenance commit once a deletion-capable GitHub operation is available; no customer data or secrets should be stored there.
