# Configurando Linux

## Configuración red UC3M

### Eduroam
La configuración de la red es la siguiente:

- **Security**: _WPA/WPA2 Enterprise_
- **Authentication**: _Tunnelled TLS_
- Selecciona _No CA certificate is required_
- **Inner authentication**: _MSCHAPv2 (no EAP)_
- **Username**: El correo de la universidad (`100XXXXXX@alumnos.uc3m.es`)
- **Password**: La contraseña de dicho correo

!!! tip
    Usamos el correo como _username_ en vez del NIA porque esto permite autenticarse también en el resto de redes Eduroam (e.g. otras universidades).

Alternativamente, puedes usar el [_script_ de Python proporcionado por GÉANT](https://cat.eduroam.org/) para configurar la red automágicamente (con certificado).

??? info "Resultado del script"
    El _script_ anterior configura la red de la siguiente forma:

    - **Security**: _WPA/WPA2 Enterprise_
    - **Authentication**: _Tunnelled TLS_
    - **Anonymous identity**: `anonymous092023@uc3m.es`
    - **CA certificate**: `~/.config/cat_installer/ca.pem`
    - **Inner authentication**: _PAP_
    - **Username**: El ID proporcionado
    - **Password**: La contraseña proporcionada

Si te vas a conectar a través de un terminal o tty usando [`iwd`](https://wiki.archlinux.org/title/Iwd), crea el archivo `/var/lib/iwd/eduroam.8021x` (con [`nano`](https://www.nano-editor.org/) o tu editor de preferencia), y escribe lo siguiente:
```
[Security]
EAP-Method=PEAP
EAP-Identity=100XXXXXX@alumnos.uc3m.es  # tu correo
EAP-PEAP-Phase2-Method=MSCHAPV2
EAP-PEAP-Phase2-Identity=100XXXXXX@alumnos.uc3m.es  # tu correo
EAP-PEAP-Phase2-Password=contraseña123  # tu contraseña

[Settings]
AutoConnect=true
```

Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/wifi-eduroam).


### VPN
Os recomendamos usar [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect).

Una vez [instalado](https://github.com/yuezk/GlobalProtect-openconnect#installation), se ejecuta con:
```bash
sudo -E gpclient connect --browser default myvpn.uc3m.es
```

Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/vpn).

??? tip "VPN en WSL2"
    Si quieres que la VPN funcione dentro de WSL2, lo recomendable es poner la VPN en Windows y usar [wsl-vpnkit](https://github.com/sakai135/wsl-vpnkit).



## Drivers de NVIDIA
Desde hace unos años, NVIDIA publica sus [_drivers_ para Linux](https://www.nvidia.com/es-es/drivers/unix/), pero al ser _closed source_, no se pueden incluír en el kernel de Linux, por lo que tienen que ser instalados por separado.

!!! tip
    En algunas _distros_ es posible que haya una opción de "instalar drivers de terceros" en el instalador, la cual suele incluir los drivers oficiales.

!!! tip
    Es posible que los _drivers_ oficiales no estén disponibles para gráficas más antiguas. Existe una alternativa open-source, [Nouveau](https://nouveau.freedesktop.org/), la cual _suele_ ir mejor en este tipo de gráficas. Consulta su documentación para ver cómo instalarlos.


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
Ejecuta el comando `lspci -k -d ::03xx` y fíjate en el resultado, por ejemplo:
```
VGA compatible controller: NVIDIA Corporation AD107 [GeForce RTX 4060] (rev a1)
```
Mira tu tarjeta (en este caso, *AD107*) y [en la web](https://wiki.archlinux.org/title/NVIDIA#Installation) comprueba a qué gráfica se corresponde. En el caso general,

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




## Impresoras
En la mayoría de casos y _distros_, las impresoras deberían funcionar sin problemas, ya que los drivers suelen estar en el kernel. En el peor de los casos, suele bastar con instalar [CUPS](https://openprinting.github.io/cups/).

Recursos extra:

- [OpenPrinter](https://openprinting.github.io/)
- [CUPS - Arch Wiki](https://wiki.archlinux.org/title/CUPS)



## Instalar rEFInd
[rEFInd](https://www.rodsbooks.com/refind/) es un _boot manager_, al igual que
GRUB, pero más moderno y customizable. Es recomendable instalarlo en ordenadores
más modernos, y **no es recomendable instalarlo en ordenadores antiguos**.

### Linux
1. Instala el paquete `refind` (suele estar en el gestor de paquetes)
2. Reinicia. Debería salirte el _boot manager_ de rEFInd

!!! tip
    Si después de reiniciar no aparece rEFInd, entra en la BIOS y selecciónalo
    como opción de _boot_ principal.

!!! tip
    Si tienes problemas para bootear rEFInd en Mac, quizás te pueda ayudar lo siguiente: [rEFInd bootloader doesn't launch on start](https://apple.stackexchange.com/questions/446575/refind-bootloader-doesnt-launch-on-start).



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
