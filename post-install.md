# Post-install
Aquí dejamos algunos pasos opcionales que puedes realizar para mejorar tu experiencia con Linux.


## Configuración red UC3M

### Eduroam
La configuración de la red es la siguiente:
- **Security**: _WPA/WPA2 Enterprise_
- **Authentication**: _Tunnelled TLS_
- Selecciona _No CA certificate is required_
- **Inner authentication**: _MSCHAPv2 (no EAP)_
- **Username**: El correo de la universidad (`100XXXXXX@alumnos.uc3m.es`)
- **Password**: La contraseña de dicho correo

Alternativamente, puedes usar el [_script_ de Python proporcionado por GÉANT](https://cat.eduroam.org/) para configurar la red automágicamente (con certificado).

> [!TIP]
> El _script_ anterior configura la red de la siguiente forma:
> - **Security**: _WPA/WPA2 Enterprise_
> - **Authentication**: _Tunnelled TLS_
> - **Anonymous identity**: `anonymousXXXXXX@uc3m.es`
> - **CA certificate**: `~/.config/cat_installer/ca.pem`
> - **Inner authentication**: _PAP_
> - **Username**: El NIA
> - **Password**: La contraseña de Aula Global
> 
> <details>
> <summary><code>~/.config/cat_installer/ca.pem</code></summary>
> 
> Certificado X509v3 (formato PEM), válido hasta Dec 31 23:59:59 2028 GMT.
> ```
> -----BEGIN CERTIFICATE-----
> MIIEMjCCAxqgAwIBAgIBATANBgkqhkiG9w0BAQUFADB7MQswCQYDVQQGEwJHQjEb
> MBkGA1UECAwSR3JlYXRlciBNYW5jaGVzdGVyMRAwDgYDVQQHDAdTYWxmb3JkMRow
> GAYDVQQKDBFDb21vZG8gQ0EgTGltaXRlZDEhMB8GA1UEAwwYQUFBIENlcnRpZmlj
> YXRlIFNlcnZpY2VzMB4XDTA0MDEwMTAwMDAwMFoXDTI4MTIzMTIzNTk1OVowezEL
> MAkGA1UEBhMCR0IxGzAZBgNVBAgMEkdyZWF0ZXIgTWFuY2hlc3RlcjEQMA4GA1UE
> BwwHU2FsZm9yZDEaMBgGA1UECgwRQ29tb2RvIENBIExpbWl0ZWQxITAfBgNVBAMM
> GEFBQSBDZXJ0aWZpY2F0ZSBTZXJ2aWNlczCCASIwDQYJKoZIhvcNAQEBBQADggEP
> ADCCAQoCggEBAL5AnfRu4ep2hxxNRUSOvkbIgwadwSr+GB+O5AL686tdUIoWMQua
> BtDFcCLNSS1UY8y2bmhGC1Pqy0wkwLxyTurxFa70VJoSCsN6sjNg4tqJVfMiWPPe
> 3M/vg4aijJRPn2jymJBGhCfHdr/jzDUsi14HZGWCwEiwqJH5YZ92IFCokcdmtet4
> YgNW8IoaE+oxox6gmf049vYnMlhvB/VruPsUK6+3qszWY19zjNoFmag4qMsXeDZR
> rOme9Hg6jc8P2ULimAyrL58OAd7vn5lJ8S3frHRNG5i1R8XlKdH5kBjHYpy+g8cm
> ez6KJcfA3Z3mNWgQIJ2P2N7Sw4ScDV7oL8kCAwEAAaOBwDCBvTAdBgNVHQ4EFgQU
> oBEKIz6W8Qfs4q8p74Klf9AwpLQwDgYDVR0PAQH/BAQDAgEGMA8GA1UdEwEB/wQF
> MAMBAf8wewYDVR0fBHQwcjA4oDagNIYyaHR0cDovL2NybC5jb21vZG9jYS5jb20v
> QUFBQ2VydGlmaWNhdGVTZXJ2aWNlcy5jcmwwNqA0oDKGMGh0dHA6Ly9jcmwuY29t
> b2RvLm5ldC9BQUFDZXJ0aWZpY2F0ZVNlcnZpY2VzLmNybDANBgkqhkiG9w0BAQUF
> AAOCAQEACFb8AvCb6P+k+tZ7xkSAzk/ExfYAWMymtrwUSWgEdujm7l3sAg9g1o1Q
> GE8mTgHj5rCl7r+8dFRBv/38ErjHT1r0iWAFf2C3BUrz9vHCv8S5dIa2LX1rzNLz
> Rt0vxuBqw8M0Ayx9lt1awg6nCpnBBYurDC/zXDrPbDdVCYfeU0BsWO/8tqtlbgT2
> G9w84FoVxp7Z8VlIMCFlA2zs6SFz7JsDoeA3raAVGI/6ugLOpyypEBMs1OUIJqsi
> l2D4kF501KKaU73yqWjgom7C12yxow+ev+to51byrvLjKzg6CYG1a4XXvi3tPxq3
> smPi9WIsgtRqAEFQ8TmDn5XpNpaYbg==
> -----END CERTIFICATE-----
> -----BEGIN CERTIFICATE-----
> MIIFgTCCBGmgAwIBAgIQOXJEOvkit1HX02wQ3TE1lTANBgkqhkiG9w0BAQwFADB7
> MQswCQYDVQQGEwJHQjEbMBkGA1UECAwSR3JlYXRlciBNYW5jaGVzdGVyMRAwDgYD
> VQQHDAdTYWxmb3JkMRowGAYDVQQKDBFDb21vZG8gQ0EgTGltaXRlZDEhMB8GA1UE
> AwwYQUFBIENlcnRpZmljYXRlIFNlcnZpY2VzMB4XDTE5MDMxMjAwMDAwMFoXDTI4
> MTIzMTIzNTk1OVowgYgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpOZXcgSmVyc2V5
> MRQwEgYDVQQHEwtKZXJzZXkgQ2l0eTEeMBwGA1UEChMVVGhlIFVTRVJUUlVTVCBO
> ZXR3b3JrMS4wLAYDVQQDEyVVU0VSVHJ1c3QgUlNBIENlcnRpZmljYXRpb24gQXV0
> aG9yaXR5MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAgBJlFzYOw9sI
> s9CsVw127c0n00ytUINh4qogTQktZAnczomfzD2p7PbPwdzx07HWezcoEStH2jnG
> vDoZtF+mvX2do2NCtnbyqTsrkfjib9DsFiCQCT7i6HTJGLSR1GJk23+jBvGIGGqQ
> Ijy8/hPwhxR79uQfjtTkUcYRZ0YIUcuGFFQ/vDP+fmyc/xadGL1RjjWmp2bIcmfb
> IWax1Jt4A8BQOujM8Ny8nkz+rwWWNR9XWrf/zvk9tyy29lTdyOcSOk2uTIq3XJq0
> tyA9yn8iNK5+O2hmAUTnAU5GU5szYPeUvlM3kHND8zLDU+/bqv50TmnHa4xgk97E
> xwzf4TKuzJM7UXiVZ4vuPVb+DNBpDxsP8yUmazNt925H+nND5X4OpWaxKXwyhGNV
> icQNwZNUMBkTrNN9N6frXTpsNVzbQdcS2qlJC9/YgIoJk2KOtWbPJYjNhLixP6Q5
> D9kCnusSTJV882sFqV4Wg8y4Z+LoE53MW4LTTLPtW//e5XOsIzstAL81VXQJSdhJ
> WBp/kjbmUZIO8yZ9HE0XvMnsQybQv0FfQKlERPSZ51eHnlAfV1SoPv10Yy+xUGUJ
> 5lhCLkMaTLTwJUdZ+gQek9QmRkpQgbLevni3/GcV4clXhB4PY9bpYrrWX1Uu6lzG
> KAgEJTm4Diup8kyXHAc/DVL17e8vgg8CAwEAAaOB8jCB7zAfBgNVHSMEGDAWgBSg
> EQojPpbxB+zirynvgqV/0DCktDAdBgNVHQ4EFgQUU3m/WqorSs9UgOHYm8Cd8rID
> ZsswDgYDVR0PAQH/BAQDAgGGMA8GA1UdEwEB/wQFMAMBAf8wEQYDVR0gBAowCDAG
> BgRVHSAAMEMGA1UdHwQ8MDowOKA2oDSGMmh0dHA6Ly9jcmwuY29tb2RvY2EuY29t
> L0FBQUNlcnRpZmljYXRlU2VydmljZXMuY3JsMDQGCCsGAQUFBwEBBCgwJjAkBggr
> BgEFBQcwAYYYaHR0cDovL29jc3AuY29tb2RvY2EuY29tMA0GCSqGSIb3DQEBDAUA
> A4IBAQAYh1HcdCE9nIrgJ7cz0C7M7PDmy14R3iJvm3WOnnL+5Nb+qh+cli3vA0p+
> rvSNb3I8QzvAP+u431yqqcau8vzY7qN7Q/aGNnwU4M309z/+3ri0ivCRlv79Q2R+
> /czSAaF9ffgZGclCKxO/WIu6pKJmBHaIkU4MiRTOok3JMrO66BQavHHxW/BBC5gA
> CiIDEOUMsfnNkjcZ7Tvx5Dq2+UUTJnWvu6rvP3t3O9LEApE9GQDTF1w52z97GA1F
> zZOFli9d31kWTz9RvdVFGD/tSo7oBmF0Ixa1DVBzJ0RHfxBdiSprhTEUxOipakyA
> vGp4z7h/jnZymQyd/teRCBaho1+V
> -----END CERTIFICATE-----
> -----BEGIN CERTIFICATE-----
> MIIG5TCCBM2gAwIBAgIRANpDvROb0li7TdYcrMTz2+AwDQYJKoZIhvcNAQEMBQAw
> gYgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpOZXcgSmVyc2V5MRQwEgYDVQQHEwtK
> ZXJzZXkgQ2l0eTEeMBwGA1UEChMVVGhlIFVTRVJUUlVTVCBOZXR3b3JrMS4wLAYD
> VQQDEyVVU0VSVHJ1c3QgUlNBIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MB4XDTIw
> MDIxODAwMDAwMFoXDTMzMDUwMTIzNTk1OVowRDELMAkGA1UEBhMCTkwxGTAXBgNV
> BAoTEEdFQU5UIFZlcmVuaWdpbmcxGjAYBgNVBAMTEUdFQU5UIE9WIFJTQSBDQSA0
> MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApYhi1aEiPsg9ZKRMAw9Q
> r8Mthsr6R20VSfFeh7TgwtLQi6RSRLOh4or4EMG/1th8lijv7xnBMVZkTysFiPmT
> PiLOfvz+QwO1NwjvgY+Jrs7fSoVA/TQkXzcxu4Tl3WHi+qJmKLJVu/JOuHud6mOp
> LWkIbhODSzOxANJ24IGPx9h4OXDyy6/342eE6UPXCtJ8AzeumTG6Dfv5KVx24lCF
> TGUzHUB+j+g0lSKg/Sf1OzgCajJV9enmZ/84ydh48wPp6vbWf1H0O3Rd3LhpMSVn
> TqFTLKZSbQeLcx/l9DOKZfBCC9ghWxsgTqW9gQ7v3T3aIfSaVC9rnwVxO0VjmDdP
> FNbdoxnh0zYwf45nV1QQgpRwZJ93yWedhp4ch1a6Ajwqs+wv4mZzmBSjovtV0mKw
> d+CQbSToalEUP4QeJq4Udz5WNmNMI4OYP6cgrnlJ50aa0DZPlJqrKQPGL69KQQz1
> 2WgxvhCuVU70y6ZWAPopBa1ykbsttpLxADZre5cH573lIuLHdjx7NjpYIXRx2+QJ
> URnX2qx37eZIxYXz8ggM+wXH6RDbU3V2o5DP67hXPHSAbA+p0orjAocpk2osxHKo
> NSE3LCjNx8WVdxnXvuQ28tKdaK69knfm3bB7xpdfsNNTPH9ElcjscWZxpeZ5Iij8
> lyrCG1z0vSWtSBsgSnUyG/sCAwEAAaOCAYswggGHMB8GA1UdIwQYMBaAFFN5v1qq
> K0rPVIDh2JvAnfKyA2bLMB0GA1UdDgQWBBRvHTVJEGwy+lmgnryK6B+VvnF6DDAO
> BgNVHQ8BAf8EBAMCAYYwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHSUEFjAUBggr
> BgEFBQcDAQYIKwYBBQUHAwIwOAYDVR0gBDEwLzAtBgRVHSAAMCUwIwYIKwYBBQUH
> AgEWF2h0dHBzOi8vc2VjdGlnby5jb20vQ1BTMFAGA1UdHwRJMEcwRaBDoEGGP2h0
> dHA6Ly9jcmwudXNlcnRydXN0LmNvbS9VU0VSVHJ1c3RSU0FDZXJ0aWZpY2F0aW9u
> QXV0aG9yaXR5LmNybDB2BggrBgEFBQcBAQRqMGgwPwYIKwYBBQUHMAKGM2h0dHA6
> Ly9jcnQudXNlcnRydXN0LmNvbS9VU0VSVHJ1c3RSU0FBZGRUcnVzdENBLmNydDAl
> BggrBgEFBQcwAYYZaHR0cDovL29jc3AudXNlcnRydXN0LmNvbTANBgkqhkiG9w0B
> AQwFAAOCAgEAUtlC3e0xj/1BMfPhdQhUXeLjb0xp8UE28kzWE5xDzGKbfGgnrT2R
> lw5gLIx+/cNVrad//+MrpTppMlxq59AsXYZW3xRasrvkjGfNR3vt/1RAl8iI31lG
> hIg6dfIX5N4esLkrQeN8HiyHKH6khm4966IkVVtnxz5CgUPqEYn4eQ+4eeESrWBh
> AqXaiv7HRvpsdwLYekAhnrlGpioZ/CJIT2PTTxf+GHM6cuUnNqdUzfvrQgA8kt1/
> ASXx2od/M+c8nlJqrGz29lrJveJOSEMX0c/ts02WhsfMhkYa6XujUZLmvR1Eq08r
> 48/EZ4l+t5L4wt0DV8VaPbsEBF1EOFpz/YS2H6mSwcFaNJbnYqqJHIvm3PLJHkFm
> EoLXRVrQXdCT+3wgBfgU6heCV5CYBz/YkrdWES7tiiT8sVUDqXmVlTsbiRNiyLs2
> bmEWWFUl76jViIJog5fongEqN3jLIGTG/mXrJT1UyymIcobnIGrbwwRVz/mpFQo0
> vBYIi1k2ThVh0Dx88BbF9YiP84dd8Fkn5wbE6FxXYJ287qfRTgmhePecPc73Yrzt
> apdRcsKVGkOpaTIJP/l+lAHRLZxk/dUtyN95G++bOSQqnOCpVPabUGl2E/OEyFrp
> Ipwgu2L/WJclvd6g+ZA/iWkLSMcpnFb+uX6QBqvD6+RNxul1FaB5iHY=
> -----END CERTIFICATE-----
> -----BEGIN CERTIFICATE-----
> MIIKCTCCBfGgAwIBAgIUbzH8mjS6ZQiQQxlRXV1glyeVbeYwDQYJKoZIhvcNAQEL
> BQAwgZIxCzAJBgNVBAYTAkVTMQ8wDQYDVQQIDAZNYWRyaWQxEDAOBgNVBAcMB0xl
> Z2FuZXMxKTAnBgNVBAoMIFVuaXZlcnNpZGFkIENhcmxvcyBJSUkgZGUgTWFkcmlk
> MRgwFgYDVQQDDA9jYS11YzNtLnVjM20uZXMxGzAZBgkqhkiG9w0BCQEWDGNlcnRA
> dWMzbS5lczAgFw0yMDExMDQxMTQwMTJaGA8yMDUwMTEyNzExNDAxMlowgZIxCzAJ
> BgNVBAYTAkVTMQ8wDQYDVQQIDAZNYWRyaWQxEDAOBgNVBAcMB0xlZ2FuZXMxKTAn
> BgNVBAoMIFVuaXZlcnNpZGFkIENhcmxvcyBJSUkgZGUgTWFkcmlkMRgwFgYDVQQD
> DA9jYS11YzNtLnVjM20uZXMxGzAZBgkqhkiG9w0BCQEWDGNlcnRAdWMzbS5lczCC
> BCIwDQYJKoZIhvcNAQEBBQADggQPADCCBAoCggQBAJ90pd7TOkrReiFR+TiCK3Rd
> CdOHDOmVHdg954J1Mq+RfiWDoiVIRDDwylrWxvqY15Qv8WMWKJIJqtONdEhCC+Vk
> 3OMDzaAXkB/Vbz/7TzAt/DnPa/1cwuKRATtnfl/lBr7VvX/iDI1ztJsU9DGZv2IW
> r3tC0nOtVUNHveh+/++iiPujuuQyVLDjfE51ISXwr3PhJFc6E3BBMTJZ28itHffO
> h1sUJ5Rp1a8OTA0uYAoObfpZT7brb0THbzkK32k70JfmUYwf9H30yCfVObdTkP+y
> kxg3tX1BVkR/Gb3rFmMIND6Gqcy42iLETo6j3zj9uSlTXr3gwfqBNSTyPwH8u1ih
> ejXctR25FB7ke4FB9q1gBwOMijdgluMxFFO1Ur2zW4Vn0e/8fYXwtHOLS1rJJ4PL
> jbgd0S8gIY3i8fGp5FnTgXALdKsU5agZ3xELjRJnGYu9G2DyAxyMy/Or7p6GopVk
> aLki5JVvVkEfZMyTnPetxg1qtaiVa8s2Pvc2C/eb9vBxhQwO1dVy4ymahhlLqHrV
> QaedpI/HLqxTMmfyQctmG1tFGoTlFOs9pwl1/vY2H08iJ2XKH9viOCVvbHykcCUg
> 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
> Ru8hoROl7XPkuFHkm1AAftn2Ri7YyKzYhJrgurs=
> -----END CERTIFICATE-----
> ```
> 
> </details>


Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/wifi-eduroam).


### VPN
Os recomendamos usar [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect).

Una vez [instalado](https://github.com/yuezk/GlobalProtect-openconnect#installation), se ejecuta con:
```bash
sudo -E gpclient connect --browser default myvpn.uc3m.es
```

Más información en [la página del SDIC](https://www.uc3m.es/sdic/servicios/vpn).

> [!NOTE]
> Si quieres que la VPN funcione dentro de WSL2, lo recomendable es poner la VPN en Windows y añadir la siguiente configuración al archivo `%USERPROFILE%\.wslconfig` (`C:\Users\<user>\.wslconfig`):
> ```
> [wsl2]
> localhostForwarding=true
> ```



## Drivers de NVIDIA
Desde hace unos años, NVIDIA publica sus [_drivers_ para Linux](https://www.nvidia.com/es-es/drivers/unix/), pero al ser _closed source_, no se pueden incluír en el kernel de Linux, por lo que tienen que ser instalados por separado.

> [!TIP]
> En algunas _distros_ es posible que haya una opción de "instalar drivers de terceros" en el instalador, la cual suele incluir los drivers oficiales.

> [!NOTE]
> Es posible que los _drivers_ oficiales no estén disponibles para gráficas más antiguas. Existe una alternativa open-source, [Nouveau](https://nouveau.freedesktop.org/), la cual _suele_ ir mejor en este tipo de gráficas. Consulta su documentación para ver cómo instalarlos.


### Instalación
La forma de instalarlos depende de la _distro_, a continuación te dejamos las más comunes.

#### Ubuntu
Si has habilitado la opción de drivers de terceros, deberías tenerlos instalados.  

Puedes instalarlos, según la [documentación oficial de Ubuntu](https://ubuntu.com/server/docs/nvidia-drivers-installation) con:
```bash
sudo ubuntu-drivers install
```

#### Fedora
Según la [documentación de RPM fusion](https://rpmfusion.org/Howto/NVIDIA):
```bash
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda
```

Si tienes _secure boot_ activado, échale un vistazo al repositorio [roworu/nvidia-fedora-secureboot](https://github.com/roworu/nvidia-fedora-secureboot).

#### Arch
Según [Arch Wiki](https://wiki.archlinux.org/title/NVIDIA):
```bash
sudo pacman -Syu nvidia-open
```

#### EndeavourOS
Según la [documentación de Endeavouros discovery](https://discovery.endeavouros.com/nvidia/new-nvidia-driver-installer-nvidia-inst/2022/03/), puedes usar `nvidia-inst`.

Este instala la versión _closed source_, proporcionada por NVIDIA.
```bash
nvidia-inst
```
Para usar los controladores _nouveau_:
```bash
nvidia-inst --nouveau
```

### Más información
- [NVIDIA - Arch Wiki](https://wiki.archlinux.org/title/NVIDIA)
- [NVIDIA - Gentoo Wiki](https://wiki.gentoo.org/wiki/NVIDIA#Feature_support)



## Aplicaciones
Aquí te dejamos una lista de aplicaciones que pueden ser útiles a la hora de sacarle el máximo partido a tu nuevo Linux:
- [EnvyControl](https://github.com/bayasdev/envycontrol): Aplicación para configurar el uso de GPUs dedicadas, integradas, e híbridas, extremadamente útil para cuando tienes tanto gráfica integrada como gráfica dedicada
- [OpenRGB](https://github.com/CalcProgrammer1/OpenRGB): Controlador para luces RGB
- [Vesktop](https://github.com/Vencord/Vesktop): Discord para Linux, pero bien hecho
- [WasIstLos](https://github.com/xeco23/WasIstLos): Cliente de WhatsApp para Linux
- [Redshift](https://github.com/jonls/redshift): _Screen filter_ (protector de vista)
- [fwupd](https://github.com/fwupd/fwupd) (A.K.A. Linux Vendor Firmware Service): Utilidad para actualizar el _firmware_ de una [gran variedad de dispositivos](https://fwupd.org/lvfs/devices/), incluyendo portátiles
- [downgrade](https://github.com/archlinux-downgrade/downgrade) [Exclusivo de Arch]: _Rollback_ de versiones de paquetes
- [gestures](https://gitlab.com/nokun/gestures): Aplicación para ejecutar comandos a partir de gestos en el _trackpad_


### Aplicaciones de terminal
Aquí os dejamos algunas aplicaciones para sacar el máximo de vuestra terminal, distintas utilidades y versiones mejoradas de comandos de Linux:
- [eza](https://github.com/eza-community/eza): Versión mejorada de `ls`
- [bat](https://github.com/sharkdp/bat): Versión mejorada de `cat`
- [btop](https://github.com/aristocratos/btop): Versión mejorada de `top`
- [fd](https://github.com/sharkdp/fd): Versión mejorada de `find`
- [rigpgrep](https://github.com/BurntSushi/ripgrep): Versión mejorada de `grep`
- [zoxide](https://github.com/ajeetdsouza/zoxide): Versión mejorada de `cd`
- [dust](https://github.com/bootandy/dust): Versión mejorada de `du`
- [Difftastic](https://github.com/Wilfred/difftastic): `diff`, pero para humanos
- [fzf](https://github.com/junegunn/fzf): Buscador interactivo _fuzzy_, extremadamente útil usado en combinación con otros comandos
- [micro](https://github.com/zyedidia/micro): Editor de texto simple en terminal (alternativa a `nano`)
- [trash-cli](https://github.com/andreafrancia/trash-cli): Envía archivos a la papelera desde la terminal (alternativa segura a `rm`)
- [glow](https://github.com/charmbracelet/glow): Visor de Markdown en terminal
- [The Fuck](https://github.com/nvbn/thefuck): Corrector de comandos
- [Lazygit](https://github.com/jesseduffield/lazygit): TUI para Git (probablemente la mejor interfaz gráfica para Git)
- [Lazydocker](https://github.com/jesseduffield/lazydocker): TUI para Docker
- [yazi](https://github.com/sxyazi/yazi): Explorador de archivos en terminal
- [fastfetch](https://github.com/fastfetch-cli/fastfetch): Muestra información del sistema
- [tealdeer](https://github.com/tealdeer-rs/tealdeer): Mini-manuales (TL;DR) para comandos
- [coltrane](https://github.com/pedrozath/coltrane): Herramienta para teoría musical
- [pokeget](https://github.com/talwat/pokeget-rs): Visor de _sprites_ de Pokémon en terminal


### Aplicaciones para hardware específico
Muchos dispositivos vienen con herramientas específicas para controlar aspectos del hardware, (batería o ventiladores en portátiles, botones en ratones, etc.), pero normalmente están disponibles exclusivamente para Windows. Aquí os dejamos algunas alternativas:
- [Lenovo Legion Linux](https://github.com/johnfanv2/LenovoLegionLinux): Herramientas para configurar portátiles de la gama _Legion_ de Lenovo (alternativa a [Lenovo Vantage](https://support.lenovo.com/eg/es/solutions/ht505081))
- [xpadneo](https://github.com/atar-axis/xpadneo): Drivers para los mandos _wireless_ de XBox
- [Piper](https://github.com/libratbag/piper): Aplicación para configurar ratones _gaming_ de diferentes marcas
- [Solaar](https://github.com/pwr-Solaar/Solaar): Herramienta para configurar dispositivos de Logitech (ratones, teclados, etc.)


### _Gaming_
Echa un vistazo a nuestra [guía de juegos en Linux](play-on-linux.md).


### Ejecutando programas de Windows
Aunque la compatibilidad de Windows varía de programa en programa, existen herramientas que te permiten ejecutar aplicaciones nativas de Windows en Linux, sin necesidad de crear una máquina virtual (lo cual [también se puede hacer](#usando-una-maquina-virtual)).
- [Wine](https://www.winehq.org/) (y [winetricks](https://github.com/Winetricks/winetricks)): La herramienta original y más usada, crea una capa de compatibilidad entre Windows y Linux
- [Winapps](https://github.com/Fmstrat/winapps): Permite una integración transparente con una máquina virtual de Windows, permitiendo ejecutar aplicaciones de Windows como si fueran ventanas en Linux

#### Usando una Máquina Virtual
Al igual que puedes [ejecutar Linux en una VM desde Windows](vm-install.md), también puedes ejecutar Windows en una VM desde Linux, asegurándote una compatibilidad prácticamente perfecta, aunque sacrificando algo de _performance_.

Aparte de la virtualización "tradicional" que ofrecen plataformas como [VirtualBox](https://www.virtualbox.org/) o [VMware](https://www.vmware.com/), en Linux existe [KVM](https://linux-kvm.org/), una virtualización basada en _kernel_, la cual es altamente eficiente. Para utilizar este tipo de VMs, te recomendamos usar [virt-manager](https://github.com/virt-manager/virt-manager).



## Instalar rEFInd
[rEFInd](https://www.rodsbooks.com/refind/) es un _boot manager_, al igual que
GRUB, pero más moderno y customizable. Es recomendable instalarlo en ordenadores
más modernos, y **no es recomendable instalarlo en ordenadores antiguos**.

### Linux
1. Instala el paquete `refind` (suele estar en el gestor de paquetes)
2. Reinicia. Debería salirte el _boot manager_ de rEFInd

> [!NOTE]
> Si después de reiniciar no aparece rEFInd, entra en la BIOS y selecciónalo
> como opción de _boot_ principal.


## Temas de GRUB
Si usas el _bootloader_ [GRUB](https://www.gnu.org/software/grub/) (lo más probable es que sí), puedes usar un tema personalizado.

Links de interés:
- [Jacksaur/Gorgeous-GRUB](https://github.com/Jacksaur/Gorgeous-GRUB): Repositorio con una selección de temas _chulos_ de GRUB
- [Gnome Look](https://www.gnome-look.org/browse?cat=109&ord=rating): Plataforma para compartir y descargar temas de GRUB
- [Tutorial de creación de temas para GRUB2](http://web.archive.org/web/20241209100014/http://wiki.rosalab.ru/en/index.php/Grub2_theme_tutorial)
