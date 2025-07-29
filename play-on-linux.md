# Guía de _gaming_ en Linux
A diferencia de lo que se podría suponer en principio, Linux ofrece una experiencia bastante buena en cuanto a los videojuegos. A pesar de todos los mitos, hoy en día, la gran mayoría de los juegos ofrecidos por plataformas como [Steam](https://store.steampowered.com/), [Epic Games](https://www.epicgames.com/), [GOG](https://www.gog.com), [EA](https://www.ea.com/), y los demás funcionan, y además, según _benchmarks_ y evidencias empíricas de varios miembros de la GUL, en muchos casos corren incluso mejor que en Windows.

Sin embargo, antes de hacer ningún cambio a tu PC gaming, es imprescindible que compruebes que todo lo que vayas a jugar y que no puedas vivir sin él esté soportado, especialmente juegos multijugador competitivos (los del _anticheat_ de kernel, os estoy mirando a vosotros), ya que muchos están completamente rotos en Linux. Para ello te dejamos los siguientes recursos:

- [Compatibilidad de los juegos de Steam con Linux (ProtonDB)](https://www.protondb.com/)
- [Compatibilidad de los anticheats y sus correspondientes juegos (Are we anticheat yet?)](https://areweanticheatyet.com/)
- [Instalador automático de juegos a través de Lutris](https://lutris.net/games)

> [!TIP]
> Si quieres tener una máquina exclusiva para jugar, y sin tener que configurar mucho, (e.g. un PC en el salón, o una _handheld_) te recomendamos [Bazzite](https://bazzite.gg/).  
> Es una _distro_ inmutable, lo cual quiere decir que está pensada para funcionar y que no se rompa nada, a cambio de tener limitaciones a la hora de modificar el sistema.
> Sin embargo, viene con todo lo que puedas necesitar para jugar a tus jueguitos, y con muy buena [documentación y guías](https://docs.bazzite.gg/).



## Preparación
Para obtener una experiencia _gaming_ semejante a la de Windows, lo único que hay que hacer es descargar unas aplicaciones que permiten instalar cualquier videojuego que puedas desear. Para los juegos de Steam, hay una versión nativa de la aplicación para las _distros_ de Linux más populares.  

Para [Epic Games](https://www.epicgames.com/) existe el [Heroic Games Launcher](https://heroicgameslauncher.com/), y para el resto de juegos nuestra recomendación es de instalar [Lutris](https://lutris.net/games). Lutris facilita la instalación de juegos no solo de otros _launcher_, sino tambíen emuladores, juegos que has obtenido perfectamente legalmente (_te vemos_), y juegos nativos de Linux, los que podrás acceder a todos desde una sola aplicación, incluyendo tu libreria de Steam. En este apartado te explicaremos como instalar cada uno de ellos.


### Instalación de Steam
Dependiendo de la plataforma en la que te encuentres, habrá un método de instalación u otro.
Toda la información se puede encontrar en la [guia oficial de Fedora](https://docs.fedoraproject.org/en-US/gaming/proton/).

#### Distribuciones basadas en Debian (Ubuntu, Mint, ...)
Puedes descargártelo directamente de APT:
```
sudo apt-get install steam
```

O descargar el [paquete `.deb`](https://cdn.fastly.steamstatic.com/client/installer/steam.deb) directamente de la pagina de Steam y hacer doble click sobre el (o `sudo dpkg -i steam.deb && sudo apt-get install -f`).

En algunas distribuciones, también estará disponible dentro de la aplicación de software (Ubuntu, Mint, ...).


#### Distribuciones basada en Arch (Manjaro, Endeavour, ...)
Dependiendo de la distribución que estés usando, `multilib` puede estar habilitado ya o no (el repositorio de paquetes de 32-bits, donde esta almacenado el paquete de Steam), en cualquier caso para comprobar que esté habilitado, hay que descomentar la linea del archivo `/etc/pacman.conf` donde aparezca:

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Y finalmente instalar el paquete usando:
```
sudo pacman -Syu steam
```

> [!TIP]
> Siempre antes de instalar algo está bien actualizar los paquetes del sistema, ya que los repositorios pueden o no estar actualizados o que surjan conflictos con otros paquetes.

> [!NOTE]
> Al instalar, es posible que os pidan elegir qué paquete del driver de [Vulkan](https://wiki.archlinux.org/title/Vulkan#Installation) instalar. En cualquier caso, para gráficas integradas de Intel o las nuevas Arc, elegir `vulkan-intel`. Para gráficas NVIDIA, `nvidia-utils`. Finalmente, para gráficas AMD, usar `vulkan-radeon`.

Toda la información se puede encontrar en la [documentación de ArchWiki](https://wiki.archlinux.org/title/Steam).


#### Distribuciones basadas en Red Hat (Fedora, RedStar, Nobara ...)
De acuerdo con la [documentación de Fedora](https://docs.fedoraproject.org/gaming/proton/), basta con habilitar el repositorio `rpmfusion Nonfree`:

```
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
sudo dnf config-manager --enable fedora-cisco-openh264 -y
```

E instalar desde DNF:
```
sudo dnf install steam
```

#### Configuración básica
Para habilitar el uso de Proton en juegos no verificados por Steam, ve a _Steam_ → _Settings_ → _Compatibility_ y habilita _Enable Steam Play for all other titles_. Lo recomendable es seleccionar la última versión estable (a la hora de escribir, esa es `Proton 9.0-4`). Las versiones `Proton-Hotfix` y `Proton-Experimental` son versiones _bleeding edge_ que puede que funcionen o que no.

De cualquier forma, puedes seleccionar la versión de Proton para cada juego, en los ajustes (ruedecita) → `Properties` → `Compatibility` → `Force the use of a specific Steam Play compatibility tool`.

<!-- TODO: #### Distribuciones basadas en Jurix (OpenSUSE, ...) -->


<!-- TODO: ### Instalación de Heroic Games Launcher -->


### Instalación de Lutris 
¿Pero si ya tengo Steam, para que quiero otra aplicación para jugar? Digamos que puedes jugar a juegos de Windows en Linux a través de Steam gracias a un componente llamado Wine, o como es la implementation específica de este para jugar, Proton. Al ser un componente a parte que no requiere de Steam ya que es open source, realmente puedes jugar a "cualquier cosa" que sea tenga un ejecutable (Los navegantes de los siete mares están incluidos).

En esta caso, Lutris existe como launcher de juegos universal, el cual admite juegos instalados de una gran variedad de tiendas y de emuladores de consolas (Ver sección de emulación), disponibles como "Ejecutores" dentro de la configuración.

Gracias a esto, y a una comunidad asombrosa, en la página de Lutris hay instrucciones para [instalar cualquier juego](https://lutris.net/games) que se te pueda venir a la cabeza. Estos son configuraciones programadas para instalar y parchear errores automáticamente.

Al igual que con Steam, cada distribución tiene su propio paquete y tienen métodos de instalación diferentes.

> [!NOTE]
> A excepción de algunos programas, los métodos de instalación son casi siempre los mismos, buscas lo que quieras descargar en internet, seguido de tu distribución, y normalmente será un comando que tendrás que ejecutar o un paquete que tienes que descomprimir / instalar.

#### Distribuciones basadas en Debian (Ubuntu, Mint, ...)
[Descargar](https://github.com/lutris/lutris/releases) el paquete `.deb` de la última versión de Lutris.

#### Distribuciones basada en Arch (Manjaro, Endeavour, ...)
```
sudo pacman -Syu lutris
```

#### Distribuciones basadas en Red Hat (Fedora, RedStar, Nobara ...)
```
sudo dnf install lutris
```


## Ajustes
Ante cualquier problema con el que puedas encontrar, [ArchWiki](https://wiki.archlinux.org/title/Main_page) es tu navaja suiza. Gracias a la gran cantidad de contribuidores han conseguido lograr una guía para todo lo que te pueda ocurrir. Es por ello que la gran mayoría de soluciones están presentes ahí.

Incluso si instalas juegos que según ProtonDB u otros recursos deberían funcionar bien, puedes llegar a tener alguna incompatiblidad o dependencia que falta. Estos problemas se pueden resolver de varias maneras.

Para juegos de Proton o Lutris, puedes probar versiones alternativas de Proton o Wine, como [Proton-GE](#proton-ge). Te recomendamos instalarlas a través de [ProtonUp-Qt](https://github.com/DavidoTek/ProtonUp-Qt) o [ProtonPlus](#protonplus).

> [!NOTE]
> "¿Para que me sirve a mi esto?", te preguntarás. Hay casos bastante puntuales donde un juego solo funciona en una versión especifica de proton o algún fork que no esté disponible a través de otros medios. Es por esto que a veces tener varias versiones instaladas es necesario.

### Proton-GE
[Proton-GE](https://github.com/GloriousEggroll/proton-ge-custom) es una versión de Proton alternativa con patches no oficiales los que a veces pueden ayudarte a correr un juego muy reciente o uno que acaba de ser actualizado.

Viene con varias ventajas que pueden mejorar tu experiencia dentro de Steam (fuera de Steam puedes instalar Wine-GE, aunque con Lutris y Heroic las ventajas están integradas en el launcher). Una de estas es el FSR1 (AMD FidelityFX Super Resolution 1) habilitado por defecto. Este filtro hace el juego parecer más nítido en el caso de que lo estes jugando con una resolución más baja que la de tu pantalla. Puedes modificar el valor de nitidez poniendo esto en los _Launch Parameters_ del juego en Steam:
```
WINE_FULLSCREEN_FSR_STRENGTH=valor
```
Dónde el valor está en el rango entre `0` y `5`, `0` siendo nitidez máxima.


### Gamescope
[Guía de ArchWiki para su instalación y uso](https://wiki.archlinux.org/title/Gamescope).
<!-- TODO: HDR, escalado, captura de cursor, ... -->


### Gamemode
[Gamemode](https://github.com/FeralInteractive/gamemode) deshabilita efectos del Desktop, cambia el estado del CPU, etc. para mejorar rendimiento mientras juegas.

<!--TODO: Documentarlo como usarlo-->


### Instalación de un kernel alternativo
Tranquilo, no vas a tener ni que tocar la BIOS, ni usar la terminal para modificar nada (bueno, hay que ejecutar un comando, qué te esperabas). El kernel es lo que se encuentra entre el sistema operativo y tu hardware, y éste es posible modificarlo para optimizarlo en ciertas tareas como puede ser si no en esta guía, para jugar.

Hay bastantes para [elegir](https://wiki.archlinux.org/title/Kernel), pero el que os recomendamos es el [Zen Kernel](https://github.com/zen-kernel/zen-kernel). Después de instalarlo, te aparecerán en GRUB nuevas opciones de arranque, así que en cualquier momento puedes volver a usar el _kernel_ por defecto por si en algún momento te llega a dar problemas.

> [!TIP]
> Para forzar a que aparezca GRUB en el arranque, presiona repetidamente la tecla `Esc`.


### Uso de mandos
Por defecto, en los ultimos años la compatibilidad con mandos en Linux se ha vuelto practicamente nativo, y solo con conectar el mando ya puedes ponerte a jugar directamente. Pero puede haber casos donde el mando no es directamente detectado por el sistema operativo o por Steam, por lo que guías con la [ArchWiki](https://wiki.archlinux.org/title/Gamepad) pueden ayudar a solucionar el problema bastante rápido.

Para probar que el mando está siendo detectado y no es problema del sistema operativo, existe [evtest](https://archlinux.org/packages/?name=evtest), el cual detecta todas las entradas de cualquier dispositivo.

#### Bluetooth
Para mandos de XBox (One S y posteriores), basta con instalar el driver [xpadneo](https://atar-axis.github.io/xpadneo/).

Para mandos de PlayStation (como el DualShock 4), el modulo de kernel necesario para que el mando sea detectado puede no está cargado automaticamente y, aunque éste aparezca conectado, puede no estar funcionando. Es necesario tener cargados los siguientes módulos:
```
sudo modprobe hid_sony
sudo modprobe joydev
```

Por otro lado, si quieres que, teniendo el bluetooth activado, se conecte el mando automaticamente pulsando el botón de play, deberás configurarlo desde [`bluetoothctl`](https://wiki.archlinux.org/title/Bluetooth), ejecutando los siguientes comandos:
```
$ bluetoothctl
```
```
agent on
default-agent
power on
discoverable on
pairable on
scan on
```

<!--## Grabación-->

<!--### OBS-->

<!--### obs-vkcapture-->

<!--### gstreamer-vaapi-->

<!--### H264/H265 vs AV1-->


## Emulación
No se lo contéis a Nintendo, pero si tu objetivo principal es emular juegos mas viejos o de otras consolas, Linux es la mejor opción ya que muchos emuladores se ejecutan nativamente en Linux y están específicamente optimizados para ello.

En el caso en el que quieras emular, pero no tengas las ROMs de tus juegos comprados legalmente y de los cuales también tienes la consola, en [Vimm's Lair](https://vimm.net/) podrás encontrarlas para consolas de hace 4 generaciones, subidas y moderadas por la comunidad. Suponemos que no hace falta comentar que todos los juegos de Mario están quitados. Otra alternativa es [r/ROMs Megathread](https://r-roms.github.io/), la cual contiene los enlaces más actualizados a todas las ROMs que puedas querer.

En esta guía vamos a cubrir dos métodos para emular en Linux, de los cuales ambos tienen cierto público objetivo.

### Standalone
Si tu objetivo es emular un par de juegos, tocarlos a lo mejor una vez cada dos meses por recordar la nostalgia, o si quieres tenerlo ahí en caso de que hayas perdido la ultima ranked del LoL y te den ganas de desinstalarlo, lo mejor será descargar directamente el emulador para la consola que quieras jugar. Este es objetivamente el más "straightforward" y fácil de usar ya que no hay que toquetear demasiado (Plug and Play).

A continuación están los emuladores que siguen siendo mantenidos y que miembros de GUL dan fe que funcionan:
- [Wii / GameCube - Dolphin](https://es.dolphin-emu.org/?cr=es)
- [WiiU - Cemu](https://cemu.info/)
- [Switch - Suyu](https://suyu.dev/)
- [GBA - VisualBoy Advance](https://visualboyadvance.org/)
- [nDS - MelonDS](https://melonds.kuribo64.net/)
- [3DS - Azahar](https://azahar-emu.org/)
- [PS1 - Duckstation](https://www.duckstation.org/)
- [PS3 - RCPS3](https://rpcs3.net/)


### Gestores y _frontends_
En el caso de que tengas una librería extensa de emuladores y ROMs completamente legales, puede merecer la pena usar alguna aplicación para gestionar tus configuraciones y juegos.

#### EmuDeck
[EmuDeck](https://www.emudeck.com/) es un gestor originariamente concebido para simplificar el uso de emuladores en la SteamDeck, pero funciona perfectamente en cualquier _Desktop Enviroment_ de Linux. Tiene la ventaja de ser fácil de usar y de configurar automáticamente los emuladores, además de añadir los juegos con sus carátulas correspondientes a _frontends_ como [Steam](https://store.steampowered.com/), [EmulationStation](https://emulationstation.org/), o [Pegasus](https://pegasus-frontend.org/).

#### RetroArch
[RetroArch](https://www.retroarch.com/) es un _frontend_ para "núcleos" creados por desarrolladores vinculados al proyecto, que actúan como emuladores y aunque la curva de aprendizaje sea un poco alta, se convierte en una herramienta bastante útil.

Este además de tener compatibilidad con cualquier mando que te puedas imaginar, tiene la opción de usar shaders personalizados, multiples guardados de partidas, interfaz customizable, núcleos actualizados, y una lista más de opciones que trae consigo.


## Lossless Scaling Frame Generation
Actualmente hay una herramienta llamada [lsfg-vk](https://github.com/PancakeTAS/lsfg-vk) en desarrollo, que permite usar [Lossless Scaling](https://losslessscaling.com) (generación de fotogramas) en juegos nativos de Vulkan, y los que usan DXVK. Esta herramienta funciona oficialmente con cualquier juego de 64 bits, y no oficialmente, a través de WOW64, en juegos de 32 bits (lo que se puede activar aplicando la variable de entorno `PROTON_USE_WOW64=1` en versiones _bleeding edge_ de Proton, Proton-GE y Wine-GE).

Esta herramienta permite correr videojuegos con _framerates_ limitados a más FPS de los que está diseñado el juego (o los que logra renderizar tu GPU), sin tener que modificar archivos, ni romper la lógica del juego, aunque con latencia de entrada añadida.
> [!NOTE]
> ¡Funciona incluso en los emuladores y aplicaciones que no son juegos, como el reproductor de videos MPV!

Para instalarla, se puede seguir o la [guía de instalación del repositorio oficial](https://github.com/PancakeTAS/lsfg-vk/wiki), o instalando el [paquete de AUR](https://aur.archlinux.org/packages/lsfg-vk-git) (en el caso de usar Arch, _btw_).
