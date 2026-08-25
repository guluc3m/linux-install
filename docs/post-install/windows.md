# Ejecutando programas de Windows
Aunque la compatibilidad de Windows varía de programa en programa, existen herramientas que te permiten ejecutar aplicaciones nativas de Windows en Linux, sin necesidad de crear una máquina virtual (lo cual [también se puede hacer](#usando-una-maquina-virtual)).
- [Wine](https://www.winehq.org/) (y [winetricks](https://github.com/Winetricks/winetricks)): La herramienta original y más usada, crea una capa de compatibilidad entre Windows y Linux
- [Winapps](https://github.com/Fmstrat/winapps): Permite una integración transparente con una máquina virtual de Windows, permitiendo ejecutar aplicaciones de Windows como si fueran ventanas en Linux

## Usando una Máquina Virtual
Al igual que puedes [ejecutar Linux en una VM desde Windows](../guías/vm-win.md), también puedes ejecutar Windows en una VM desde Linux, asegurándote una compatibilidad prácticamente perfecta, aunque sacrificando algo de _performance_.

Aparte de la virtualización "tradicional" que ofrecen plataformas como [VirtualBox](https://www.virtualbox.org/) o [VMware](https://www.vmware.com/), en Linux existe [KVM](https://linux-kvm.org/), una virtualización basada en _kernel_, la cual es altamente eficiente. Para utilizar este tipo de VMs, te recomendamos usar [virt-manager](https://github.com/virt-manager/virt-manager).

> [!TIP]
> Te dejamos aquí también un par de guías para configurar KVM y Windows:
> - [How Do I Properly Install KVM on Linux](https://sysguides.com/install-kvm-on-linux)
> - [How to Properly Install a Windows 11 Virtual Machine on KVM](https://sysguides.com/install-a-windows-11-virtual-machine-on-kvm)
