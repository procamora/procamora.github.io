---
title: Usos de samba
description: 
date: 2016-04-22
lastmod: 2016-04-22
slug: usos-de-samba
image: "covers/draft.png"
tags:
  - samba
categories:
  - Software
---





###Crear usuario
`sudo useradd -s /bin/true username`


###Asignarle contraseña
```
sudo smbpasswd -L -a username
sudo smbpasswd -L -e username
```



###Listar usuarios samba
```
sudo pdbedit -L -v
```


testparm /etc/samba/smb.conf















