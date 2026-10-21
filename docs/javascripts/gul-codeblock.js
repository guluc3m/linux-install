// Convierte los bloques de código de Zensical (div.highlight > pre > code) en
// el markup de gul-CodeBlock.astro de webpage: <pre><code> con el estilo base
// de global.css + el botón de copiar en la esquina, con la misma lógica que el
// <script> del componente (navigator.clipboard, icono copiar → check 1.5 s).
// gul-CodeBlock no colorea sintaxis, así que se descarta el div.highlight y
// con él los colores de pygments.
(() => {
  const BUTTON = `<button type="button" data-gul-copy aria-label="Copiar" class="absolute top-1/2 right-3 -translate-y-1/2 text-gul-muted hover:text-gul-ink">
    <svg data-icon="copy" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    <svg data-icon="check" class="hidden" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
  </button>`;

  document.querySelectorAll('.md-typeset div.highlight').forEach((hl) => {
    const src = hl.querySelector('pre > code');
    if (!src) return;
    const code = document.createElement('code');
    code.append(...src.childNodes);
    // pygments deja un \n final: copiado tal cual, pegarlo en una terminal
    // ejecutaría el comando sin dar opción a revisarlo.
    const last = code.lastChild;
    if (last?.nodeType === Node.TEXT_NODE) last.textContent = last.textContent.replace(/\n$/, '');
    const pre = document.createElement('pre');
    pre.append(code);

    const block = document.createElement('div');
    block.className = 'relative';
    block.dataset.gulCodeblock = '';
    block.append(pre);
    block.insertAdjacentHTML('beforeend', BUTTON);
    hl.replaceWith(block);

    const btn = block.querySelector('[data-gul-copy]');
    const copyIcon = btn.querySelector('[data-icon="copy"]');
    const checkIcon = btn.querySelector('[data-icon="check"]');
    btn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code.textContent ?? '');
      } catch {
        return;
      }
      copyIcon.classList.add('hidden');
      checkIcon.classList.remove('hidden');
      btn.setAttribute('aria-label', 'Copiado');
      window.setTimeout(() => {
        copyIcon.classList.remove('hidden');
        checkIcon.classList.add('hidden');
        btn.setAttribute('aria-label', 'Copiar');
      }, 1500);
    });
  });
})();
