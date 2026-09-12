#!/usr/bin/env python3
"""Build script que ensambla los archivos de secciones en una sola página HTML."""
import os
import re
import sys
import shutil

SECTIONS_DIR = os.path.join(os.path.dirname(__file__), "sections")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "dist")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

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

  <!-- Canonical -->
  <link rel="canonical" href="https://maselli-automotores.vercel.app/">

  <!-- Open Graph -->
  <meta property="og:title" content="Maselli Automotores | Compra y venta de autos en Salta">
  <meta property="og:description" content="Compra y venta de vehículos usados en Salta Capital. Stock multimarca, asesoramiento personalizado y financiación.">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_AR">
  <meta property="og:site_name" content="Maselli Automotores">
  <meta property="og:image" content="https://maselli-automotores.vercel.app/image/maselli-logo2.webp">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Maselli Automotores | Compra y venta de autos en Salta">
  <meta name="twitter:description" content="Compra y venta de vehículos usados en Salta Capital.">
  <meta name="twitter:image" content="https://maselli-automotores.vercel.app/image/maselli-logo2.webp">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "AutoDealer",
    "name": "Maselli Automotores",
    "description": "Compra y venta de vehículos usados en Salta Capital. Stock multimarca, asesoramiento personalizado y financiación.",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Salta",
      "addressRegion": "Salta",
      "addressCountry": "AR",
      "postalCode": "4400"
    }},
    "telephone": "+5493875322496",
    "url": "https://maselli-automotores.vercel.app"
  }}
  </script>

  <!-- Fonts (self-hosted) -->
  <link rel="stylesheet" href="css/fonts.css">

  <!-- Theme -->
  <meta name="theme-color" content="#0A1628">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">

  <!-- Styles -->
  <link rel="stylesheet" href="css/style.css">

  <!-- Preload hero image -->
  <link rel="preload" href="image/maselli-logo2.webp" as="image">
</head>

<body>
  {sections}

  <!-- JavaScript -->
  <script defer src="js/main.js"></script>
  <noscript>
    <style>.skip-link,.hamburger,.mobile-drawer{{display:none}}</style>
  </noscript>
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
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Copy static assets to dist/
    static_dirs = ["css", "js", "fonts", "image"]
    static_files = ["favicon.svg", "robots.txt", "sitemap.xml"]

    for dirname in static_dirs:
        src = os.path.join(os.path.dirname(__file__), dirname)
        dst = os.path.join(OUTPUT_DIR, dirname)
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)

    for filename in static_files:
        src = os.path.join(os.path.dirname(__file__), filename)
        dst = os.path.join(OUTPUT_DIR, filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)

    # Build HTML from sections
    parts = []
    for section_file in SECTION_ORDER:
        path = os.path.join(SECTIONS_DIR, section_file)
        if not os.path.isfile(path):
            print(f"Error: sección no encontrada: {path}", file=sys.stderr)
            sys.exit(1)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().rstrip("\n")
        except Exception as e:
            print(f"Error leyendo {path}: {e}", file=sys.stderr)
            sys.exit(1)
        parts.append(strip_wrappers(content))

    html = HTML_TEMPLATE.format(sections="\n\n".join(parts))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Build completado: {OUTPUT_FILE} desde {len(parts)} secciones")


if __name__ == "__main__":
    build()
