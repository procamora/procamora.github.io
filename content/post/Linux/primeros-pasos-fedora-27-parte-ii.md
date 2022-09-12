---
title: Primeros pasos Fedora 27 KDE Parte II
description: "En esta segunda parte, haré una configuración del entorno de trabajo (fstab, crontab, .ssh, etc) y den entorno gráfico"
date: 2017-03-30
lastmod: 2017-03-30
slug: primeros-pasos-fedora-27-parte-ii
image: "covers/linux.png"
tags:
  - fedora
  - console
  - fedora27
categories:
  - Linux
---


# Introducción

En esta segunda parte, haré una configuración del entorno de trabajo (fstab, crontab, .ssh, etc) y den entorno gráfico

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
*/7 *	*  *  *	procamora	cd /home/procamora/Documentos/Wiki-Personal/ && bash pushgit.sh >> /tmp/wiki.log 2>&1
```


## Fichero fstab {#mark1}

`vim /etc/fstab`

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
//192.168.1.71/DiscoUSB   /mnt/DescargasPi    cifs      credentials=/home/procamora/.smbcredentials,iocharset=utf8,sec=ntlm  0  0
```


`vim /home/procamora/.smbcredentials`

```bash
#username=xxxxx
#password=xxxxx
```


## Clave privada {#mark2}

COnfiguraremos tanto la clave privada para conectarnos a otros equipos sin necesidad de usar contraseña como la clave publica para que otros de nuestros equipos se conecten a nosotros con nuestra clave privada

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
192.168.1.71    pi
```


## Configuración de aplicaciones con autoarranque

```bash
systemctl enable sshd
systemctl enable smb
systemctl enable nmb
systemctl disable firewalld.service # solo en el pc de casa
```


## Fichero bashrc

Poner para los usuarios: procamora, root

`vim .bashrc`

```bash
echo '
# User specific aliases and functions
alias ls="ls -lhGQ --color=auto"
alias rm="echo Use trash, or the full path i.e. /bin/rm"
alias which="alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde"

export VISUAL=/usr/bin/vim
export EDITOR="$VISUAL"

' >> ~/.bashrc
```



## Configuración de vim


```bash
USERS="root procamora"

# Clonamos repositorio
su -c "git clone --depth=1 https://github.com/amix/vimrc.git /opt/vim_runtime"

# Instalamos para los usuarios seleccionados
su -c "sh /opt/vim_runtime/install_awesome_parameterized.sh /opt/vim_runtime $USERS"

# Dar permiso a los ficheros para los usuarios no root
su -c "chmod 755 /opt/vim_runtime/ -R"
su -c "chown procamora:procamora /home/procamora/.vimrc -R"

# to install for all users with home directories
#sh /opt/vim_runtime/install_awesome_parameterized.sh /opt/vim_runtime --all
```





# Configuración del entorno gráfico {#header1}


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
dir="/home/procamora/"
ln -s /mnt/WD_BLACK/pablojoserocamora@gmail.com $dir # directorio google drive
ln -s /home/procamora/pablojoserocamora@gmail.com/scripts/ $dir # directorio de scripts
ln -s /home/procamora/pablojoserocamora@gmail.com/Musica/* /home/procamora/Música/ # Enlazo todos los discos
```



## Configuración energía

![configuración de la energía](/images/2017/2017-03-31-gestion_energia.png)



## Configuración de aplicaciones con autoarranque


Vamos a `Preferencias del sistema/Arranque y apagado/Autoarranque`

![configuración de la energía](/images/2017/2017-03-31-autoarranque.png)

