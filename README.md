# Automation Company Core

A Streamlit dashboard and automation-agent foundation with optional integrations for n8n, Rasa, Huginn, and Mautic.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python -m pytest -q
streamlit run app.py
```

Open <http://localhost:8501>.

## Run with Docker

```bash
docker compose up --build app
```

The complete integration stack is available with:

```bash
docker compose up --build
```

Services:

- Streamlit: <http://localhost:8501>
- n8n: <http://localhost:5678>
- Rasa: <http://localhost:5005>
- Huginn: <http://localhost:3000>
- Mautic: <http://localhost:8080>

## Configuration

Set `AGENT_STEP_DELAY_SECONDS` to a non-negative number when a slower, demonstrative agent run is needed. It defaults to `0` for fast local and container execution.

## Project notes

The application imports the maintained `agents` package. The legacy directories with leading spaces are left untouched in this branch to avoid deleting unknown user work; they can be migrated separately after their contents are reviewed.

## License

This project is licensed under the MIT License.
