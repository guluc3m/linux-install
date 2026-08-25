# Introducción

!!! info
    Si vas a instalar Linux en un [Apple Mac](https://www.apple.com/mac/) o un [Microsoft Surface](https://www.microsoft.com/surface), lee antes la sección [Linux en Hardware Especial](especialitos.md).


## Distribuciones
Una distribución, o _distro_, es una serie de aplicaciones y herramientas que se empaquetan encima del [kernel de Linux](https://github.com/torvalds/linux) para tener un Sistema Operativo completo.

!!! tip
    Es recomendable, especialmente antes de instalar Linux en físico (_full install_ / _dual boot_), comprobar la compatibilidad de tu ordenador con la distro específica.

    - Si es un portátil relativamente nuevo, es posible que algunos drivers todavía no estén en los repositorios (ver [Solucionar Drivers Wi-Fi](troubleshoot.md#solucionar-drivers-wi-fi)).
    - Si es un portátil relativamente antiguo, es posible que las _distros_ más _bleeding edge_ te den problemas.
    
    Buscando en [Google](https://google.com) o preguntándole [al patito](https://duckduckgo.com/) se suelen encontrar respuestas.

Hay muchísimas, y puedes verlas todas en [DistroWatch.com](https://distrowatch.com/), pero aquí te dejamos nuestras recomendaciones:

- Si eres principiante, te recomendamos [Linux Mint](https://linuxmint.com/) o [Ubuntu](https://ubuntu.com/desktop), basadas en [Debian](https://www.debian.org/), ya que son "estables" y fáciles de usar _out of the box_.
- Si quieres paquetes algo más actualizados, te recomendamos [Fedora](https://fedoraproject.org/workstation).
- Si te gusta trastear y estar a la última, échale un vistazo a [Manjaro](https://manjaro.org/products/download/x86) o [EndevourOS](https://endeavouros.com/), ambas basadas en [Arch Linux](https://wiki.archlinux.org/title/Installation_guide). Si te interesa esta última pero no sabes por donde empezar, consulta esta [guía](guías/arch.md).


### Distribuciones especializadas
Las _distros_ mencionadas anteriormente se consideran "generalistas", es decir, que funcionan para la mayoría de la gente en la mayoría de situaciones, y son un buen punto de partida. Sin embargo, si quieres algo más especial y/o te apetece trastear un poco, te dejamos otras opciones:

- Para jugones, recomendamos [Nobara Linux](https://nobaraproject.org/).
  - Si quieres tener una máquina exclusiva para jugar, y sin tener que configurar mucho, (e.g. un PC en el salón, o una _handheld_) te recomendamos [Bazzite](https://bazzite.gg/).  
  Es una _distro_ inmutable, lo cual quiere decir que está pensada para funcionar y que no se rompa nada, a cambio de tener limitaciones a la hora de modificar el sistema.  
  Sin embargo, viene con todo lo que puedas necesitar para jugar a tus jueguitos, y con muy buena [documentación y guías](https://docs.bazzite.gg/).
- Para gente (_otakus_, furros, _femboys_, programadores de [Rust](https://www.rust-lang.org/)) que quiera probar la verdadera experiencia Linux moderna, con [_tiling window manager_](https://en.wikipedia.org/wiki/Tiling_window_manager) incluído, pero que no quieran empezar de cero, recomendamos [Omarchy](https://omarchy.org/). Es [Arch Linux](https://wiki.archlinux.org/) con [Hyprland](https://hypr.land/) y [Quickshell](https://quickshell.org/), con una configuración excelente.
    - Otra altenativa interesante es instalar [Noctalia](https://docs.noctalia.dev/) encima de cualquier distro.
- Si tienes un ordenador moderno y quieres exprimirlo al máximo, échale un vistazo a [CachyOS](https://cachyos.org/).

!!! info
    La mayoría de estas _distros_ simplemente añaden paquetes, configuraciones, y/o kernels ya preinstalados, lo cual hace una gran experiencia _out of the box_.  
    Sin embargo, puedes coger cualquier distribución e instalar estos componentes manualmente. Eso es lo bonito de Linux.


## Formas de instalar Linux

Hay diversas formas de "instalar" Linux. Entendemos que no todos tenéis las mismas circunstancias, así que recomendamos que tengáis en cuenta todas y elijáis la que más os convenga.


### Método 1: Full Linux
Este método consiste en decir [_fuck Microsoft_](https://www.youtube.com/watch?v=2zpCOYkdvTQ), borrar Windows, y correr sólo Linux.  

- **Restricciones:** Ninguna.  
Bueno sí, un ordenador con menos de 20 años.
- **Ventajas:** Todas las ventajas de Linux, sin los posibles problemas derivados de tener _dual boot_.
- **Desventajas:** Tu ordenador no va a tener Windows.  
Espera, ¿ese es un problema? Si tienes que usar Office, Adobe Creative Cloud, o algún programa o juego específico de Windows (y [Wine](https://www.winehq.org/) o [Proton](https://github.com/ValveSoftware/Proton) no te puede ayudar), sí.
- **Recomendado para:**
    - Linuxeros (frikis)
    - Un segundo ordenador portátil que uses para la uni
    - Tu tía la del pueblo que sólo usa Internet Explorer
- **Cosas que preparar:**
    - Copia de seguridad de tus archivos (fotos, fanfics, etc.)
    - Un [Live USB con Linux](liveusb.md#como-crear-un-liveusb).

Guía de como instalarlo en [Full Install](guías/full.md).

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
    - Apple _fanboys_ que quieran seguir usando su macbook de 2014 que Apple ya no actualiza
- **Cosas que preparar:**
    - Copia de seguridad de tus archivos (fotos, fanfics, etc.)
    - Un [Live USB con Linux](liveusb.md#como-crear-un-liveusb).

[Ver guía](guías/dualboot-win.md).


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

[Ver guía](guías/wsl.md).


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


!!! note
    También puedes [correr Windows en una VM](post-install/windows.md#usando-una-maquina-virtual).

    Esto es lo recomendable si tienes un ordenador lo suficientemente potente y sólo necesitas hacer unas pocas cosas en Windows.

[Ver guía](guías/vm-win.md).


### Método 5: Disco externo
Puedes instalar Linux en un disco duro externo y conectarlo a tu PC cuando quieras usar Linux. Viene a ser lo mismo que [_dual boot_](#metodo-2-dual-boot).

- **Restricciones:**
    - Tener un disco duro externo (vacío)
    - Recomendable tener un puerto USB 3.0 para tener velocidades decentes
- **Ventajas:**
    - Todas las de tener un _dual boot_
    - No necesitas usar/expandir el almacenamiento interno de tu PC
- **Desventajas:**
    - Las mismas de un _dual boot_
    - Tienes que cargar con el disco externo
- **Recomendado para:** Portátiles con poco almacenamiento, pero que quieran tener toda la experiencia Linux
- **Cosas que preparar:**
    - Disco duro externo (preferible USB 3.0)  
      **IMPORTANTE:** Todos los datos del disco duro externo se borrarán. Estás avisado.
    - Un [Live USB con Linux](liveusb.md#como-crear-un-liveusb).

!!! note
    También se puede tener Windows en un disco externo, lo cual puede dar hasta menos problemas.

[Ver guía](guías/dualboot-external.md).


### Método 6: "Sólo la puntita"
Si quieres seguir el taller pero no quieres liarte a instalar nada (_cobarde_), un [Live USB con Linux](liveusb.md#como-crear-un-liveusb) te permite correr Linux desde él mismo, sin necesidad de instalar ninguna cosa.



## Más información
Si tienes alguna duda, nos puedes escribir a info AT gul.uc3m.es, o un MD a nuestro Twitter, [@guluc3m](https://twitter.com/guluc3m).

También échale un vistazo a nuestra sección [post-install](post-install/index.md) y nuestra [guía de juegos en Linux](post-install/play-on-linux.md).


### Transparencias de _install partys_ anteriores
- [Mi primer Linux](https://cloud-gul.uc3m.es/s/HQseLfimS2THFgg) ([vídeo disponible](https://youtu.be/-8oo17P29VU?si=PSGMAl-zqWNDO_XA)) (2021)
- [Linux 404: Introducción a GNU/Linux](https://cloud-gul.uc3m.es/s/4qXKozr7DmDSZiN) (2022)
- [Linux 404: Cómo Instalar Linux](https://github.com/joseaverde/linux-install-party/blob/master/traspas.pdf) (2023/2024)

