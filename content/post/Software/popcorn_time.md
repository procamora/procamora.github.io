---
title: Instalar popcorn-time
description: 
date: 2015-08-02
lastmod: 2015-08-02
slug: popcorn_time
image: "covers/software.png"
tags:
  - popcorn
  - linunx
categories:
  - Software
---

## popcorn time es un programa para streaming de películas y series

##### Primero añadimos lso repositorios a nuestro sistema
`sudo echo "deb http://ppa.launchpad.net/webupd8team/popcorntime/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-popcorntime.list`

`sudo echo "deb-src http://ppa.launchpad.net/webupd8team/popcorntime/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-popcorntime.list`


##### Añadimos la clave publica para certificar que es un paquete valido
`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886`


##### Actualizamos nuestros repositorios
`sudo apt-get update`


##### Instalar popcorn time
`sudo apt-get install popcorn-time`


##### Ya podemos ejecutarlo, se pondrá en la lista de *internet* en gnome
`popcorn-time`
