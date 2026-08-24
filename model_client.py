"""
Pluggable model client.

MockModelClient is the default: no downloads, no external server, no
API key. It returns deterministic canned responses so the app works
out of the box and students can build and test features (HW1-HW3)
without needing a real model running.

LlamaCppClient is left here, ready to use, for HW4: point it at a
running llama.cpp server (llama-server, OpenAI-compatible endpoint,
default port 8080) and swap it in for MockModelClient in app.py.
That's the only change HW4 requires in this file.
"""

import time


class MockModelClient:
    """Default client. Deterministic, no dependencies beyond the stdlib."""

    def chat(self, messages, system_prompt=None):
        last_user_msg = messages[-1]["content"] if messages else ""
        time.sleep(0.3)  # simulate real network/inference latency
        return {
            "role": "assistant",
            "content": (
                f"[mock response] You said: {last_user_msg!r}. "
                f"(system prompt: {system_prompt or 'none'})"
            ),
        }


class LlamaCppClient:
    """
    HW4: connects to a local llama.cpp server's OpenAI-compatible
    chat completions endpoint. Not used by default; swap it in for
    MockModelClient in app.py once your local server is running.

    Start a server first, e.g.:
        llama-server -m path/to/model.gguf --port 8080
    """

    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url

    def chat(self, messages, system_prompt=None):
        import requests

        payload_messages = []
        if system_prompt:
            payload_messages.append({"role": "system", "content": system_prompt})
        payload_messages.extend(messages)

        resp = requests.post(
            f"{self.base_url}/v1/chat/completions",
            json={"messages": payload_messages},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]
