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


## Quick Reference: Flask & JS Patterns

You don't need deep experience with Flask or JavaScript to do HW1,
but if you haven't used either before, here's the pattern this app
follows. Everything you need for the four HW1 features looks like
one of the examples below.

### Flask: reading data from a request

```python
@app.route("/api/example", methods=["POST"])
def example():
    data = request.get_json(force=True)   # parses the JSON body
    value = data.get("some_key")          # pull out a field, like a dict
    return jsonify({"result": value})     # send JSON back
```

That's the whole pattern used throughout `app.py`. A route is a
Python function. It reads whatever the frontend sent in the request
body, does something with it, and returns JSON.

### Flask: adding a new route

```python
@app.route("/api/regenerate", methods=["POST"])
def regenerate():
    # your logic here
    return jsonify({"reply": "..."})
```

Copy the shape of an existing route (`chat()` in `app.py` is the best
example), rename it, change what's inside.

### JavaScript: calling your Flask route from the frontend

```javascript
const res = await fetch("/api/example", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ some_key: "some value" }),
});
const data = await res.json();
console.log(data.result);
```

This is the same pattern used in `static/chat.js`'s `fetch("/api/chat", ...)`
call. `fetch` sends a request, `await res.json()` reads the response
back as a JavaScript object.

### JavaScript: adding a UI element

```javascript
// creating and inserting an element
const div = document.createElement("div");
div.textContent = "some text";
document.getElementById("chat-log").appendChild(div);

// reacting to a click
document.getElementById("some-button").addEventListener("click", () => {
  // your logic here
});
```

`static/chat.js` already does both of these (see `appendMessage` and
the form's `submit` listener). Copy the pattern rather than starting
from a blank file.

### If you get stuck

- Read the existing code in `app.py` and `chat.js` before writing
  anything new, most of what you need is a small variation on a
  pattern that's already there.
- Python errors print to the terminal where `python app.py` is
  running, read the last few lines, they usually say exactly what
  broke.
- JavaScript errors show up in the browser console (right-click the
  page, Inspect, Console tab).
- Come to office hours before you're stuck for more than 20-30
  minutes on something that feels like it should be simple.
