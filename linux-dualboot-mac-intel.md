# 1. Prepara tu mac

## Sigue estos pasos para hacer hueco a la partición de linux:

1. Abre "Utilidad de discos"
2. Ve al dispositivo (volumen) Apple SSD/SATA/lo que sea, no sus particiones Macintosh SSD, el dispositivo físico. Verás ahi todas sus particiones.
3. Elige la opción "crear partición".
4. En ese menú podrás reducir el tamaño de la partición Machintosh SSD, el propio ordenador te indicará qué tanto puede liberar.
5. Una vez elegido el tamaño, aplica los cambios. Te recomiendo igualmente hacer copia de seguridad de las cosas importantes.
6. El espacio liberado quedará marcado como "espacio libre" o "free space". Quédate con su tamaño, así como el de la partición de tu SO principal.

# 2. Accede a la ISO

Reinicia el ordenador y mantén pulsado "alt" u "opción" hasta que veas un listado de discos duros para arrancar, elige "EFI Boot".
Por lo general, cuando inices la ISO no podrás abrirla en "normal mode", si se congela, mantén "alt", "shift" y "cmd" y pulsa el botón de encendido para apagar el ordenador.
Después, repite este paso pero seleccionando "Boot in grub2 mode".

# 3. Listo

Los pasos de instalación son iguales a los de otras máquinas: Debes crear las particiones, instalar el kernel, entorno de escritorio, instalar el bootloader...
