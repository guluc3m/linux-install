# Instalación de Windows Subsystem for Linux 2 (WSL2)

## 1. Activar características de Windows
Es posible que Windows venga con estas características deshabilitadas, así que las habilitaremos desde consola.

Para ello, es necesario ejecutar los siguientes comandos **desde Powershell** (`Win`+`R` → `powershell` → `Enter`):
```powershell
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```


## 2. Instalar WSL
Es tan sencillo como, desde la terminal (CMD/Powershell) ejecutar:
```powershell
wsl.exe --install
```

> [!NOTE]
> Es posible que este comando falle con un mensaje como:
> ```
> WslRegisterDistribution failed with error: 0x80370102
> Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS
> ```
> Esto indica que es posible que tengas que habilitar la virtualización desde la BIOS de tu PC. Busca en Internet cómo hacerlo para tu modelo / placa base específico.

> [!IMPORTANT]
> Después de este paso, es **necesario reiniciar el ordenador**.


## 3. Instalar tu distro
Es tan simple como ejecutar el siguiente comando desde terminal (CMD/powershell) especificando tu distro preferida, en este caso, Ubuntu:
```powereshell
wsl.exe --install Ubuntu
```

> [!NOTE]
> Es posible que este comando falle con un mensaje como:
> ```
> WslRegisterDistribution failed with error: 0x800701bc
> Error: 0x800701bc WSL 2 requires an update to its kernel component
> ```
> Esto significa que ya tienes WSL1 instalado (la versión antigua). Para actualizar a WSL2, ejecuta los siguientes comandos:
> ```powershell
> wsl.exe --update
> wsl --set-default-version 2
> ```
> Y después vuelve a instalar la distro.

> [!TIP]
> Puedes ver el listado de distros con `wsl.exe --list --online`


## 4. Setup
Una vez instalada la distro, te pedirá que crees un usuario, con nombre de usuario y contraseña.

Recuerda que siempre puedes volver a entrar en WSL mediante el comando `wsl`, o desde la aplicación 'Windows Terminal'.

<!-- TODO: how to disable sudo password -->

## Más info
- [Documentación oficial de Microsoft](https://learn.microsoft.com/windows/wsl/)
