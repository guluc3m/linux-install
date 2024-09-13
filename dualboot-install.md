# Instalación de Linux con Windows en dualboot

En este tutorial vamos a explicar cómo instalar Linux junto a Windows
(dualboot). Este tutorial está pensado para instalar ambos sistemas operativos
en el disco duro interno / los discos duros internos que tengas en el
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
Para instalar Linux tenemos que reducir la partición de Windows/MacOS, y quién
mejor para hacerlo que el mismísimo Windows/MacOS. Es más seguro que Windows/MacOS
haga lo que quiera para reducir la partición que hacerlo desde Linux y Windows se
lleve la sorpresa de que ha encogido.

### Encoger particiones

#### Windows
 1. Click derecho en el icono de Windows
 2. Selecciona "Administración de Discos"
 3. Click derecho en la partición a reducir
 4. Selecciona "Reducir Volumen..."
 5. Cambia "Tamaño del espacio que desea reducir en MB" por el tamaño que le
 quieras dejar a la partición de Linux mínimo 65536 MiB (64GiB). Y clica
 reducir. Si no puedes reducir el espacio dicha cantidad y sabes que tienes más
 de 64GiB libres (deberías tenerlo si te has leído el README `>:(`),
 defragmenta el disco.

#### MacOS
<!--
TODO
https://www.makeuseof.com/tag/install-linux-macbook-pro/
-->

### Defragmentación del Disco (sólo Windows)
#### Windows 10
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


## 2. Desactivar encripción BitLocker (sólo Windows)
Si tu ordenador tiene encripción BitLocker. Para ello, en el menú busca
"Encripción BitLocker". Si no aparece, genial pasa al paso 3, si no continúa.

 1. Abre la configuración que has buscado antes ("Encripción BitLocker")
 2. Haz una copia de seguridad de tu clave de recuperación de BitLocker.
 Guárdala como un archivo y súbela a Drive o a un disco duro externo.
 3. Haz click en Desactivar BitLocker.
 4. Cuando aparezca que lo vuelvas a activar, significa que se ha desactivado
 corréctamente.


## 3. Desactivar inicio rápido (sólo Windows)
Sigue los pasos para comprobar que lo tienes desactivado.

### Windows 10
 1. Entra en el "Panel de Control"
 2. Busca "Opciones de Energía"
 3. Elegir el "Comportamiento de los botones inicio/apagado"
 4. Desactiva inicio rápido
 5. "Guardar Cambios"

### Windows 11
 1. Busca "Opciones de Energía" en el "Panel de Control"
 (Panel de Control > Hardware y sonido > Opciones de Energía)
 2. Elegir la acción de los botones de inicio/apagado
 3. Desactiva el Inicio Rápido
 4. "Guardar Cambios"

Si no aparece la opciones de energía, ejecutar en una CMD

> powercfg.exe /h on

Y cuando termines

> powercfg.exe /h off


## 4. Arrancar en Linux
Apaga el ordenador, mete el pincho en el ordenador y arranca la BIOS. El botón
para entrar en la BIOS depende del ordenador, así que prueba teclas hasta que
alguna funcione. Por lo general son: `ESC`, `F11`, `F12` o `DEL` (Suprimir). Si
no consigues arrancar la BIOS busca en internet tu modelo de ordenador y qué
tecla utilizar.

Ya que estamos en la BIOS asegúrate de que "Intel(R) Rapid Start Technology"
está **desactivado**.

No es necesario desactivar "Secure Boot" para Ubuntu, si estás instalando otra
distro, desactívalo por si acaso, es posible que no te deje arrancar desde el
USB.

Cambia el orden de arranque de los discos y pon que el USB esté primero.

Guarda cambios y sal.

Debería arrancar el LiveUSB.


## 5. Instalar Linux
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

## 6. Wrap-Up
Ya hemos terminado `:)`. Al reiniciar verás el GRUB, selecciona primero Windows
y asegúrate de que funciona. Reinicia y entra en Ubuntu.

## Links de interés
- [Dual boot with Windows - ArchWiki](https://wiki.archlinux.org/title/Dual_boot_with_Windows)
- [Multi-boot - Linux Mint Instalation Guide](https://linuxmint-installation-guide.readthedocs.io/en/latest/multiboot.html)
- [How to set up Linux dual-boot on a MacBook Pro](https://gist.github.com/Tomasvrba/f91f7399d99d3e25b62116cbe54794f8)
- [Dual Boot Windows and Linux With rEFInd](https://www.youtube.com/watch?v=1vEkn_kcXas)
