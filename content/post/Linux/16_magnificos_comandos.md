---
title: 16 comandos útiles
description: 
date: 2015-11-16
lastmod: 2015-11-16
slug: 16_magnificos_comandos
image: "covers/linux.png"
tags:
  - linux
categories:
  - Linux
---



######1. Controla la cantidad de RAM que tiene libre:
`free`


######2. Donde esta la aplicación que acabo de instalar (todos los directorios)
`whereis [app]`


######3. Uso del espacio de su disco
`df -h`


######4. Crear una lista de reproducción de los archivos de audio en una carpeta.
`ls -R > playlist.m3u`


######5. Matar un proceso por su nombre
`sudo killall` por ejemplo: `sudo killall firefox`. O via pid (program id): `sudo kill`

para ver el pid: `pidof` por ejemplo: `pidof firefox`

o puedes probar ver la lista de procesos que se están ejecutando actualmente con:
`ps -e`


######6. Encontrar la versión del software instalado:
`sudo apt-cache policy`


######7. Encontrar el UUID de tus particiones:
`ls /dev/disk/by-uuid/ -alh`


######8. Mostrar los diez procesos principales que se están ejecutando – ordenados por el uso de la memoria:
`ps aux | sort -nrk 4 | head`


######9. Establecer una alarma sonora cuando una dirección IP salga online
`ping -i 60 -a IP_address`


######10. Montar un archivo .iso en UNIX/Linux:
`mount /path/to/file.iso /mnt/cdrom -oloop`


######11. Compartir un archivo a través del puerto 80 http:
`nc -w 5 -v -l -p 8081 < file.ext`

Desde la otra máquina abrir un navegador web y vaya a la ip de la máquina desde la que quiere lanzar netcat, **http://ip-address:8081**
Si usted tiene alguno servidor web escuchando en el puerto 80, entonces sería necesario detenerlos o seleccionar otro puerto antes de lanzar: net cat ;-)

>P.d.:es necesario instalar netcat tool


######12. Extracto de audio stream de un archivo AVI usando mencoder:
`mencoder "${file}" -of rawaudio -oac mp3lame -ovc copy -o
audio/"${file/%avi/mp3}`


######13. Captura de video desde linux desktop:
`ffmpeg -f x11grab -s wxga -r 25 -i :0.0 -sameq /tmp/out.mpg`


######14. Descarga una website completa:
`wget --random-wait -r -p -e robots=off -U mozilla http://www.example.com`


######15. Matar: un proceso que esta bloqueando un archivo:
`fuser -k filename`


######16. Escaneo de puertos usando telnet:
`HOST=127.0.0.1;for((port=1;port/dev/null | grep 'Connected to' >
/dev/null; then echo -en "nnport $port/tcp is opennn";fi;done | grep open`
