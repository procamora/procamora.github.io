---
title: Import ova proxmox
description: Para convertir una ova generada por Virtualbox o equivalentes en una imagen valida para Proxmox, hay que realizar una serie de pasos, que serian los siguientes.
date: 2020-03-08
lastmod: 2020-03-08
slug: import_ova_proxmox
image: "covers/htb.png"
tags:
  - proxmox
  - virtualbox
categories:
  - Linux
---


Para convertir una ova generada por Virtualbox o equivalentes en una imagen valida para Proxmox, hay que realizar una serie de pasos, que serian los siguientes:

Lo primero que hay que tener en cuenta es que una ova es un archivo tar que contiene tres ficheros

- arch-disk001.vmdk: Contiene el disco.
- arch.mf: Contiene los hash de los otros dos ficheros.
- arch.ovf: Contiene la información de la máquina, para importarla con los mismos ajustes.

El primer  paso sera enviar la ova al servidor, esto se puede hacer fácilmente con el comando _scp_


```bash
scp arch.ova root@192.168.1.254:~
```


Una vez que ya tenemos la máquina dentro de Proxmox tendremos que descomprimir la ova.

```bash
tar xf arch.ova
```

A Partir de este punto tenemos dos métodos para proceder, el primero método es el mas automático, ya que se puede hacer prácticamente todo por consola, en segundo método requiere de interfaz gráfica.




# Método 1 (Pendiente de testear)


Lo primero es saber cual va a ser el _VMid_ de la máquina, para saber cual es el siguiente podemos verlo gráficamente o con el comando _qm list_. Una vez que sabemos el id lo que haremos sera indicarlo en la variable de entorno para que lo usen los siguientes comandos.

El primer paso sera convertir el disco de formato _vmdk_ a formato _qcow2_. Además este comando ya deja el disco en la ruta que usará la máquina virtual cuando se cree.



```bash
VMID=115

qemu-img convert \
 -f vmdk \
 -O qcow2 \
 arch-disk001.vmdk \
 /var/lib/vz/images/$VMID/vm-$VMID-disk-1.qcow2
```


Una vez que esta creado el disco en su ruta unicamente sera necesario crear la máquina usando este disco. En general se puede modificar este comando para que se ajuste mas a los requisitos de la máquina final, pero personalmente me parece mas cómodo y seguro hacerlo gráficamente una vez que este creada.



```bash
NAME="arch"

qm create $VMID \
 --name $NAME \
 --net0 virtio,bridge=vmbr0 \
 --bootdisk virtio0 \
 --ostype l26 \
 --memory 1024 \
 --onboot no \
 --sockets 1 \
 --cores 1 \
 --virtio0 local:$VMID/vm-$VMID-disk-1.qcow2
```


Una vez hecho esto solo seria necesario ajustar la configuración y arrancar la máquina para probar su correcto funcionamiento.



# Método 2

Este método es el que he estado usando y funciona por el momento bastante bien, la diferencia con el otro reside en donde se guardan las imágenes, en este se guardan en _local-lvm_ mientras que en otro se guardan en el disco _local_. Además este proceso es mas gráfico y por lo tanto mas lento.


El primero paso consiste en crear una máquina, se puede hacer gráficamente o con el comando mostrado anteriormente. Lo importante de este paso es que el disco que se crea hay que hacerle _deteach_ y despues borrarlo, ya que no lo vamos a usar.


## CONFIRMAR QUE ESTE COMANDO FUNCIONA BIEN SI PONER EL DISCO

```bash
VMID=115
NAME="arch"

qm create $VMID \
 --name $NAME \
 --net0 virtio,bridge=vmbr0 \
 --bootdisk virtio0 \
 --ostype l26 \
 --memory 1024 \
 --onboot no \
 --sockets 1 \
 --cores 1
```


Una vez que se ha borrado el disco de la imagen, el siguiente paso sera importar el nuevo disco, esto se realiza con el siguiente comando:


```bash
VMID=115

qm importdisk $VMID \
 arch-disk001.vmdk \
 local-lvm
 -format qcow2
```


Finalmente el disco aparece gráficamente, pero no esta conectado con la máquina, es necesario editarlo y darle a aplicar para que se registre accesible para la máquina. También seria posible editar el tipo de conectar usando y ponerlo como SATA o IDE.






> Un dato interesante es la ruta donde se guardan los fichero ISOs subidos gráficamente, esta ruta es: _/var/lib/vz/template/sio/_