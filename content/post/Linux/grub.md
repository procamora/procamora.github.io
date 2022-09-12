---
title: Modificar el grub
description: 
date: 2015-11-13
lastmod: 2015-11-13
slug: grub
image: "covers/linux.png"
tags:
  - grub
categories:
  - Linux
---

###### instalar paquete de imágenes
`sudo aptitude install grub2-splashimages`


###### carpeta de imágenes del grub
`/usr/share/images/grub/`


###### archivo configuración grub
`sudo gedit /etc/grub.d/05_debian_theme`


###### actualizar grub
`update-grub2`

###### en caso de no ser suficiente
`sudo grub-mkconfig -o /boot/grub/grub.cfg`


las imágenes del grub deben estar a 640x480


## RECUPERAR EL ARRANQUE GRUB
**Método 1**
Consiste en usar una distribución en modo LiveCD para instalar nuevamente el GRUB. Usaremos el LiveCD de Ubuntu 9.10 o superior (debe ser la versión Live o Desktop), aunque puede ser cualquier otra distribución que use GRUB2 como gestor de arranque y no LILO ni Grub 1.


###### Lo primero que debemos hacer es arrancar el live-cd y abrir una terminal. Después escribimos los siguiente para ver las particiones de los distintos discos duros:
`sudo fdisk -l`


###### Después vemos cual es la partición donde tenemos Ubuntu y la montamos en /mnt (en la mayoría de los casos esta partición será sda1, el ejemplo lo haré con esa partición pero mira cual es tu partición con el comando fdisk):
`sudo mount /dev/sda8 /mnt`


###### Ahora, monta el resto de los dispositivos:

`sudo mount --bind /dev /mnt/dev`

`sudo mount --bind /dev/pts  /mnt/dev/pts`

`sudo mount --bind /proc /mnt/proc`

`sudo mount --bind /sys  /mnt/sys`


###### Y ejecuta el comando chroot de forma que accedemos como root al sistema de archivos de nuestro antiguo Ubuntu:
`sudo chroot /mnt`

###### Por último cargamos el Grub en el MBR ejecutando el siguiente comando:
`# grub-install --recheck /dev/sda`

(sda lo debemos substituir por el disco duro que utilizamos para arrancar los sistemas operativos, casi siempre es sda. Ojo!! no poner el número de partición, solo sda).

###### Reiniciamos y cuando vuelva a arrancar Ubuntu (no el del LiveCD), podemos ajustar en el menú del GRUB manualmente para que aparezca en el menú de arranque el nuevo sistema operativo que nos borró el MBR, o dejar que lo haga el automáticamente con el siguiente comando:
`sudo update-grub2`

###### Si el comando no te funciona, quizás necesites instalar el paquete grub2:
`sudo apt-get install grub2`






`
