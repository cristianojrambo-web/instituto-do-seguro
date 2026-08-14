import argparse
import sys

from check_post_metrics import fetch_metrics
from notify_telegram import send

BASELINE_REACH = 2  # alcance travado observado nos primeiros posts em imagem/carrossel


def build_message(post_id: str, label: str) -> str:
    post = fetch_metrics(post_id)
    metrics = post.get("metrics") or []
    header = f"Instituto do Seguro: metricas {label} do 1o Reels (post {post_id[:8]}...)"

    if not metrics:
        return (
            f"{header}\n\n"
            f"Status do post: {post['status']}. Nenhuma metrica disponivel ainda no Buffer "
            f"(pode ser que o Instagram ainda nao tenha reportado os dados)."
        )

    by_name = {m["name"]: m for m in metrics}
    lines = [f"- {m['name']}: {m['value']:g}{m['unit'] or ''}" for m in metrics]
    reach = next((m["value"] for m in metrics if "reach" in m["name"].lower() or "alcance" in m["name"].lower()), None)

    veredito = "sem dado de alcance pra comparar"
    if reach is not None:
        if reach > BASELINE_REACH:
            veredito = f"SUPEROU o baseline anterior de {BASELINE_REACH} de alcance"
        elif reach == BASELINE_REACH:
            veredito = f"empatou com o baseline anterior de {BASELINE_REACH} de alcance"
        else:
            veredito = f"ficou ABAIXO do baseline anterior de {BASELINE_REACH} de alcance"

    return f"{header}\n\n" + "\n".join(lines) + f"\n\nVeredito: {veredito}."


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--post-id", required=True)
    ap.add_argument("--label", required=True, help="ex: 24h ou 48h")
    args = ap.parse_args()

    msg = build_message(args.post_id, args.label)
    print(msg)
    send(msg)
