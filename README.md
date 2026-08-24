# Local Chat, Starter App

Minimal local-LLM chat app. This is the shared starter code for
Senior Design HW1 through HW5.

**No deployment, no API keys, and no model download are required to
run this.** It works out of the box using a mock model client. You'll
swap in a real local model later, in HW4.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open **http://localhost:5000** in your browser.

## Run the tests

```bash
pytest
```

## How it's structured

- `app.py` — Flask app and routes. Look here first.
- `model_client.py` — `MockModelClient` (default, no dependencies) and
  `LlamaCppClient` (for HW4, connects to a real local model server).
- `templates/index.html`, `static/style.css`, `static/chat.js` — the
  frontend. Plain HTML/CSS/JS, no build step, no framework.
- `tests/test_app.py` — a few basic tests. Add to these as you add
  features.

## HW1: pick one feature

Look for `TODO (HW1, ...)` comments in `app.py` and `static/chat.js`.
Pick **one** of the four features described in the HW1 assignment
sheet, implement it on your own branch, and open a PR. Don't
implement more than one, small and well-executed beats sprawling.

## Later assignments

- **HW3** (agentic coding): you'll use an AI coding agent to implement
  a more ambiguous feature on this same codebase.
- **HW4** (local model infrastructure): you'll stand up a real
  llama.cpp server and swap `LlamaCppClient` in for `MockModelClient`
  in `app.py`. That's the only code change required, everything else
  in this app already expects that interface.

## Troubleshooting

- **Port 5000 already in use:** change `port=5000` in `app.py`, or
  stop whatever else is using it.
- **`ModuleNotFoundError`:** make sure your virtual environment is
  activated and `pip install -r requirements.txt` completed without
  errors.
