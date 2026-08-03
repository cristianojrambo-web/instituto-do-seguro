"""Renderiza um arquivo HTML local em PNG via Chromium headless.

Funciona tanto no PC local (Windows, usa o Edge) quanto em rotinas de nuvem
(Linux, usa o Chromium do Playwright pré-instalado em /opt/pw-browsers, com
--no-sandbox porque roda como root em container).
"""

import glob
import os
import shutil
import subprocess
import sys

WINDOWS_EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def _find_browser():
    if sys.platform == "win32" and os.path.exists(WINDOWS_EDGE_PATH):
        return WINDOWS_EDGE_PATH, []

    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        path = shutil.which(name)
        if path:
            return path, ["--no-sandbox"]

    matches = glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome") + glob.glob(
        "/opt/pw-browsers/chromium*/chrome"
    )
    if matches:
        return matches[0], ["--no-sandbox"]

    raise RuntimeError(
        "Nenhum navegador Chromium/Edge encontrado pra renderizar HTML. "
        "No Windows, instale o Edge. Na nuvem, verifique /opt/pw-browsers ou "
        "rode 'pip install playwright && playwright install chromium'."
    )


def render(html_path: str, png_path: str, width: int = 1080, height: int = 1350):
    file_url = "file:///" + html_path.replace("\\", "/")
    browser_path, extra_flags = _find_browser()
    result = subprocess.run(
        [
            browser_path,
            "--headless",
            "--disable-gpu",
            *extra_flags,
            f"--screenshot={png_path}",
            f"--window-size={width},{height}",
            file_url,
        ],
        capture_output=True,
        timeout=30,
    )
    if not os.path.exists(png_path) or os.path.getsize(png_path) < 500:
        raise RuntimeError(
            f"Renderização falhou ou gerou arquivo vazio/corrompido: {png_path}\n"
            f"stdout: {result.stdout.decode(errors='replace')[:500]}\n"
            f"stderr: {result.stderr.decode(errors='replace')[:500]}"
        )
