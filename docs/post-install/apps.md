# Aplicaciones
Normalmente, tu gestor de paquetes (APT para Debian/Ubuntu/Mint, DNF para Fedora, Pacman para Arch) tendrá todos los paquetes que te puedas instalar. Tu _distro_ probablemente también traiga una aplicación GUI para buscar e instalar software. Alternativamente (sobretodo en los casos en los que un paquete no esté disponible), puedes usar [Flatpak](https://flatpak.org/) (puedes usar la GUI [Bazaar](https://flathub.org/es/apps/io.github.kolunmi.Bazaar), y también recomendamos tener [Flatseal](https://flathub.org/en/apps/com.github.tchx84.Flatseal) a mano) o [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) (en el caso de Arch) con un _helper_ como [Yay](https://github.com/Jguer/yay). En ocasiones también te proporcionan un AppImage, y recuerda que siempre es factible compilar desde _source_.

!!! info "¿Qué es un _AppImage_?"

    Una aplicación empaquetada en un AppImage es el equivalente de un `.exe` en windows, doble click y se abre. A veces, para poder abrirlo, hay que decirle al sistema operativo que es un archivo ejecutable por el sistema mediante `chmod +x .\aplicación.AppImage`.

    También existen aplicaciones para gestionar AppImages, como [Gear Lever](https://github.com/mijorus/gearlever) (o, para los _Apple fanboys_, [AppManager](https://github.com/kem-a/AppManager)).


Aquí te dejamos una lista de aplicaciones que pueden ser útiles a la hora de sacarle el máximo partido a tu nuevo Linux:

- [EnvyControl](https://github.com/bayasdev/envycontrol): Aplicación para configurar el uso de GPUs dedicadas, integradas, e híbridas, extremadamente útil para cuando tienes tanto gráfica integrada como gráfica dedicada
- [OpenRGB](https://github.com/CalcProgrammer1/OpenRGB): Controlador para luces RGB
- [OpenTabletDriver](https://opentabletdriver.net/): Drivers para controlar la tablet gráfica. Recomendado/Necesario incluso para distribuciones como KDE que vienen con configuradores nativos.
- [Dual Function Keys](https://gitlab.com/interception/linux/plugins/dual-function-keys): Plugin para [interception tools](https://gitlab.com/interception/linux) que permite configurar teclas del teclado con múltiples funciones (e.g. Caps Lock si lo pulsas funciona como Caps Lock, pero si lo mantienes funciona como Control).
- [Vesktop](https://github.com/Vencord/Vesktop): Discord para Linux, pero bien hecho
- [ZapZap](https://rtosta.com/zapzap/): Cliente de WhatsApp para Linux
- [Redshift](https://github.com/jonls/redshift): _Screen filter_ (protector de vista)
- [fwupd](https://github.com/fwupd/fwupd) (A.K.A. Linux Vendor Firmware Service): Utilidad para actualizar el _firmware_ de una [gran variedad de dispositivos](https://fwupd.org/lvfs/devices/), incluyendo portátiles
- [downgrade](https://github.com/archlinux-downgrade/downgrade) [Exclusivo para [pacman](https://wiki.archlinux.org/title/Pacman) (Arch Linux y derivados)]: _Rollback_ de versiones de paquetes
- [gestures](https://gitlab.com/nokun/gestures): Aplicación para ejecutar comandos a partir de gestos en el _trackpad_
- [nala](https://gitlab.com/volian/nala): [Exclusivo para APT (Debian/Ubuntu/Mint y derivados)] _Frontend_ alternativo para APT
- [informant](https://github.com/bradford-smith94/informant): Lector de [Arch Linux News](https://archlinux.org/news/) en terminal, extremadamente útil para distros basadas en Arch Linux, ya que te avisa de cuándo las actualizaciones te van a romper cosas
- [mpv](https://mpv.io/): Reproductor de vídeo con soporte para _todo_ (alternativa a [VLC](https://www.videolan.org/vlc/))
- [Vicinae](https://github.com/vicinaehq/vicinae): _Launcher_ de aplicaciones con extensiones y funcionalidades extra ([Raycast](https://www.raycast.com/) para Linux)
- [Kdenlive](https://kdenlive.org/es/): Editor de vídeo FOSS
- [Ardour](https://ardour.org/): DAW (Digital Audio Workstation) FOSS
- [Newsflash](https://apps.gnome.org/es/NewsFlash/): Lector y agregador de _feeds_ [RSS](https://es.wikipedia.org/wiki/RSS)
- [Localsend](https://localsend.org): Aplicación para compartir archivos entre dispositivos en la misma red, compatible con MacOS, Windows, Android, IOS, etc.
- [scrcpy](https://github.com/Genymobile/scrcpy): Control y _streaming_ de móviles Android directamente al ordenador (no requiere de una aplicación extra ya que se basa en el ADB de Android)
- [wayland-scroll-factor](https://github.com/daniel-g-carrasco/wayland-scroll-factor): Permite controlar la sensibilidad del _touchpad_ en Gnome con Wayland (porque no hay otra forma, ver [Gnome #18097](https://discourse.gnome.org/t/add-touchpad-scroll-sensitivity-adjustment-feature/18097/36))


## Emuladores de terminal
Una de las grandes ventajas de Linux es el uso de la terminal (y sus [multiples aplicaciones](#aplicaciones-de-terminal)). Es un entorno que en muchos casos es preferible a usar frente a aplicaciones GUI, y en otros casos es obligatorio.

En el caso de que seas un ávido usuario de ella, es recomendable cambiar el emulador de terminal (la aplicación que ejecuta la terminal) que venga por defecto por una más moderna, ya que añaden funcionalidades extra (como mostrar imágenes, las cuales son usadas en algunas aplicaciones), y permiten una mayor configuración.

Hay una cantidad ingente de ellos, pero te recomendamos estos tres:

- [kitty](https://sw.kovidgoyal.net/kitty/): El emulador con más funcionalidades y el mejor soportado
- [Ghostty](https://ghostty.org/): Emulador que combina una gran cantidad de funcionalidades con una "experiencia nativa" en entornos de escritorio y sin sacrificar el rendimiento
- [st](https://st.suckless.org/): Un emulador centrado en ser sencillo, rápido y ligero. Puedes añadir [_patches_](https://st.suckless.org/patches/) para funcionalidades extra


## Shells
El programa que ejecuta la terminal en sí se llama _shell_. La mayoría de distros vienen con [Bash](https://www.gnu.org/software/bash/), pero tienes otras alternativas:

- [Zsh](https://www.zsh.org/): La más popular, con una gran cantidad de plugins hechos por la comunidad (ver [Zinit](https://github.com/zdharma-continuum/zinit))
- [fish](https://fishshell.com/): _Shell_ "_batteries-included_", con muchas funcionalidades configuradas _out of the box_
- [Nushell](https://www.nushell.sh/): Una _shell_ moderna, hecha desde cero, y muy diferente al resto, con plugins, mensajes de error fantásticos y muchísimas funcionalidades para trabajar con datos

### Prompt
El _prompt_ es lo que aparece antes de ejecutar cada comando, y muestra información sobre el estado de la shell, e.g.:
```bash
gul@corneja:~$ 
 ^     ^    ^^
 |     |    |└- user mode
 |     |    └- current directory
 |     └- hostname
 └- username
```

Cada una de las _shells_ te permite configurarlo hasta cierto punto, pero si quieres tener más control, o mostrar información como el tiempo, la hora, el estado de Git, o la música que estás escuchando, échale un vistazo a [Oh My Posh](https://ohmyposh.dev/) y [Starship](https://starship.rs/).


## Aplicaciones de terminal
Aquí os dejamos algunas aplicaciones para sacar el máximo de vuestra terminal, distintas utilidades y versiones mejoradas de comandos de Unix:

### Comandos de shell
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
- [trash-cli](https://github.com/andreafrancia/trash-cli): Envía archivos a la papelera desde la terminal (alternativa segura a `rm`)
- [The Fuck](https://github.com/nvbn/thefuck): Corrector de comandos


### Herramientas
- [edit](https://github.com/microsoft/edit) y [micro](https://github.com/zyedidia/micro): Editores de texto simple en terminal (alternativas a `nano`)
- [caligula](https://github.com/ifd3f/caligula): Herramienta para _flashear_ discos (alternativa a `dd`)
- [croc](https://github.com/schollz/croc): Aplicación simple para enviar archivos entre ordenadores (soporta distintos Sistemas Operativos)
- [glow](https://github.com/charmbracelet/glow): Visor de Markdown en terminal
- [impala](https://github.com/pythops/impala): TUI para Wi-Fi
- [beets](https://beets.io/): Gestor de archivos de música
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
- [cliamp](https://github.com/bjarneo/cliamp): TUI para reproducir/streamear música
  - [rmpc](https://mierak.github.io/rmpc/): Reproductor de música en terminal, con soporte para imágenes
- [jqp](https://github.com/noahgorstein/jqp): Permite hacer _queries_ interactivas de [jq](https://github.com/jqlang/jq) en archivos JSON
- [witr](https://github.com/pranshuparmar/witr): Navaja suiza para _debuggear_ procesos y puertos


## Aplicaciones para hardware específico
Muchos dispositivos vienen con herramientas específicas para controlar aspectos del hardware, (batería o ventiladores en portátiles, botones en ratones, etc.), pero normalmente están disponibles exclusivamente para Windows. Aquí os dejamos algunas alternativas:

- [Lenovo Legion Linux](https://github.com/johnfanv2/LenovoLegionLinux): Herramientas para configurar portátiles de la gama _Legion_ de Lenovo (alternativa a [Lenovo Vantage](https://support.lenovo.com/eg/es/solutions/ht505081))
- [xpadneo](https://github.com/atar-axis/xpadneo): Drivers para los mandos _wireless_ de XBox
- [Piper](https://github.com/libratbag/piper): Aplicación para configurar ratones _gaming_ de diferentes marcas
- [Solaar](https://github.com/pwr-Solaar/Solaar): Herramienta para configurar dispositivos de Logitech (ratones, teclados, etc.)
  - [OpenLogi](https://github.com/AprilNEA/OpenLogi): Alternativa más _user-friendly_
- [Framework System TUI](https://github.com/grouzen/framework-tool-tui) /
  [Framework System](https://github.com/FrameworkComputer/framework-system):
  Herramienta de configuración para ordenadores [Framework](https://frame.work)
- [GalaxyBudsClient](https://github.com/timschneeb/GalaxyBudsClient): Aplicación para configurar auriculares de Samsung Galaxy


## Timeshift
Esta aplicación se ocupa de crear algo llamado _snapshots_ de tu sistema. Estos snapshots son copias del estado de tu sistema en un momento particular, que sirven como backups para poder restaurarlo en el caso de que se rompa. Se instala a través del gestor de paquetes, y es universal para todas las distros.

Los usuarios de Arch tienen a su disposición [este paquete de AUR](https://aur.archlinux.org/packages/timeshift-autosnap) que implementa un [Pacman Hook](https://wiki.archlinux.org/title/Pacman#Hooks), el que hace un snapshot de tu sistema antes de cada actualización que ejecutas, pero los usuarios de otras distros también pueden utilizar la herramienta GUI, los servicios de Systemd, y los cron jobs, para especificar momentos en los cuales Timeshift va a hacer un snapshot automatico (por ejemplo cada semana).

!!! warning
    Timeshift hace copias solo de los archivos de sistema, **NO DE LA CARPETA `/home`**, así que si no quieres perder tus archivos personales, tendrás que usar otro método. Este sirve solo para restaurar un sistema roto.

### Diferencias entre sistemas de archivos
En sistemas de archivos que no son [BTRFS](https://wiki.archlinux.org/title/Btrfs), el primer snapshot hace una copia física de los archivos con [RSYNC](https://wiki.archlinux.org/title/Rsync). Las siguientes solo hacen copias de los archivos que han cambiado, y para el resto se usan _enlaces duros_, lo que es más eficiente que copiarlos cada vez manualmente, pero igualmente es un backup que ocupa un espacio igual de grande que tu sistema, así que tendrás que tener espacio libre para hacer el snapshot.

Mientras que en sistemas BTRFS, todos los snapshots solo hacen copias de las diferencias de archivos entre un snapshot y el otro. Esto significa que no ocupan casi nada de espacio, pero solo funcionan en sistemas que tienen un diseño de subvolumen tipo Ubuntu (con subvolúmenes `@` y `@home`). Esto incluye distros basados en Debian y Arch, pero excluye Fedora, al no ser que lo instalas cambiando la partición `root` a `@` y la `home` a `@home`.
