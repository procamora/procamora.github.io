---
title: Uso de Screen
description: Uso basico de screen en linux
date: 2015-12-06
lastmod: 2015-12-06
slug: comando_screen
image: "covers/linux.png"
tags:
  - screen
  - console
categories:
  - Linux
---

GNU Screen es una herramienta destinada a la terminal de Linux con la que se puede crear y manejar varias sesiones y programas de manera simultanea desde una sola terminal.

Pero además, permite cerrar la terminal y volverse a conectar a la sesión de screen que conservará las "terminales virtuales" que tuviéramos abiertas.


Instalar: `sudo apt-get install screen`


###Opciones básicas
```
-S sockname  Da nombre a la sesión [pid].sockname.
ls           Lista las sesiones abiertas de screen.
-r           Reattach a un sesión. Es posible especificar el nombre ej: screen -r sockname
-t título    Permite dar un título a una ventana.
```
Ejemplo: `screen -S NombreSesion -t NombreVentana`


###Manejo de las ventanas

```bash
[Ctrl]+[A],[C]         Nos permite abrir más terminales virtuales
[Ctrl]+[A],[N]         Nos permite cambiar de una terminal a otra
[Ctrl]+[A],[Shift]+[C] Nos permite renombrar el terminal, por defecto todos se llaman bash

[Ctrl]+[A],[D]         Nos permite cerrar la terminal sin cerrar los procesos que se están ejecutando
[Ctrl]+[D]             Cierra la terminal, si es la única que tenemos bierta, salir de screen

[Ctrl]+[A],[x]         Bloquear todas las terminales con una clave  

[Ctrl]+[A],[?]         Nos muestra las combinaciones de teclas
```

### Ejemplo de uso:

```bash
screen
```



Fuentes: [0][0] [1][1]
[0]: http://www.muylinux.com/2009/01/05/gestion-remota-desconectando
[1]: https://dreyacosta.com/jugando-con-screen-un-manejador-de-sesiones-linux/
