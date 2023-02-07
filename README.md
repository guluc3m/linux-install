# Linux 404<sup>2</sup>: Introducción a GNU/Linux

## 1. Cosas a tener en cuenta ANTES DE ASISTIR AL TALLER
Uno de los objetivos de éste taller es instalar Linux en vuestros ordenadores.  
Para agilizar éste proceso, es recomendable que leáis la siguiente información:  

Hay diversas formas de "instalar" Linux. Entendemos que no todos tenéis las mismas circunstancias, así que recomendamos que tengáis en cuenta todas y elijáis una antes de venir, trayendo el material correspondiente dependiendo del método.  

### Prefacio: Nota para gente con Apple Macs
Si tenéis un ordenador con un procesador M1/M1Pro/M1Max/M2/M2Pro (Macbook Air/Pro de 2020 o posterior), la única forma que tenéis de correr Linux es correr una VM ([UTM](https://mac.getutm.app/)) con una versión de Linux para ARM-64 (por ejemplo, [Ubuntu para ARM-64](https://ubuntu.com/download/server/arm)).

### Método 1: Full Linux
Este método consiste en decir "fuck Microsoft", borrar Windows, y correr sólo Linux.  
- **Restricciones:** Ninguna.  
Bueno sí, un ordenador con menos de 20 años.
- **Ventajas:** Todas las ventajas de Linux, sin los posibles problemas derivados de tener Dual Boot.
- **Desventajas:** Tu ordenador no va a tener Windows.  
Espera, ¿ese es un problema? Si tienes que usar Office, Adobe Creative Cloud, o algún programa o juego (cualquiera con AntiCheat) específico de Windows (y [Wine](https://www.winehq.org/) no te puede ayudar), sí.
- **Recomendado para:** 
    - Linuxeros (frikis)
    - Tu tía la del pueblo que sólo usa Internet Explorer
    - Un segundo ordenador portátil que uses para la uni
- **Cosas que preparar:** 
    - Copia de seguridad de tus archivos (fotos, fanfics, etc.)
    - Un [live USB con Linux](#2-cómo-crear-un-live-usb-de-ubuntu).

### Método 2: Dual Boot
Consiste en instalar en tu ordenador los dos sistemas operativos: Windows/MacOS y Linux.
- **Restricciones:** Mínimo 64GB de espacio libre en disco.
- **Ventajas:** Todas las ventajas de Windows (si las hay) y todas las de Linux.
- **Desventajas:** 
    - Puede ser un poco coñazo usar y mantener (configurar y actualizar) ambos sistemas operativos.  
    - Problemas de almacenamiento si tienes un disco pequeño.
- **Recomendado para:** 
    - Estudiantes que necesiten Linux para la carrera pero que quieran seguir usando su PC para jugar al Fortnite (u otras cosas de Windows)
    - Personas a la que gente malvada le obligue a usar Windows
- **Cosas que preparar:** 
    - Copia de seguridad de tus archivos (fotos, fanfics, etc.)
    - Un [live USB con Linux](#2-cómo-crear-un-live-usb-de-ubuntu).

### Método 3: Windows Subsystem for Linux (WSL)
WSL te permite "correr Linux" dentro de Windows, pero sólo mediante una terminal, con un excelente nivel de compatibilidad.
- **Restricciones:** Tener Windows.
- **Ventajas:** 
    - Fácil y rápido de instalar
    - Ligero
- **Desventajas:** No hay GUI, sólo pedes usar una terminal.
- **Recomendado para:** 
- **Cosas que preparar:** 

### Método 4: Virtual Machine (VM)

- **Restricciones:** 
- **Ventajas:** 
- **Desventajas:** 
- **Recomendado para:** 
- **Cosas que preparar:** 


### Método 5: Disco externo

- **Restricciones:** 
- **Ventajas:** 
- **Desventajas:** 
- **Recomendado para:** 
- **Cosas que preparar:** 

## 2. Cómo crear un Live USB de Ubuntu
Lo primero, necesitas un USB con al menos 8GB de almacenamiento.  
Sí, todo lo que haya ahí dentro va a desaparecer, así que estás avisado.