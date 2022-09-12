---
title: Tareas Pendientes
description: 
date: 2020-03-31
lastmod: 2020-03-31
slug: tareas_pendientes
image: "covers/draft.png"
tags:
  - todo
categories:
  - Linux
---




- [ ] Testear OpenVPN y WireGuard
- [ ] Testear OpenVPN con push routing
- [ ] Porbar a poner routa estatica en tpc, para que acceda a red proxmox (sudo ip route add 10.0.0.0/16 via 192.168.1.254)
- [ ] Leer Paper WireGuard: Next Generation Kernel Network Tunnel
- [ ] get let's encrypt certificate
- [ ] Probar asciiflow.com
- [ ] Upgrading Simple Shells to Fully Interactive TTYs (https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)
- [ ] python -c 'import pty; pty.spawn("/bin/bash")'
- [ ] Makefile -> cat -e -t -v Makefile para detectar si se usan Tab (Bien) o espacios. Tiene que salir: ^M
- [ ] smbtree -b -N
- [ ] latexmk -pvc -pdf file.tex
- [x] usar curl con interfaz especifica en promox para api flash
- [ ] Documentar proxmox + script remove suscription
- [ ] Ctrl + l -> para limiar terminal
- [ ] sudo -l -> para mostrar /etc/sudoers
- [ ] port knocking linux
- [ ] Vim -> :W == :w !sudo tee %
- [ ] Recabar informacion sobre reporistorio Red Team
- [ ] Recabar informacion sobre reporistorio fingerprint (snmp, smtp, http, etc)
- [ ] Comprobar BackupPC funciona scheluder
- [ ] Investgar sobre DetectionLab (https://www.flu-project.com/2020/03/tu-laboratorio-de-Red-Team.html
- [ ] Diseñar taza con nmap (2 imagenes con nmap)
- [x] Proxmox probar health 
- [ ] https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
- [x] Crear script inserte cumpleaños telegram
- [x] Invertigar mount sshfs (https://wiki.archlinux.org/index.php/SSHFS_(Espa%C3%B1ol))
- [ ] https://likegeeks.com/es/servidor-de-correo-linux-postfix/
- [ ] https://munahack.github.io/download.html






Diseñar alias interesastes

```
# User specific aliases and functions

! ssh-add -l > /dev/null && eval "$(ssh-agent -s)" && ssh-add ~/.ssh/services

# Alias
alias ls='ls -lhGQ --color=auto'
alias rm="echo Use trash, or the full path i.e. /bin/rm"
alias which="alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde"
alias web='python3 -m http.server 8080'

# Scripts
~/scripts/cargaKeyPi.sh


export VISUAL=/usr/bin/vim
export EDITOR="$VISUAL"

```

