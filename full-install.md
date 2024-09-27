# Instalación de Linux como único SO

En este tutorial vamos a explicar como abandonar Windows y pasarte a
cualquier distribución (preferiblemente Arch :D) de Linux. Al seguir
este tutorial se borrará toda la información del disco principal para
hacer hueco al nuevo SO, por lo que una copia de todo lo que tengas en
el disco tiene que estar guardado en otro lado. [Discos externos](https://www.tomshardware.com/how-to/mount-drives-linux)
no se verán afectados y los particionados por Windows son legibles dentro
de Linux.

## Requisitos

* Un ordenador que pueda correr el Doom original.
* 20 minutos de tu tiempo para instalarlo (Y otras 30 
horas para personalizarlo).

  
## 1. Preparar el equipo

Antes de comenzar con la instalación, hay que cambiar algunas cosas
en la BIOS (conecta el USB con la ISO flasheada antes).

1. Al encender el ordenador, spamear F11, F12, ESC, o el respectivo
al modelo de tu ordenador. / Desde windows, hacer click en reiniciar
manteniendo pulsado SHIFT para ir al `menú de recuperacion -> Solucionar
problemas -> Opciones Avanzadas -> Firmware UEFI o relacionados`.
2. Desactivar Secure Boot y poner el USB con Linux como primera opción
3. Guardar y reiniciar

> No es necesario desactivar el Secure Boot para distros como Ubuntu, pero si
> estás instalando otra distro, o estás teniendo problemas al arrancar,
> desactívalo.


## 2. Instalar Linux

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
   actualizaciones. Si el WIFI no se detecta, significa que los drivers genéricos
   no funcionan, ante esto [conectar el móvil al ordenador y usarlo como puente](https://www.tomsguide.com/how-to/how-to-share-wi-fi-on-android-using-usb-tethering)
   para conectarlo a internet. 

5. Aceptar el instalar software propietario. No 
   son indispensables, pero para algunos casos son mejores (Como jugar por ejemplo).
6. Seleccionar borrar el disco e instalar Ubuntu. Cuidado con qué disco eliges, especialmente
   si tienes discos externos con fotos, documentos, etc... conectados.
7. Finalmente configurar el usuario e instalar el sistema operativo.

### Otras Distribuciones
Al igual que Ubuntu, pero puede que cambie algún paso.


## 3. Wrap-Up
Ya hemos terminado `:)`. Al reiniciar verás el GRUB, de donde puedes entrar directamente
a la BIOS o iniciar otro sistema operativo en caso de que tengamos mas de uno instalado.
Como tip, al instalar programas preferiblemente usar el gestor de paquetes, `apt` en el caso
de Ubuntu.


## Links de interes
* [Gnome Looks / personalización](https://www.gnome-look.org/browse/)
* [OpenRGB / Controlar las luces del ordenador](https://github.com/CalcProgrammer1/OpenRGB)
* [EnvyControl / Cambiar entre GPU dedicada e integrada](https://github.com/bayasdev/envycontrol)
* [Vesktop / Discord para linux pero bien hecho](https://github.com/Vencord/Vesktop)
* [Tuberias :D](https://github.com/pipeseroni/pipes.sh)