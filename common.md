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
Para instalar Linux es necesario _bootear_ (arrancar) desde el instalador de Linux que tenemos en el [LiveUSB](README.md#cómo-crear-un-live-usb). Para ello, apaga el ordenador y conecta el LiveUSB. Dado que el ordenador _bootea_ automáticamente en el Sistema Operativo que esté configurado, hay que cambiar esto antes de que arranque.

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



## Post-install
Aquí dejamos algunos pasos opcionales que puedes realizar para mejorar tu experiencia con Linux.

### Configuración red UC3M

#### Eduroam
La configuración de la red es la siguiente:
- **Security**: _WPA/WPA2 Enterprise_
- **Authentication**: _Tunnelled TLS_
- Selecciona _No CA certificate is required_
- **Inner authentication**: _MSCHAPv2 (no EAP)_
- **Username**: El NIA.
- **Password**: La contraseña de Aula Global.

#### VPN
Os recomendamos usar [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect).

La dirección del portal es `myvpn.uc3m.es`.

Más información en [la página oficial del SDIC](https://www.uc3m.es/sdic/servicios/vpn).


### Drivers de NVIDIA
Si tienes una gráfica de NVIDIA, es posible que los drivers no vengan instalados, ya que son third-party.
> [!NOTE]
> En algunas _distros_, hay una opción de "instalar drivers de terceros", la cual los suele incluír.

La forma de instalarlos depende de la _distro_, a continuación te dejamos las más comunes.

#### Ubuntu
Si has habilitado la opción de drivers de terceros, deberías tenerlos instalados.  

Puedes instalarlos, según la [documentación oficial de Ubuntu](https://ubuntu.com/server/docs/nvidia-drivers-installation) con:
```bash
sudo ubuntu-drivers install
```


#### Fedora
Según la [documentación de RPM fusion](https://rpmfusion.org/Howto/NVIDIA):
```bash
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda
```

Si tienes el secure boot, échale un vistazo al repositorio [roworu/nvidia-fedora-secureboot](https://github.com/roworu/nvidia-fedora-secureboot)


#### Arch
Según [Arch Wiki](https://wiki.archlinux.org/title/NVIDIA):
```bash
sudo pacman -Syu nvidia-open
```

#### EndeavourOS
Según la [documentación de Endeavouros discovery](https://discovery.endeavouros.com/nvidia/new-nvidia-driver-installer-nvidia-inst/2022/03/), puedes usar `nvidia-inst`.

Este instala la versión _closed source_, proporcionada por NVIDIA.
```bash
nvidia-inst
```
Para gráficas mas antiguas, es recomendable usar los drivers _open-source_ ([Nouveau](https://nouveau.freedesktop.org/)).
```bash
nvidia-inst --nouveau
```

#### Más información
- [NVIDIA - Arch Wiki](https://wiki.archlinux.org/title/NVIDIA)
- [NVIDIA - Gentoo Wiki](https://wiki.gentoo.org/wiki/NVIDIA#Feature_support)



### Aplicaciones
Aquí te dejamos una lista de aplicaciones que pueden ser útiles a la hora de sacarle el máximo partido a tu nuevo Linux:
- [EnvyControl](https://github.com/bayasdev/envycontrol): Aplicación para configurar el uso de GPUs dedicadas, integradas, e híbridas, extremadamente útil para cuando tienes tanto gráfica integrada como gráfica dedicada
- [OpenRGB](https://github.com/CalcProgrammer1/OpenRGB): Controlador para luces RGB
- [Vesktop](https://github.com/Vencord/Vesktop): Discord para Linux, pero bien hecho
- [Redshift](https://github.com/jonls/redshift): _Screen filter_ al estilo del protector de vista de Windows
- [Piper](https://github.com/libratbag/piper): Aplicación para configurar ratones _gaming_ (y otros como el Logitech MX Master 3)
- [xpadneo](https://github.com/atar-axis/xpadneo): Drivers para los mandos _wireless_ de XBox
- [fwupd](https://github.com/fwupd/fwupd) (A.K.A. Linux Vendor Firmware Service): Utilidad para actualizar el _firmware_ de una [gran variedad de dispositivos](https://fwupd.org/lvfs/devices/), incluyendo portátiles
- [downgrade](https://github.com/archlinux-downgrade/downgrade) [Exclusivo de Arch]: _Rollback_ de versiones de paquetes

#### Aplicaciones de terminal
Aquí os dejamos algunas aplicaciones para sacar el máximo de vuestra terminal, distintas utilidades y versiones mejoradas de comandos de Linux:
- [eza](https://github.com/eza-community/eza): Versión mejorada de `ls`
- [bat](https://github.com/sharkdp/bat): Versión mejorada de `cat`
- [btop](https://github.com/aristocratos/btop): Versión mejorada de `top`
- [fd](https://github.com/sharkdp/fd): Versión mejorada de `find`
- [rigpgrep](https://github.com/BurntSushi/ripgrep): Versión mejorada de `grep`
- [zoxide](https://github.com/ajeetdsouza/zoxide): Versión mejorada de `cd`
- [dust](https://github.com/bootandy/dust): Versión mejorada de `du`
- [Difftastic](https://github.com/Wilfred/difftastic): `diff`, pero para humanos
- [fzf](https://github.com/junegunn/fzf): Buscador interactivo _fuzzy_, extremadamente útil usado en combinación con otros comandos
- [micro](https://github.com/zyedidia/micro): Editor de texto simple en terminal (alternativa a `nano`)
- [trash-cli](https://github.com/andreafrancia/trash-cli): Envía archivos a la papelera desde la terminal (alternativa segura a `rm`)
- [glow](https://github.com/charmbracelet/glow): Visor de Markdown en terminal
- [The Fuck](https://github.com/nvbn/thefuck): Corrector de comandos
- [Lazygit](https://github.com/jesseduffield/lazygit): TUI para Git (probablemente la mejor interfaz gráfica para Git)
- [Lazydocker](https://github.com/jesseduffield/lazydocker): TUI para Docker
- [yazi](https://github.com/sxyazi/yazi): Explorador de archivos en terminal
- [fastfetch](https://github.com/fastfetch-cli/fastfetch): Muestra información del sistema
- [tealdeer](https://github.com/tealdeer-rs/tealdeer): Mini-manuales (TL;DR) para comandos
- [coltrane](https://github.com/pedrozath/coltrane): Herramienta para teoría musical
- [pokeget](https://github.com/talwat/pokeget-rs): Visor de _sprites_ de Pokémon en terminal

#### Aplicaciones para hardware específico
Muchos portátiles vienen con herramientas específicas para controlar aspectos del hardware, como la la batería, ventiladores, etc., pero normalmente están disponibles exclusivamente para Windows. Aquí os dejamos algunas alternativas:
- [Lenovo Legion Linux](https://github.com/johnfanv2/LenovoLegionLinux): Herramientas para configurar portátiles de la gama _Legion_ de Lenovo (alternativa a [Lenovo Vantage](https://support.lenovo.com/eg/es/solutions/ht505081))



### Instalar rEFInd
[rEFInd](https://www.rodsbooks.com/refind/) es un boot manager, al igual que
GRUB, pero más moderno y customizable. Es recomendable instalarlo en ordenadores
más modernos, y **no es recomendable instalarlo en ordenadores antiguos**.

### Linux
1. Instala el paquete `refind` (suele estar en el gestor de paquetes)
2. Reinicia. Debería salirte el boot manager de rEFInd

> [!NOTE]
> Si después de reiniciar no aparece rEFInd, entra en la BIOS y selecciónalo
> como opción de boot principal.



## Solucionar drivers Wi-Fi
Es relativamente común que los _drivers_ de la tarjeta de red Wi-Fi de los portátiles no vengan instalados por defecto en Linux.

Una forma de obtener conexión a Internet es usando un cable Ethernet, ya sea mediante el puerto Ethernet del ordenador (si lo tiene), o mediante el uso de un adaptador. Si no tienes nada de eso a mano, siempre puedes conectar el ordenador a tu móvil por USB, poner los datos, y compartirlos mediante _Módem USB_ (en Android suele estar en `Ajustes` > `Redes e Internet` > `Punto de acceso y anclaje de red` > `Compartir conexión por USB`).

En ocasiones los _drivers_ se actualizan solos al actualizar el sistema (e.g. `sudo apt update && sudo apt upgrade` para Ubuntu/Mint/Debian, `sudo dnf upgrade` para Fedora, `sudo pacman -Syu` para Arch/Manjaro).

En caso de que esto no solucione tu problema, te va a tocar buscar, descargar, e instalar los _drivers_ a mano. Para ello, primero tendrás que averiguar qué chipset Wi-Fi tiene tu ordenador. Te recomendamos ir a la página del fabricante, o seguir la [guía de nixCraft](https://www.cyberciti.biz/faq/linux-find-wireless-driver-chipset/). Una vez averigüado, te tocará buscar la guía de instalación del _driver_ para tu chipset y distribución específica. Para ello, busca en Google.
