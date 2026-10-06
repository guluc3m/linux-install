# Guía del GUL-UC3M para la instalación de Linux

Esta página es generada usando [Zensical](https://zensical.org/).


Para generar la página, usando [uv](https://docs.astral.sh/uv/):
```
uv run zensical build
```

Servir la página (con hot-reload):
```
uv run zensical serve
```


## Estilos de la web del GUL

La guía usa el CSS, las fuentes, el header y el footer de la web principal
([guluc3m/webpage](https://github.com/guluc3m/webpage)). No se copian a mano:
`scripts/sync_webpage_styles.py` los extrae del `dist/` ya compilado de webpage y
genera estos ficheros (**no editarlos directamente**, se sobreescriben en cada sync):

- `docs/assets/webpage/` — CSS, fuentes, favicon, logo y otros SVG.
- `overrides/partials/header.html` y `overrides/partials/footer.html`.

Cualquier ajuste al header/footer (botones extra, enlaces, atributos) va en el
propio script, para que se reaplique en cada sync.

### Automático

Al publicar un tag en webpage, su `release.yml` sube el `dist/` a una GitHub
Release y avisa a este repo, cuyo workflow `sync-webpage-styles.yml` descarga ese
release, ejecuta el script y commitea el resultado. Necesita el secret
`LINUX_INSTALL_DISPATCH_TOKEN` en webpage (un token con permiso sobre este repo).
Sin él, el workflow se puede lanzar a mano desde *Actions → Sync webpage styles →
Run workflow*.

Ojo: solo sincroniza **releases**; un commit en `master` de webpage no llega a la
guía hasta que se publica un tag.

### Manual (en local)

Con webpage clonado al lado (`../webpage`):
```
cd ../webpage && git pull && pnpm install && pnpm build
cd ../linux-install && python3 scripts/sync_webpage_styles.py --dist-dir ../webpage/dist
uv run zensical serve
```