#!/usr/bin/env python3
"""Vendoriza el CSS y el Header/Footer compilados de ../webpage dentro de
docs/, a partir de un `dist/` de Astro ya construido (el tarball que
webpage's release.yml adjunta a cada GitHub Release). Ver issue #22 y el
plan en .claude/plans/fluttering-swimming-riddle.md.

Uso:
    python scripts/sync_webpage_styles.py --dist-dir /tmp/webpage-dist

Se ejecuta desde .github/workflows/sync-webpage-styles.yml tras descargar y
extraer el último release de guluc3m/webpage. No añade dependencias: solo
stdlib.
"""

import argparse
import re
import shutil
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "docs" / "assets" / "webpage"
OVERRIDES_DIR = REPO_ROOT / "overrides" / "partials"

DRAWER_TOGGLE = (
    '<label class="md-header__button md-icon" for="__drawer" '
    'aria-label="Navegación">'
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
    '<path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" fill="none"/>'
    "</svg></label>"
)


def extract_element(html: str, tag: str, attr: tuple[str, str] | None = None) -> str:
    """Devuelve el HTML exacto del primer <tag ...>...</tag> que hace match
    (si `attr` se da, requiere que el atributo coincida en la etiqueta de
    apertura). Usa html.parser (stdlib) en vez de una dependencia de parsing
    HTML de terceros."""
    lines = html.splitlines(keepends=True)
    cum = [0]
    for line in lines:
        cum.append(cum[-1] + len(line))

    state = {"start": None, "end": None, "depth": 0}

    class _P(HTMLParser):
        def handle_starttag(self, t, attrs):
            if t != tag or state["end"] is not None:
                return
            if state["start"] is None:
                if attr and dict(attrs).get(attr[0]) != attr[1]:
                    return
                line, col = self.getpos()
                state["start"] = cum[line - 1] + col
                state["depth"] = 1
            else:
                state["depth"] += 1

        def handle_endtag(self, t):
            if t != tag or state["start"] is None or state["end"] is not None:
                return
            state["depth"] -= 1
            if state["depth"] == 0:
                line, col = self.getpos()
                state["end"] = cum[line - 1] + col + len(f"</{t}>")

    _P().feed(html)
    if state["start"] is None or state["end"] is None:
        needle = f"<{tag}>" if not attr else f'<{tag} {attr[0]}="{attr[1]}">'
        raise ValueError(f"no se encontró {needle} en el dist/ de webpage")
    return html[state["start"] : state["end"]]


def sync(dist_dir: Path) -> None:
    index_html = (dist_dir / "index.html").read_text(encoding="utf-8")

    # 1. CSS: solo los ficheros que index.html enlaza (Astro los parte en
    #    varios chunks — uno "global" con el bundle de Tailwind completo,
    #    otros con estilos scoped de componentes de esta página en
    #    concreto), no _astro/ entero — ese directorio también contiene
    #    fotos/JS de páginas de webpage que no pintan nada aquí. Se copian
    #    además los ficheros que esos CSS referencian vía url() (fuentes,
    #    iconos), resolviendo esas referencias de forma recursiva.
    astro_src = dist_dir / "_astro"
    astro_dst = ASSETS_DIR / "_astro"
    if astro_dst.exists():
        shutil.rmtree(astro_dst)  # limpia hashes de un sync anterior
    astro_dst.mkdir(parents=True)

    css_hrefs = re.findall(r'<link rel="stylesheet" href="([^"]+)"', index_html)
    if not css_hrefs:
        raise ValueError('no se encontró <link rel="stylesheet"> en index.html')

    copied: set[str] = set()

    def copy_asset(basename: str) -> None:
        if basename in copied:
            return
        copied.add(basename)
        src = astro_src / basename
        shutil.copy2(src, astro_dst / basename)
        if src.suffix == ".css":
            for ref in re.findall(r'url\((["\']?)([^"\')]+)\1\)', src.read_text(encoding="utf-8")):
                url = ref[1]
                if url.startswith("data:"):
                    continue
                copy_asset(url.rsplit("/", 1)[-1])

    for href in css_hrefs:
        copy_asset(href.rsplit("/", 1)[-1])

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    imports = "\n".join(
        f'@import url("_astro/{href.rsplit("/", 1)[-1]}");' for href in css_hrefs
    )
    (ASSETS_DIR / "global.css").write_text(imports + "\n", encoding="utf-8")

    # 2. Header: el header de webpage no trae el toggle del panel de
    #    navegación de la guía (drawer) ni el buscador (movido al panel
    #    izquierdo, docs/overrides/main.html) — se le añade solo el toggle,
    #    sin el que no habría forma de abrir la navegación en móvil.
    header_html = extract_element(index_html, "header")
    header_html = header_html.replace("</header>", f"{DRAWER_TOGGLE}</header>")
    OVERRIDES_DIR.mkdir(parents=True, exist_ok=True)
    (OVERRIDES_DIR / "header.html").write_text(
        "{% raw %}\n" + header_html + "\n{% endraw %}\n", encoding="utf-8"
    )

    # 3. Footer: verbatim. gul-Footer.astro's <script>/<noscript> (reveal-on-
    #    scroll, y el <script> que desofusca los data-gul-email — usado
    #    también por el dropdown de Contacta del header) son HERMANOS de
    #    <footer>, no hijos — sin ellos el footer se queda en opacity:0 para
    #    siempre (nada añade .is-visible) y el email nunca se desofusca.
    #    Se incluyen tal cual detrás del footer: al ir después del header en
    #    el documento, su querySelectorAll también alcanza los elementos del
    #    header.
    footer_html = extract_element(index_html, "footer", attr=("id", "legal"))
    footer_end = index_html.index(footer_html) + len(footer_html)
    body_end = index_html.index("</body>")
    trailing = index_html[footer_end:body_end].strip()
    footer_html = footer_html + "\n" + trailing
    (OVERRIDES_DIR / "footer.html").write_text(
        "{% raw %}\n" + footer_html + "\n{% endraw %}\n", encoding="utf-8"
    )

    print(f"CSS: docs/assets/webpage/global.css -> {len(css_hrefs)} chunk(s)")
    print(f"Header: {len(header_html)} bytes -> docs/overrides/partials/header.html")
    print(f"Footer: {len(footer_html)} bytes -> docs/overrides/partials/footer.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dist-dir",
        required=True,
        type=Path,
        help="Directorio con el dist/ de webpage ya extraído (contiene index.html, _astro/, ...)",
    )
    args = parser.parse_args()
    sync(args.dist_dir)
