# Post-install
Aquí dejamos algunos pasos opcionales que puedes realizar para mejorar tu experiencia con Linux.


## Configuración red UC3M

### Eduroam
La configuración de la red es la siguiente:
- **Security**: _WPA/WPA2 Enterprise_
- **Authentication**: _Tunnelled TLS_
- Selecciona _No CA certificate is required_
- **Inner authentication**: _MSCHAPv2 (no EAP)_
- **Username**: El correo de la universidad (`100XXXXXX@alumnos.uc3m.es`)
- **Password**: La contraseña de dicho correo

> [!NOTE]
> Usamos el correo como _username_ en vez del NIA porque esto permite autenticarse también en el resto de redes Eduroam (e.g. otras universidades).

Alternativamente, puedes usar el [_script_ de Python proporcionado por GÉANT](https://cat.eduroam.org/) para configurar la red automágicamente (con certificado).

> [!TIP]
> El _script_ anterior configura la red de la siguiente forma:
> - **Security**: _WPA/WPA2 Enterprise_
> - **Authentication**: _Tunnelled TLS_
> - **Anonymous identity**: `anonymous092023@uc3m.es`
> - **CA certificate**: `~/.config/cat_installer/ca.pem`
> - **Inner authentication**: _PAP_
> - **Username**: El ID proporcionado
> - **Password**: La contraseña proporcionada


Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/wifi-eduroam).


### VPN
Os recomendamos usar [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect).

Una vez [instalado](https://github.com/yuezk/GlobalProtect-openconnect#installation), se ejecuta con:
```bash
sudo -E gpclient connect --browser default myvpn.uc3m.es
```

Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/vpn).

> [!NOTE]
> Si quieres que la VPN funcione dentro de WSL2, lo recomendable es poner la VPN en Windows y usar [wsl-vpnkit](https://github.com/sakai135/wsl-vpnkit).



## Drivers de NVIDIA
Desde hace unos años, NVIDIA publica sus [_drivers_ para Linux](https://www.nvidia.com/es-es/drivers/unix/), pero al ser _closed source_, no se pueden incluír en el kernel de Linux, por lo que tienen que ser instalados por separado.

> [!TIP]
> En algunas _distros_ es posible que haya una opción de "instalar drivers de terceros" en el instalador, la cual suele incluir los drivers oficiales.

> [!NOTE]
> Es posible que los _drivers_ oficiales no estén disponibles para gráficas más antiguas. Existe una alternativa open-source, [Nouveau](https://nouveau.freedesktop.org/), la cual _suele_ ir mejor en este tipo de gráficas. Consulta su documentación para ver cómo instalarlos.


### Instalación
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

Si tienes _secure boot_ activado, échale un vistazo al repositorio [roworu/nvidia-fedora-secureboot](https://github.com/roworu/nvidia-fedora-secureboot).

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
Para usar los controladores _nouveau_:
```bash
nvidia-inst --nouveau
```

### Más información
- [NVIDIA - Arch Wiki](https://wiki.archlinux.org/title/NVIDIA)
- [NVIDIA - Gentoo Wiki](https://wiki.gentoo.org/wiki/NVIDIA#Feature_support)



## Aplicaciones
Normalmente, tu gestor de paquetes (APT para Debian/Ubuntu/Mint, DNF para Fedora, Pacman para Arch) tendrá todos los paquetes que te puedas instalar. Alternativamente (sobretodo en los casos en los que un paquete no esté disponible), puedes usar [Flatpak](https://flatpak.org/) (con [Flatseal](https://flathub.org/en/apps/com.github.tchx84.Flatseal)) o [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) (en el caso de Arch) con un _helper_ como [Yay](https://github.com/Jguer/yay). En ocasiones también te proporcionan un AppImage, y recuerda que siempre es factible compilar desde source.

> [!TIP]
> ¿Qué es un _AppImage_?
> 
> Una aplicación empaquetada en un AppImage es el equivalente de un `.exe` en windows, doble click y se abre. A veces, para poder abrirlo, hay que decirle al sistema operativo que es un archivo ejecutable por el sistema mediante `chmod +x .\aplicación.AppImage`.


Aquí te dejamos una lista de aplicaciones que pueden ser útiles a la hora de sacarle el máximo partido a tu nuevo Linux:
- [EnvyControl](https://github.com/bayasdev/envycontrol): Aplicación para configurar el uso de GPUs dedicadas, integradas, e híbridas, extremadamente útil para cuando tienes tanto gráfica integrada como gráfica dedicada
- [OpenRGB](https://github.com/CalcProgrammer1/OpenRGB): Controlador para luces RGB
- [Vesktop](https://github.com/Vencord/Vesktop): Discord para Linux, pero bien hecho
- [WasIstLos](https://github.com/xeco23/WasIstLos): Cliente de WhatsApp para Linux
- [Redshift](https://github.com/jonls/redshift): _Screen filter_ (protector de vista)
- [fwupd](https://github.com/fwupd/fwupd) (A.K.A. Linux Vendor Firmware Service): Utilidad para actualizar el _firmware_ de una [gran variedad de dispositivos](https://fwupd.org/lvfs/devices/), incluyendo portátiles
- [downgrade](https://github.com/archlinux-downgrade/downgrade) [Exclusivo para [pacman](https://wiki.archlinux.org/title/Pacman) (Arch Linux y derivados)]: _Rollback_ de versiones de paquetes
- [gestures](https://gitlab.com/nokun/gestures): Aplicación para ejecutar comandos a partir de gestos en el _trackpad_
- [nala](https://gitlab.com/volian/nala): [Exclusivo para APT (Debian/Ubuntu/Mint y derivados)] _Frontend_ alternativo para APT
- [informant](https://github.com/bradford-smith94/informant): Lector de [Arch Linux News](https://archlinux.org/news/) en terminal, extremadamente útil para distros basadas en Arch Linux, ya que te avisa de cuándo las actualizaciones te van a romper cosas
- [Vicinae](https://github.com/vicinaehq/vicinae): _Launcher_ de aplicaciones con extensiones y funcionalidades extra ([Raycast](https://www.raycast.com/) para Linux)
- [Kdenlive](https://kdenlive.org/es/): Editor de vídeo


### Emuladores de terminal
Una de las grandes ventajas de Linux es el uso de la terminal (y sus [multiples aplicaciones](#aplicaciones-de-terminal)). Es un entorno que en muchos casos es preferible a usar frente a aplicaciones GUI, y en otros casos es obligatorio.

En el caso de que seas un ávido usuario de ella, es recomendable cambiar el emulador de terminal (la aplicación que ejecuta la terminal) que venga por defecto por una más moderna, ya que añaden funcionalidades extra (como mostrar imágenes, las cuales son usadas en algunas aplicaciones), y permiten una mayor configuración.

Hay una cantidad ingente de ellos, pero te recomendamos estos tres:
- [kitty](https://sw.kovidgoyal.net/kitty/): El emulador con más funcionalidades y el mejor soportado
- [Ghostty](https://ghostty.org/): Emulador que combina una gran cantidad de funcionalidades con una "experiencia nativa" en entornos de escritorio y sin sacrificar el rendimiento
- [st](https://st.suckless.org/): Un emulador centrado en ser sencillo, rápido y ligero. Puedes añadir [_patches_](https://st.suckless.org/patches/) para funcionalidades extra


### Shells
El programa que ejecuta la terminal en sí se llama _shell_. La mayoría de distros vienen con [Bash](https://www.gnu.org/software/bash/), pero tienes otras alternativas:
- [Zsh](https://www.zsh.org/): La más popular, con una gran cantidad de plugins hechos por la comunidad (ver [Zinit](https://github.com/zdharma-continuum/zinit))
- [fish](https://fishshell.com/): _Shell_ "_batteries-included_", con muchas funcionalidades configuradas _out of the box_
- [Nushell](https://www.nushell.sh/): Una _shell_ moderna, hecha desde cero, y muy diferente al resto, con plugins, mensajes de error fantásticos y muchísimas funcionalidades para trabajar con datos

#### Prompt
El _prompt_ es lo que aparece antes de ejecutar cada comando, y muestra información sobre el estado de la shell, e.g.:
```bash
gul@corneja:~$ 
```
<!--
 ^     ^    ^^
 |     |    |└- user mode
 |     |    └- current directory
 |     └- hostname
 └- username
```
-->

Cada una de las _shells_ te permite configurarlo hasta cierto punto, pero si quieres tener más control, o mostrar información como el tiempo, la hora, el estado de Git, o la música que estás escuchando, échale un vistazo a [Oh My Posh](https://ohmyposh.dev/) y [Starship](https://starship.rs/).


### Aplicaciones de terminal
Aquí os dejamos algunas aplicaciones para sacar el máximo de vuestra terminal, distintas utilidades y versiones mejoradas de comandos de Unix:
- [eza](https://github.com/eza-community/eza): Versión mejorada de `ls`
- [bat](https://github.com/sharkdp/bat): Versión mejorada de `cat` (ver también [bat-extras](https://github.com/eth-p/bat-extras))
- [advcpmv](https://github.com/jarun/advcpmv): Parche para `cp` y `mv` que añade una barra de progreso
- [btop](https://github.com/aristocratos/btop): Versión mejorada de `top`, con soporte para GPUs
- [fd](https://github.com/sharkdp/fd): Versión mejorada de `find`
- [rigpgrep](https://github.com/BurntSushi/ripgrep): Versión mejorada de `grep`
- [zoxide](https://github.com/ajeetdsouza/zoxide): Versión mejorada de `cd`
- [dust](https://github.com/bootandy/dust): Versión mejorada de `du`
- [dysk](https://github.com/Canop/dysk): Versión mejorada de `df`
- [Difftastic](https://github.com/Wilfred/difftastic): `diff`, pero para humanos
- [xh](https://github.com/ducaale/xh): Versión mejorada de `curl`
- [fzf](https://github.com/junegunn/fzf): Buscador interactivo _fuzzy_, extremadamente útil usado en combinación con otros comandos
- [edit](https://github.com/microsoft/edit) y [micro](https://github.com/zyedidia/micro): Editores de texto simple en terminal (alternativas a `nano`)
- [trash-cli](https://github.com/andreafrancia/trash-cli): Envía archivos a la papelera desde la terminal (alternativa segura a `rm`)
- [caligula](https://github.com/ifd3f/caligula): Herramienta para _flashear_ discos (alternativa a `dd`)
- [glow](https://github.com/charmbracelet/glow): Visor de Markdown en terminal
- [The Fuck](https://github.com/nvbn/thefuck): Corrector de comandos
- [impala](https://github.com/pythops/impala): TUI para Wi-Fi
- [bluetui](https://github.com/pythops/bluetui): TUI para Bluetooth
- [wiremix](https://github.com/tsowell/wiremix): TUI para control de audio
- [Lazygit](https://github.com/jesseduffield/lazygit): TUI para Git (probablemente la mejor interfaz gráfica para Git)
- [Lazydocker](https://github.com/jesseduffield/lazydocker): TUI para Docker
- [yazi](https://github.com/sxyazi/yazi): Explorador de archivos en terminal
- [fastfetch](https://github.com/fastfetch-cli/fastfetch): Muestra información del sistema
- [tealdeer](https://github.com/tealdeer-rs/tealdeer): Mini-manuales (TL;DR) para comandos
- [coltrane](https://github.com/pedrozath/coltrane): Herramienta para teoría musical
- [pokeget](https://github.com/talwat/pokeget-rs): Visor de _sprites_ de Pokémon en terminal
- [carbonyl](https://github.com/fathyb/carbonyl): Navegador en terminal
- [rmpc](https://mierak.github.io/rmpc/): Reproductor de música en terminal, con soporte para imágenes
- [beets](https://beets.io/): Gestor de archivos de música
- [jqp](https://github.com/noahgorstein/jqp): Permite hacer _queries_ interactivas de [jq](https://github.com/jqlang/jq) en archivos JSON


### Aplicaciones para hardware específico
Muchos dispositivos vienen con herramientas específicas para controlar aspectos del hardware, (batería o ventiladores en portátiles, botones en ratones, etc.), pero normalmente están disponibles exclusivamente para Windows. Aquí os dejamos algunas alternativas:
- [Lenovo Legion Linux](https://github.com/johnfanv2/LenovoLegionLinux): Herramientas para configurar portátiles de la gama _Legion_ de Lenovo (alternativa a [Lenovo Vantage](https://support.lenovo.com/eg/es/solutions/ht505081))
- [xpadneo](https://github.com/atar-axis/xpadneo): Drivers para los mandos _wireless_ de XBox
- [Piper](https://github.com/libratbag/piper): Aplicación para configurar ratones _gaming_ de diferentes marcas
- [Solaar](https://github.com/pwr-Solaar/Solaar): Herramienta para configurar dispositivos de Logitech (ratones, teclados, etc.)

### Timeshift
Esta aplicación se ocupa de crear algo llamado _snapshots_ de tu sistema. Estos snapshots son copias del estado de tu sistema en un momento particular, que sirven como backups para poder restaurarlo en el caso de que se rompa. Se instala a través del gestor de paquetes, y es universal para todas las distros.

Los usuarios de Arch tienen a su disposición [este paquete de AUR](https://aur.archlinux.org/packages/timeshift-autosnap) que implementa un [Pacman Hook](https://wiki.archlinux.org/title/Pacman#Hooks), el que hace un snapshot de tu sistema antes de cada actualización que ejecutas, pero los usuarios de otras distros también pueden utilizar la herramienta GUI, los servicios de Systemd, y los cron jobs, para especificar momentos en los cuales Timeshift va a hacer un snapshot automatico (por ejemplo cada semana).

> [!IMPORTANT]
> Timeshift hace copias solo de los archivos de sistema, **NO DE LA CARPETA `/home`**, así que si no quieres perder tus archivos personales, tendrás que usar otro método. Este sirve solo para restaurar un sistema roto.

#### Diferencias entre sistemas de archivos
En sistemas de archivos que no son [BTRFS](https://wiki.archlinux.org/title/Btrfs), el primer snapshot hace una copia física de los archivos con [RSYNC](https://wiki.archlinux.org/title/Rsync). Las siguientes solo hacen copias de los archivos que han cambiado, y para el resto se usan _enlaces duros_, lo que es más eficiente que copiarlos cada vez manualmente, pero igualmente es un backup que ocupa un espacio igual de grande que tu sistema, así que tendrás que tener espacio libre para hacer el snapshot.

Mientras que en sistemas BTRFS, todos los snapshots solo hacen copias de las diferencias de archivos entre un snapshot y el otro. Esto significa que no ocupan casi nada de espacio, pero solo funcionan en sistemas que tienen un diseño de subvolumen tipo Ubuntu (con subvolúmenes `@` y `@home`). Esto incluye distros basados en Debian y Arch, pero excluye Fedora, al no ser que lo instalas cambiando la partición `root` a `@` y la `home` a `@home`.

### _Gaming_
Echa un vistazo a nuestra [guía de juegos en Linux](play-on-linux.md).


### Ejecutando programas de Windows
Aunque la compatibilidad de Windows varía de programa en programa, existen herramientas que te permiten ejecutar aplicaciones nativas de Windows en Linux, sin necesidad de crear una máquina virtual (lo cual [también se puede hacer](#usando-una-maquina-virtual)).
- [Wine](https://www.winehq.org/) (y [winetricks](https://github.com/Winetricks/winetricks)): La herramienta original y más usada, crea una capa de compatibilidad entre Windows y Linux
- [Winapps](https://github.com/Fmstrat/winapps): Permite una integración transparente con una máquina virtual de Windows, permitiendo ejecutar aplicaciones de Windows como si fueran ventanas en Linux

#### Usando una Máquina Virtual
Al igual que puedes [ejecutar Linux en una VM desde Windows](vm-install.md), también puedes ejecutar Windows en una VM desde Linux, asegurándote una compatibilidad prácticamente perfecta, aunque sacrificando algo de _performance_.

Aparte de la virtualización "tradicional" que ofrecen plataformas como [VirtualBox](https://www.virtualbox.org/) o [VMware](https://www.vmware.com/), en Linux existe [KVM](https://linux-kvm.org/), una virtualización basada en _kernel_, la cual es altamente eficiente. Para utilizar este tipo de VMs, te recomendamos usar [virt-manager](https://github.com/virt-manager/virt-manager).

> [!TIP]
> Te dejamos aquí también un par de guías para configurar KVM y Windows:
> - [How Do I Properly Install KVM on Linux](https://sysguides.com/install-kvm-on-linux)
> - [How to Properly Install a Windows 11 Virtual Machine on KVM](https://sysguides.com/install-a-windows-11-virtual-machine-on-kvm)



## Instalar rEFInd
[rEFInd](https://www.rodsbooks.com/refind/) es un _boot manager_, al igual que
GRUB, pero más moderno y customizable. Es recomendable instalarlo en ordenadores
más modernos, y **no es recomendable instalarlo en ordenadores antiguos**.

### Linux
1. Instala el paquete `refind` (suele estar en el gestor de paquetes)
2. Reinicia. Debería salirte el _boot manager_ de rEFInd

> [!NOTE]
> Si después de reiniciar no aparece rEFInd, entra en la BIOS y selecciónalo
> como opción de _boot_ principal.


## Temas de GRUB
Si usas el _bootloader_ [GRUB](https://www.gnu.org/software/grub/) (lo más probable es que sí), puedes usar un tema personalizado.

Además de editar los archivos de configuración directamente, puedes usar [Grub Customizer](https://launchpad.net/grub-customizer), una aplicación con interfaz gráfica y fácil de usar.  
Para instalarla en las distintas distribuciones:
- Arch (AUR): [`grub-customizer`](https://aur.archlinux.org/packages/grub-customizer)
- Debian/Ubuntu/Mint (PPA): [`grub-customizer`](https://launchpad.net/~danielrichter2007/+archive/ubuntu/grub-customizer)
- Fedora: [`grub-customizer`](https://packages.fedoraproject.org/pkgs/grub-customizer/grub-customizer/)

Otros links de interés:
- [Jacksaur/Gorgeous-GRUB](https://github.com/Jacksaur/Gorgeous-GRUB): Repositorio con una selección de temas _chulos_ de GRUB
- [Gnome Look](https://www.gnome-look.org/browse?cat=109&ord=rating): Plataforma para compartir y descargar temas de GRUB
- [Tutorial de creación de temas para GRUB2](http://web.archive.org/web/20241209100014/http://wiki.rosalab.ru/en/index.php/Grub2_theme_tutorial)
- [ArchWiki - GRUB](https://wiki.archlinux.org/title/GRUB)
