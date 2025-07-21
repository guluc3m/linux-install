## Cómo crear un LiveUSB
Lo primero, necesitas un USB con al menos 8GB de almacenamiento.  
Sí, todo lo que haya ahí dentro va a desaparecer, así que estás avisado.

1. Descárgate el archivo ISO (e.g. [Ubuntu](https://ubuntu.com/download/desktop)).
2. Descarga [Balena Etcher](https://www.balena.io/etcher), puedes usar la versión portable (sin necesidad de instalar nada), o instalar la aplicación entera.
3. Inserta el USB
4. Corre Balena Etcher
5. Selecciona "Flash from file" y la ISO que te has descargado
6. Selecciona "Select target" y el USB
7. Haz click en "Flash"

> [!TIP]
> Si quieres poder bootear distintas ISOs desde el mismo USB, te recomendamos [Ventoy](https://www.ventoy.net/). _Hasta puedes usar nuestro [tema para Ventoy](https://github.com/guluc3m/ventoy-theme)_.
>
> Échale un vistazo también a [netbook.xyz](https://netboot.xyz/) para bootear ISOs a través de Internet.



## Arrancar desde el LiveUSB
Para instalar Linux es necesario _bootear_ (arrancar) desde el instalador de Linux que tenemos en el [LiveUSB](#cómo-crear-un-live-usb). Para ello, apaga el ordenador y conecta el LiveUSB. Dado que el ordenador _bootea_ automáticamente en el Sistema Operativo que esté configurado, hay que cambiar esto antes de que arranque.

### Desde el _boot menu_
Algunos ordenadores tienen lo que se conoce como un _boot menu_, el cual te permite elegir desde qué disco arrancar el ordenador. Se suele poder acceder a través de alguna tecla como `F11`, `F12` o `DEL`/`Supr` nada más encender el ordenador (antes de entrar al SO). Puedes buscar en Google si tu ordenador lo tiene y cómo acceder a él.  
De cualquier forma, es recomendable entrar en la BIOS para hacer algunas otras configuraciones.

### Desde la BIOS
La alternativa es cambiar la configuración de la BIOS para que arranque el LiveUSB por defecto. Para ello, hay que entrar en la BIOS. Se suele poder acceder a través de alguna tecla nada más encender el ordenador.  
El botón para entrar en la BIOS depende del ordenador. Por lo general son `ESC`, `F11`, `F12`, `F2`, o `DEL`/`Supr`. Si no consigues arrancar la BIOS busca en internet tu modelo de ordenador y qué tecla utilizar.  
Desde Windows, puedes hacer click click en 'Reiniciar'
manteniendo pulsado SHIFT para reiniciar en modo seguro. De ahí, `Menú de recuperacion` → `Solucionar problemas` → `Opciones Avanzadas` → `Firmware UEFI o relacionados`.

Una vez dentro de la BIOS, desactiva el _Secure Boot_ e _Intel(R) Rapid Start Technology_, si lo tienes.
> [!NOTE]
> No es necesario desactivar el Secure Boot para distros como Ubuntu o Fedora, pero si
> estás instalando otra distro, o estás teniendo problemas al arrancar, desactívalo.

Para cambiar el disco de arranque en la BIOS, suele haber una opción o listado de opciones llamada _Boot option Priorities_ o similar, normalmente en el menú _Boot_. Pon como primera opción el LiveUSB, suele llamarse algo como _Generic USB device_ o similar.

> [!NOTE]
> Si ves alguna opción como _Allow booting from USB device_ o similar, asegúrate de que esté activada.

Una vez esté cambiada la prioridad, reinicia y debería arrancar el LiveUSB.



## Solucionar drivers Wi-Fi
Es relativamente común que los _drivers_ de la tarjeta de red Wi-Fi de los portátiles no vengan instalados por defecto en Linux.

Una forma de obtener conexión a Internet es usando un cable Ethernet, ya sea mediante el puerto Ethernet del ordenador (si lo tiene), o mediante el uso de un adaptador. Si no tienes nada de eso a mano, siempre puedes conectar el ordenador a tu móvil por USB, poner los datos, y compartirlos mediante _Módem USB_ (en Android suele estar en `Ajustes` > `Redes e Internet` > `Punto de acceso y anclaje de red` > `Compartir conexión por USB`).

En ocasiones los _drivers_ se actualizan solos al actualizar el sistema (e.g. `sudo apt update && sudo apt upgrade` para Ubuntu/Mint/Debian, `sudo dnf upgrade` para Fedora, `sudo pacman -Syu` para Arch/Manjaro).

En caso de que esto no solucione tu problema, te va a tocar buscar, descargar, e instalar los _drivers_ a mano. Para ello, primero tendrás que averiguar qué chipset Wi-Fi tiene tu ordenador. Te recomendamos ir a la página del fabricante, o seguir la [guía de nixCraft](https://www.cyberciti.biz/faq/linux-find-wireless-driver-chipset/). Una vez averigüado, te tocará buscar la guía de instalación del _driver_ para tu chipset y distribución específica. Para ello, busca en Google.
