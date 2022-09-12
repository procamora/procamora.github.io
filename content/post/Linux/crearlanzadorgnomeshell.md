---
title: Crear Lanzador GnomeShell
description: Para crear accesos directos en el menu de gnome shell tienes que tener un fichero en.
date: 2015-12-06
lastmod: 2015-12-06
slug: crearlanzadorgnomeshell
image: "covers/linux.png"
tags:
  - gnome shell
categories:
  - Linux
---

Title: Crear Lanzador GnomeShell
Date: 2015-12-6 17:30
Category: Linux
Tags: linux, gnome shell
Slug: crearlanzadorgnomeshell
Summary: Para crear accesos directos en el menu de gnome shell tienes que tener un fichero en.
Status: published


Below is a sample of desktop file:
```
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Application Name
Comment=Application description
Icon=/path/to/icon.xpm
Exec=/path/to/application/executable
Terminal=false
Categories=Tags;Describing;Application
```

Explanation

* `[Desktop Entry]` the `Desktop Entry` group header identifies the file as a desktop entry
* `Type` the type of the entry, valid values are `Application`, `Link` and `Directory`
* `Encoding` the character encoding of the desktop file
* `Name` the application name visible in menus or launchers
* `Comment` a description of the application used in tooltips
* `Icon` the icon shown for the application in menus or launchers
* `Exec` the command that is used to start the application from a shell.
* `Terminal` whether the application should be run in a terminal, valid values are true or false
* `Categories` semi-colon (`;`) separated list of menu categories in which the entry should be shown


Command line arguments in the Exec key can be signified with the following variables:

* `%f` a single filename.
* `%F` multiple filenames.
* `%u` a single URL.
* `%U` multiple URLs.
* `%d` a single directory. Used in conjunction with %f to locate a file.
* `%D` multiple directories. Used in conjunction with %F to locate files.
* `%n` a single filename without a path.
* `%N` multiple filenames without paths.
* `%k` a URI or local filename of the location of the desktop file.
* `%v` the name of the Device entry.

Este serie un ejemplo de un fichero

`vim /usr/share/applications/thunderbird.desktop`

```
[Desktop Entry]
Encoding=UTF-8
Name=Thunderbird
Comment=Access the Internet
Exec=/opt/thunderbird/thunderbird
Terminal=false
Icon=/opt/thunderbird/icons/logo.png
Type=Application
Categories=Networkr;
```


##Importante
Para hacer que se pueda hacer: "abrir con" de cualquier tipo de fichero/extension hay que añadir **%F**

`Exec=geany %F`

Fuentes: [1][1]

[1]: http://unix.stackexchange.com/questions/103213/how-can-i-add-an-application-to-the-gnome-window-manager

