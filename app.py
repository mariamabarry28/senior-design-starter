"""
Minimal local-LLM chat app. Starter code for Senior Design HW1-HW5.

Run it:
    python app.py
Then open http://localhost:5000

No deployment, no API keys, no model download required to get this
running. It uses MockModelClient by default (see model_client.py).
"""

from flask import Flask, render_template, request, jsonify #The class that makes the web application itself
#The above imports allows for the application to work as intended through requests
#redner_templte is what I will manipulate for the conversation history save
from model_client import MockModelClient #Importing the local python file

app = Flask(__name__) #Creates the actual application
model_client = MockModelClient() #Reused instance

# In-memory, single global conversation. Fine for a local demo app;
# intentionally not session-based or persisted yet.
#
# TODO (HW1, "conversation history"): if you pick this feature, make
# this real: persist history per session/user, and display the full
# back-and-forth in the UI, not just the latest exchange.
conversation = []


@app.route("/")
def index(): 
    return render_template("index.html", messages=conversation) #Added the conversation argument to pass to render_template functions from the Flask Import


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify({"error": "message is required"}), 400

    # TODO (HW1, "system-prompt selector"): if you pick this feature,
    # read a chosen preset (e.g. "concise" / "detailed" / "casual")
    # from the request body and turn it into a real system_prompt
    # string passed to model_client.chat() below.
    system_prompt = None

    conversation.append({"role": "user", "content": user_message})

    reply = model_client.chat(conversation, system_prompt=system_prompt)
    conversation.append(reply)

    response_payload = {"reply": reply["content"]}

    # TODO (HW1, "token-count display"): if you pick this feature,
    # compute a token count for the conversation (a simple whitespace
    # split is a fine approximation, you don't need a real tokenizer)
    # and include it in response_payload.

    return jsonify(response_payload)


# TODO (HW1, "regenerate-response button"): if you pick this feature,
# add a route (e.g. POST /api/regenerate) that drops the last
# assistant reply and asks model_client for a new one using the same
# last user message.


@app.route("/api/reset", methods=["POST"])
def reset():
    """Clears the in-memory conversation. Useful while testing."""
    conversation.clear()
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
