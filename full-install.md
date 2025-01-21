# Instalación de Linux como único SO

En este tutorial vamos a explicar como abandonar Windows y pasarte a
cualquier distribución (preferiblemente Arch :D) de Linux. Al seguir
este tutorial se borrará toda la información del disco principal para
hacer hueco al nuevo SO, por lo que una copia de todo lo que tengas en
el disco tiene que estar guardado en otro lado. [Discos externos](https://www.tomshardware.com/how-to/mount-drives-linux)
no se verán afectados y los particionados por Windows son legibles dentro
de Linux.

## Requisitos

- Live USB




## 2. Instalar Linux

### Ubuntu
1. Instalar Ubuntu.
2. Selecciona el idioma.
3. **IMPORTANTE**, incluso si has seleccionado otro idioma que no sea el
   español, asegúrate de elegir en la distribución del teclado la que se adapte
   a tu ordenador o la que uses normalmente.
4. Selecciona "Instalación Normal" e "Instalar software de terceros"; y
   **deselecciona** "Descargar actualizaciones mientras se instala Ubuntu", que
   luego nos echan la culpa si se cae Eduroam.
5. Aceptar el instalar software propietario. No son indispensables, pero para algunos casos son mejores (Como jugar por ejemplo).
6. Seleccionar borrar el disco e instalar Ubuntu. Cuidado con qué disco eliges, especialmente
   si tienes discos externos con fotos, documentos, etc... conectados.
7. Finalmente configurar el usuario e instalar el sistema operativo.


### Otras Distribuciones
Al igual que Ubuntu, pero puede que cambie algún paso.


## 3. Wrap-Up
Ya hemos terminado `:)`. Al reiniciar verás el GRUB, de donde puedes entrar directamente a la BIOS o iniciar otro sistema operativo en caso de que tengamos mas de uno instalado.

También te recomendamos echarle un vistazo a nuestra sección [Post-Install](post-install.md).



## Troubleshooting
- [Solucionar drivers Wi-Fi](common.md#solucionar-drivers-wi-fi)



## Links de interes
- [GRUB - ArchWiki](https://wiki.archlinux.org/title/GRUB)