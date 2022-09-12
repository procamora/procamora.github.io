---
title: VirtualBox Guest Additions
description: "Para instalar los Guest Additions en VirtualBox desde la ISO que proporciona, es necesario compilarlos y por ende tener las librerías de compilación necesarias. Estas librerías son:"
date: 2020-04-07
lastmod: 2020-04-07
slug: virtualbox_guest_additions
image: "covers/linux.png"
tags:
  - virtualbox
  - ubuntu
  - fedora
  - opensuse
  - debian
  - guest additions
  - linux mint
categories:
  - Linux
---


Para instalar los Guest Additions en VirtualBox desde la ISO que proporciona, es necesario compilarlos y por ende tener las librerías de compilación necesarias. Estas librerías son:



##  Debian / Ubuntu / Linux Mint


En sistemas basados en Debian habría que instalar las siguientes herramientas de compilación, después reiniciar y ya después montar la ISO y ejecutar el script.


```bash
sudo apt install gcc make perl dkms linux-headers-$(uname -r) build-essential
reboot
# Montar ISO y ejecutar script
```


Como excepción, en Ubuntu podemos instalar los Guest Additions directamente desde los repositorios con:

```bash
sudo apt install virtualbox-guest-x11 virtualbox-guest-utils virtualbox-guest-dkms
```




## Fedora

En Fedora los Guest Additions ya vienen instalados por defecto por lo que no debería ser necesario hacer nada, pero en caso de querer instalarlos desde el ISO, habría que instalar:

```bash
sudo dnf update kernel*
sudo dnf install gcc automake make kernel-headers kernel-devel perl dkms elfutils-libelf-devel
# Montar ISO y ejecutar script
```









## openSUSE

En openSUSE habría que instalar las siguientes herramientas de compilación, y ya después montar la ISO y ejecutar el script.



```bash
sudo zypper install gcc make dkms kernel-devel kernel-default-devel
# Montar ISO y ejecutar script
```









https://www.linuxuprising.com/2019/01/manual-virtualbox-guest-additions.html
