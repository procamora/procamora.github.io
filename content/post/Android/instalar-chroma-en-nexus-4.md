---
title: Instalar Chroma en Nexus 4
description: Instrucciones para instalar la rom de Chroma en un Nexus 4
date: 2016-01-28
slug: "Uso-de-adb"
image: "covers/android.png"
tags:
  - chroma
  - nexus4
categories:
  - Android
---


Instrucciones para instalar la rom de Chroma en un Nexus 4

# Requisitos:

* Tener el móvil con al menos el **50%** de batería.
* Tener liberado el **bootloader**.
* Tener **twrp** instalado, en caso de no tenerlo instalarlo
(url de donde explico como instalarlo)
* tener **Android 5.0.1** (no se si es necesario)


#Pasos:
1. Descargarse el zip de la rom de: [descarga][rom]

2. Con twrp hacer un advanced wipe de:
    * Dalvik Cache
    * System
    * Data
    * Cache

    Poner foto


3. Poner el zip de la rom en la memoria interna del dispositivo

    `mv chroma_mako-2016-01-18.zip /media/nexus4/Internal Storage/`

4. instalar la zip con twrp

    poner foto

5. Instalar gaps

[rom]: https://www.androidfilehost.com/?fid=24369303960688159

6. Hacer un wipe(No se si es necesario)

7. Reiniciar dispositivo y esperar unos 5-10 min a que se inicie correctamente


http://forum.xda-developers.com/nexus-4/development/rom-chroma-03-31-2015-layers-t3069936
