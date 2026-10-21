# Guía del GUL-UC3M para la instalación de Linux

[gul.uc3m.es/guia](https://gul.uc3m.es/guia/)


Esta página es generada usando [Zensical](https://zensical.org/).

Para generar la página, usando [uv](https://docs.astral.sh/uv/):
```
uv run python scripts/sync_webpage_styles.py
uv run zensical build
```

Servir la página (con hot-reload):
```
uv run zensical serve
```


## Estilos de la web del GUL

El CSS, las fuentes, el header y el footer vienen de
[guluc3m/webpage](https://github.com/guluc3m/webpage):
`scripts/sync_webpage_styles.py` los genera en `docs/assets/webpage/` y
`overrides/partials/` a partir del último release de webpage. No están en el repo
(`.gitignore`), así que hay que ejecutarlo antes del primer build. No se editan a
mano: los cambios van en el _script_.

Para usar un build local de webpage en vez del release:
```
cd ../webpage && pnpm install && pnpm build
cd ../linux-install && uv run python scripts/sync_webpage_styles.py --dist-dir ../webpage/dist
```