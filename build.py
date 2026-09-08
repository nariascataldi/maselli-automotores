#!/usr/bin/env python3
"""Build script que ensambla los archivos de secciones en una sola página HTML."""
import os
import re

SECTIONS_DIR = os.path.join(os.path.dirname(__file__), "sections")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "index.html")

SECTION_ORDER = [
    "01-intro.html",
    "02-header.html",
    "03-mobile-drawer.html",
    "04-hero.html",
    "05-about.html",
    "06-servicios.html",
    "07-testimonios.html",
    "08-contacto.html",
    "09-footer.html",
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Maselli Automotores - Compra y venta de vehículos usados en Salta Capital. Stock multimarca, asesoramiento personalizado y financiación.">
  <meta name="robots" content="index, follow">
  <title>Maselli Automotores | Compra y venta de autos en Salta</title>

  <!-- Open Graph -->
  <meta property="og:title" content="Maselli Automotores | Compra y venta de autos en Salta">
  <meta property="og:description" content="Compra y venta de vehículos usados en Salta Capital. Stock multimarca, asesoramiento personalizado y financiación.">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_AR">
  <meta property="og:site_name" content="Maselli Automotores">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">

  <!-- Theme -->
  <meta name="theme-color" content="#0A1628">

  <!-- Styles -->
  <link rel="stylesheet" href="css/style.css">
</head>

<body>
{sections}

  <!-- JavaScript -->
  <script defer src="js/main.js"></script>
</body>

</html>
"""

HEAD_PATTERN = re.compile(r"<head>.*?</head>\s*", re.DOTALL)
DOCTYPE_PATTERN = re.compile(r"<!DOCTYPE[^>]*>\s*", re.IGNORECASE)
HTML_OPEN_PATTERN = re.compile(r"<html[^>]*>\s*", re.IGNORECASE)
HTML_CLOSE_PATTERN = re.compile(r"</html>\s*", re.IGNORECASE)
BODY_OPEN_PATTERN = re.compile(r"<body[^>]*>\s*", re.IGNORECASE)
BODY_CLOSE_PATTERN = re.compile(r"</body>\s*", re.IGNORECASE)


def strip_wrappers(html_content):
    content = DOCTYPE_PATTERN.sub("", html_content)
    content = HEAD_PATTERN.sub("", content)
    content = HTML_OPEN_PATTERN.sub("", content)
    content = HTML_CLOSE_PATTERN.sub("", content)
    content = BODY_OPEN_PATTERN.sub("", content)
    content = BODY_CLOSE_PATTERN.sub("", content)
    return content


def build():
    parts = []
    for section_file in SECTION_ORDER:
        path = os.path.join(SECTIONS_DIR, section_file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().rstrip("\n")
        parts.append(strip_wrappers(content))

    html = HTML_TEMPLATE.format(sections="\n\n".join(parts))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Build completado: {OUTPUT_FILE} desde {len(parts)} secciones")


if __name__ == "__main__":
    build()
