"""
Publica uma imagem com legenda no Instagram via Graph API da Meta.

Uso:
    python scripts/publish.py --image URL_OU_CAMINHO_PUBLICO --caption "texto da legenda"

Pré-requisito: config/.env preenchido (ver SETUP.md, Parte 3).
A imagem precisa estar acessível por URL pública (a Graph API não aceita upload de arquivo local
diretamente) — por enquanto, hospede em um bucket público ou pasta servida via HTTP antes de publicar.
"""

import argparse
import os
import sys
import time

import requests
from dotenv import load_dotenv

GRAPH_API_VERSION = "v21.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "config", ".env"))

ACCESS_TOKEN = os.environ.get("IG_ACCESS_TOKEN")
IG_ACCOUNT_ID = os.environ.get("IG_BUSINESS_ACCOUNT_ID")


def create_media_container(image_url: str, caption: str) -> str:
    resp = requests.post(
        f"{GRAPH_API_BASE}/{IG_ACCOUNT_ID}/media",
        data={
            "image_url": image_url,
            "caption": caption,
            "access_token": ACCESS_TOKEN,
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["id"]


def wait_until_ready(container_id: str, timeout_s: int = 60) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        resp = requests.get(
            f"{GRAPH_API_BASE}/{container_id}",
            params={"fields": "status_code", "access_token": ACCESS_TOKEN},
            timeout=30,
        )
        resp.raise_for_status()
        status = resp.json().get("status_code")
        if status == "FINISHED":
            return
        if status == "ERROR":
            raise RuntimeError(f"Container {container_id} falhou ao processar")
        time.sleep(2)
    raise TimeoutError(f"Container {container_id} não ficou pronto em {timeout_s}s")


def publish_container(container_id: str) -> str:
    resp = requests.post(
        f"{GRAPH_API_BASE}/{IG_ACCOUNT_ID}/media_publish",
        data={"creation_id": container_id, "access_token": ACCESS_TOKEN},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["id"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True, help="URL pública da imagem")
    parser.add_argument("--caption", required=True, help="Legenda do post")
    args = parser.parse_args()

    if not ACCESS_TOKEN or not IG_ACCOUNT_ID:
        sys.exit("Faltam IG_ACCESS_TOKEN / IG_BUSINESS_ACCOUNT_ID em config/.env — ver SETUP.md")

    container_id = create_media_container(args.image, args.caption)
    print(f"Container criado: {container_id}")
    wait_until_ready(container_id)
    post_id = publish_container(container_id)
    print(f"Publicado! ID do post: {post_id}")


if __name__ == "__main__":
    main()
