---
title: Uso telegram en Arduino WeMos
description: Instalar la tarjeta *esp8266* en el IDE de arduino para poder configurar una placa Wemos con la que tener un bot de telegram. 
date: 2016-09-06
lastmod: 2016-09-06
slug: uso-telegram-en-arduino-wemos
image: "covers/programming.png"
tags:
  - wemos
  - arduino
  - telegram
  - telegrambot
  - esp8266
categories:
  - Programacion
---


## Introducción:

Instalar la tarjeta *esp8266* en el IDE de arduino para poder configurar una placa Wemos con la que tener un bot de telegram.


## Requisitos previos:

Tener instalado Arduino IDE

- Linux:

```bash
#Fedora y derivadas
sudo dnf install arduino

#Debian y derivados
sudo apt-get install arduino
```
	
- Resto:

	- [Pagina oficial de arduino][arduino]

[arduino]: https://www.arduino.cc/en/Main/Software



## Instalación de la tarjeta ESP8266

1. En el IDE de arduino vamos a *Archivo/Preferencias* y añadimos una nueva tarjeta en el Gestor de URLs Adicionales de Tarjetas.

La tarjeta que hay que añadir es:

`http://arduino.esp8266.com/stable/package_esp8266com_index.json`

![preferencias](/images/2017/preferencias.png)

>  Puede agregar varias URL, separándolas con comas.


2. Instalamos la nueva placa, para eso vamos a *Herramientas/Placa/Gestor de tarjetas* y buscamos la placa `esp8266` y le damos a instalar.

![placas](/images/2017/placas.png)


3. Una vez instalada ya podemos seleccionar la placa y configurarla.

```
Seleccionamos la placa: WeMos D1 R2 & mini

Upload Using:
Serial – Use USB port on board to upload flash
OTA – Use OTA to upload flash

CPU Frequency:
80MHz
160MHz

Flash Size:
4M (3M SPIFFS) – 3M File system size
4M (1M SPIFFS) – 1M File system size

Upload Speed:
921600 bps – recommend
```

![wemos](/images/2017/wemos.png)



## Instalacion de los ejemplos de uso para la placa Wemos

1. Nos descargamos el [repositorio de ejemplos de Wemos][D1_mini_Examples] (como un zip)


2. Renombramos el zip como D1_mini_Examples

3. En *Programa/Incluir librería/Añadir librería .ZIP* seleccionamos la librería para que se importe y ya esta lista para ser usada.

![ejemplos](/images/2017/ejemploswemos.png)

[D1_mini_Examples]: https://github.com/wemos/D1_mini_Examples



## Instalación de la librería Universal Telegram Bot Library


1. Descargar la librería [Universal Telegram Bot Library][telebot]

2. Añadir la librería al IDE de arduino y ya la podremos usar


[telebot]: https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot

#### IMPORTANTE:

A la hora de hacer la conexión WIFI los ejemplos por defecto no funcionan correctamente

```c
void bien() {
  Serial.begin(115200);
  WiFi.begin(SSID_WIFI, PASS_WIFI);  //definidas en credentials.h
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi conectado");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void mal() {
  Serial.begin(115200);
  while (WiFi.begin(ssid, password) != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  IPAddress ip = WiFi.localIP();
  Serial.println(ip);
}
```
