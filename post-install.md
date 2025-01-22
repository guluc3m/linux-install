# Post-install
Aquí dejamos algunos pasos opcionales que puedes realizar para mejorar tu experiencia con Linux.


## Configuración red UC3M

### Eduroam
La configuración de la red es la siguiente:
- **Security**: _WPA/WPA2 Enterprise_
- **Authentication**: _Tunnelled TLS_
- Selecciona _No CA certificate is required_
- **Inner authentication**: _MSCHAPv2 (no EAP)_
- **Username**: El NIA.
- **Password**: La contraseña de Aula Global.

### VPN
Os recomendamos usar [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect).  
Una vez [instalado](https://github.com/yuezk/GlobalProtect-openconnect#installation):
```bash
sudo -E gpclient connect --browser default myvpn.uc3m.es
```

Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/vpn).



## Drivers de NVIDIA
Desde hace unos años, NVIDIA publica sus [_drivers_ para Linux](https://www.nvidia.com/es-es/drivers/unix/), pero al ser _closed source_, no se pueden incluír en el kernel de Linux, por lo que tienen que ser instalados por separado.

> [!TIP]
> En algunas _distros_ es posible que haya una opción de "instalar drivers de terceros" en el instalador, la cual suele incluir los drivers oficiales.

> [!NOTE]
> Los _drivers_ oficiales son posible que no estén disponibles para gráficas más antiguas. Existe una alternativa open-source, [Nouveau](https://nouveau.freedesktop.org/), la cual _suele_ ir mejor en este tipo de gráficas. Consulta su documentación para ver cómo instalarlos.


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

Si tienes el secure boot, échale un vistazo al repositorio [roworu/nvidia-fedora-secureboot](https://github.com/roworu/nvidia-fedora-secureboot).

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
Aquí te dejamos una lista de aplicaciones que pueden ser útiles a la hora de sacarle el máximo partido a tu nuevo Linux:
- [EnvyControl](https://github.com/bayasdev/envycontrol): Aplicación para configurar el uso de GPUs dedicadas, integradas, e híbridas, extremadamente útil para cuando tienes tanto gráfica integrada como gráfica dedicada
- [OpenRGB](https://github.com/CalcProgrammer1/OpenRGB): Controlador para luces RGB
- [Vesktop](https://github.com/Vencord/Vesktop): Discord para Linux, pero bien hecho
- [Redshift](https://github.com/jonls/redshift): _Screen filter_ (protector de vista)
- [fwupd](https://github.com/fwupd/fwupd) (A.K.A. Linux Vendor Firmware Service): Utilidad para actualizar el _firmware_ de una [gran variedad de dispositivos](https://fwupd.org/lvfs/devices/), incluyendo portátiles
- [downgrade](https://github.com/archlinux-downgrade/downgrade) [Exclusivo de Arch]: _Rollback_ de versiones de paquetes


### Aplicaciones de terminal
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


### Aplicaciones para hardware específico
Muchos dispositivos vienen con herramientas específicas para controlar aspectos del hardware, (batería o ventiladores en portátiles, botones en ratones, etc.), pero normalmente están disponibles exclusivamente para Windows. Aquí os dejamos algunas alternativas:
- [Lenovo Legion Linux](https://github.com/johnfanv2/LenovoLegionLinux): Herramientas para configurar portátiles de la gama _Legion_ de Lenovo (alternativa a [Lenovo Vantage](https://support.lenovo.com/eg/es/solutions/ht505081))
- [xpadneo](https://github.com/atar-axis/xpadneo): Drivers para los mandos _wireless_ de XBox
- [Piper](https://github.com/libratbag/piper): Aplicación para configurar ratones _gaming_ de diferentes marcas
- [Solaar](https://github.com/pwr-Solaar/Solaar): Herramienta para configurar dispositivos de Logitech (ratones, teclados, etc.)


### Ejecutando programas de Windows (`.exe`)
Aunque la compatibilidad de Windows varía de programa en programa, existen herramientas que te permiten ejecutar aplicaciones nativas de Windows en Linux, sin necesidad de crear una máquina virtual (lo cual [también se puede hacer](#usando-una-maquina-virtual)).
- [Wine](https://www.winehq.org/) (y [winetricks](https://github.com/Winetricks/winetricks)): La herramienta original y más usada, crea una capa de compatibilidad entre Windows y Linux
- [Winapps](https://github.com/Fmstrat/winapps): Permite una integración transparente con una máquina virtual de Windows, permitiendo ejecutar aplicaciones de Windows como si fueran ventanas en Linux
<!-- TODO: link linux-gaming -->

#### Usando una Máquina Virtual
Al igual que puedes [ejecutar Linux en una VM desde Windows](vm-install.md), también puedes ejecutar Windows en una VM desde Linux, asegurándote una compatibilidad prácticamente perfecta, aunque sacrificando algo de _performance_.

Aparte de la virtualización "tradicional" que ofrecen plataformas como [VirtualBox](https://www.virtualbox.org/) o [VMware](https://www.vmware.com/), en Linux existe [KVM](https://linux-kvm.org/), una virtualización basada en _kernel_, la cual es altamente eficiente. Para utilizar este tipo de VMs, te recomendamos usar [virt-manager](https://github.com/virt-manager/virt-manager).



## Instalar rEFInd
[rEFInd](https://www.rodsbooks.com/refind/) es un _boot manager_, al igual que
GRUB, pero más moderno y customizable. Es recomendable instalarlo en ordenadores
más modernos, y **no es recomendable instalarlo en ordenadores antiguos**.

### Linux
1. Instala el paquete `refind` (suele estar en el gestor de paquetes)
2. Reinicia. Debería salirte el boot manager de rEFInd

> [!NOTE]
> Si después de reiniciar no aparece rEFInd, entra en la BIOS y selecciónalo
> como opción de boot principal.
