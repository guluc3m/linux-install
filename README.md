# Guía del GUL para la instalación de Linux


## 1. Formas de instalar Linux

Hay diversas formas de "instalar" Linux. Entendemos que no todos tenéis las mismas circunstancias, así que recomendamos que tengáis en cuenta todas y elijáis la que más os convenga.

<!--
# Linux Install Party

## 1. Cosas a tener en cuenta ANTES DE ASISTIR AL TALLER
Uno de los objetivos de éste taller es instalar Linux en vuestros ordenadores.  
Para agilizar éste proceso, es recomendable que leáis la siguiente información:  

Hay diversas formas de "instalar" Linux. Entendemos que no todos tenéis las mismas circunstancias, así que recomendamos que tengáis en cuenta todas y elijáis una antes de venir, trayendo el material correspondiente dependiendo del método.
-->


### Prefacio: Nota para gente con Apple Macs
La instalación de Linux depende del modelo y, más importante, del microprocesador. En cualquier caso, debido a que _es un MAC_, sólo hay dos formas de ejecutar Linux: en dual boot y en VM.

#### Apple Silicon
Ordenadores con un procesador de la familia M1/M2 (Macbook Air/Pro de 2020 o posterior) con lleva un procesador [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family).

Las opciones son:
1. Dual boot (tener MacOS y Linux en el mismo ordenador) con [Ashahi Linux](https://asahilinux.org/). Guía en [`dualboot-mac-install.md`](dualboot-mac-install.md)
2. Correr una VM con una versión de Linux para ARM a través de [UTM](https://mac.getutm.app/). Guía en [`vm-install-mac.md`](vm-install-mac.md)


#### Intel
Ordenadores con procesador Intel (pre-2020).

Las opciones son:
1. Dual boot (tener MacOS y Linux en el mismo ordenador).
    - Si es un ordenador sin [chip de seguridad T2](https://support.apple.com/es-es/103265) (pre-2018), no suele haber demasiados problemas al instalar, y los pasos generales para la instalación son fundamentalmente iguales que para cualquier otra máquina. Te recomendamos la [siguiente guía](https://www.makeuseof.com/tag/install-linux-macbook-pro/).
    - Para ordenadores con chip T2 (2018-2019), lo más recomendable es usar [t2linux](https://t2linux.org/). Son parches específicos para múltiples distribuciones de Linux, ya que cosas como el Wi-Fi o el teclado y el trackpad no suelen funcionar con una ISO normal debido a los drivers.
2. Correr una VM como en cualquier otro ordenador. Guía en [`vm-install.md`](vm-install.md)


> [!NOTE]
> Para más información sobre _troubleshooting_ y resolución de problemas en portátiles Mac, ve a [Laptop/Apple - ArchWiki](https://wiki.archlinux.org/title/Laptop/Apple).


> [!INFO]
> Si tienes problemas para bootear rEFInd en Mac, quizás te pueda ayudar lo siguiente: [rEFInd bootloader doesn't launch on start](https://apple.stackexchange.com/questions/446575/refind-bootloader-doesnt-launch-on-start).


### Método 1: Full Linux
Este método consiste en decir "fuck Microsoft", borrar Windows, y correr sólo Linux.  
- **Restricciones:** Ninguna.  
Bueno sí, un ordenador con menos de 20 años.
- **Ventajas:** Todas las ventajas de Linux, sin los posibles problemas derivados de tener Dual Boot.
- **Desventajas:** Tu ordenador no va a tener Windows.  
Espera, ¿ese es un problema? Si tienes que usar Office, Adobe Creative Cloud, o algún programa o juego (cualquiera con AntiCheat) específico de Windows (y [Wine](https://www.winehq.org/) o [Proton](https://github.com/ValveSoftware/Proton) no te puede ayudar), sí.
- **Recomendado para:**
    - Linuxeros (frikis)
    - Un segundo ordenador portátil que uses para la uni
    - Tu tía la del pueblo que sólo usa Internet Explorer
- **Cosas que preparar:**
    - Copia de seguridad de tus archivos (fotos, fanfics, etc.)
    - Un [live USB con Linux](#2-cómo-crear-un-live-usb-de-ubuntu).


### Método 2: Dual Boot
Consiste en instalar en tu ordenador los dos sistemas operativos: Windows/MacOS y Linux.
- **Restricciones:** Mínimo 64GB de espacio libre en disco.
- **Ventajas:** Todas las ventajas de Windows (si las hay) y todas las de Linux.
- **Desventajas:** 
    - Puede ser un poco coñazo usar y mantener (configurar y actualizar) ambos sistemas operativos.  
    - Problemas de almacenamiento si tienes un disco pequeño.
    - Archivos en distintas particiones del disco
    - A las actualizaciones de Windows les gusta romper el Grub (bootloader)
    - Se desconfigura la zona horaria cada dos por tres
- **Recomendado para:** 
    - Estudiantes que necesiten Linux para la carrera, pero que quieran seguir usando su PC para jugar al Fortnite (u otras cosas de Windows)
    - Personas a la que gente malvada le obligue a usar Windows
- **Cosas que preparar:** 
    - Copia de seguridad de tus archivos (fotos, fanfics, etc.)
    - Un [live USB con Linux](#2-cómo-crear-un-live-usb-de-ubuntu).

Guía de cómo instalarlo en [`dualboot-install.md`](dualboot-install.md).


### Método 3: Windows Subsystem for Linux 2 (WSL2)
WSL te permite "correr Linux" dentro de Windows, pero sólo mediante una terminal, con un buen nivel de compatibilidad.
- **Restricciones:** Windows 10/11.
- **Ventajas:** 
    - Fácil y rápido de instalar
    - Ligero
    - Fácil acceso a los archivos
    - Soporte en bastantes aplicaciones: [Vs Code](https://code.visualstudio.com/docs/remote/wsl), IDEs de Jetbrains ([CLion](https://www.jetbrains.com/help/clion/how-to-use-wsl-development-environment-in-product.html), [PyCharm](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html), etc.), [CUDA](https://docs.nvidia.com/cuda/wsl-user-guide/index.html), y muchas más.
- **Desventajas:** 
    - No hay GUI, sólo puedes usar una terminal
    - Número de distros limitado
    - Eficiencia algo limitada
- **Recomendado para:** 
    - Gente que, por cualquier motivo, tenga que usar Windows y no tenga espacio para un segundo SO
    - Gente que no le tenga miedo a la terminal y decida seguir usando Windows (por algún motivo)
- **Cosas que preparar:** Nada, simplemente trae tu portátil

Guía de cómo instalarlo en [`wsl-install.md`](wsl-install.md).


### Método 4: Virtual Machine (VM)
Una máquina virtual (VM) te permite correr un SO virtual por encima de tu propio sistema operativo.
- **Restricciones:** Tener potencia de procesamiento suficiente para correr una VM.
- **Ventajas:** 
    - Entorno aislado del resto del PC
    - Fácil de desinstalar
- **Desventajas:** 
    - Mala eficiencia
    - Funciones, como usar la GPU dedicada, pueden estar detrás de pagos en VM managers
- **Recomendado para:** Gente que quiera probar la "experiencia Linux" sin comprometerse, y/o que no tengan espacio suficiente.
- **Cosas que preparar:**
    - Instalar [VirtualBox](https://www.virtualbox.org/) o similar
    - Descargarse la [ISO de Ubuntu](https://ubuntu.com/download/desktop)

Guía de cómo instalarlo en [`vm-install.md`](vm-install.md).


### Método 5: Disco externo
Puedes instalar Linux en un disco duro externo y conectarlo a tu PC cuando quieras usar Linux. Viene a ser lo mismo que [dual boot](#método-2-dual-boot).
- **Restricciones:** 
    - Tener un disco duro externo (vacío)
    - Recomendable tener un puerto USB 3.0 para tener velocidades decentes
- **Ventajas:** 
    - Todas las de tener un Dual Boot
    - No necesitas usar/expandir el almacenamiento interno de tu PC
- **Desventajas:** 
    - Las mismas de un Dual Boot
    - Tienes que cargar con el disco externo
- **Recomendado para:** Portátiles con poco almacenamiento, pero que quieran tener toda la experiencia Linux
- **Cosas que preparar:** 
    - Disco duro externo (preferible USB 3.0)  
      **IMPORTANTE:** Todos los datos del disco duro externo se borrarán. Estás avisado.
    - Un [live USB con Linux](#2-cómo-crear-un-live-usb-de-ubuntu).

**NOTA**: También se puede tener Windows en un disco externo...

Guía de cómo instalarlo en [`dualboot-external-install.md`](dualboot-external-install.md).


### Método 6: "Sólo la puntita"
Si quieres seguir el taller pero no quieres liarte a instalar nada (_cobarde_), un [live USB](#2-cómo-crear-un-live-usb-de-ubuntu) te permite correr Linux desde él mismo, sin necesidad de instalar ninguna cosa.



## 2. Cómo crear un Live USB de Ubuntu
Lo primero, necesitas un USB con al menos 8GB de almacenamiento.  
Sí, todo lo que haya ahí dentro va a desaparecer, así que estás avisado.

1. Descárgate la [ISO de Ubuntu](https://ubuntu.com/download/desktop).
2. Descarga [Balena Etcher](https://www.balena.io/etcher), puedes usar la versión portable (sin necesidad de instalar nada), o instalar la aplicación entera.
3. Inserta el USB
4. Corre Balena Etcher
5. Selecciona "Flash from file" y la ISO que te has descargado
6. Selecciona "Select target" y el USB
7. Haz click en "Flash"



## Ruegos y preguntas
Si tienes alguna duda, nos puedes escribir a info AT gul.uc3m.es, o un MD a nuestro Twitter, [@guluc3m](https://twitter.com/guluc3m).

## Transparencias
- [Mi primer Linux](https://cloud-gul.uc3m.es/s/HQseLfimS2THFgg) ([vídeo disponible](https://youtu.be/-8oo17P29VU?si=PSGMAl-zqWNDO_XA)) (2021)
- [Linux 404: Introducción a GNU/Linux](https://cloud-gul.uc3m.es/s/4qXKozr7DmDSZiN) (2022)
- [Linux 404: Cómo Instalar Linux](https://github.com/joseaverde/linux-install-party/blob/master/traspas.pdf) (2023/2024)
