#!/usr/bin/env python3
"""Genera los estilos de webpage para la guía: CSS, fuentes, favicon, SVG
(docs/assets/webpage/) y el header y footer (overrides/partials/), a partir
del dist/ ya compilado de guluc3m/webpage. Ver issue #22.

Uso:
    python3 scripts/sync_webpage_styles.py                             # último release de webpage
    python3 scripts/sync_webpage_styles.py --dist-dir ../webpage/dist  # build local

Hay que ejecutarlo antes de `zensical build`/`serve`: lo que genera está en
.gitignore. Solo stdlib.
"""

import argparse
import json
import os
import re
import shutil
import tarfile
import tempfile
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "docs" / "assets" / "webpage"
OVERRIDES_DIR = REPO_ROOT / "overrides" / "partials"
LATEST_RELEASE = "https://api.github.com/repos/guluc3m/webpage/releases/latest"

# Botón del menú de navegación de la guía (#__drawer de Zensical), con el
# mismo aspecto y posición (order-1) que la hamburguesa de gul-Nav, que en la
# guía se oculta (extra.css) para no tener dos.
DRAWER_TOGGLE = (
    '<label for="__drawer" aria-label="Navegación" class="gul-drawer-toggle order-1 '
    'flex size-9 cursor-pointer items-center justify-center rounded-md text-gul-muted hover:text-gul-ink">'
    '<svg viewBox="0 0 24 24" class="size-5 stroke-current stroke-2" fill="none">'
    '<path d="M4 7h16M4 12h16M4 17h16"/></svg></label>'
)
# En móvil/tablet el buscador (que vive en el panel izquierdo) queda tapado
# por el menú desplegable: lupa en el header que pulsa ese mismo botón.
SEARCH_TOGGLE = (
    '<button type="button" aria-label="Buscar" onclick="document.querySelector(\'.md-search__button\').click()" '
    'class="gul-search-toggle order-2 flex size-9 cursor-pointer items-center justify-center rounded-md text-gul-muted hover:text-gul-ink">'
    '<svg viewBox="0 0 24 24" class="size-5 stroke-current stroke-2" fill="none">'
    '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg></button>'
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
        if src.suffix == ".css":
            # Astro emite url() absolutas a /_astro/... (asume deploy en la
            # raíz del dominio) — aquí el CSS y sus fuentes/iconos viven
            # juntos y planos, así que basta la ruta relativa. Sin esto, en
            # local (y en cualquier deploy que no sea la raíz exacta de
            # webpage) esas URLs dan 404 y el navegador cae a la fuente del
            # sistema sin avisar.
            text = re.sub(r'(url\((["\']?))/_astro/', r'\1', src.read_text(encoding="utf-8"))
            (astro_dst / basename).write_text(text, encoding="utf-8")
            for ref in re.findall(r'url\((["\']?)([^"\')]+)\1\)', text):
                url = ref[1]
                if url.startswith("data:"):
                    continue
                copy_asset(url.rsplit("/", 1)[-1])
        else:
            shutil.copy2(src, astro_dst / basename)

    for href in css_hrefs:
        copy_asset(href.rsplit("/", 1)[-1])

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    imports = "\n".join(
        f'@import url("_astro/{href.rsplit("/", 1)[-1]}");' for href in css_hrefs
    )
    (ASSETS_DIR / "global.css").write_text(imports + "\n", encoding="utf-8")

    # 1b. Favicon, logo y Tux: ficheros estáticos de webpage/public/, no de
    #     _astro/ (Astro los copia tal cual a la raíz del dist). Favicon y
    #     logo van a theme.favicon/theme.logo en zensical.toml (el logo solo
    #     se ve en el header de fallback); tux.svg lo usa extra.css como
    #     máscara para el icono de Tux.
    for name in ("favicon.png", "logo-gul-dark.svg", "tux.svg"):
        shutil.copy2(dist_dir / name, ASSETS_DIR / name)

    def local_images(html: str) -> str:
        # Header/footer piden imágenes de webpage/public/ con ruta absoluta
        # (src="/logo-gul-dark.svg"): solo resuelven si webpage está servido
        # en la raíz del mismo dominio — en local, rotas. Se copian a la guía y el
        # src pasa por el filtro `url` de Zensical (relativo a cada página).
        def sub(m: re.Match) -> str:
            name = m.group(1)
            shutil.copy2(dist_dir / name, ASSETS_DIR / name)
            return f"src=\"{{% endraw %}}{{{{ 'assets/webpage/{name}' | url }}}}{{% raw %}}\""

        return re.sub(r'src="/([^"/]+\.(?:svg|png|jpe?g|webp))"', sub, html)

    def webpage_links(html: str) -> str:
        # Los enlaces del header (logo → "/", nav → "/actividades/"...) son
        # rutas de webpage; servidos desde la guía caerían en la guía (en
        # local, "/" redirige a /guia). Se anclan a extra.homepage.
        return re.sub(
            r'href="/(?!/)',
            'href="{% endraw %}{{ config.extra.homepage }}{% raw %}/',
            html,
        )

    # 2. Header: el header de webpage no trae el toggle del panel de
    #    navegación de la guía (drawer) ni el buscador (movido al panel
    #    izquierdo, overrides/main.html) — se le añaden ese toggle y una lupa,
    #    sin los que en móvil no habría forma de navegar ni buscar.
    header_html = extract_element(index_html, "header")
    # bundle.js de Zensical exige un [data-md-component=header]: sin él lanza
    # al arrancar y no monta el resto de componentes (la búsqueda incluida).
    header_html = header_html.replace("<header ", '<header data-md-component="header" ', 1)
    header_html = header_html.replace("</header>", f"{DRAWER_TOGGLE}{SEARCH_TOGGLE}</header>")
    header_html = webpage_links(local_images(header_html))
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
    footer_html = webpage_links(local_images(footer_html + "\n" + trailing))
    (OVERRIDES_DIR / "footer.html").write_text(
        "{% raw %}\n" + footer_html + "\n{% endraw %}\n", encoding="utf-8"
    )

    print(f"CSS: docs/assets/webpage/global.css -> {len(css_hrefs)} chunk(s)")
    print(f"Favicon/logo: docs/assets/webpage/{{favicon.png,logo-gul-dark.svg}}")
    print(f"Header: {len(header_html)} bytes -> {OVERRIDES_DIR / 'header.html'}")
    print(f"Footer: {len(footer_html)} bytes -> {OVERRIDES_DIR / 'footer.html'}")


def download_latest_release(dest: Path) -> None:
    """Descarga y extrae en `dest` el dist/ del último release de webpage
    (el tarball que adjunta su release.yml)."""
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.environ.get("GITHUB_TOKEN"):  # evita el límite de la API en CI
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(LATEST_RELEASE, headers=headers)
    with urllib.request.urlopen(req) as resp:
        release = json.load(resp)
    asset = next(a for a in release["assets"] if a["name"].endswith(".tar.gz"))
    print(f"Release: {release['tag_name']} ({asset['name']})")
    tarball = dest / asset["name"]
    with urllib.request.urlopen(asset["browser_download_url"]) as resp, open(tarball, "wb") as f:
        shutil.copyfileobj(resp, f)
    with tarfile.open(tarball) as tar:
        tar.extractall(dest, filter="data")  # sin rutas absolutas ni ../


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--dist-dir",
        type=Path,
        help="dist/ de webpage ya compilado (por defecto se descarga el último release)",
    )
    args = parser.parse_args()
    if args.dist_dir:
        sync(args.dist_dir)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            download_latest_release(Path(tmp))
            sync(Path(tmp))
