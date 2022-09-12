---
title: Privatekey_linux
description: 
date: 2015-12-19
lastmod: 2015-12-19
slug: privatekey_linux
image: "covers/linux.png"
tags:
  - ssh
  - github
  - privatekey
categories:
  - Linux
---



fichero OpenSSH.GitHub

`cat ~/.ssh/OpenSSH.GitHub`

```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,4AFCBF8D0AF1ABB6

+G1vplr+DfWb2h/a04BfdsfdsffYcqewrwrewvH5RYcqi4Q4eqhjj5UIXF6cQ5ZY
pqIWBBmC3sIwkztnCZC5KqMYjLy9hbDdFQ5EplW3QN7wV9Bs2PXRl0NIDWMBicjS
em+jS0365JIle+ofYPeGiZIjZq6VxUQJeVgIFG56AWP/Vq9nvHjvblwOl5rFQaLh
nDJT+06jmkhFlN6sdfdfdsfdfS4MdOlPQkJBvfdhOJ4viUYfdjspy2NjuMvXH2Wb
rIHC0wtYFiNhPTCeCXfEXqv7Fhw2bBZM//W/oqleyz+Y5EBlWZLcyqG6FYtHTEkL
Mh6Y4NL8XMqg3Gly9PKH0RfT2mJYJhN1ni1KBn6H6SXzlLU5bKgfM8aNJ9RVS9it
rQ4B38i8HuoS6lOvIAdsfsdffffssffODyrMi0kREuvQC5fhfuQB83cn1lx5u/Ut
ETC......
-----END RSA PRIVATE KEY-----
```

Creamos el directorio para las claves y ponemos las claves en el con los permisos adecuados

```bash
mkdir -p ~/.ssh
touch ~/.ssh/OpenSSH.GitHub
vim ~/.ssh/OpenSSH.GitHub        # guardamos el contenido de la clave privada
chmod 600 ~/.ssh/OpenSSH.GitHub  # le quitamos los permisos necesarios
ssh-add ~/.ssh/OpenSSH.GitHub    # ponemos la contraseña y ya tenemos cargala la clave
```

Si obtenemos este error al cargar la clave con `ssh-add OpenSSH`:

```bash
Could not open a connection to your authentication agent.
```

Entonces tendremos que ejecutar `eval $(ssh-agent)` y colocarlo al final de _.bashrc_ para que se ejecute al inicio de cada sesión.



`ssh -T git@github.com`

```
Resultado
Hi procamora! You've successfully authenticated, but GitHub does not provide shell access.
```

Para hacer que se auto cargue la clave al inicio de la sesión crear un script como este y ponerlo en el arranque de linux, para descargarlo pulse [aquí][script]

```bash
#!/usr/bin/expect -f

set USER [exec whoami]

spawn ssh-add /home/$USER/.ssh/OpenSSH
expect "Enter passphrase for /home/$USER/.ssh/OpenSSH:"
send "PASSWORD$\n";
interact
```

Fuentes: [stackexchange][0]

[0]: http://unix.stackexchange.com/questions/90853/how-can-i-run-ssh-add-automatically-without-password-prompt
[script]: /code/cargaKey.sh