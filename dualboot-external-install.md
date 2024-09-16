# Instalación de Linux en un disco externo con Windows en dualboot

En este tutorial vamos a explicar cómo instalar Linux en un disco duro externo en ordenadores que ya tienen otro sistema operativo (por ejemplo, Windows) con dualboot.


## Requisitos
 * Un disco externo con un Mínimo de 64GiB de almacenamiento disponible. Mantén este disco conectado al ordenador durante todo el proceso.
 * Si quieres hacer una partición `swap` (memoria virtual) para poder hibernar  el ordenador (por ejemplo). Se recomienda dejar una partición un poco más grande que el tamaño de tu memoria RAM. Si tienes 16GiB de RAM, hacerla de,  por ejemplo 18GiB (aparte de los 64 GiB anteriores). Esta partición es opcional.
 * Dos puertos USB disponibles, uno para el disco externo, y otro para el instalador (LiveUSB).


## 1. Desactivar inicio rápido
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

## 2. Arrancar en Linux
Apaga el ordenador, asegúrate de tener el disco externo conectado, mete el LiveUSB, arranca el ordenador y entra en la BIOS. El botón para entrar en la BIOS depende del ordenador y normalmente lo pone en la pantalla de arranque. Si no es así, prueba teclas hasta que alguna funcione. Por lo general son: `ESC`, `F11`, `F12` o `DEL` (Suprimir). Si no consigues arrancar la BIOS busca en internet tu modelo de ordenador y qué tecla utilizar. En equipos UEFI también se puede acceder desde el sistema operativo.

Ya que estamos en la BIOS asegúrate de que "Intel(R) Rapid Start Technology" está **desactivado**.

No es necesario desactivar "Secure Boot" para Ubuntu, pero si estás instalando otra distro, desactívalo en caso de que no te deje arrancar desde el USB.

Cambia el orden de arranque de los discos y pon que el USB esté primero.

Guarda cambios y sal.

Debería arrancar el Linux LiveUSB.

## 2. Sistemas UEFI

Hay dos maneras de instalar y arrancar un sistema operativo actualmente:

 * Normal: El sistema inicia con el basic input output system (BIOS), la cual realiza varias tareas iniciales (escaneo de memoria, detección de periféricos, etc...) y da paso a la primera línea de código del sistema operativo, que se encuentra en el sector de arranque del disco principal (el primero en la lista de arranque en la configuración de BIOS).

 * UEFI Boot: El arranque se configura durante la instalación del sistema operativo, y se guarda la configuración de la bios, incluyendo en ID del disco en el que se instala el sistema, de forma que ese arranque solamente funcionará para ése sistema operativo y en ese disco.

Muchos sistemas preinstalados (windows sobre todo) tienen arranque UEFI y algunos tienen SecureBoot (que impide arrancar desde cualquier otro disco). Por eso para instalar cualquier otro sistema operativo tendremos que lidiar con éstos conceptos y probablemente deshabilitarlos (al menos SecureBoot).

## 3. Arranque en dual boot con UEFI

La forma más cómoda y que se recomienda para arrancar un PC con varios sistemas operativos es GRUB (Linux).

Éste programita (realmente, es muy pequeño) se instala en el sector de arranque del disco principal (vuelve a leer dessde el pricipio si no entiendes éste párrafo), y muestra un diálogo que permite elegir entre varios sistemas operativos instalados (Linux, windows, ...).

En un sistema windows UEFI, el arranque irá directamente al sistema operativo sin pasar por el sector de arranque, por lo que si instalamos GRUB en el disco principal, nunca se ejecutará, y no tendremos acceso a Linux.

Por otra parte, si instalamos GRUB en el disco externo y lo configuramos como disco principal desde la BIOS, funcionará correctamente hasta que desconectemos el disco externo y encendamos el PC. En este caso, la BIOS elegirá el siguiente disco disponible y arrancará desde ése, o no arrancará si no hay ninguno. Si queremos recuperar el arranque en GRUB, hay que entrar a la configuración de BIOS con el disco externo conectado y volver a configurarlo como disco principal.

Muchos sistemas tienen la opción de elegir el disco principal en el momento de arranque si se pulsa una tecla (suele ser F8) al principio del arranque del PC, en la pantalla de POST.

Si no te convence ninguna de estas opciones de arranque, lo mejor es que consideres otra opción de instalación, como hacer una partición en un disco interno, o añadir un nuevo disco a tu ordenador.

Una vez que has elegido la forma de arrancar, puedes continuar con el siguiente paso.

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
 6. Elige el disco (externo) de instalación. **Cuidado**, asegúrate de que sea un disco vacío, o de lo contrario borrarás lo que contenga (incluído windows si es el caso).
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
