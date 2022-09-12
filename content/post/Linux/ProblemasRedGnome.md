---
title: Arreglar problema de red en gnome
description: 
date: 2015-10-05
lastmod: 2015-10-05
slug: ProblemasRedGnome
image: "covers/linux.png"
tags:
  - network
categories:
  - Linux
---


A veces sucede que, cuando tienes que instalar o configurar un ordenador nuevo, simplemente esperas que todo funcione como debiera tras instalar los tantos megas correspondientes. Pero no siempre es así y, como la memoria de uno ya no es lo que era, la búsqueda de soluciones se vuelve un laberinto del que no resulta fácil salir.

En esta ocasión (habrá otras, no lo dudo), el culpable ha sido Caja, al tratar de acceder vía SAMBA a mi raspberry para recuperar el último episodio de una serie. Con toda su desfachatez, me mostraba el mensaje:


> Could not display "network:///"
>
> Caja cannot handle "network" locations.
>

NOTA: el error, lo he constatado, aparece tanto para nautilus como para caja.

Fue echarle un ojo y saber que estaba relacionado con GVFS porque todo lo que huela a red en GNOME y alrededores tiene que ver con ese paquete, pero me tuve que pasar mis buenos quince minutos buscando, cribando la red en dos idiomas distintos para dar con la solución. Son dos míseros paquetes:

`sudo apt-get install gvfs-backends libsmbclient`

Y listo, caja (o nautilus) volverá a funcionar como siempre, accediendo vía samba y ssh al resto de la red.

Fuente: [0][0]


[0]: https://debianhackers.net/cajanautilus-no-puede-con-las-direcciones-network/
