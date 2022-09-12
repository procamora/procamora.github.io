---
title: Netplan
description: Netplan es la nueva utilidad de Linux para la configuración de red de los sistemas. Se basa en crear un fichero de texto siguiendo las especificaciones YAML. Este fichero tiene que estar ubicado en el directorio _/etc/netplan_. Por defecto se crea el fichero _50-cloud-init.yaml_ que tendrá la primera interfaz puesta en DHCP, a no ser que durante la instalación se haya indicado lo contrario.
date: 2020-03-15
lastmod: 2020-03-15
slug: netplan
image: "covers/draft.png"
tags:
  - netplan
  - network
  - networking
  - ipv4
  - ipv6
  - interfaces
  - ip
  - static
  - dhcp
  - vlan
categories:
  - Linux
---


Netplan es la nueva utilidad de Linux para la configuración de red de los sistemas. Se basa en crear un fichero de texto siguiendo las especificaciones YAML. Este fichero tiene que estar ubicado en el directorio _/etc/netplan_. Por defecto se crea el fichero _50-cloud-init.yaml_ que tendrá la primera interfaz puesta en DHCP, a no ser que durante la instalación se haya indicado lo contrario.


> Es importante destacar que YAML no funciona bien con tabuladores y que aunque no hay una especificación formal de como formatear los ficheros, mi recomendación de usar espacios y que cada subsección este separada por dos espacios del padre. 
También indicar que permite un formato amplio a la hora de especificar las configuraciones, muchas veces se pueden indicar en formato lineal o multi-lineal.


![netplan](/images/2019/netplan_design_overview.svg){:height="auto" width="50%"}



Para modificar las interfaces, lo recomendable es cambiar la extensión de ese fichero, para que netplan no lo reconozca y crear uno nuevo, por ejemplo _01-netcfg.yaml_. Este fichero es el que debería de tener toda la configuración de las interfaces, aunque se puede crear un fichero diferente por cada interfaz.




> Si se tiene la misma interfaz en distintos ficheros y se les asignan IPs en cada uno, se crearan varias IPs virtuales.





Hay que tener en cuenta que netplan admite dos formas de configurar el host:

- NetworkManager: que será utilizado cuando disponemos de entorno gráfico o dejamos que este se encarga de la configuración.
- Systemd-networkd: será usando cuando no disponemos de entorno gráfico o cuando hacemos la configuración manualmente.


A continuación se puede ver un ejemplo de como se especifica estas formas:


```yaml
# Opción Network Manager
network:
  version: 2
  renderer: NetworkManager

# Opción Systemd-networkd
network:
  version: 2
  renderer: networkd
```


# IPv4


A continuación se muestra un ejemplo de un fichero de configuración con tres interfaces. La configuración de estas interfaces también se ven en la siguiente tabla:


| INTERFAZ | IP | VLAN 
|----------|----------|------
| enp0s3 | 10.0.2.16 | No
| enp0s8 | 192.168.10.11 | 100
| enp0s9 | DHCP | No





```yaml
# This file describe the network interfaces avaliable on your system
# For more information, see netplan(5)

network:
  version: 2
  renderer: networkd
  ethernets:
    # IP FIJA
    enp0s3:
      dhcp4: no
      dhcp6: no
      addresses: [10.0.2.16/24]
      gateway4: 10.0.2.2
      nameservers:
        search: [localhost]
        addresses: [1.1.1.1, 9.9.9.9]
```




```yaml
# This file describe the network interfaces avaliable on your system
# For more information, see netplan(5)

network:
  version: 2
  renderer: networkd
  ethernets:
    # IP con VLAN
    enp0s8: {}
    # IP con DHCP
  vlans:
    vlans.100:
      ip: 100
      link: enp0s8
      addresses: [192.168.10.11/24]
```




```yaml
# This file describe the network interfaces avaliable on your system
# For more information, see netplan(5)

network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s9:
      dhcp4: true
```







El fichero completo seria el siguiente:



```yaml
# This file describe the network interfaces avaliable on your system
# For more information, see netplan(5)

network:
  version: 2
  renderer: networkd
  ethernets:
    # IP FIJA
    enp0s3:
      dhcp4: no
      dhcp6: no
      addresses: [10.0.2.16/24]
      gateway4: 10.0.2.2
      nameservers:
        search: [localhost]
        addresses: [1.1.1.1, 9.9.9.9]
    # IP con VLAN
    enp0s8: {}
    # IP con DHCP
    enp0s9:
      dhcp4: true
  vlans:
    vlans.100:
      ip: 100
      link: enp0s8
      addresses: [192.168.10.11/24]
```




# IPv6

También se puede configurar direcciones IPv6, la configuración es prácticamente la misma, solo hay que tener en cuenta dos cambios:

- El formato en el que se introducen las direcciones IP en vez de colocarse en una única linea, tienen que hacerse en una linea por dirección IP.
- La dirección IPv6 tiene que colocarse dentro de comillas.


> Estos cambios no se porque son necesarios, pero es de la única forma que me ha funcionado en las pruebas realizadas.





```yaml
# This file describe the network interfaces avaliable on your system
# For more information, see netplan(5)

network:
  version: 2
  renderer: networkd
  ethernets:
    # IP FIJA
    enp0s3:
      dhcp4: no
      dhcp6: no
      addresses:
        - 10.0.2.16/24
        - "3bb7::15/64"
      gateway4: 10.0.2.2
      gateway6: "3fb7::1"
      nameservers:
        search: [localhost]
        addresses: [1.1.1.1, 9.9.9.9]
    # IP con VLAN
    enp0s8: {}
    # IP con DHCP
    enp0s9:
      dhcp4: true
  vlans:
    vlans.100:
      ip: 100
      link: enp0s8
      addresses: [192.168.10.11/24]
```




Si no se va a usar IPv6 lo mas recomendable es desactivarlo, esto se puede hacer con los siguientes comandos de forma termporal


```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
```



Para hacer os cambios persistentes habría que añadir en el fichero _/etc/sysctl.conf_ las siguientes lineas:


```
net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
```



# Aplicar cambios

Una vez que se ha realizado la configuración necesaria, se puede comprobar que el fichero esta correctamente escrito y aplicar los cambios con los siguientes comandos:


```bash
# Comprobar la configuración
netplan --debug generate

# Aplicar los cambios
netplan --debug apply
```




# Fuentes


Fuentes: [1][netplan], [2][netplan_examples], [3][mytcpip]



[netplan]: https://netplan.io/

[netplan_examples]: https://netplan.io/examples

[mytcpip]:  https://mytcpip.com/2019/05/05/ubuntu-18-04-y-netplan-tutorial-rapido-de-los-cambios-de-networking/