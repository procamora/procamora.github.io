---
title: "Let's Encrypt Dns Wildcard"
description: En este post hablaremos de como generar un certificado SSL usando Let's Encrypt con un Wildcard a un dominio y usando como reto DNS.
date: 2023-03-27T08:57:32+02:00
lastmod: 2023-03-27T08:57:32+02:00
slug: "letsencrypt_dns_wildcard"
image: "covers/security.png"
hidden: false
draft: false
tags:
  - letsencrypt
  - ssl
  - https
  - nginx
  - ecdsa
categories:
  - Security
---


En este post hablaremos de como generar un certificado SSL usando Let's Encrypt con un Wildcard a un dominio y usando como reto DNS.


Usaremos este tipo de configuración por dos motivos:

- Reto DNS: Debido a que en nuestro router no tenemos capacidad de abrir los puertos WEB necesarios por certbot (80 y 443).
- Wildcard: Debido a que tenemos control total en el dominio, lo que nos permitirá tener todos nuestros servicios con el mismo certificado y añadir la entrada TXT que requiere esta configuración.



## Instalación

- Fedora: `sudo dnf install certbot`

- MacOs: `brew install certbot`

Podemos encontrar el resto de documentación sobre instalación y uso en la [documentación oficial][certbot_eff].


[certbot_eff]: https://certbot.eff.org/instructions?ws=nginx&os=osx&tab=standard


Los comandos ejecutados en este post se han realizado con la siguiente versión de certbot:

```bash
sudo certbot --version
certbot 2.4.0
```

## Generación del certificado

El comando a ejecutar sería el siguiente:


```bash
sudo certbot certonly --manual --preferred-challenges=dns --email tu_correo_electronico --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.procamora.com
```

En el caso de que se quiera ejecutar sin ser root, se deben pasar estos parámetros:

```
--config-dir=./config/ --work-dir=./work/ --logs-dir=./logs/
```


> En mi caso, al usar zsh el dominio debe de ir entrecomillado o fallará con el error:
 zsh: no matches found: *.procamora.com

Este comando es interactivo y nos hará una serie de preguntas, una de ellas es que creemos un registro TXT en nuestro dominio, para verificar que somos los dueños de este. Esto lo realizamos con el servicio con el que tengamos comprado el dominio.


```
Please deploy a DNS TXT record under the name:

_acme-challenge.procamora.com.

with the following value:

aRyhYI-l8bP_bGCC2tF20RuWLbepjZzshG8rIu3ABtM
```


![dondominio](/images/2023/letsencrypt_dns_wildcard_dondominio.png)


Una vez creado, debería de propagarse el cambio en segundos o minutos, dependiendo de nuestro proveedor de DNS. Podemos verificar que se creó bien la entrada TXT con cualquiera de los siguientes comandos:


```bash
dig -t txt +short _acme-challenge.procamora.com
host -t txt _acme-challenge.procamora.com
```

Si todo ha ido bien, se crearán los certificados en las siguientes rutas (las proporciona el script, pueden cambiar dependiendo del sistema).

```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/procamora.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/procamora.com/privkey.pem
This certificate expires on 2023-06-25.
These files will be updated when the certificate renews.
```

Y nos proporciona la información de como renovar el certificado dentro de 3 meses cuando caduque.

```
NEXT STEPS:
- This certificate will not be renewed automatically. Autorenewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same certbot command before the certificate's expiry date.
```



## Cron

Mi recomendación es actualizar el certificado con el siguiente comando dentro de un cron:

```bash
echo "0 12 */15 * *   root    cd ~/letsencrypt/ && certbot renew" | sudo tee -a /etc/cron.d/letsencrypt
```

> Aunque el certificado caduca en 90 días, yo intento renovarlo cada 15 dias para evitar que me pueda caducar antes de que lo haya renovado, obligandome a volver a generarlo. El cron es cada 15 días debido a que este servidor no siempre está encendido.


La documentación oficial recomienda ejecutar el siguiente comando para la renovación automática:

```bash
echo "0 0,12 * * * root $(command -v python3) -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo $(command -v certbot) renew -q" | sudo tee -a /etc/crontab > /dev/null
```


## Nginx Proxy Manager


El último paso sería usar el certificado, en mi caso personal uso Nginx Proxy Manager por la facilidad que me proporciona para la gestión de hosts y ACLs.

![nginx](/images/2023/letsencrypt_dns_wildcard_nginx.png)


