# Instalación de Linux en dualboot

En este tutorial vamos a explicar cómo instalar Linux junto a Windows/MacOS
(dualboot). Este tutorial está pensado para instalar ambos sistemas operativos
en el disco duro interno `/` los discos duros internos que tengas en el
ordenador.

En el caso en el que quieras instalar el sistema operativo en un disco externo,
puedes saltarte el primer paso, las particiones se pueden hacer desde el
LiveUSB.



## Requisitos
 * Mínimo 64GiB de almacenamiento disponible para la partición de Linux.
 * Si quieres hacer una partición `swap` (memoria virtual) para poder hibernar
 el ordenador (por ejemplo). Se recomienda dejar una partición un poco más
 grande que el tamaño de tu memoria RAM. Si tienes 16GiB de RAM, hacerla de,
 por ejemplo 18GiB. Esta opción es opcional.



## 1. Dejar espacio para la partición de Linux
Para instalar Linux tenemos que reducir la partición del SO (Windows/MacOS),
y quién mejor para hacerlo que el mismísimo SO. Es más seguro que el SO haga lo
que quiera para reducir la partición que hacerlo desde Linux y el SO se lleve
la sorpresa de que ha encogido.

### 1.W. Windows
 1. Click derecho en el icono de Windows
 2. Selecciona "Administración de Discos"
 3. Click derecho en la partición a reducir
 4. Selecciona "Reducir Volumen..."
 5. Cambia "Tamaño del espacio que desea reducir en MB" por el tamaño que le
 quieras dejar a la partición de Linux mínimo 65536 MiB (64GiB). Y clica
 reducir. Si no puedes reducir el espacio dicha cantidad y sabes que tienes más
 de 64GiB libres (deberías tenerlo si te has leído el README `>:(`),
 defragmenta el disco.

### 1.M. MacOS
 1. Abre la aplicación 'Disk Utility' (`Applications` > `Utilities` en Finder)
 2. En la barra de menú, ve a `View` > `Show All Devices`
 3. En el menú de la izquierda, selecciona el SSD
 4. En el menú de arriba a la derecha, selecciona `Partition`, y en la ventana
 nueva haz click en el `+`. Crea una partición de mínimo 64GB, y ponle de nombre
 'Linux' (por ej.). En el formato, selecciona `MS-DOS (FAT)`.

> [!NOTE]
> Si no te deja crear nuevas particiones, es posible que tu disco esté
> encriptado por FileVault. Ve a `System Settings` > `Network` > `FileVault`
> para desactivarlo.



## 2. Preparar el SO

### 2.W.1. Defragmentar el Disco (sólo Windows)
##### Windows 10
 1. Abre el explorador de archivos
 2. Ve a "Este Equipo"
 3. Selecciona el Disco a defragmentar.
 4. Arriba clica en "Herramientas de unidad"
 5. Clica "Optimizar"
 6. Clica en "Optimizar" e inserta tu contraseña si fuera necesario.

#### Windows 11
 1. Abre el explorador de archivos
 2. Ve a "Este equipo"
 3. Click derecho en el disco a desfragmentar
 4. Ve a "Propiedades"
 5. Ve a "Herramientas"
 6. Clica en "Optimizar"
 7. Clica en "Optimizar" e inserta tu contraseña si fuera necesario.


### 2.W.2. Desactivar encripción BitLocker (sólo Windows)

Si tu ordenador tiene encripción BitLocker. Para ello, en el menú busca
"Encripción BitLocker". Si no aparece, genial pasa al paso 3, si no continúa.

 1. Abre la configuración que has buscado antes ("Encripción BitLocker")
 2. Haz una copia de seguridad de tu clave de recuperación de BitLocker.
 Guárdala como un archivo y súbela a Drive o a un disco duro externo.
 1. Haz click en `Desactivar BitLocker`.
 2. Cuando aparezca que lo vuelvas a activar, significa que se ha desactivado
 corréctamente.


### 2.W.3. Desactivar inicio rápido (sólo Windows)
Sigue los pasos para comprobar que lo tienes desactivado.

#### Windows 10
 1. Entra en el "Panel de Control"
 2. Busca "Opciones de Energía"
 3. Elegir el "Comportamiento de los botones inicio/apagado"
 4. Desactiva inicio rápido
 5. "Guardar Cambios"

#### Windows 11
 1. Busca "Opciones de Energía" en el "Panel de Control"
 (`Panel de Control` > `Hardware y sonido` > `Opciones de Energía`)
 2. Elegir la acción de los botones de inicio/apagado
 3. Desactiva el Inicio Rápido
 4. "Guardar Cambios"

Si no aparecen la opciones de energía, ejecuta en CMD:

```cmd
powercfg.exe /h on
```

Y cuando termines:
```cmd
powercfg.exe /h off
```


### 2.M.1. Permitir bootear desde disco externo (sólo MacOS)
Para Macs con chip de seguridad T2 (2018-2020), es necesario habilitar que pueda
arrancar el SO desde un disco externo. Para ello:
 1. Reinicia el Mac en _recovery mode_ (Mantén `Command`+`R` mientras arranca)
 2. Selecciona tu usuario (debe tener permisos de administrador) y pon la
 contraseña
 4. En la barra de herramientas, ve a `Utilities` > `Startup Secutiry Utility`
 5. En el apartado `Allowed Boot Media`, selecciona `Allow booting from external
 or removable media`
 6. Reinicia el ordenador



## 3. Arrancar en Linux

> [!INFO]
> Dependiendo del ordenador, es posible que puedas entrar directamente al _boot
> menu_ y seleccionar qué bootear. Por ejemplo, en Mac es manteniendo la tecla
> `Option` durante el arranque.

1. Apaga el ordenador, mete el pincho en el ordenador y arranca la BIOS. El
botón para entrar en la BIOS depende del ordenador, así que prueba teclas hasta
que alguna funcione. Por lo general son: `ESC`, `F11`, `F12` o `DEL` (Suprimir).
Si no consigues arrancar la BIOS busca en internet tu modelo de ordenador y qué
tecla utilizar.
2. Ya que estamos en la BIOS asegúrate de que "Intel(R) Rapid Start Technology"
está **desactivado**.
3. Desactiva "Secure Boot"
> [!INFO]
> No es necesario desactivar el Secure Boot para distros como Ubuntu, pero si
> estás instalando otra distro, o estás teniendo problemas al arrancar,
> desactívalo
4. Cambia el orden de arranque de los discos y pon que el USB esté primero.
5. Guarda cambios y sal.

Debería arrancar el LiveUSB.



## 4. Instalar Linux

### Ubuntu
 1. Instalar Ubuntu.
 2. Selecciona el idioma.
 3. **IMPORTANTE**, incluso si has seleccionado otro idioma que no sea el
 español, asegúrate de elegir en la distribución del teclado la que se adapte
 a tu ordenador o la que uses normalmente.
 4. Selecciona "Instalación Normal" e "Instalar software de terceros"; y
 **deselecciona** "Descargar actualizaciones mientras se instala Ubuntu", que
 luego nos echan la culpa si se cae Eduroam. Si estás haciéndolo desde casa,
 primero ¿por qué no has venido `:(`? y segundo puedes activar lo de descargar
 actualizaciones.
 5. Selecciona la tercera opción "Something else" (o como se diga en español).
 6. Piensa cómo vas a dividir el disco:
    1. Crear una única partición con todo.
    2. Crear dos particiones `/` y `/home`, la primera partición tendrá el
    sistema operativo y el software que descargues y la segunda tus archivos
    personales. Se recomienda esta segunda opción porque permite reinstalar
    Linux u otra distribución fácilmente. A `/` se le darían 32GiB y a `/home`,
    el resto.
    3. Si has decidido crear un `swap`, tendrás que hacer otra partición.
 7. Selecciona el disco donde va el gestor de arranque (normalmente en el mismo
 disco donde está Windows).
 8. Para hacer una partición sigue los siguientes pasos:
    1. Selecciona el hueco libre
    2. Selecciona "Primaria"
    3. Especifica el tamaño de la partición.
    4. El formato de las particiones y el punto de montaje es:
       - Para `/` es `ext4` y se monta en `/`.
       - Para `/home` es `ext4` y se monta en `/home`.
       - Para `swap` seleccionar usar como `área de intercambio`.
 9. Clica en instalar y **asegúrate de que está todo bien**.
 10. Entra tus credenciales y a esperar.

Un ejemplo de particionado de disco es:

```plain
Dispositivo    Tipo     Punto de Montaje     Formatear   Tamaño
/dev/sda7      ext4     /                    Sí          32GiB
/dev/sda8      ext4     /home                Sí          32GiB
/dev/sda9      swap     swap                 Sí          18GiB
```

**No se debería formatear ninguna otra partición**.

### Otras Distribuciones
Al igual que Ubuntu, pero puede que cambie algún paso.



## 5. Wrap-Up
Ya hemos terminado `:)`. Al reiniciar verás el GRUB, selecciona primero Windows
y asegúrate de que funciona. Reinicia y entra en Ubuntu.

> [!NOTE]
> Si después de reiniciar no aparece GRUB, entra en la BIOS y selecciónalo
> como opción de boot principal.


## Extra: Instalar rEFInd
[rEFInd](https://www.rodsbooks.com/refind/) es un boot manager, al igual que
GRUB, pero más moderno y customizable. Es recomendable instalarlo en ordenadores
más modernos, y **no es recomendable instalarlo en ordenadores antiguos**.

### MacOS
Es recomendable instalarlo desde Mac antes que desde Linux

1. Desactiva System Integrity Protection (SIP)
   1. Reinicia el Mac en _recovery mode_ (Mantén `Command`+`R` mientras arranca)
   2. Selecciona tu usuario (debe tener permisos de administrador) y pon la
   contraseña
   3. En la barra de herramientas, ve a `Utilities` > `Terminal`
   4. Ejecuta el siguiente comando:
      ```
      csrutil disable
      ```
2. Reinicia
3. [Descarga rEFInd](https://sourceforge.net/projects/refind/)
4. Descomprime el ZIP y entra en la carpeta.
5. Abre un terminal en la carpeta (desde Finder, `Ctrl`+`click` en la barra de
ruta y selecciona `Abrir en Terminal`)
6. Ejecuta `./refind-install`
7. Vuelve a activar System Integrity Protection (SIP), siguiendo los mismos
pasos que para desactivarlo, pero ejecutando el comando
   ```
   csrutil enable
   ```
8. Reinicia. Debería salirte el boot manager de rEFInd


### Linux
1. Instala el paquete `refind` (suele estar en el gestor de paquetes)
2. Reinicia. Debería salirte el boot manager de rEFInd

> [!NOTE]
> Si después de reiniciar no aparece rEFInd, entra en la BIOS y selecciónalo
> como opción de boot principal.



## Links de interés
- [Dual boot with Windows - ArchWiki](https://wiki.archlinux.org/title/Dual_boot_with_Windows)
- [Multi-boot - Linux Mint Instalation Guide](https://linuxmint-installation-guide.readthedocs.io/en/latest/multiboot.html)
- [Dual Boot Windows and Linux With rEFInd](https://www.youtube.com/watch?v=1vEkn_kcXas)
- [How to set up Linux dual-boot on a MacBook Pro](https://gist.github.com/Tomasvrba/f91f7399d99d3e25b62116cbe54794f8)
