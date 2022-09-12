---
title: Crar administrador por consola
description: 
date: 2015-09-10
lastmod: 2015-09-10
slug: crear_administrador_windows
image: "covers/windows.png"
tags:
  - windows
  - consola
categories:
  - Windows
---


## Para crear un usuario administrador a través de la consola:

###### 1. Creamos un usuario
`net user /add SuperAdmin`

###### 2. Metemos dentro del grupo *Administradores* el usuario creado
`net localgroup administradores SuperAdmin /add`

###### 3. Asignamos una contraseña al usuario creado
`net user SuperAdmin "contraseña"`
