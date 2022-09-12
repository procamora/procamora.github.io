---
title: Primeros pasos Fedora 32 KDE Parte II
description: En esta segunda parte, haré una configuración del entorno de trabajo (fstab, crontab, .ssh, etc) y del entorno gráfico.
date: 2020-06-21 1:07
lastmod: 2020-06-21 1:07
slug: primeros-pasos-fedora-32-parte-ii
image: "covers/draft.png"
tags:
  - fedora
  - consola
  - fedora32
  - rpmfusion
  - dnf
categories:
  - Linux
---


# Introducción

En esta segunda parte, haré una configuración del entorno de trabajo (fstab, crontab, .ssh, etc) y del entorno gráfico.

- [Ficheros](#header0)
    - [Fichero crontab](#mark0)
    - [Fichero fstab](#mark1)
    - [Clave privada](#mark2)
- [Entorno grafico](#header1)


# Configuración de ficheros {#header0}

## Fichero crontab {#mark0}

`vim /etc/crontab`

```bash
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
# 0 *	*  *  *	procamora	cd /home/procamora/ && ./rsync_samba.sh >/tmp/rsync.log 2>&1 
# 0 */2	*  *  *	procamora	cd /home/procamora/BoxCryptor/ && ./rsync_i7.sh >/tmp/rsync_gdrive.log 2>&1
0 22	*  *  *	procamora	python3 /home/procamora/scripts/backup.py i7_rsync.sh >> /tmp/rsync_gdrive.log 2>&1
*/7 *	*  *  *	procamora	cd /home/procamora/Documents/Wiki-Personal/ && bash pushgit.sh >> /tmp/wiki.log 2>&1
```



## Fichero fstab {#mark1}

```bash
sudo mkdir -p /mnt/{WD_BLACK,640Gb,pi,zero}
sudo chown $USER:$USER /mnt/{WD_BLACK,640Gb,pi,zero}
vim /etc/fstab
```


```bash
#
# /etc/fstab
# Created by anaconda on Wed Mar 29 21:50:12 2017
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
# Particiones por defecto
UUID=9c64fe32-84c5-4954   /                   ext4      defaults,relatime               1 1
UUID=659ee856-118a-433b   /boot               ext4      defaults,relatime               1 2
UUID=F6DB-090A            /boot/efi           vfat      umask=0077,shortname=winnt      0 2
UUID=7f4fc31b-e92d-4d31   /home               ext4      defaults,relatime               1 2
/dev/mapper/fedora-swap   swap                swap      defaults                        0 0
# Disco NTFS con todos los permisos + posibilidad de usar chmod
UUID=EE3A29F53A29BC09     /mnt/WD_BLACK       ntfs-3g   permissions,locale=es_ES.utf8   0 2
# Disco de red montado por samba
#//192.168.1.71/DiscoUSB   /mnt/DescargasPi    cifs      credentials=/home/procamora/.smbcredentials,iocharset=utf8,sec=ntlm  0  0
```




## Clave privada {#mark2}

Configuraremos tanto la clave privada para conectarnos a otros equipos sin necesidad de usar contraseña como la clave publica para que otros de nuestros equipos se conecten a nosotros con nuestra clave privada

```bash
mkdir -p ~/.ssh
touch ~/.ssh/OpenSSH
vim ~/.ssh/OpenSSH        # guardamos el contenido de la clave privada
chmod 600 ~/.ssh/OpenSSH  # le quitamos los permisos necesarios
ssh-add ~/.ssh/OpenSSH    # ponemos la contraseña y ya tenemos cargada la clave
vim ~/.ssh/authorized_keys # guardamos el contenido de la clave publica
chmod 600 ~/.ssh/authorized_keys  # le quitamos los permisos necesarios
chmod 700 ~/.ssh
```


## Fichero hosts {#mark3}

`vim /etc/hosts`

```bash
127.0.0.1       localhost 4770K localhost4
::1             localhost 4770K localhost6
192.168.1.1     router
192.168.1.59    4770K
192.168.1.55    xiaomi
192.168.1.71    rp3
192.168.1.72    zero
```


## Configuración de aplicaciones con autoarranque

```bash
systemctl enable sshd
#systemctl enable smb
#systemctl enable nmb
systemctl disable firewalld.service # solo en el pc de casa
```




# Configuración del entorno gráfico {#header1}


```bash
DIRS=( Documents Downloads Public Pictures Videos Templates Music Desktop )
for dirs in "${DIRS[@]}"; do
    test $(ls $HOME/$dirs/ | wc -l) = 0 && rm -rf $HOME/$dirs && ln -s /media/data/$dirs $HOME/$dirs
done
test -d $HOME/Programs || ln -s /media/data/Programs $HOME/Programs

kwriteconfig5 --file "$HOME/Documents/.directory" --group "Desktop Entry" --key "Icon" "folder-documents"
kwriteconfig5 --file "$HOME/Downloads/.directory" --group "Desktop Entry" --key "Icon" "folder-downloads"
kwriteconfig5 --file "$HOME/Public/.directory" --group "Desktop Entry" --key "Icon" "folder-public"
kwriteconfig5 --file "$HOME/Pictures/.directory" --group "Desktop Entry" --key "Icon" "folder-pictures"
kwriteconfig5 --file "$HOME/Videos/.directory" --group "Desktop Entry" --key "Icon" "folder-videos"
kwriteconfig5 --file "$HOME/Templates/.directory" --group "Desktop Entry" --key "Icon" "folder-templates"
kwriteconfig5 --file "$HOME/Music/.directory" --group "Desktop Entry" --key "Icon" "folder-music"
kwriteconfig5 --file "$HOME/Desktop/.directory" --group "Desktop Entry" --key "Icon" "desktop"
kwriteconfig5 --file "$HOME/scripts/.directory" --group "Desktop Entry" --key "Icon" "folder-script"
```

## Configuración dolphin

### Configuración de vistas

1. Vamos a `Control/Configurar las barras de herramientas`
    - Abrir tereminal
    - Archivos ocultos

2. Vamos a `Control/Ajustar las propiedades de vista`
    - Ordenar por fecha Descendente
    - Mostar archivos ocultos
    - Aplicar a todas las carpetas
    - Usar estas propiedades de vista como predeterminadas

### Configuración de accesos directos

![Accesos directos dolphin](/images/2017/2017-03-31-acceos_directos_dolphin.png)


```bash
ln -rs /mnt/WD_BLACK/Insync/pablojoserocamora@gmail.com/GoogleDrive ~/pablojoserocamora@gmail.com
ln -s ~/pablojoserocamora@gmail.com/scripts/ ~ # directorio de scripts
ln -s ~/pablojoserocamora@gmail.com/Musica/* ~/Music/ # Enlazo todos los discos
```



## Instalacion de bspwm

```bash
git clone git@github.com:procamora/custom_workspace.git ~/Documents/custom_workspace
cd ~/Documents/custom_workspace
chmod u+x custom_workspace.sh
./custom_workspace.sh all
```
