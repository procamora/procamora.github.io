---
title: Primeros pasos Fedora 30 KDE Parte I
description: En esta primera parte pondré todos las librerías y programas que suelo instalar en Fedora 30 con KDE, en la segunda parte haré una configuración del entorno de trabajo (fstab, crontab, .ssh, etc)
date: 2019-04-14
lastmod: 2019-04-14
slug: primeros-pasos-fedora-30-parte-i
image: "covers/linux.png"
tags:
  - fedora
  - console
  - fedora30
  - rpmfusion
  - dnf
categories:
  - Linux
---


# Introducción

En esta primera parte pondré todos las librerías y programas que suelo instalar en Fedora 30, en la segunda parte haré una configuración del entorno de trabajo (fstab, crontab, .ssh, etc)


- [RPMFusion](#mark0)
- [Librerias basicas](#mark1)
- [Compilación](#mark2)
- [Compresión](#mark3)
- [Codecs](#mark4)
- [DVD's](#mark5)
- [Programas basicos](#mark6)
- [HP](#mark7)
- [Insync](#mark8)
- [Pandoc y Latex](#mark9)
- [Spotify](#mark10)
- [Atom](#mark11)
- [Visual Studio Code](#mark12)
- [Skype](#mark13)
- [Teamviewer](#mark14)
- [Dropbox](#mark15)
- [Gitkraken](#mark16)
- [Pycharm](#mark17)
- [Telegram](#mark18)
- [Eclipse](#mark19)
- [Docker y Docker-Compose](#mark27)
- [Google Chrome](#mark21)
- [Google Music](#mark22)
- [system-config-samba](#mark23)
- [Drivers Nvidia](#mark24)
- [Peek](#mark25)
- [Sublime Text 3 y Sublime Merge](#mark26)
- [OpenRazer y Polychromatic](#mark27)



## Importante

Primero tenemos que instalar los drivers de nvidia que están en la sección [Drivers nvidia](#mark24)


## Actualización inicial

Lo primero  que hay que hacer es actualizar el sistema y lo reiniciamos, posiblemente haya una gran cantidad de paquetes a actualizar, junto con la actualización del kernel por lo que después es bueno hacer un reinicio del sistema.

```bash
sudo dnf update
reboot
```

## Eliminar programas no necesarios

```bash
sudo dnf remove dragon calligra-core
```



## Añadir repositorio RPMFusion {#mark0}

Este repositorio es necesario para varios paquetes que instalaremos después (contiene programas importantes y paquetes nonfree).

```bash
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```


## Paquetes y librerías que mas uso {#mark1}

Conjunto de librerías y utilidades básicas, traducciones de programas a español, corrector ortográficos, etc.

```bash
sudo dnf -y install kde-i18n-Spanish mythes-es hyphen-es autocorr-es hunspell-es langpacks-es \
aspell-es man-pages-es-extra kde-l10n-es android-tools expect flac-libs \
fluid-soundfont-common  encfs samba wine curl system-config-users meld youtube-dl \
wget iftop trash-cli
```

## Java

```bash
sudo dnf -y install java-openjdk java-1.8.0-openjdk-javadoc java-1.8.0-openjdk-devel
```


## Herramientas básicas de compilación {#mark2}

Conjunto de librerías básicas de compilación

```bash
sudo dnf -y install kernel-headers kernel-devel git make libxml2 libxml2-devel mercurial \
cmake python-devel python3-devel gcc-c++ dkms openssl-devel
```


# Compresión y descompresión {#mark3}

Conjunto de librerías básicas de compresión y descompresión

```bash
sudo dnf -y install p7zip p7zip-plugins zip unzip unrar
```


## Codecs {#mark4}

Conjunto de codecs necesarios para la reproducción de audio con código privado (mp3, etc)

```bash
sudo dnf -y install gstreamer gstreamer1-libav gstreamer1-plugins-bad-free-extras \
gstreamer1-plugins-bad-freeworld gstreamer1-plugins-good-extras pavucontrol \
gstreamer-ffmpeg gstreamer-plugins-bad gstreamer-plugins-bad-free-extras \
gstreamer-plugins-ugly ffmpeg ffmpeg-libs libmatroska xvidcore libva-vdpau-driver \
libvdpau libvdpau-devel gstreamer1-vaapi gstreamer1-plugins-base-tools mencoder \
alsa-firmware gstreamer1-plugins-ugly
```


## Soporte para DVD's {#mark5}

Conjunto de librerías necesarias para la reproducción de DVD's

```bash
sudo dnf -y install lsdvd libdvbpsi libdvdread libdvdnav
```


## Programas básicos {#mark6}

```bash
sudo dnf -y install VirtualBox vim yakuake libreoffice libreoffice-langpack-es \
gnome-disk-utility sqlitebrowser gimp vlc fritzing kdenlive frei0r-plugins \
calibre picard chromaprint-tools arduino vokoscreen filezilla
```


## Dispositivos HP (impresora) {#mark7}

```bash
sudo dnf -y install hplip hplip-common libsane-hpaio hplip-gui
```


# Insync {#mark8}

```bash
sudo rpm --import https://d2t3ff60b2tol4.cloudfront.net/repomd.xml.key
sudo echo "[insync]
name=insync repo
baseurl=http://yum.insynchq.com/fedora/29/
gpgcheck=1
gpgkey=https://d2t3ff60b2tol4.cloudfront.net/repomd.xml.key
enabled=1
metadata_expire=120m" > /etc/yum.repos.d/insync.repo
sudo dnf install insync
```


# Pandoc y Latex {#mark9}

```bash
sudo dnf -y install pandoc texstudio texlive texlive texlive-latex texlive-xetex texlive-xetex-def \
texlive-collection-latexrecommended texlive-collection-xetex texlive-collection-latex
```

También serán necesarias un conjunto de librerías de Latex:

```bash
sudo dnf -y install texlive-matlab-prettifier texlive-apacite texlive-breakcites texlive-xpatch \
texlive-multirow texlive-tikzpagenodes texlive-tikzmark texlive-pgfplots texlive-glossaries-spanish \
texlive-anyfontsize texlive-framed texlive-mdframed texlive-todonotes texlive-glossaries \
texlive-IEEEtran.noarch texlive-textpos
```

## Spotify {#mark10}

```bash
sudo dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo
sudo dnf -y install spotify-client
```


## Atom {#mark11}

```bash
programa="atom.x86_64.rpm"
wget -O $programa https://atom.io/download/rpm
sudo dnf -y install $programa
rm $programa
```


## Visual Studio Code {#mark12}

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
dnf check-update
sudo dnf -y install code
```


## Skype {#mark13}

```bash
sudo dnf -y install https://go.skype.com/skypeforlinux-64.rpm
```


## Teamviewer {#mark14}

```bash
sudo dnf -y install https://download.teamviewer.com/download/linux/teamviewer.x86_64.rpm
```


## Dropbox {#mark15}

```bash
sudo dnf -y install https://www.dropbox.com/download?dl=packages/fedora/nautilus-dropbox-2015.10.28-1.fedora.x86_64.rpm
sudo dnf -y install python-gpgme
```


## Gitkraken {#mark16}

```bash
programa="gitkraken-amd64.tar.gz"
wget -O $programa https://release.gitkraken.com/linux/gitkraken-amd64.tar.gz
mv $programa ~/Programas/ && cd ~/Programas/
tar -xvf $programa && rm $programa && cd -
```


## Pycharm Community {#mark17}

```bash
programa="pycharm-community-2017.1.tar.gz"
wget -O $programa https://download.jetbrains.com/python/pycharm-community-2017.1.tar.gz
mv $programa ~/Programas/ && cd ~/Programas/
tar -xvf $programa && rm $programa && cd -
```


## Telegram {#mark18}

```bash
programa="telegram.tar.xz"
wget -O $programa https://tdesktop.com/linux
mv $programa ~/Programas/ && cd ~/Programas/
tar -xvf $programa && rm $programa && cd -
```


## Eclipse {#mark19}

```bash
programa="eclipse-inst-linux64.tar.gz"
wget -O $programa http://mirror.ibcp.fr/pub/eclipse//oomph/epp/neon/R2a/eclipse-inst-linux64.tar.gz
mv $programa ~/Programas/ && cd ~/Programas/
tar -xvf $programa && rm $programa && cd -
```


## Docker y Docker-Compose  {#mark27}




```bash
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Fuentes: [docker][docker] y [docker-compose][docker-compose]


[docker]: https://docs.docker.com/install/linux/docker-ce/fedora/
[docker-compose]: https://docs.docker.com/compose/install/




## Google Chrome {#mark21}

Descargar RPM de aqui: [url][gchrome]

[gchrome]: https://www.google.com/chrome/browser/desktop/index.html


## Google Music {#mark22}

Descargar RPM de aqui: [url][gmusic]

[gmusic]: https://www.googleplaymusicdesktopplayer.com/#!


## system-config-samba {#mark23}

Descargar RPM de aqui: [url][system-config-samba]

[system-config-samba]: https://rpmfind.net/linux/rpm2html/search.php?query=system-config-samba



## Instalar drivers Nvidia {#mark24}

Opcion recomendable

Primero instalamos los repositorios que necesitamos [url][nvidia_conf]


```bash
#RPM Fusion free for Fedora 30
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

#RPM Fusion nonfree for Fedora 30
sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Enable access to both the free and the nonfree repository
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Una vez instalados instalamos los drivers de nvidia [url][nvidia_inst]


```bash
sudo dnf -y install xorg-x11-drv-nvidia akmod-nvidia
sudo dnf -y install xorg-x11-drv-nvidia-cuda #optional for cuda/nvdec/nvenc support
sudo dnf update -y
```


[nvidia_conf]: https://rpmfusion.org/Configuration

[nvidia_inst]: https://rpmfusion.org/Howto/NVIDIA#Legacy_GeForce_6.2F7




Opcion **no recomendable** pero que funciona:

```bash
https://www.if-not-true-then-false.com/2015/fedora-nvidia-guide/
```



Fuente: [url][urlnvidia]

[urlnvidia]: http://unix.stackexchange.com/questions/251629/how-to-install-nvidia-proprietary-drivers-on-fedora-23



## Peek para grabar la pantalla y crear gif/mp4 {#mark25}

```bash
sudo dnf config-manager --add-repo http://download.opensuse.org/repositories/home:/Bajoja/Fedora_29/home:Bajoja.repo
sudo dnf -y install peek
```


## Sublime Text 3 y Sublime Merge {#mark26}

```bash
sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
sudo dnf -y install sublime-text sublime-merge
```



## OpenRazer y Polychromatic {#mark27}

```bash
# Due to a bug in Fedora, the wrong kernel headers (kernel-debug-devel) may be installed and cause OpenRazer to fail installation. 
sudo dnf install kernel-devel
sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/hardware:razer/Fedora_30/hardware:razer.repo
sudo dnf install openrazer-meta polychromatic
# reboot
```





Url [gitgub][peek]

[peek]: https://github.com/phw/peek#fedora

