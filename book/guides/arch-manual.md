# Guía de instalación de Arch Linux

Antes de seguir con la guía, pasa por la preparación previa antes:

- [Dualboot Windows](dualboot-install.md)
- [Dualboot MAC](dualboot-mac-install.md)

## 1. Requisitos mínimos
Para poder instalar arch linux en tu ordenador, necesitamos lo siguiente:

- Un sistema de arquitectura x86.64 compatible.
- Un mínimo de 512 MB de RAM para ejecutarse.
  - **OJO**: Para poder acceder a la instalación, se necesita más. Son recomendables 2 GB de RAM.
- Mínimo de 2 GB de disco duro.
- Un USB con al menos 2 GB de espacio para *flashear* la ISO.
- Un dispositivo distinto a mano para poder seguir la guía.
- Una conexión estable a internet.

## 2. Primeros pasos
Este paso es la continuación a la guía mencionada arriba, una vez has accedido a la ISO desde el selector de disco de arranque.

- Elige la opción de instalar arch.
- Espera un rato, la ISO se está copiando en memoria RAM. Una vez termine, puedes desconectar el USB.

**Sanity check:** ejecuta `lsblk` (list blocks), deberías tener algo así como
```bash
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 931.5G  0 disk 
├─sda1        8:1    0   200M  0 part 
├─sda2        8:2    0 631.3G  0 part 
└─sda3        8:17   0   300G  0 part 
```
Si tu espacio libre es de 300 GigaBytes, lo has hecho bien. Nota como `/sda` lo marca como "disk" y el resto "part". Esto es porque el primero es un volumen y las partes son sus distintas particiones.
**NOTA:** En lugar de `sda` y `sdaX` es posible que el disco se llame `nvme0n1` y sus particiones `nvme0n1pX`. Comprueba bien los nombres de las particiones que te salen con `lsblk`.

## 3. Elegir el layout del teclado

Ejecuta el siguiente comando para cargar el *layout* del teclado español:
```bash
loadkeys es
```
Si tu teclado no es layout es,
```bash
localectl list-keymaps
```
y encuentra tu modelo.

### 3.1. Verifica que estás en modo UEFI, lo cual es lo más probable
```bash
cat /sys/firmware/efi/fw_platform_size
```
Te debe salir un 64 o 32 como resultado. Si no te sale eso, consulta el [enlace](https://wiki.archlinux.org/title/Installation_guide#Verify_the_boot_mode) de la wiki de arch para más profundidad.

> Si no existe el directorio, es muy probable que hayas arrancado desde BIOS, algo común en máquinas más antiguas. En los pasos que esto implique una variación del proceso, se incluirá una nota al pie como esta.

## 4. Internet.

Ejecuta el comando `ip link` y comprueba si tienes una interfaz "wlan0" "eth0"... Asegúrate que un proceso rfkill no esté bloqueando tu tarjeta de red. Consulta la [wiki](https://wiki.archlinux.org/title/Installation_guide#Connect_to_the_internet) de arch para más profundidad.
- Si es un cable ethernet, conéctalo sin más.
- Si es una WiFi, salta al paso 4.1.
- Si es un móvil por cable, ve a ajustes -> Punto de acceso portátil -> Activa compartir por USB.

### 4.1. WiFi
Ejecuta el comando `iwctl`. Esta es una [herramienta](https://wiki.archlinux.org/title/Iwd) para conectarse a redes inalámbricas.

Para conectarte a internet usarás tu interfaz inalámbrica, en el caso de ejemplo, "wlan0", la cual es probable que tengas tú también.
```iwd
station wlan0 scan
station wlan0 get-networks
station wlan0 connect X
```
En donde X es el SSID de la red. Si son varias palabras, ponlo entre "comillas".
- `scan` busca redes cerca de tí.
- `get-networks` te lista los resultado.
- `connect` te permite conectarte a la deseada.
Si es una WiFi normal como la de casa, pon la contraseña, si es eduroam, consulta nuestro [post-install](post-install.md#eduroam).
Haz `ping 9.9.9.9` y comprueba que hay flujo de paquetes.

## 5. Reloj interno
Ejecuta `timedatectl` para sincronizar el reloj interno.

## 6. Hacer las particiones
Este paso **es clave**, presta atención:

Ejecuta `cfdisk`.

La interfaz es muy intuitiva, navega con las flechas a la partición de 300 GB y elige, si no figura ya como "free space", "delete".

- Ve con las flechas al espacio libre y elige "add new" o similar. Elige el tamaño de 1 GB (recomendado en la wiki de arch).
- Repite el paso y crea una de igual tamaño a tu RAM más 2 GB (Si tienes 16 GB, pon 18). Esta será sdaY.
- Repite y elige todo el epsacio restante, se suele poner automático el espacio libre que queda. Esta sdaZ.
**Es muy importante que recuerdes qué division de /dev/sdaX es cada una**
**Cuidado de no borrar la partición con tu otro OS, si procede**

> En el caso BIOS, al ejecutar el comando te debe salir arriba "Partition type: dos", si no es así, consulta la [wiki de arch](https://wiki.archlinux.org/title/Installation_guide#Verify_the_boot_mode).
> 
### 6.1. Formatear
- La partición de 1 GB es la de arranque, será formato EFI montado en /boot. (Formatea esta únicamente si la has creado desde `cfdisk`). Se formatea en FAT32.
- La de tamaño RAM es una partición de SWAP, importante para hibernar el sistema o si se queda sin RAM. Se formatea como swapspace.
- La grande es el sistema de ficheros, donde guardarás tus documentos y juegos. Puede ser cualquier sistema de ficheros, pero se recomienda ext4.
```bash
mkfs.fat -F 32 /dev/sdaX
mkswap /dev/sdaY
mkfs.ext4 /dev/sdaZ
```

> En elc aso BIOS, haz una particion swap y deja el resto como root, no necesitas una partición separada para boot. Es decir, haz solo sdaY y sdaZ.

### 6.2. Montar el sistema de archivos
Ejecuta estos comandos para habilitar y poder trabajar sobre estas nuevas particiones y así instalar arch linux:
```bash
mount --mkdir /dev/sdaX /mnt/boot
swapon /dev/sdaY
mount /dev/sdaZ /mnt
```
> En BIOS, si no has hecho partición de boot, puedes ignorar el primer comando de la lista.
> 
## 7. Instalar el kernel de linux
El kernel es el núcleo del sistema operativo, es lo que hay detrás que tú no ves. Sin ello, no existe sistema operativo.
Linux tiene varios kernel, el nomral, el LTS, el zen.... Depende de gustos o necesidades los hay mejores y peores. Si buscas algo estable a largo plazo, quédate con linux-lts
```bash
pacstrap -K /mnt base linux-lts linux-firmware
```
Donde yo he puesto `linux-lts` pon el kernel de tu elección. Consulta la [wiki de arch](https://wiki.archlinux.org/title/Kernel) para más profundidad.
**NOTA:** Si tu gráfica es de NVIDIA, necesitarás drivers y paquetes adicionales, consulta [esta guía](post-install.md#Drivers de NVIDIA).

## 8. Configura la tabla de particiones y puntos de montaje
```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
Puedes revisar el resultado con `cat` o `nano` para asegurarte de que sean correctos. Este archivo le dirá al bootloader donde encontrar qué cosa al arrancar el sistema.

## 9. Accede al nuevo sistema
Ejecuta este comando para entrar al sistema como si hubieras arrancado en él:
```bash
arch-chroot -S /mnt
```
Ahora podrás manejar el sistema de ficheros como si estuvieras en tu sistema, pero aún faltan unas cuantas cosas.

## 10. Instalar paquetes esenciales.
Aunque hayas usado `iwd`, éste no viene instalado por defecto, por lo que te recomiendo instalar estos paquetes esenciales para evitar problemas:
```bash
pacman -S nano iwd sudo dhcpcd man
```
`nano` es un editor de archivos para el terminal.
`iwd` es una herramienta (de terminal) para poder conectarte a redes WiFi.
`sudo` te permite ejecutar comandos que requieran permiso de administrador sin ser `root`.
`dhcpcd` te permite resolver los *dynamic host* y acceder a internet.
`man` te permite ver los manuales de Unix de los comandos.

## 11. Zona horaria
```bash
ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime
```
Europe y Madrid son los puntos de zona horaria, para otra zona horaria cambia la ciudad por London, Prague o Moscow y el continente por el que convenga. Si escribes el comando a mano, `/zoneinfo/` y tabulas un par de veces, se mostrarán todas las opciones disponibles.

Usa el comando `hwclock --systohc` para generar el archivo `/etc/adjtime`

## 12. Genera y configura las *locales*

Usa `locale-gen` para generar las locales. Crea y edita, con `nano`, el archivo `/etc/locale.conf` y añade este texto:
```
LANG=en_US.UTF-8
```
para una configuración default con localización EEUU. Para más info de las locales y cuál usar, lee la [wiki de arch](https://wiki.archlinux.org/title/Locale).

## 13. El layout... de nuevo

Para hacer permanente la elección del layout de tu teclado, abre, con `nano`, el archivo `/etc/vconsole.conf` y pon este texto:
```
KEYMAP=es
```
para un layout español estánar. Si tienes otro layout, sustituye *es* por el que te saliera en el paso 3.

## 14. Elige el nombre de tu máquina

Crea con `nano` el archivo `/etc/hostname` y pon en él, en una única línea el nombre que le quieras dar a tu máquina. (Servirá como nombre de dominio para resoluciones DNS)

## 15. Crea de nuevo el intramfs para guardar las configuraciones del teclado

```bash
mkinitcpio -P
```
Con esto el sistema base queda configurado.

## 16. Contraseña de *root*
Usa el comando `passwd` y pon la contraseña. Esta contraseña será la necesaria para entrar al sistema como *root*, lo cual concede permisos de admin automáticamente. MUCHO CUIDADO a lo que ejecutes siendo *root*, podrías literalmente borrar todos y cada uno de tus archivos.

## 17. Agrega tu usuario
```bash
useradd -m -G wheel nombre
```
Para modificar o eliminar usuarios, usa `usermod` o `userdel`.

Para tener permisos de aministrador, ejecuta este comando:
```bash
EDITOR=nano visudo
```
Y descomenta (quita el *hashtag* '#') de la línea 
```
%wheel ALL=(ALL:ALL) ALL
```
la cual está en la parte inferior del documento. Con esto, estamos dando permisos de admin (bajo contraseña) a los usuarios del grupo *Wheel*, al cual añadimos el usuariuo antes.

Ahora, ejecuta
```bash
passwd nombre
```
para poner contraseña a tu usuario. Cuando uses `sudo` será ésta la contraseña a utilizar, no la de `root`.

## 18. Boot loader

[Guía oficial con todas las opciones](https://wiki.archlinux.org/title/Arch_boot_process#Boot_loader).

Es lo que permite al sistema arrancar e inicializarse.
El boot loader por excelencia es *grub*, aunque hay alguno más. En esta guía explicaré como instalar *grub*.

### 18.1. Instala los paquetes necesarios
```bash
pacman -S grub efibootmgr
```
> En BIOS, no necesitas el `efibootmgr` pues no estás usando el arranque EFI. sino BIOS. Descarga solo el paquete `grub`.

### 18.2. Instala [grub](https://wiki.archlinux.org/title/GRUB)
```bash
grub-install --target=x86_64-efi --efi-directory=/dev/sdaX --bootloader-id=GRUB
```
Recuerda que sdaX es la partición /boot que hemos formateado antes en el paso **6**.

> Aquí el comando cambia, pues no hay directorio efi ni partición boot.
> ```bash
> grub-install --target=i386-pc /dev/sda
> ```

### 18.3. Crea el archivo de configuración
```bash
grub-mkconfig -o /boot/grub/grub.cfg
```
Creando este archivo, verás una interfaz manejable con flechitas cuando arranques la partición EFI, en lugar de una consola de comandos de GRUB.

## 19. Escritorio
Para terminar, sólo falta una cosa: elegir tu entorno de escritorio. Esto es lo que verás al arrancar el sistema. El más popular es KDE, por sus amplias opciones de personalización; si tu ordenador es una patata, te recomiendo xfce, bastante ligero en memoria; si te gustan los pies, pues tienes GNOME; y para cualquier otro, tienes una lista completa en la [arch wiki](https://wiki.archlinux.org/title/Desktop_environment).

### 19.1. KDE
Descarga todos estos paquetes para una instalción completa. Recomeindo que no instales KDE si tienes menos de 8 GB de memoria RAM.
```bash
pacman -S plasma kde-applications plasma-login-manager
```
Ahora, habilita el servicio con `systemd` para que se abra una sesión de plasma al encender el ordenador.
```bash
systemctl enable plasmalogin.service
```

### 19.2. Xfce
Rápido, sencillo, bueno, bonito, barato (más bien gratis). Recomendado para ordenadores más viejos o de pocos recursos RAM (por ejemplo, 4 GB).
```bash
pacman -S xfce4 xfce4-goodies xorg-server lightdm lightdm-gtk-greeter
```
Y una vez estén instalados, habilita *lightdm*, así, se arrancará la sesión al encender el sistema.
```bash
systemctl enable lightdm.service
```

### 19.3. GNOME
Visualmente simple, fácil de usar "out of the box".... y ya. No es muy personalizable, no lo recomiendo para sistemas de bajos recursos.
```bash
pacman -S gnome gnome-circle gnome-extra
```
Y habilitamos el servicio.
```bash
systemctl enable gdm.service
```

### 19.4. Otros
Hay muchos entornos de escritorio, según tus gustos o necesidades puedes instalar uno u otro, referenciados están en la [arch wiki](https://wiki.archlinux.org/title/Desktop_environment). Yo he probado estos 3 y para un ordenador potente, instala KDE.

## 20. Listo
Sal del *chroot* con `exit` o `ctrl+D`. Después haz `reboot` y repite el paso de abrir el selector de arranque. Si lo has hecho bien, en mac te saldrá un nuevo disco interno bajo el nombre "EFI Boot", minertras que en windows te saldrá como GRUB o similar. Entra en esa opción y comprueba que todo vaya bien.
Una vez en el nuevo sistema, haz login, abre un terminal y ejecuta estos comandos:
```bash
sudo systemctl enable dhcpcd.service
```
Con esto, cada vez que te conectes a una red, se resolverá solo el cliente dhcp.

## Links de utilidad
- [Guía de instalación base](https://wiki.archlinux.org/title/Installation_guide)
- [Entornos de escritorio](https://wiki.archlinux.org/title/Desktop_environment)
- [Boot loader](https://wiki.archlinux.org/title/Arch_boot_process#Boot_loader)
