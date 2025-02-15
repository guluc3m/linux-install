<!--
# Linux Install Party

## Cosas a tener en cuenta ANTES DE ASISTIR AL TALLER
Uno de los objetivos de éste taller es instalar Linux en vuestros ordenadores.  
Para agilizar éste proceso, es recomendable que leáis la siguiente información:  

Hay diversas formas de "instalar" Linux. Entendemos que no todos tenéis las mismas circunstancias, así que recomendamos que tengáis en cuenta todas y elijáis una antes de venir, trayendo el material correspondiente dependiendo del método.
-->


# Guía del GUL para la instalación de Linux

## Prefacio

### Apple Macs
La instalación de Linux depende del modelo y, más importante, del microprocesador. En cualquier caso, debido a que _es un Mac_, sólo hay dos formas de ejecutar Linux: en dual boot y en VM.

> [!WARNING]
> MacOS tiene la tendencia de formatear el disco a la hora de hacer una partición, **eliminando el sistema operativo y todos tus archivos de la faz de la tierra**. Es algo aleatorio y que te hará replantearte el volver a comprar un Mac, y la única forma de "protegerte" es **haciendo una copia de seguridad** si vas a hacer un dual boot.
> 
> Te recomendamos usar [Time Machine](https://support.apple.com/es-es/104984), una herramienta del propio Apple.


#### Apple Silicon
Ordenadores con un procesador de la familia M (M1/M2/...) (2020 o posterior, dependiendo del modelo del dispositivo), los cuales están basados en la arquitectura [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family).

Las opciones son:
1. Dual boot (tener MacOS y Linux en el mismo ordenador) con [Ashahi Linux](https://asahilinux.org/). Guía en [`dualboot-mac-install.md`](dualboot-mac-install.md)
2. Correr una VM con una versión de Linux para ARM a través de [UTM](https://mac.getutm.app/). Guía en [`vm-install-mac.md`](vm-install-mac.md)


#### Intel
Ordenadores con procesador Intel (pre-2020), los cuales están basados en la arquitectura [AMD64](https://es.wikipedia.org/wiki/X86-64).

Las opciones son:
1. Dual boot (tener MacOS y Linux en el mismo ordenador).
    - Si es un ordenador sin [chip de seguridad T2](https://support.apple.com/es-es/103265) (pre-2018), no suele haber demasiados problemas al instalar, y los pasos generales para la instalación son fundamentalmente iguales que para cualquier otra máquina. Te recomendamos la [siguiente guía](https://www.makeuseof.com/tag/install-linux-macbook-pro/).
    - Para ordenadores con chip T2 (2018-2019), lo más recomendable es usar [t2linux](https://t2linux.org/). Son parches específicos para múltiples distribuciones de Linux, ya que cosas como el Wi-Fi o el teclado y el trackpad no suelen funcionar con una ISO normal debido a los drivers.

>  [!TIP]
> Si has instalado una distribución sin [t2linux](https://t2linux.org/), puedes encontrar _firmware_ ya compilado en Internet.
> Por ejemplo:
> - [Macbook Air 8](https://github.com/ztybigcat/brcm43xx)

2. Correr una VM como en cualquier otro ordenador. Guía en [`vm-install.md`](vm-install.md)


> [!NOTE]
> Para más información sobre _troubleshooting_ y resolución de problemas en portátiles Mac, ve a [Laptop/Apple - ArchWiki](https://wiki.archlinux.org/title/Laptop/Apple).

> [!TIP]
> Si tienes problemas para bootear rEFInd en Mac, quizás te pueda ayudar lo siguiente: [rEFInd bootloader doesn't launch on start](https://apple.stackexchange.com/questions/446575/refind-bootloader-doesnt-launch-on-start).


### Microsoft Surface
Dado que algunos de los drivers son privativos, para los casos de full install o dual boot es recomendable instalar un kernel específico para Surface, como [linux-surface](https://github.com/linux-surface/linux-surface). Guía de instalación [aquí](https://github.com/linux-surface/linux-surface/wiki/Installation-and-Setup).



## Distribuciones
Una distribución, o _distro_, es una serie de aplicaciones y herramientas que se empaquetan encima del [kernel de Linux](https://github.com/torvalds/linux) para tener un Sistema Operativo completo.

Hay muchísimas, y puedes verlas todas en [DistroWatch.com](https://distrowatch.com/), pero aquí te dejamos nuestras recomendaciones:
- Si eres principiante, te recomendamos [Ubuntu](https://ubuntu.com/desktop) o [Linux Mint](https://linuxmint.com/), basadas en [Debian](https://www.debian.org/), ya que son estables* y fáciles de usar _out of the box_.
- Si quieres paquetes algo más actualizados, te recomendamos [Fedora](https://fedoraproject.org/workstation).
- Si te gusta trastear y estar a la última, échale un vistazo a [Manjaro](https://manjaro.org/products/download/x86) o [EndevourOS](https://endeavouros.com/), ambas basadas en [Arch Linux](https://wiki.archlinux.org/title/Installation_guide).


> [!TIP]
> Es recomendable, especialmente antes de instalar Linux en físico (_full install_ / _dual boot_), comprobar la compatibilidad de tu ordenador con la distro específica.
> - Si es un portátil relativamente nuevo, es posible que algunos drivers todavía no estén en los repositorios (tocará añadirlos manualmente, ver[Solucionar Drivers Wi-Fi](common.md#solucionar-drivers-wi-fi)).
> - Si es un portátil relativamente antiguo, es posible que las _distros_ más _bleeding edge_ te den problemas.
> 
> Buscando en [Google](https://google.com) o preguntándole [al patito](https://duckduckgo.com/) se suelen encontrar respuestas.


<!--
## Formas de instalar Linux

Hay diversas formas de "instalar" Linux. Entendemos que no todos tenéis las mismas circunstancias, así que recomendamos que tengáis en cuenta todas y elijáis la que más os convenga.
-->


### Método 1: Full Linux
Este método consiste en decir [_fuck Microsoft_](https://www.youtube.com/watch?v=2zpCOYkdvTQ), borrar Windows, y correr sólo Linux.  
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
    - Un [live USB con Linux](common.md#cómo-crear-un-liveusb) .

Guía de como instalarlo en [`full-install.md`](full-install.md)

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
    - Un [live USB con Linux](common.md#cómo-crear-un-liveusb) .

Guía de cómo instalarlo en [`dualboot-install.md`](dualboot-install.md).


### Método 3: Windows Subsystem for Linux 2 (WSL2)
WSL te permite "correr Linux" dentro de Windows, pero sólo mediante una terminal, con un buen nivel de compatibilidad.
- **Restricciones:** Windows 10/11.
- **Ventajas:**
    - Fácil y rápido de instalar
    - Ligero
    - Fácil acceso a los archivos
    - Puedes lanzar aplicaciones GUI, incluso desde el propio Windows
    - Soporte en bastantes aplicaciones: [Vs Code](https://code.visualstudio.com/docs/remote/wsl), IDEs de Jetbrains ([CLion](https://www.jetbrains.com/help/clion/how-to-use-wsl-development-environment-in-product.html), [PyCharm](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html), etc.), [CUDA](https://docs.nvidia.com/cuda/wsl-user-guide/index.html), y muchas más.
- **Desventajas:**
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
    - Un [live USB con Linux](common.md#cómo-crear-un-liveusb).

**NOTA**: También se puede tener Windows en un disco externo...

Guía de cómo instalarlo en [`dualboot-external-install.md`](dualboot-external-install.md).


### Método 6: "Sólo la puntita"
Si quieres seguir el taller pero no quieres liarte a instalar nada (_cobarde_), un [live USB](common.md#cómo-crear-un-liveusb)  te permite correr Linux desde él mismo, sin necesidad de instalar ninguna cosa.



## Ruegos y preguntas
Si tienes alguna duda, nos puedes escribir a info AT gul.uc3m.es, o un MD a nuestro Twitter, [@guluc3m](https://twitter.com/guluc3m).


## Transparencias de _install partys_ anteriores
- [Mi primer Linux](https://cloud-gul.uc3m.es/s/HQseLfimS2THFgg) ([vídeo disponible](https://youtu.be/-8oo17P29VU?si=PSGMAl-zqWNDO_XA)) (2021)
- [Linux 404: Introducción a GNU/Linux](https://cloud-gul.uc3m.es/s/4qXKozr7DmDSZiN) (2022)
- [Linux 404: Cómo Instalar Linux](https://github.com/joseaverde/linux-install-party/blob/master/traspas.pdf) (2023/2024)
