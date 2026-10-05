# Troubleshooting

## Solucionar drivers Wi-Fi
Es relativamente común que los _drivers_ de la tarjeta de red Wi-Fi de los portátiles no vengan instalados por defecto en Linux.

Una forma de obtener conexión a Internet es usando un cable Ethernet, ya sea mediante el puerto Ethernet del ordenador (si lo tiene), o mediante el uso de un adaptador. Si no tienes nada de eso a mano, siempre puedes conectar el ordenador a tu móvil por USB, poner los datos, y compartirlos mediante _Módem USB_ (en Android suele estar en `Ajustes` > `Redes e Internet` > `Punto de acceso y anclaje de red` > `Compartir conexión por USB`).

En ocasiones los _drivers_ se actualizan solos al actualizar el sistema (e.g. `sudo apt update && sudo apt upgrade` para Ubuntu/Mint/Debian, `sudo dnf upgrade` para Fedora, `sudo pacman -Syu` para Arch/Manjaro).

En caso de que esto no solucione tu problema, te va a tocar buscar, descargar, e instalar los _drivers_ a mano. Para ello, primero tendrás que averiguar qué chipset Wi-Fi tiene tu ordenador. Te recomendamos ir a la página del fabricante, o seguir la [guía de nixCraft](https://www.cyberciti.biz/faq/linux-find-wireless-driver-chipset/). Una vez averigüado, te tocará buscar la guía de instalación del _driver_ para tu chipset y distribución específica. Para ello, busca en Google.


## Cómo salvar un sistema que no arranca
Si despues de una actualización o configuración que hiciste, lo único que ves son errores de GRUB en la pantalla y no logras llegar a tu login manager, tu mejor amigo es el [chroot](https://wiki.archlinux.org/title/Chroot).

A pesar de que el artículo pertenece a la Arch Wiki, el paso [4.3](https://wiki.archlinux.org/title/Chroot#Using_chroot) se puede aplicar en otras distribuciones también. Este artículo existe también en [Español](https://wiki.archlinux.org/title/Chroot_(Espa%C3%B1ol)), pero es un poco menos completo.

Para esto necesitaras un disco o memoria USB externa desde la que podrás cargar un GNU/Linux en modo LiveOS (preferiblemente el mismo distributivo que el que tienes instalado). Para ello tendrás que [crear un LiveUSB](liveusb.md#como-crear-un-liveusb) y [arrancar desde él](liveusb.md#arrancar-desde-el-liveusb).

Despues de haber conseguido el chroot, básicamente obtienes acceso a tu sistema original, en el que puedes hacer las modificaciones necesarias para obtener un sistema funcional otra vez. Esto incluye actualizarla, regenerar GRUB, cambiar el mirrorlist y descargar versiones antiguas de paquetes, correr Timeshift, etc.

!!! note
    Cuando la actualizas, tienes que actualizar la partición que has montado con chroot, no el root original del sistema LiveUSB. La manera en la que se hace depende de tu distro:

    - Arch: `pacman -Syu --sysroot /mnt`
    - Ubuntu/Debian: `chroot /mnt apt update && chroot /mnt apt upgrade`
    - Fedora: `dnf --installroot=/mnt --releasever=XX update`

Cuando crees que el error ya está arreglado, ¡puedes reiniciar tu dispositivo y rezar que lo que has hecho era suficiente para restaurarlo!

### Cómo prevenir que te pase esto otra vez
1. Usa [Timeshift](https://github.com/linuxmint/timeshift). Puedes leer más sobre él [aquí](post-install/apps.md#timeshift).
2. Verifica que si ejecutas cualquier comando, especialmente si es con sudo, **QUE NO TE HAS EQUIVOCADO ESCRIBIENDOLO**. Puedes romper tu sistema con tan solo olvidar el "." (_punto_) en algo tan simple como un `mv ./* carpeta/`, porque en Linux no hay un comando de "ir atrás".
3. Ten cuidado cambiando o moviendo archivos del sistema. Si piensas que puedes mover alguna carpeta como la de `/usr/`, para liberar espacio en una partición, y luego hacer symlinks a ella para restaurar el funcionamiento previo, no lo vas a poder hacer, porque el programa que hace el symlink **está contenido dentro**. Y allí incluso un chroot puede no salvarte...
4. No dejes errores de sintaxis u otros problemas en archivos de configuración importantes del sistema. Si algo no puede cargar su configuración, quizás no va a ni inicializarse, y esto puede suponer un gran problema para el funcionamiento correcto de tu sistema entero.
5. **CREA BACKUPS**. No hay nada peor que perder todos tus archivos. Incluso si siempre tienes cuidado con tu sistema, el mundo es cruel y puedes acabar instalandote un virus o rompiendo tu dispositivo. Si tienes backups en un disco duro, un NAS, la nube, incluso solo de los archivos más importantes para tí, vas a estar en una sitacuión muchísimo mejor que con todos esos archivos completamente inrecuperables. Vale toda la pena no estar arrepentiendote en el futuro por no haber hecho más.


## Estoy en Ubuntu Server y no me va el DHCP
1. Activa los servicios
```bash
sudo systemctl enable --now systemd-networkd
sudo systemctl enable --now systemd-resolved
```

2. Mira cual es el adaptador que estas usando con `ip a`

3. Creas /etc/systemd/network/20-wired.network con este contenido:
```
[Match]
Name=nombredelainterfazaqui

[Network]
DHCP=yes
```
4. Ejecuta `sudo systemctl restart systemd-networkd systemd-resolved` para reiniciar los servicios
5. Revisa si tienes intenet con `ping 8.8.8.8` (la IP es de una DNS Google)
