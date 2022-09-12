---
title: autorun script linux systemd
description: 
date: 
lastmod: 
slug: 
image: "covers/linux.png"
tags:
  - 
categories:
  - Linux
---


Title: uso de apt
Date: 2015-11-3 14:25
Modified: 2015-11-3 14:25
Category: Linux
Tags: linux, apt
Slug: comando_apt
Authors: procamora
Summary:

## APT-GET

######Instalar un paquete:
`sudo apt-get install <paquete> `


######Desinstalar un paquete:
`sudo apt-get remove <paquete> `


######Eliminar un paquete incluidos sus ficheros de configuración:
`sudo apt-get purge <paquete> `


######Eliminar de forma automática aquellos paquetes que no se estén utilizando:
`sudo apt-get autoremove `


######Actualizar un paquete a la última versión disponible en el repositorio:
`sudo apt-get update <paquete>`


######Actualizar el sistema. Actualizará todos los paquetes que dispongan de una versión superior dentro de la rama instalada de la distribución:
`sudo apt-get upgrade`


######Actualizar la distribución completa. Actualizará nuestro sistema a la siguiente versión disponible de la distribución:
`sudo apt-get dist-upgrade`


######Descargar únicamente las fuentes de un paquete para manipularlas de forma manual:
`sudo apt-get source <paquete>`


######Limpiar caches, paquetes descargados, etc:
`sudo apt-get clean`

`sudo apt-get autoclean`


######Verificar que no tenemos ninguna dependencia incumplida:
`sudo sudo apt-get check`


## APT-CACHE

######Buscar un paquete en los repositorios, se puede especificar un patrón, expresión regular, el nombre exacto del paquete, etc:
`sudo apt-cache search <paquete>`


######Mostrar información sobre un paquete específico (nombre del paquete, versión, dependencias…):
`sudo apt-cache showpkg <paquete>`


######Mostrar información del paquete incluyendo la descripción, información del paquete como su sitio web, página de bugs…
`sudo apt-cache show <paquete>`


######Mostrar dependencias de un paquete:
`sudo apt-cache depends <paquete>`


######Mostrar los nombres de todos los paquetes instalados en el sistema:
`sudo apt-cache pkgnames`
