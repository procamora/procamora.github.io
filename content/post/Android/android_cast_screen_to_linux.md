---
title: Android cast screen to Linux
description: La aplicación_ scrcpy_ proporciona la visualización y control de dispositivos Android conectado por USB, aunque también tiene compatibilidad con el control por TCP/IP. No requiere acceso root y es multiplataforma, funcionando sobre Windows, Linux Y macOS.
date: 2020-05-10
slug: "android_cast_screen_to_linux"
image: "covers/android.png"
tags:
  - android
  - cast
  - windows
  - linux
  - screen
  - scrcpy
categories:
  - Android
---

Summary: La aplicación_ scrcpy_ proporciona la visualización y control de dispositivos Android conectado por USB, aunque también tiene compatibilidad con el control por TCP/IP. No requiere acceso root y es multiplataforma, funcionando sobre Windows, Linux Y macOS.
Status: published

La aplicación [scrcpy][scrcpy] proporciona la visualización y control de dispositivos Android conectado por USB, aunque también tiene compatibilidad con el control por TCP/IP. No requiere acceso root y es multiplataforma, funcionando sobre Windows, Linux Y macOS.


Sus características son:

- Ligero (nativo, muestra sólo la pantalla del dispositivo).
- Rendimiento (30 ~ 60 fps).
- Calidad (1920 × 1080 o más).
- Baja latencia (35 ~ 70ms).
- Bajo tiempo de inicio (~ 1 segundo para mostrar la primera imagen).
- No intrusivo (no se deja nada instalado en el dispositivo).



![android_cast](/images/2020/20200510_android_cast.png){:height="auto" width="100%"}



# Instalación


Requisitos previos:

- El dispositivo Android requiere al menos la API 21 (Android 5.0).
- Tener habilitado la depuración _adb_ en el dispositivo.


Para instalarlo en Fedora podemos usar el gestor de paquetes _snap_:


```bash
sudo snap install scrcpy
snap connections scrcpy
sudo snap connect scrcpy:network :network
sudo snap connect scrcpy:network-bind :network-bind
sudo snap install core
```

> En Ubuntu 20.04 ya se puede instalar desde el repositorio oficial.



# Uso

Un ejemplo básico de uso sería el siguiente:


```bash
scrcpy --max-size 1920 --max-fps 60 --fullscreen
```


## Rotación


La ventana puede ser rotada con:


```bash
scrcpy --rotation 1
```


Los posibles valores son:

- 0: no hay rotación.
- 1: 90 grados en sentido contrario a las agujas del reloj.
- 2: 180 grados.
- 3: 90 grados en el sentido de las agujas del reloj.



## Grabación

Es posible grabar la pantalla mientras se refleja con el comando:


```bash
scrcpy --record file.mp4
scrcpy --record file.mkv
```

Para deshabilitar el espejo mientras se graba:

```bash
scrcpy --no-display --record file.mp4
```


> Interrumpir la grabación con Ctrl+C
> Ctrl+C no termina correctamente en Windows, así que desconecta el dispositivo.



[scrcpy]: https://github.com/Genymobile/scrcpy

