---
title: Primeros pasos Docker
description: Primeros pasos en la instalación y uso de docker
date: 2018-10-26
lastmod: 2018-10-26
slug: primeros-pasos-docker
image: "covers/software.png"
tags:
  - docker
  - linux
  - cowrie
categories:
  - Software
---

Primeros pasos en la instalación y uso de docker


# Instalación y configuración

```bash
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
dnf install docker-ce
usermod -aG docker procamora
newgrp docker # Esto permite “refrescar” el grupo sin tener que reiniciar
systemctl enable docker
systemctl start docker
docker run hello-world # Confirmar que esta bien instalado
```


# Buscamos la imagen que necesitemos

```bash
docker search cowrie
```


# Nos descargamos las imágenes que necesitemos

```bash
docker pull ouspg/cowrie
docker pull kalilinux/kali-linux-docker
```


# Mostrar las imágenes disponibles

```bash
docker images
```


# Crear el contenedor (Solo ejecutar la primera vez)

```bash
docker run [IMAGE]
docker run hello-world
docker run -it -p 2222:2222 -p 2223:2223 cowrie/cowrie
docker run -it -p 8081:80 httpd # Host anfitrión 8081 , Docker 80
docker run -it --name="webserver" -p 8081:80 httpd # Asignamos un nombre
docker run -it kalilinux/kali-linux-docker /bin/bash # También te abre una consola al SO
docker run -dit -p 2222:2222 -p 2223:2223 -v $(pwd)/dl:/home/cowrie/cowrie/dl -v $(pwd)/log:/home/cowrie/cowrie/log ouspg/cowrie # -d lo lanza como demonio -v para montar los volumenes entre la maquina fisica y el contenedor
```


# Iniciar un contenedor previamente creado

```bash
docker ps -a   # Vemos los contenedores creados
docker start [CONTAINER_ID]
docker start e7d1b0de6fe9
```


# Entrar en un contenedor en ejecución:

```bash
docker ps -a
docker exec -it [CONTAINER_ID] bash
docker exec -it e7d1b0de6fe9 bash 
```


# Borrar un contenedor creado

```bash
docker ps -a   # Vemos los contenedores creados
docker rm [CONTAINER_ID]
docker rm e7d1b0de6fe9
```


# Borrar una imagen descargada

```bash
docker images
docker rmi [IMAGE]
docker rmi httpd
```


# Modificar etiqueta

```bash
docker tag httpd a/b:latest
```


# Guardar una imagen

```bash
docker commit [CONTAINER_ID] httpd_mod
```


# Ver la IP de un contenedor

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [CONTAINER_ID]
```


# login cowrie

```bash
docker run -dit -p 2222:2222 -p 2223:2223 -v $(pwd)/dl:/home/cowrie/cowrie/dl -v $(pwd)/log:/home/cowrie/cowrie/log ouspg/cowrie

ssh root@172.17.0.2 -p 2222
```

