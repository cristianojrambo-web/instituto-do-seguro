"""Renderiza um arquivo HTML local em PNG via Chromium headless (Edge)."""

import subprocess

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def render(html_path: str, png_path: str, width: int = 1080, height: int = 1350):
    file_url = "file:///" + html_path.replace("\\", "/")
    subprocess.run(
        [
            EDGE_PATH,
            "--headless",
            "--disable-gpu",
            f"--screenshot={png_path}",
            f"--window-size={width},{height}",
            file_url,
        ],
        capture_output=True,
        timeout=30,
    )
