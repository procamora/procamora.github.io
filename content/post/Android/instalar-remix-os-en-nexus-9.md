---
title: Instalar Remix OS en Nexus 9
description: Instrucciones para instalar la rom de Remix OS 1.5 en una Nexus 9
date: 2016-01-27
lastmod: 2016-01-27
slug: instalar-remix-os-en-nexus-9
image: "covers/android.png"
tags:
  - nexus9
  - remix
  - remixos
  - twrp
categories:
  - Android
---

Instrucciones para instalar la rom de Remix OS 1.5 en una Nexus 9

#Requisitos:
* Tener el móvil con al menos el **50%** de batería.
* Tener liberado el **bootloader**.
* Tener **twrp** instalado, en caso de no tenerlo instalarlo.
(url de donde explico como instalarlo).
* tener **Android 5.0.1** (no se si es necesario).


#Pasos:
1. Descargarse el zip de la rom de: [descarga][rom]

2. Con twrp hacer un advanced wipe de:
    * Dalvik Cache
    * System
    * Data
    * Cache

    ![wipe.jpg](/images/wipe.jpg){:height="auto" width="100%"}


3. Poner el zip de la rom en la memoria interna del dispositivo

    `mv chroma_mako-2016-01-18.zip /media/nexus9/Internal Storage/`

4. instalar la zip con twrp
    ![installrom.jpg](/images/installrom.jpg){:height="auto" width="100%"}
    ![install_rom.jpg](/images/install_rom.jpg){:height="auto" width="100%"}

5. Instalar gaps

    poner foto

6. Hacer un wipe(No se si es necesario)

7. Reiniciar dispositivo y esperar unos 5-10 min a que se inicie correctamente



[rom]: https://www.androidfilehost.com/?fid=24369303960687942

http://forum.xda-developers.com/nexus-9/development/5-1-1r6-resurrection-remix-unofficial-t3157330
