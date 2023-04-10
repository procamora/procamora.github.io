---
title: "Let's Encrypt Dns Wildcard"
description: In this post we will talk about how to generate an SSL certificate using Let's Encrypt with a Wildcard to a domain and using DNS as a challenge.
date: 2023-03-27T08:57:32+02:00
lastmod: 2023-03-27T08:57:32+02:00
slug: "letsencrypt_dns_wildcard"
image: "covers/linux.png"
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


In this post we will talk about how to generate an SSL certificate using Let's Encrypt with a Wildcard to a domain and using DNS as a challenge.

We will use this type of configuration for two reasons:

- DNS Challenge: Because in our router, we do not have the capacity to open the necessary WEB ports by certbot (80 and 443).
- Wildcard: Because we have total control in the domain, which allows us to have all our services with the same certificate and add the TXT entry required by this configuration.


## Installation

- Fedora: `sudo dnf install certbot`

- MacOs: `brew install certbot`

Further documentation on installation and usage can be found in the [official documentation][certbot_eff].

[certbot_eff]: https://certbot.eff.org/instructions?ws=nginx&os=osx&tab=standard


The commands executed in this post were performed with the following version of certbot:

```bash
sudo certbot --version
certbot 2.4.0
```
## Certificate generation

The command to execute would be as follows:


```bash
sudo certbot certonly --manual --preferred-challenges=dns --email tu_correo_electronico --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.procamora.com
```

In case you want to run it without root, you must pass these parameters:

```
--config-dir=./config/ --work-dir=./work/ --logs-dir=./logs/
```


> In my case, when using zsh the domain must be enclosed in quotation marks or it will fail with the error:
 zsh: no matches found: *.procamora.com

This command is interactive and will ask us a series of questions, one of them is that we create a TXT record in our domain, to verify that we are the owners of this. We do this with the service with which we have purchased the domain.

```
Please deploy a DNS TXT record under the name:

_acme-challenge.procamora.com.

with the following value:

aRyhYI-l8bP_bGCC2tF20RuWLbepjZzshG8rIu3ABtM
```


![dondominio](/images/2023/letsencrypt_dns_wildcard_dondominio.png)


Once created, the change should propagate within seconds or minutes, depending on our DNS provider. We can verify that the TXT entry was created correctly with any of the following commands:

```bash
dig -t txt +short _acme-challenge.procamora.com
host -t txt _acme-challenge.procamora.com
```

If everything went well, the certificates will be created in the following paths (provided by the script, they may change depending on the system).


```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/procamora.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/procamora.com/privkey.pem
This certificate expires on 2023-06-25.
These files will be updated when the certificate renews.
```

And it provides us with information on how to renew the certificate in 3 months when it expires.


```
NEXT STEPS:
- This certificate will not be renewed automatically. Autorenewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same certbot command before the certificate's expiry date.
```



## Cron

My recommendation is to update the certificate with the following command within a cron:


```bash
echo "0 12 */15 * *   root    cd ~/letsencrypt/ && certbot renew" | sudo tee -a /etc/cron.d/letsencrypt
```

> Although the certificate expires in 90 days, I try to renew it every 15 days to avoid that it could expire before I have renewed it, forcing me to generate it again. The cron is every 15 days because this server is not always on.

The official documentation recommends running the following command for automatic renewal:

```bash
echo "0 0,12 * * * root $(command -v python3) -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo $(command -v certbot) renew -q" | sudo tee -a /etc/crontab > /dev/null
```


## Nginx Proxy Manager


The last step would be to use the certificate, in my personal case I use Nginx Proxy Manager for the ease it provides me for the management of hosts and ACLs.

![nginx](/images/2023/letsencrypt_dns_wildcard_nginx.png)


