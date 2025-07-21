## Cómo salvar un sistema que no arranca
Si despues de una actualización o configuración que hiciste, lo único que ves son errores de GRUB en la pantalla y no logras llegar a tu login manager, tu mejor amigo es el [chroot](https://wiki.archlinux.org/title/Chroot).

A pesar de que el artículo pertenece a la Arch Wiki, el paso [3.3](https://wiki.archlinux.org/title/Chroot#Using_chroot) se puede aplicar en otras distribuciones también. Este artículo existe también en [Español](https://wiki.archlinux.org/title/Chroot_(Espa%C3%B1ol)), pero es un poco menos completo.

Para esto necesitaras un disco o memoria USB externa desde la que podrás cargar un GNU/Linux en modo LiveOS (preferiblemente el mismo distributivo que el que tienes instalado). Para obtener información sobre como crear un LiveUSB, accede a [este artículo](common.md#cómo-crear-un-live-usb) en la Guía.

Despues de haber conseguido el chroot, básicamente obtienes acceso a tu sistema original, en el que puedes hacer las modificaciones necesarias para obtener un sistema funcional otra vez. Esto incluye actualizarla, regenerar GRUB, cambiar el mirrorlist y descargar versiones antiguas de paquetes, correr Timeshift, etc.

Cuando crees que el error ya está arreglado, ¡puedes reiniciar tu dispositivo y rezar que lo que has hecho era suficiente para restaurarlo!

## Cómo prevenir que te pase esto otra vez
1. Usa [Timeshift](https://github.com/linuxmint/timeshift). Puedes leer más sobre él [aquí](/post-install.md#timeshift).
2. Verifica que si ejecutas cualquier comando, especialmente si es con sudo, **QUE NO TE HAS EQUIVOCADO ESCRIBIENDOLO**. Puedes romper tu sistema con tan solo olvidar el "." (_punto_) en algo tan simple como un `mv ./* carpeta/`, porque en Linux no hay un comando de "ir atrás".
3. Ten cuidado cambiando o moviendo archivos del sistema. Si piensas que puedes mover alguna carpeta como la de /usr/, para liberar espacio en una partición, y luego hacer symlinks a ella para restaurar el funcionamiento previo, no lo vas a poder hacer, porque el programa que hace el symlink **está contenida dentro**. Y allí incluso un chroot puede no salvarte...
4. No dejes errores de sintaxis u otros problemas en archivos de configuración importantes del sistema. Si algo no puede cargar su configuración, igual no va a ni inicializarse, y esto puede suponer un gran problema para el funcionamiento correcto de tu sistema entero.
5. **CREA BACKUPS**. No hay nada peor que perder todos tus archivos. Incluso si siempre tienes cuidado con tu sistema, el mundo es cruel y puedes acabar instalandote un virus o rompiendo dispositivo. Si tienes backups en un disco duro, un NAS, la nube, incluso solo de los archivos más importantes para tí, vas a estar mejor que con todos esos archivos completamente perdidos. Vale toda la pena no estar arrepentiendote en el futuro por no haber hecho más.
