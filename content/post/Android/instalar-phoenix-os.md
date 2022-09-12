---
title: Instalar Phoenix OS en nexus 9
description: "Uso de adb"
date: 2016-01-19
slug: instalar-phoenix-os
image: "covers/android.png"
tags:
  - phoenixos
  - nexus9
  - phoenix
  - adb
categories:
  - Android
---


#Requisitos:
Tener instalados los drivers del dispositivo

#Pasos:

`adb reboot bootloader`

A la hora de instalar Phoenix OS  1.0 en la nexus 9 LTE he tenido este problema al ejecutar el script de instalación
`./flash-all.sh`
```
sending 'system' (678746 KB)...
FAILED (remote: data length is too large)
finished. total time: 3.146s
```


ere are the steps i took to manually flash:
run the flash-all.bat up until the point where it fails

```bash
unzip Nexus9_flounder_jenkins_stable_11_2016-01-04_20-25.zip
fastboot flash system system.img
fastboot flash recovery recovery.img
fastboot flash cache cache.img
fastboot flash boot boot.img
fastboot flash userdata vendor.img # - looks like userdata should be vendor? - mine worked with userdata regardless
from tablet - select hboot
select factory reset
```


IMPORTANTE INSTALAR LA PLAY STORE, ESTA LA APK PARA BAJÁRSELA EN DESCARGAS
https://www.reddit.com/r/RemixOS/comments/40olez/install_google_play_services_on_remix_os_official/


instalar gaps. lo anterior no me funciona

http://opengapps.org/


http://www.xda-developers.com/download-google-apps-gapps/




http://forum.xda-developers.com/nexus-9/help/factory-image-flash-t2929019/post56529332#post56529332
