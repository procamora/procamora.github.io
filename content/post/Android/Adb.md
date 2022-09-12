---
title: Uso de adb
description: "Uso de adb"
date: 2015-09-09 11:11
slug: "Uso-de-adb"
image: "covers/draft.png"
tags:
  - android
  - adb
  - linux
  - consola
  - fastboot
  - nexus
categories:
  - Android
---

Para mostrar si tu dispositivo esta instalado

`adb devices`
`fastboot devices`

> Sino lo esta después de haber instalado los usb drivers desconectar y conectar y tendrás que aceptar el certificado

Para iniciar el modo bootloader
`adb reboot bootloader`
`fastboot reboot-bootloader`


Iniciar el modo recovery
`adb reboot recovery`

Reiniciar el teléfono
`fastboot reboot`
`adb reboot`

Bloquear y desbloquear el bootloader
`fastboot oem unlock`
`fastboot oem lock`
> Precaución, elimina todo el contenido de nuestro dispositivo.


`fastboot flash bootloader bootloader-mako-makoz10l.img`
`fastboot flash radio radio-mako-m9615a-cefwmazm-2.0.1700.33.img`
`fastboot flash system system.img`
`fastboot flash userdata userdata.img`
`fastboot flash boot boot.img`
`fastboot flash recovery recovery.img`
`fastboot erase cache`



```
Acabo de actualizar mi Nexus 4 siguiendo los pasos de un post de XDA:
http://forum.xda-developers.com/showthread.php?p=43918377

Para poder actualizar sin perder los datos hay que borrar el archivo "userdata.img" dentro de "image-***-***.zip". Os dejo el tutorial modificado para no perder datos y traducido para quien le interese y no sepa inglés:

1. Descargar la imagen de fábrica de Android 4.3 desde este enlace:
https://developers.google.com/android/nexus/images

2. Extraer los archivos con Winrar o similar

3. Abrir el archivo "image-***-*****.zip" con Winrar y borrar el archivo "userdata.img"

4. Copiar todos los archivos extraídos a la carpeta android-sdk/platform-tools/ o a la carpeta donde tengas adb y fastboot

5. Conectar tu Nexus por USB con la opción de Debug activada en las Opciones de desarrollo

6. Ejecutar estos comandos por orden:

6.a: adb reboot bootloader
6.b: fastboot flash bootloader bootloader-***-***.img
6.c: fastboot reboot-bootloader
6.d: fastboot flash radio radio-***-***.img
6.e: fastboot reboot-bootloader
6.f: fastboot update image-***-***.zip

PD: Se que hay mucha gente que no sabe usar la consola (por miedo o porque nunca lo han probado), en ese caso recomiendo esperar a la OTA..

PD2: Si no tienes el bootloader desbloqueado es imposible actualizar manualmente sin perder los datos, hay que esperar a la OTA..
```
