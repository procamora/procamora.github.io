---
title: "Guia Tmux"
description: 
date: 2022-09-25T15:13:17+02:00
lastmod: 2022-09-25T15:13:17+02:00
slug: "Guia_tmux"
image: covers/blue.jpg
hidden: false
draft: true
tags:
  - a
categories:
  - a
---

También es posible darle un nombre a la sesión. Para hacerlo puedes escribir el siguiente comando  al abrir una sesión nueva:

root@osp01:/home/procamora# tmux new -s devstack


Usando los prefijos para controlar Tmux

Tmux se basa en comandos que realizan una tarea específica. Sin embargo, para ejecutar estos comandos, primero debe usarse un prefijo. El prefijo le indica a Tmux que se ejecutará un comando. Por defecto, el prefijo es CTRL + B.

De manera que, la forma correcta de estructurar un comando en Tmux es:

<prefijo> + Comando

Es decir, tienes que presionar las teclas CTRL+B y luego el comando. Por ejemplo, para crear una nueva sesión, el comando sería C. Entonces, para crear una nueva sesión, debes presionar CTRL+B y luego C – CTRL+B, C.

### detach

Luego, usa el comando detach. Entonces, primero ingresa el prefijo presionando CTRL+B y luego, el comando D. Verás un mensaje en la terminal.


### attach

tmux attach -t devstack

si no tiene nombre de sesion
tmux attach -t 0





tmux ls





https://www.hostinger.es/tutoriales/usar-tmux-cheat-sheet