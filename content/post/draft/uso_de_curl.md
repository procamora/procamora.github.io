---
title: Uso de curl
description: El comando _curl_ esta diseñado para verificar una url y ademas permite la transferencia de datos. Hace uso de la librería opensource _libcurl_ disponible en todas las distribuciones Linux.
date: 2020-03-19
lastmod: 2020-03-19
slug: uso_de_curl
image: "covers/draft.png"
tags:
  - curl
  - http
  - web
  - post
  - put
  - get
  - delete
categories:
  - Software
---



El comando _curl_ esta diseñado para verificar una url y ademas permite la transferencia de datos. Hace uso de la librería opensource _libcurl_ disponible en todas las distribuciones Linux.




- [Operaciones básicas](#header0)
- [HTTP con curl](#header1):
    - [Gestión certificados](#mark0)
    - [User Agent](#mark1)
    - [Customize headers](#mark2)
    - [Referer](#mark3)
    - [Proxy con autenticación](#mark4)
    - [Cookies](#mark5)
    - [GET](#mark6)
    - [POST](#mark7)
    - [PUT](#mark8)
    - [DELETE](#mark9)
    - [PATCH](#mark10)
    - [MOVE](#mark11)
    - [OPTIONS](#mark12)
    - [MKCOL](#mark13)
- [FTP/FTPS/SFTP/SCP con curl](#header2):
    - [Descarga](#mark14)
    - [Subida](#mark15)
- [SMB con curl](#header3):
- [LDAP/LDAPS con curl](#header4)



El comando Curl es compatible con la siguiente lista de protocolos:

- HTTP y HTTPS
- FTP y FTPS
- IMAP e IMAPS
- POP3 y POP3S
- SMB y SMBS
- SFTP
- SCP
- TELNET
- GOPHER
- LDAP y LDAPS
- SMTP y SMTPS



# Operaciones básicas {#header0}


La sintaxis básica del comando es la siguiente:

```
curl [OPTIONS] [URL]
```


Algunas de las opciones mas relevantes son:


- -#, --progress-bar Make curl display a simple progress bar instead of the more informational standard meter.
- -b, --cookie <name=data> Supply cookie with request. If no =, then specifies the cookie file to use (see -c).
- -c, --cookie-jar <file name> File to save response cookies to.
- -d, --data <data> Send specified data in POST request. Details provided below.
- -f, --fail Fail silently (don't output HTML error form if returned).
- -F, --form <name=content> Submit form data.
- -H, --header <header> Headers to supply with request.
- -i, --include Include HTTP headers in the output.
- -I, --head Fetch headers only.
- -k, --insecure Allow insecure connections to succeed.
- -L, --location Follow redirects.
- -o, --output <file> Write output to . Can use --create-dirs in conjunction with this to create any directories specified in the -o path.
- -O, --remote-name Write output to file named like the remote file (only writes to current directory).
- -s, --silent Silent (quiet) mode. Use with -S to force it to show errors.
- -v, --verbose Provide more information (useful for debugging).
- -w, --write-out <format> Make curl display information on stdout after a completed transfer. See man page for more details on available variables. Convenient way to force curl to append a newline to output: -w "\n" (can add to ~/.curlrc).
- -X, --request The request method to use.




Se puede realizar la peticion por una IP o un interfaz especifico con el flag _--interface_:


```bash
curl --interface eth0:1 http://host.com/

curl --interface 192.168.1.10 http://host.com/
```

# HTTP con curl {#header1}



Es posible reanudar una descarga interrumpida con el siguiente comando:


```bash
curl -C - -O  http://host.com/file.tar
```


Podemos limitar la velocidad de descarga con:

```bash
curl --limit-rate 200k -O http://host.com/file.tar
```

## Gestión certificados {#mark0}


Podemos verificar un certificado SSL con:

```bash
$ curl --cacert cacert.crt http://host.com
```





Podemos ignorar certificado SSL con:


```bash
curl -k http://host.com
```



## User Agent {#mark1}


Podemos indicar un User-Agent especifico con el flag _-A_:

```bash
curl -A 'Mozilla/3.0 (Win95; I)' http://host.com
```


Aquí hay una lista de User-Agent validos:

```
Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15
```



## Customize headers {#mark2}


Podemos modificar las cabeceras con el flag _-H_:


```bash
curl -H "Host: test.example" http://host.com/
curl -H "User-Agent:" http://host.com/
```


## Referer {#mark3}

Podemos indicar que estamos realizando una referencia de otra url con el flag _--referer_:


```bash
curl --referer http://comes-from.example.com https://host.com/
```






## Proxy con autenticación {#mark4}


Podemos indicar un proxy y las credenciales si son necesarias para el proxy con el flag _-u_:


```bash
curl PROXY:8000 -u username:password -O http://host.com/file.tar
```


Si el proxy requiere una autenticación especifica, habría que usar el flag _-U_:

```bash
curl PROXY:8000 -U username:password -O http://host.com/file.tar
```



## Cookies {#mark5}



Podemos navegar usando unas cookies previamente descargadas:


```bash
curl --cookie-jar cookie.txt https://www.host.com/index.html
```


## GET {#mark6}

Para usar el método GET basta con usar el comando:


```bash
curl http://localhost:5000
```


## POST {#mark7}

Para usar el método POST hay que usar _-X POST_. Es necesario indicar el campo data y opcionalmente se puede enviar el Content-Type.





Formas de enviar datos:

```
form urlencoded: -d "param1=value1&param2=value2" or -d @data.txt
json: -d '{"key1":"value1", "key2":"value2"}' or -d @data.json
```


El formato para enviar un POST con un JSON con los flags en formato largo sería:


```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"abc","password":"xyz"}' \
  http://localhost:5000
```


El mismo comando pero en formato corto sería:


```bash
curl -H "Content-Type: application/json" \
  -X POST \
  -d '{"username":"abc","password":"xyz"}' \
  http://localhost:5000
```



Para enviar un fichero en vez de un string se usa el data _@fichero_:

```bash
curl -H "Content-Type: application/json" \
  -X POST \
  -d '@example.json' \
  http://localhost:5000
```


Para enviar un POST con Content-Type www-form podemos ponerlo en el flag _-H_ o eliminarlo, ya que es el Content-Type por defecto en curl.




```bash
curl -H "Content-Type: application/x-www-form-urlencoded" \
  -X POST \
  -d 'username=abc&password=xyz' \
  http://localhost:5000
```




## PUT {#mark8}

El proceso es el mismo que con POST.



```bash
curl -H "Content-Type: application/json" \
  -X PUT \
  -d '{"username":"abc","password":"xyz"}' \
  http://localhost:5000
```




```bash
curl -H "Content-Type: application/x-www-form-urlencoded" \
  -X PUT \
  -d 'username=abc&password=xyz' \
  http://localhost:5000
```



## DELETE {#mark9}


Podemos borrar un fichero con el comando:

```bash
curl -X "DELETE" http://localhost:5000/file
```



## PATCH {#mark10}


```bash
curl -X PATCH http://localhost:5000/file?status=closed
```




## MOVE {#mark11}


Podemos mover un fichero con el comando:

```bash
curl -X MOVE --header 'Destination:http://host.org/new.txt' 'https://host.com/old.txt'
```



## OPTIONS {#mark12}


Podemos ver los métodos que están permitidos en un servidor HTTP con el comando:


```bash
curl -X OPTIONS http://localhost:5000 -i
```





## MKCOL {#mark13}

Podemos crear un directorio con el comando:


```bash
curl -X MKCOL 'https://example.com/new_folder'
```



# FTP/FTPS/SFTP/SCP con curl {#header2}


## Descarga {#mark14}

Podemos descargar ficheros de un servidores FTP con los comandos:

```bash
curl -u username:password -O ftp://server_ftp/test.tar.gz

curl ftps://files.are.secure.com/secrets.txt
curl --ftp-ssl ftp://files.are.secure.com/secrets.txt # equivalente
```


También podemos descargar ficheros de servidores SSH usando SFTP o SCP con los siguientes comandos:


```bash
curl -u username sftp://example.com/etc/issue

# Clave prinvada sin contraseña
curl -u username: --key ~/.ssh/id_rsa scp://example.com/~/file.txt

# Clave privada con contraseña
curl -u username: --key ~/.ssh/id_rsa --pass private_key_password scp://example.com/~/file.txt
```



## Subida {#mark15}


También es posible subir ficheros al servidor FTP con el flag _-T_:


```bash
curl -u username:password -T test.tar.gz ftp://server_ftp
```



# SMB con curl {#header3}

Podemos descargar ficheros de un servidor SMB con el comando:

```bash
curl -u "domain\username:password" smb://server.example.com/share/file.txt
```


También es posible subir ficheros al servidor SMB con el flag _-T_:


```bash
curl -T file.txt -u "domain\username:passwd" smb://server.example.com/share/
```






# LDAP/LDAPS con curl {#header4}


Si se tiene instalada la librería OpenLDAP, es posible usar curl para real;izar peticiones utilizando el protocolo _ldap://_. Por defecto se usará LDAPv3 y en caso de que este falle se usará LDAPv2.


La sintaxis de una consulta con LDAP es algo compleja, para obtener ayuda seria relevante usar el [RFC 2255][rfc2255]


[rfc2255]: https://tools.ietf.org/html/rfc2255


Algunos ejemplos de consultas son las siguientes:


```bash
# LDAP sin autenticación
curl -B "ldap://ldap.frontec.se/o=frontec??sub?mail=*sth.frontec.se"

# LDAP con autenticación
curl -u user:passwd "ldap://ldap.frontec.se/o=frontec??sub?mail=*"
curl "ldap://user:passwd@ldap.frontec.se/o=frontec??sub?mail=*"

# Por defecto se usa autenticacion basica. --basic, --ntlm o --digest
curl --ntlm "ldap://user:passwd@ldap.frontec.se/o=frontec??sub?mail=*"
```


Fuentes: [0][hostinger], [1][subfuzion], [2][haxx] 


[hostinger]: https://www.hostinger.es/tutoriales/comando-curl/

[subfuzion]: https://gist.github.com/subfuzion/08c5d85437d5d4f00e58

[haxx]: https://curl.haxx.se/docs/manual.html














