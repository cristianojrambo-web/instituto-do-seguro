import argparse
import json
import os
import sys

import requests
from dotenv import load_dotenv

QUERY = """
query CheckPost($input: PostInput!) {
  post(input: $input) {
    id
    status
    sentAt
    metricsUpdatedAt
    text
    metrics { name type unit value description }
  }
}
"""


def fetch_metrics(post_id: str) -> dict:
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "config", ".env"))
    key = os.environ["BUFFER_API_KEY"]
    r = requests.post(
        "https://api.buffer.com/graphql",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"query": QUERY, "variables": {"input": {"id": post_id}}},
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(data["errors"])
    return data["data"]["post"]


def format_summary(post: dict) -> str:
    metrics = post.get("metrics") or []
    if not metrics:
        return f"Post {post['id']} (status={post['status']}): metricas ainda nao disponiveis."
    parts = [f"{m['name']}={m['value']:g}{m['unit'] or ''}" for m in metrics]
    return f"Post {post['id']} (status={post['status']}): " + ", ".join(parts)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--post-id", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    post = fetch_metrics(args.post_id)
    if args.json:
        print(json.dumps(post, indent=2, ensure_ascii=False))
    else:
        print(format_summary(post))
