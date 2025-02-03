# Instalación de Linux en dualboot

En este tutorial vamos a explicar cómo instalar Linux junto a Windows
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

1. Click derecho en el icono de Windows
2. Selecciona "Administración de Discos"
3. Click derecho en la partición a reducir
4. Selecciona "Reducir Volumen..."
5. Cambia "Tamaño del espacio que desea reducir en MB" por el tamaño que le
quieras dejar a la partición de Linux mínimo 65536 MiB (64GiB). Y clica
reducir. Si no puedes reducir el espacio dicha cantidad y sabes que tienes más
de 64GiB libres (deberías tenerlo si te has leído el README `>:(`),
defragmenta el disco.



## 2. Preparar Windows

### 2.1. Defragmentar el Disco
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


### 2.2. Desactivar encripción BitLocker

Si tu ordenador tiene encripción BitLocker. Para ello, en el menú busca
"Encripción BitLocker". Si no aparece, genial pasa al paso 3, si no continúa.

1. Abre la configuración que has buscado antes ("Encripción BitLocker")
2. Haz una copia de seguridad de tu clave de recuperación de BitLocker.
   Guárdala como un archivo y súbela a Drive o a un disco duro externo.
3. Haz click en `Desactivar BitLocker`.
4. Cuando aparezca que lo vuelvas a activar, significa que se ha desactivado
   corréctamente.


### 2.3. Desactivar inicio rápido
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
1. Elegir la acción de los botones de inicio/apagado
2. Desactiva el Inicio Rápido
3. "Guardar Cambios"

Si no aparecen la opciones de energía, ejecuta en CMD:

```cmd
powercfg.exe /h on
```

Y cuando termines:
```cmd
powercfg.exe /h off
```



## 3. Arrancar en Linux
Ver [Arrancar desde el Live USB](common.md#arrancar-desde-el-liveusb).



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
> como opción de boot principal. Suele venir 'camuflado' con el nombre de la
> distribución, e.g. `ubuntu`.

También te recomendamos echarle un vistazo a nuestra sección [Post-Install](post-install.md).


## Troubleshooting
- [Solucionar drivers Wi-Fi](common.md#solucionar-drivers-wi-fi)



## Links de interés
- [Dual boot with Windows - ArchWiki](https://wiki.archlinux.org/title/Dual_boot_with_Windows)
- [GRUB - ArchWiki](https://wiki.archlinux.org/title/GRUB)
- [rEFInd - ArchWiki](https://wiki.archlinux.org/title/REFInd)
- [Multi-boot - Linux Mint Instalation Guide](https://linuxmint-installation-guide.readthedocs.io/en/latest/multiboot.html)
- [Dual Boot Windows and Linux With rEFInd](https://www.youtube.com/watch?v=1vEkn_kcXas)
