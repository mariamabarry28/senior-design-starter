"""
Minimal tests for the starter app. Run with: pytest

These are intentionally small. When you add your HW1 feature, add at
least one test that exercises it, that's part of good PR hygiene,
even though it's not separately graded this round.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app, conversation


@pytest.fixture
def client():
    app.config["TESTING"] = True
    conversation.clear()
    with app.test_client() as c:
        yield c


def test_index_loads(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_chat_requires_message(client):
    resp = client.post("/api/chat", json={})
    assert resp.status_code == 400


def test_chat_returns_reply(client):
    resp = client.post("/api/chat", json={"message": "hello"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "reply" in data
    assert "hello" in data["reply"]


def test_reset_clears_conversation(client):
    client.post("/api/chat", json={"message": "hello"})
    assert len(conversation) > 0
    client.post("/api/reset")
    assert len(conversation) == 0
