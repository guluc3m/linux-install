A diferencia de lo que se podría suponer en principio, Linux ofrece una experiencia bastante buena en cuanto a los videojuegos. A pesar de todos los mitos, hoy en día, la gran Mayoría de los juegos ofrecidos por plataformas como Steam, Epic Games, GOG, EA, y los demás funcionan, y además, según benchmarks y evidencias empíricas de varios miembros de la GUL, en muchos casos corren incluso mejor que en Windows. 

> Sin embargo, antes de hacer ningún cambio a tu PC gaming, es imprescindible que compruebes que todo lo que vayas a jugar y que no puedas vivir sin él esté soportado, especialmente juegos multijugador competitivos (Los del anticheat de kernel, a vosotros os estoy mirando), ya que muchos están completamente rotos en Linux.

> [Compatibilidad de los juegos de Steam con Linux (ProtonDB)](https://www.protondb.com/)

> [Compatibilidad de los anticheats y sus correspondientes juegos (Are we anticheat yet?)](https://areweanticheatyet.com/)

> [Instalador automático de juegos a través de Lutris](https://lutris.net/games)


# Preparación
Para obtener una experiencia gaming semejante a la de Windows, lo único que hay que hacer es descargar unas aplicaciones que permiten instalar cualquier videojuego que puedas desear. Para los juegos de Steam, hay una versión nativa de la aplicación para todos los distros de Linux más populares.  

Para Epic Games existe el Heroic Games Launcher, y para el resto de juegos nuestra recomendación es de instalar Lutris. Lutris facilita la instalación de juegos no solo de otros launcher, sino tambíen emuladores, juegos que has obtenido perfectamente legalmente (te vemos), y juegos nativos de Linux, los que podrás acceder a todos desde una sola aplicación, incluyendo tu libreria de Steam. En este apartado te explicaremos como instalar cada uno de ellos.


## Instalación de Steam
Dependiendo de la plataforma en la que te encuentres, habrá un método de instalación u otro.


### Distribuciones basadas en Debian (Ubuntu, Mint, ...)
En la terminal ejecutar:

```
sudo apt-get install steam
```

O [descargar](https://cdn.fastly.steamstatic.com/client/installer/steam.deb) directamente el paquete .deb de la pagina de Steam y hacer doble click sobre el.

En algunas distribuciones, también estará disponible dentro de la aplicación de software (Ubuntu, Mint, ...).


### Distribuciones basada en Arch (Manjaro, Endeavour, ...)
Toda la información se puede encontrar en la [documentación de ArchWiki](https://wiki.archlinux.org/title/Steam)

Dependiendo de la distribución que estés usando, `multilib` puede estar habilitado ya o no (el repositorio de paquetes de 32-bits, donde esta almacenado el paquete de Steam), en cualquier caso para comprobar que esté habilitado, hay que des-comentar la linea del archivo `/etc/pacman.conf` donde aparezca:

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


### Distribuciones basadas en Red Hat (Fedora, RedStar, Nobara ...)
Toda la información se puede encontrar en la [guia oficial de Fedora](https://docs.fedoraproject.org/en-US/gaming/proton/)


### Distribuciones basadas en Jurix (OpenSUSE, ...)



# Ajustes

Ante cualquier problema con el que puedas encontrar, [ArchWiki](https://wiki.archlinux.org/title/Main_page) es tu navaja suiza. Gracias a la gran cantidad de contribuidores han conseguido lograr una guía para todo lo que te pueda ocurrir. Es por ello que la gran mayoría de soluciones están presentes ahí.

Incluso si instalas juegos que según ProtonDB u otros recursos deberían funcionar bien, puedes llegar a tener alguna incompatiblidad o dependencia que falta. Estos problemas se pueden resolver de varias maneras.
Para juegos de Proton o Lutris, puedes probar otra versión de Proton o Wine. Algunos juegos pueden jugar mal con el Wine de tu sistema, así que puedes instalar otras versiones a través de ProtonUp-Qt o ProtonPlus. Estas aplicaciones te permiten también descargar Proton-GE, que es una versión de Proton alternativa con patches no oficiales los que a veces pueden ayudarte a correr un juego muy reciente o uno que acaba de ser actualizado. 


## Instalación de ProtonUp-Qt
[Repositorio del proyecto](https://github.com/DavidoTek/ProtonUp-Qt)


## Instalación de ProtonPlus
[Repositorio del proyecto](https://github.com/Vysp3r/ProtonPlus)

(En Arch Proton-GE se puede instalar desde el paquete de AUR proton-ge-custom o proton-ge-custom-bin)

Proton-GE viene con varias ventajas que pueden mejorar tu experiencia dentro de Steam (fuera de Steam puedes instalar Wine-GE, aunque con Lutris y Heroic las ventajas están integradas en el launcher). Una de estas es el FSR1 (AMD FidelityFX Super Resolution 1) habilitado por defecto. Este filtro hace el juego parecer más nítido en el caso de que lo estes jugando con una resolución más baja que la de tu pantalla. Puedes modificar el valor de nitidez poniendo esto en los "Launch Parameters" del juego en Steam:
```
WINE_FULLSCREEN_FSR_STRENGTH=valor
```
Dónde el valor está en el rango entre 0 y 5, 0 siendo nitidez máxima.


## Instalación de Gamescope
[Guía de ArchWiki para su instalación y uso](https://wiki.archlinux.org/title/Gamescope)
HDR, escalado, captura de cursor, ...


## Instalación de Gamemode
[Repositorio del proyecto](https://github.com/FeralInteractive/gamemode)
Deshabilita efectos del Desktop, cambia el estado del CPU, y etc para mejorar rendimiento


## Instalación de un kernel alternativo
Tranquilo, no vas a tener ni que tocar la bios, ni usar la terminal para modificar nada (Bueno, hay que ejecutar un comando, que te esperabas). El kernel es lo que se encuentra entre el sistema operativo y tu hardware, y este es posible modificarlo para optimizarlo en ciertas tareas como puede ser si no en esta guía, para jugar.
Hay bastantes para [elegir](https://wiki.archlinux.org/title/Kernel), pero el que os recomendamos el el [Zen Kernel](https://github.com/zen-kernel/zen-kernel). Después de instalarlo, te aparecerán en GRUB nuevas opciones de arranque, así que en cualquier momento puedes volver a usar el kernel default por si en algún momento te llega a dar problemas. 


# Grabación

## OBS

## obs-vkcapture

## gstreamer-vaapi

## H264/H265 vs AV1
