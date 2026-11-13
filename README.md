# B2B Automation Company Core

Phase 1 foundation for a productized B2B automation service.

## Current capabilities

- Streamlit administrator console
- SQLite-backed lead storage
- Structured lead qualification
- Approval-first outreach workflow boundary
- Basic pipeline metrics
- Unit tests for qualification and persistence

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
python -m unittest discover -s tests -p 'test_*.py'
```

Set `AUTOMATION_DB_PATH` to choose a different SQLite database location. Do not commit credentials or customer data.

## Initial plans

- Starter: $299/month
- Growth: $799/month
- Managed: $1,499/month

These are commercial targets, not guaranteed revenue. Outreach, publishing, billing, refunds, and production changes require explicit administrator controls.
