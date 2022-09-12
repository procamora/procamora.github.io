---
title: Virtualbox cli
description: 
date: 2019-10-17
lastmod: 2019-10-17
slug: virtualbox-cli
image: "covers/software.png"
tags:
  - virtualbox
  - console
categories:
  - Software
---




# Listar maquinas virtuales

```bash
VBoxManage list vms
```


```
"FedoraServer" {e5cfa75c-0145-4de8-94ca-fa3357563d6a}
"win7_drive_UNI" {be4acbeb-3920-4ada-9d39-00c27adc785c}
"Kali" {f355d814-0561-49ea-90a2-71d9124d2957}
```




# Arrancar una maquina 

Se puede arrancar una maquina virutal de dos formas distintas, con el nombre de la maquina o con su identificador.


```bash
VBoxManage startvm "Kali"
VBoxManage startvm f355d814-0561-49ea-90a2-71d9124d2957
```



# Pausar una maquina


```bash
VBoxManage controlvm "Kali" pause
```


# Reiniciar maquina pausada

```bash
VBoxManage controlvm "Kali" resume
```


# Reiniciar maquina inmediatamente

```bash
VBoxManage controlvm "Kali" reset
```

# Apagar maquina


```bash
VBoxManage controlvm "Kali" poweroff
```


# Guardar el estado de una maquina


```bash
VBoxManage controlvm "Kali" savestate
```





# Exportar maquinas virtuales

Se pueden exportan en un unico ova todas las maquinas que se deseen

```bash
vboxmanage export "s1_lan" "s1_dmz" -o S1.ova
``` 





# Reducir el tamaño que ocupa en disco la maquina


```bash
#!/bin/bash

#vboxmanage modifymedium --compact /path/to/thedisk.vdi
#vboxmanage modifyhd /path/to/thedisk.vdi --compact

script='vboxmanage modifyhd '

find . -type f -name "*.vdi" -exec $script {} --compact \;
```








[Fuente1]: https://www.garron.me/en/go2linux/vboxmanage-control-and-manage-virtualbox-command-line.html
