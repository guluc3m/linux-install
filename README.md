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

El CSS, las fuentes, el header y el footer vienen de
[guluc3m/webpage](https://github.com/guluc3m/webpage) y los genera
`scripts/sync_webpage_styles.py` en `docs/assets/webpage/` y `overrides/partials/`.
No los edites a mano: los cambios van en el script.

Se sincroniza solo al publicar un release en webpage (workflow
`sync-webpage-styles.yml`, también lanzable a mano desde *Actions*). En local:
```
cd ../webpage && git pull && pnpm install && pnpm build
cd ../linux-install && python3 scripts/sync_webpage_styles.py --dist-dir ../webpage/dist
```
