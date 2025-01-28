# Instalación de Linux con MacOS en dualboot (Para Mac con procesador M1/M2 y variantes unicamente)

En este tutorial vamos a explicar cómo instalar Linux junto a MacOS. Este tutorial está pensado para instalar ambos sistemas operativos en el disco duro interno / los discos duros internos que tengas en el ordenador. 

Es importante tener en cuenta que desde que Apple utiliza procesadores ARM, la compatibilidad con Linux es limitada y el arrancar desde un disco duro externo no es posible. Por lo que si tienes un Mac con procesador ARM y quieres instalar Linux nativamente, no hay muchas opciones.

## Requisitos
 * Mac con Apple Silicon: serie M1 o M2 (M3 no tiene soporte).
 * Al menos 55GB de espacio libre en el disco duro interno.
 * Conexión a internet.


## 1. Crear la partición y descargar el instalador
Para instalar Linux en un Mac con procesador ARM, necesitamos crear una partición en el disco duro interno. Para ello, NO vamos a utilizar la herramienta de discos de MacOS, sino que utilizaremos la herramienta de instalación que nos ofrece Asahi Linux.

## 2. Descargar Asahi Linux
Abre una terminal y ejecuta el siguiente comando:
```bash
curl https://alx.sh | sh
```
Con este comando descargaremos la herramienta de instalación de Asahi Linux. Ahora solo hay que seguir las instrucciones que aparecen en la terminal. Nos pedirá acceso root para poder crear las particiones e intalar en esa partición Linux.

## 3. Configuración de la partición
Lo primero que nos pedirá es que queremos hacer. En este caso, queremos redimensionar la partición que tiene MacOS para dejar espacio para Linux. Para ello, presionamos la tecla r y luego la tecla Enter. A continuaicón, nos pedirá cuánto espacio queremos dejar para Linux. Tenemos varias opciones:
- Si queremos dejar 55GB, escribimos 55G y presionamos Enter.
- Si queremos dejar un % del disco para mac, pondremos el porcentaje con el símbolo de % y presionamos `Enter`. Cabe recalcar que 100-<porcenaje_introducido> es lo que se dejará para Linux.
- "min" + `Enter` -> Reduce al máximo la partición de MacOS.

Cuando hayamos seleccionado una opción nos pedirá confirmación. Para confirmar, como ocurre muchas veces en la terminal, escribimos una "y" y presionamos Enter. 
Es completamente normal que este proceso tarde un poco, ya que está redimensionando la partición de MacOS. Y se puede quedar congelado en el proceso, pero no te preocupes, déjalo un rato. 


Una vez tengamos la partición hecha, nos preguntará que queremos hacer, como en la primera vez que ejecutamos el programa. Pero esta vez, seleccionaremos "f: Instalar un Sistema Operativo en el espacio libre" presionando la tecla `f`. 

Ahora es el momento de elegir el "flavor" que queremos instalar. Los disponibles ahora mismo son:
- Fedora Asahi Remix 40 with [KDE Plasma](https://kde.org)
- Fedora Asahi Remix 40 with [GNOME](https://www.gnome.org)
- Fedora Asahi Remix 40 Server
- Fedora Asahi Remix 40 Minimal
- UEFI environment only (m1n1 + U-Boot + ESP)

Para este tutorial, seleccionaremos la primera o la segunda opción. La única diferencia entre ellas es el entorno de escritorio que traen por defecto.

Cuando esté elegido el sistema, nos pedirá cuanto espacio se debería utilizar para el sistema. Aquí es recomendable poner `max` para que utilice todo el espacio disponible.
Por último nos pedirá un Nombre, por ejemplo, podemos poner Linux.

Cuando le demos a Enter, empezará a descargar las imágenes, configurar la partición de arranque y a instalar el sistema. Este proceso puede tardar un rato, así que ten paciencia.

Cuando termine, nos pedirá apagar el sistema. Para ello, presionamos Enter. Para volver a encenderlo, en vez de precionar y solar una vez la tecla de encendido (la que tiene el lector de huellas), la mantenemos presionada hasta que aparezca el logo de apple, un texto debajo que ponga continue presionando para las opciones de arranque y cuando cambie de texto, podremos solar la tecla. Ahora, seleccionamos el disco de arranque de Linux y presionamos Enter.


## 4. Configuración de recovery
Cuando hayamos hecho click en la partición, nos llevará al recovery, donde nos pedirá la contraseña del usuario administrador en MacOS. Una vez introducida, veremos una terminal. En ella, nos muestra una alerta sobre los mensjes de alerta que nos mostrará el portatil ya que no es algo que apple quiera que hagamos, pero nosotros si que queremos. Para continuar nos pedirá que preisonemos enter y cuando nos lo pida, introducimos la contraseña de administrador de MacOS. Para continuar, nos muestra un resumen de lo que va a llevar a cabo y si estamos de acuerdo, preciosamos `y`. 

Para confirmar que somos nosotros los que queremos hacer esta operación, nos pide el usuario y la contraseña de la cuenta de administrador. Una ve introducida y presionado enter, cuando termine podremos presionar enter y se reiniciará el sistema. 

Cuando se reinicie, ya arrancará en Linux.

## 5. Links de interés
- [Asahi Linux](https://asahilinux.org)

También te recomendamos echarle un vistazo a nuestra sección [Post-Install](post-install.md).


<!--## TODO: Troubleshooting-->
