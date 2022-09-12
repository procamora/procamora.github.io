---
title: Instalar TWRP en android
description: Proceso para instalar el recovery de TWRP en Android debemos hacer lo siguiente
date: 2016-01-26
slug: instalar-twrp-en-android
image: "covers/android.png"
tags:
  - android
  - twrp
categories:
  - Android
---

Proceso para instalar el recovery de TWRP en Android debemos hacer lo siguiente:

# Requisitos:
* Tener el móvil con al menos el **50%** de batería.
* Tener instalados los **drivers** del dispositivo. [Descarga][drivers]
* Tener instalado **ADB Tools**.
* Tener habilitada la **depuración USB**.
    ![usbdebbug.jpg](/images/usbdebbug.jpg){:height="auto" width="100%"}
* Recomendado: Tener liberado el **bootloader**.

[drivers]: http://developer.android.com/intl/es/sdk/win-usb.html


# Pasos:

1. Para buscar la imagen de TWRP de nuestro dispositivo tenemos que buscarla desde [aquí][devices]

2. Una vez que hemos buscado la pagina de nuestro dispositivo y nos hemos descargado la imagen hay que reiniciar el dispositivo en el modo bootloader, se puede hacer de 2 formas distintas:

    1. Con el comando: `adb reboot bootloader`
    2. Botón Power + Bajar Volumen


3. Comprobamos que fastboot detecta el dispositivo con `fastboot devices`, si lo detecta procedemos a instalar twrp

4. `fastboot flash recovery twrp-2.8.x.x-xxx.img`

5. Una vez que lo hemos instalado procedemos a reiniciar el dispositivo y ya lo tenemos listo con twrp instalado

6. `fastboot reboot`

En resumen:
```
adb reboot bootloader
fastboot flash recovery twrp-2.8.x.x-xxx.img
fastboot reboot
```

[devices]: https://twrp.me/Devices/


# Descargas de imágenes y paginas oficiales: (a fecha de 22/01/2016)

Nexus 4: [Pagina][n4] [url][url4]

Nexus 9: [Pagina][n9] [url][url9]

Nexus 5X: [Pagina][n5x] [url][url5x]

[n4]: https://twrp.me/devices/lgnexus4.html
[url4]: https://dl.twrp.me/mako/
[n9]: https://twrp.me/devices/htcnexus9.html
[url9]: https://dl.twrp.me/flounder/
[n5x]: https://twrp.me/devices/lgnexus5x.html
[url5x]: https://dl.twrp.me/bullhead/



Fuentes: [0][0] [1][1]

[0]: http://androiding.how/how-to-install-twrp-recovery-via-fastboot/
[1]: https://getmovil.com/nexus/instalar-android-4-4-4/
