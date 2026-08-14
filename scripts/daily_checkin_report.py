import os
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv

from notify_telegram import send

QUERY = """
query GetPosts($input: PostsInput!) {
  posts(input: $input) {
    edges { node { id text dueAt sentAt status } }
  }
}
"""

ORG_ID = "6a68ee434a6607e01f279693"
CHANNEL_ID = "6a68eeba4b2d03035f58a0e6"


def build_message() -> str:
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "config", ".env"))
    key = os.environ["BUFFER_API_KEY"]
    r = requests.post(
        "https://api.buffer.com/graphql",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"query": QUERY, "variables": {"input": {"organizationId": ORG_ID, "filter": {"channelIds": [CHANNEL_ID]}}}},
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()["data"]["posts"]["edges"]

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=30)
    recent = [
        e["node"] for e in data
        if e["node"]["dueAt"] and cutoff < datetime.fromisoformat(e["node"]["dueAt"].replace("Z", "+00:00")) <= now
    ]

    if not recent:
        return "Instituto do Seguro: check-in diario - nada estava programado pras ultimas 30h."

    sent = [p for p in recent if p["status"] == "sent"]
    errored = [p for p in recent if p["status"] == "error"]

    lines = [f"Instituto do Seguro: check-in diario - {len(sent)} publicado(s), {len(errored)} com erro."]
    for p in errored:
        lines.append(f"ERRO: {p['id']} - {p['text'][:60]}")
    return "\n".join(lines)


if __name__ == "__main__":
    msg = build_message()
    print(msg)
    send(msg)
