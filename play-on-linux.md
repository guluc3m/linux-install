> Hay problemas de compatibilidad en juegos con un alto numero de jugadores que están completamente rotos en Linux. Antes de hacer ningún cambio es imprescindible que compruebes que todo lo que vayas a jugar y que no puedas vivir sin el esté soportado, especialmente juegos multijugador competitivos (Los del anticheat de kernel, a vosotros os estoy mirando).

> [Compatibilidad de los juegos de Steam con Linux (ProtonDB)](https://www.protondb.com/)

> [Compatibilidad de los anticheats y sus correspondientes juegos (Are we anticheat yet?)](https://areweanticheatyet.com/)

> [Instalador automático de juegos a través de Lutris](https://lutris.net/games)

Ante cualquier problema con el que puedas encontrar, [ArchWiki](https://wiki.archlinux.org/title/Main_page) es tu navaja suiza. Gracias a la gran cantidad de contribuidores han conseguido lograr una guía para todo lo que te pueda ocurrir. Es por ello que la gran mayoría de soluciones están presentes ahí.
# Instalación de Steam
Dependiendo de la plataforma en la que te encuentres, habrá un método de instalación u otro.

## Distribuciones basadas en Debian (Ubuntu, Mint, ...)
En la terminal ejecutar:

```
sudo apt-get install steam
```

O [descargar](https://cdn.fastly.steamstatic.com/client/installer/steam.deb) directamente el paquete .deb de la pagina de Steam y hacer doble click sobre el.

## Distribuciones basada en Arch (Manjaro, Endeavour, ...)
Toda la información se puede encontrar en la [documentación de ArchWiki](https://wiki.archlinux.org/title/Steam)

Dependiendo de la distribución que estés usando, `multilib` puede estar habilitado ya o no (el repositorio donde esta almacenado el paquete de Steam), en cualquier caso para comprobar que esté habilitado, hay que des-comentar la linea del archivo `/etc/pacman.conf` donde aparezca:

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Y finalmente instalar el paquete usando (siempre antes de instalar algo está bien actualizar los paquetes del sistema, ya que los repositorios pueden o no estar actualizados o que surjan conflictos con otros paquetes):

```
sudo pacman -Syu
sudo pacman -S steam
```

> Al instalar, es posible que os pidan elegir que paquete del driver de [Vulkan](https://wiki.archlinux.org/title/Vulkan#Installation) instalar. En cualquier caso, para gráficas integradas de Intel o las nuevas Arc, elegir `vulkan-intel`. Para gráficas NVIDIA, `nvidia-utils`. Finalmente, para gráficas AMD, usar `vulkan-radeon`.

## Distribuciones basadas en Red Hat (Fedora, RedStar, Nobara ...)
Toda la información se puede encontrar en la [guia oficial de Fedora](https://docs.fedoraproject.org/en-US/gaming/proton/)


## Distribuciones basadas en Jurix (OpenSUSE, ...)


# Instalación de ProtonUp-Qt
[Repositorio del proyecto](https://github.com/DavidoTek/ProtonUp-Qt)

# Instalación de Gamescope
[Guía de ArchWiki para su instalación y uso](https://wiki.archlinux.org/title/Gamescope)
HDR, escalado, captura de cursor, ...
# Instalación de Gamemode
[Repositorio del proyecto](https://github.com/FeralInteractive/gamemode)

# Instalación de un kernel alternativo
Tranquilo, no vas a tener ni que tocar la bios, ni usar la terminal para modificar nada (Bueno, hay que ejecutar un comando, que te esperabas). El kernel es lo que se encuentra entre el sistema operativo y tu hardware, y este es posible modificarlo para optimizarlo en ciertas tareas como puede ser si no en esta guía, para jugar.
Hay bastantes para [elegir](https://wiki.archlinux.org/title/Kernel), pero el que os recomendamos el el [Zen Kernel](https://github.com/zen-kernel/zen-kernel). Después de instalarlo, te aparecerán en GRUB nuevas opciones de arranque, así que en cualquier momento puedes volver a usar el kernel default por si en algún momento te llega a dar problemas. 
