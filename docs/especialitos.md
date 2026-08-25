# Linux en hardware especial

### Apple Macs
La instalación de Linux depende del modelo y, más importante, del microprocesador. En cualquier caso, debido a que _es un Mac_, sólo hay dos formas de ejecutar Linux: en _dual boot_ y en máquina virtual (VM).

!!! danger
    MacOS tiene la tendencia de formatear el disco a la hora de hacer una partición, **eliminando el sistema operativo y todos tus archivos de la faz de la tierra**. Es algo aleatorio y que te hará replantearte el volver a comprar un Mac, y la única forma de "protegerte" es **haciendo una copia de seguridad** si vas a hacer un _dual boot_.

    Te recomendamos usar [Time Machine](https://support.apple.com/es-es/104984), una herramienta del propio Apple.


#### Apple Silicon
Ordenadores con un procesador de la familia M (M1/M2/...) (2020 o posterior, dependiendo del modelo del dispositivo), los cuales están basados en la arquitectura [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family).

Las opciones son:

1. Dual boot (tener MacOS y Linux en el mismo ordenador) con [Ashahi Linux](https://asahilinux.org/).  
   [Ver guía](guías/dualboot-mac.md).
2. Correr una VM con una versión de Linux para ARM a través de [UTM](https://mac.getutm.app/).  
   [Ver guía](guías/vm-mac.md).
3. Usar una VM de [Orbstack](https://orbstack.dev/) emulando x86.


#### Intel
Ordenadores con procesador Intel (pre-2020), los cuales están basados en la arquitectura [AMD64](https://es.wikipedia.org/wiki/X86-64).

Las opciones son:

1. Dual boot (tener MacOS y Linux en el mismo ordenador).
    - Si es un ordenador sin [chip de seguridad T2](https://support.apple.com/es-es/103265) (pre-2018), no suele haber demasiados problemas al instalar, y los pasos generales para la instalación son fundamentalmente iguales que para cualquier otra máquina. Puedes ver los pasos en [este archivo](guías/dualboot-mac.md). Te recomendamos también la [siguiente guía](https://www.makeuseof.com/tag/install-linux-macbook-pro/).
    - Para ordenadores con chip T2 (2018-2019), lo más recomendable es usar [t2linux](https://t2linux.org/). Son parches específicos para múltiples distribuciones de Linux, ya que cosas como el Wi-Fi o el teclado y el _trackpad_ no suelen funcionar con una ISO normal debido a los _drivers_.
    ??? tip "Distribuciones sin t2linux"
        Si has instalado una distribución sin [t2linux](https://t2linux.org/), puedes encontrar _firmware_ ya compilado en Internet.

        Por ejemplo:

        - [Macbook Air 8](https://github.com/ztybigcat/brcm43xx)

2. Correr una VM como en cualquier otro ordenador. [Ver guía](guías/vm-win.md)

!!! info
    Para más información sobre _troubleshooting_ y resolución de problemas en portátiles Mac, ve a [Laptop/Apple - ArchWiki](https://wiki.archlinux.org/title/Laptop/Apple).


### Microsoft Surface
Dado que algunos de los drivers son privativos, para los casos de [_full install_](index.md#metodo-1-full-linux) o [_dual boot_](index.md#metodo-2-dual-boot) es recomendable instalar un kernel específico para Surface, como [linux-surface](https://github.com/linux-surface/linux-surface). Guía de instalación [aquí](https://github.com/linux-surface/linux-surface/wiki/Installation-and-Setup).

Si tienes un Surface con procesador ARM (Snapdragon)... lo siento. El soporte, aún con los parches del kernel de linux-surface, es bastante pobre. Te dejamos esta pequeña [guía con el estado en el Surface Laptop 7](https://github.com/bryce-hoehn/linux-surface-laptop-7) por si quieres pegarte, pero te recomendamos que optes por [WSL](index.md#metodo-3-windows-subsystem-for-linux-2-wsl2) o [máquina virtual](index.md#metodo-4-virtual-machine-vm).
