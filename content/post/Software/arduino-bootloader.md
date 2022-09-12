---
title: Arduino burn bootloader
description: En ocasiones es necesario instalar un bootloader o actualizarlo en una placa Arduino, para realizar esto podemos usar un programador externo o usar otra placa Arduino como programador.
date: 2019-10-08
lastmod: 2019-10-08
slug: arduino-bootloader
image: "covers/software.png"
tags:
  - arduino
  - bootloader
categories:
  - Software
---



# Introducción

En ocasiones es necesario instalar un bootloader o actualizarlo en una placa Arduino, para realizar esto podemos usar un programador externo o usar otra placa Arduino como programador.

Un Arduino actuá como programador, al que se le llamara master y el otro que es al que se le va a instalar el bootloader, se le llamará slave. La comunicación entre el PC y el master se hace a través del protocolo serie de esta placa, y la comunicación entre el master y el slave se hace a través del protocolo SPI.


Este proceso se realizara en dos pasos:

1. El primer paso consiste en programar la Arduino para que actúe como programador.
2. El segundo paso consiste en interconectar los Arduinos y quemar el bootloader.


En este caso especifico se va a usar una Arduino Uno como master y una Arduino Pro Mini como slave.


# Programar Arduino master como ArduinoISP


Para preparar la Arduino master como programador, lo único que será necesario es cargar el Sketch "Arduino as ISP", esto se realiza de la siguiente forma:

1. Cargar el Sketch:

		File > Examples > 11.ArduinoISP > ArduinoISP



1. Seleccionar el tipo de placa al que se le va a cargar el Sketch:

		Tools > Board > Arduino / Genuino Uno



1. Seleccionamos el programador por defecto:

		Tools > Programmer > "AVRISP mkll"



1. Cargar el Sketch:

		Upload

Una vez cargado el Sketch ya podemos proceder a interconectar las Arduinos como master y slave para proceder con el quemado del bootloader.





# Conectar Arduino Pro Mini como slave

Las conexiones se realizan con el protocolo SPI, en la Arduino Uno y Arduino Pro Mini están en los pines 10 al 13, podemos ver las conexión de los pines en la siguiente tabla:


[jtable caption="This is caption" th="0"]
Master (Arduino Uno),Slave (Arduino Pro mini)
Pin 13 (SCK),Pin 13 (SCK)
Pin 12 (MISO),Pin 12 (MISO)
Pin 11 (MOSI),Pin 11 (MOSI)
Pin 10 (SS),Reset
5V,5V
GND,GND
[/jtable]



Podemos ver la imagen de las conexiones realizadas a continuación:


![Conexiones](/images/2019/burn_bootloader.svg){:height="auto" width="100%"}



# Quemar bootloader

Una vez que están realizadas todas las conexiones solo queda quemar el bootloader, para esto hay que seguir los siguientes pasos:


1. Seleccionar el tipo de placa del tipo que es el slave:

		Tools > Board > Arduino Pro or Arduino Pro Mini



1. Seleccionamos el programador:

		Tools > Programmer > "Arduino as ISP"



1. Quemamos el bootloader:

		Tools > Burn Bootloader



Veremos como parpadean las luces de la Arduino master durante unos segundos y después se completara el proceso.








# Esquema placa para quemar el bootloader en un procesador ATmega328P


En el caso de querer quemar el bootloader en una placa microcontroladora ATmega328P, podremos hacerlo siguiendo el siguiente esquema:


![Conexiones](/images/2019/BurnBootloaderEsquematic.svg){:height="auto" width="100%"}

![Conexiones](/images/2019/BurnBootloaderPCB.png){:height="auto" width="100%"}


Podemos descargar el esquemático y el PCB de EasyEDA desde aquí: [Esquemático][BurnBootloaderArduino], [PCB][BurnBootloaderArduinoPCB]













Fuentes: [0][0]

[0]: https://www.luisllamas.es/usar-arduino-para-reprogramar-el-bootloader/


[BurnBootloaderArduino]: /downloads/easyeda/BurnBootloaderArduino.json
[BurnBootloaderArduinoPCB]: /downloads/easyeda/BurnBootloaderArduinoPCB.json