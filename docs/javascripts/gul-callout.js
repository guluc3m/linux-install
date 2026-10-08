// Convierte las admonitions de Markdown (!!! y ???) en el markup de
// gul-Callout.astro de webpage: mismas clases de Tailwind (están en el CSS
// de webpage), sus iconos y el mismo <canvas data-pixel-dissolve> con el
// preset "full" de PixelDissolve.astro. Ese canvas lo pinta el script de
// PixelDissolve que ya trae el header sincronizado: es type="module", así que
// corre después de este (clásico, al final del body) y encuentra los canvas
// ya insertados.
(() => {
  // Un icono por tipo, en el estilo de los de gul-Callout (trazo 1.5 sobre
  // 24x24): de ahí salen info (círculo + i), success (check) y warning
  // (triángulo + !); el resto se dibujan igual.
  const ICON = {
    info: '<circle cx="12" cy="12" r="9"/><line x1="12" y1="11" x2="12" y2="16"/><circle cx="12" cy="8" r="0.75" fill="currentColor" stroke="none"/>',
    note: '<path d="M4 20l1-4L16 5l3 3L8 19z"/><line x1="14" y1="7" x2="17" y2="10"/>',
    tip: '<path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/><line x1="9.5" y1="19" x2="14.5" y2="19"/><line x1="10.5" y1="21.5" x2="13.5" y2="21.5"/>',
    question: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6"/><circle cx="12" cy="17" r="0.75" fill="currentColor" stroke="none"/>',
    warning: '<path d="M12 3.5l9.5 16.5H2.5z"/><line x1="12" y1="10" x2="12" y2="14.5"/><circle cx="12" cy="17" r="0.75" fill="currentColor" stroke="none"/>',
    danger: '<path d="M8.3 3h7.4L21 8.3v7.4L15.7 21H8.3L3 15.7V8.3z"/><line x1="12" y1="7.5" x2="12" y2="13"/><circle cx="12" cy="16.5" r="0.75" fill="currentColor" stroke="none"/>',
    failure: '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
    success: '<path d="M4 12l5 5 11-11"/>',
  };
  const COLOR = { warning: 'text-gul-amber', success: 'text-gul-green', error: 'text-gul-red' };
  // Excepciones por tipo dentro de la variante "aviso" (gul-callout-tip: extra.css).
  const TYPE_COLOR = { info: 'text-gul-blue', tip: 'gul-callout-tip' };
  // gul-Callout solo tiene 3 variantes; el resto de tipos caen en "aviso".
  const VARIANT = { success: 'success', danger: 'error', failure: 'error', bug: 'error' };
  const LABEL = {
    note: 'Nota',
    tip: 'Tip',
    info: 'Info',
    question: 'Pregunta',
    warning: 'Aviso',
    success: 'Éxito',
    danger: 'Peligro',
    failure: 'Error',
    bug: 'Bug',
    example: 'Ejemplo',
    abstract: 'Resumen',
    quote: 'Cita',
  };

  const fromHTML = (s) => {
    const t = document.createElement('template');
    t.innerHTML = s.trim();
    return t.content.firstChild;
  };
  const el = (tag, className, ...children) => {
    const e = document.createElement(tag);
    e.className = className;
    e.append(...children);
    return e;
  };
  const frame = (tag) =>
    el(
      tag,
      'gul-callout relative overflow-hidden rounded-md border border-gul-line bg-gul-surface',
      fromHTML(
        '<canvas data-pixel-dissolve data-cell="3" data-color="0, 117, 176" data-alpha="0.3" data-max-density="0.65" data-x-bias="0.8" data-falloff="1.6" data-ordered-mix="0.75" aria-hidden="true" class="pointer-events-none absolute inset-0 h-full w-full [image-rendering:pixelated]"></canvas>',
      ),
    );
  const icon = (type, color) =>
    fromHTML(
      `<svg viewBox="0 0 24 24" class="size-5 shrink-0 stroke-current stroke-[1.5] ${color}" fill="none" stroke-linejoin="round" stroke-linecap="round">${ICON[type] ?? ICON.info}</svg>`,
    );

  document.querySelectorAll('.md-typeset .admonition, .md-typeset details').forEach((box) => {
    const type = [...box.classList].find((c) => c in LABEL) ?? 'note';
    const v = VARIANT[type] ?? 'warning';
    const color = TYPE_COLOR[type] ?? COLOR[v];
    const title = box.querySelector(':scope > .admonition-title, :scope > summary');
    const raw = title?.textContent.trim() ?? '';
    const text = !raw || raw.toLowerCase() === type ? LABEL[type] : raw;
    title?.remove();

    const body = el('div', 'gul-callout-body text-sm text-gul-muted', ...box.childNodes);

    let out;
    if (box.tagName === 'DETAILS') {
      // Colapsable: <summary> con icono + etiqueta, y el cuerpo en
      // div > div > cuerpo para que el plegado animado de las reglas base de
      // global.css (details > div, grid 0fr → 1fr, el de gul-Accordion)
      // funcione igual que en webpage. El padding va en el nieto, no en el
      // grid item: el padding del item seguiría ocupando alto con la fila a 0.
      out = frame('details');
      out.open = box.open;
      out.append(
        el(
          'summary',
          'relative z-10 p-4 text-sm',
          el('span', 'flex items-start gap-3', icon(type, color), el('span', `font-semibold ${color}`, text)),
        ),
        el('div', '', el('div', 'relative z-10', body)),
      );
    } else {
      // Como el <p> único de gul-Callout: "Etiqueta: texto" en la misma línea.
      const label = el('span', `font-semibold ${color}`, `${text}:`);
      const first = body.firstElementChild;
      if (first?.tagName === 'P') first.prepend(label, ' ');
      else body.prepend(el('p', '', label));
      out = frame('div');
      out.append(el('div', 'relative z-10 p-4', el('div', 'flex items-start gap-3', icon(type, color), body)));
    }
    box.replaceWith(out);
  });
})();
