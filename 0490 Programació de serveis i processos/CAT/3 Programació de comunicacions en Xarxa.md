# 3. Programació de comunicacions en xarxa

## 1. Comunicació entre aplicacions

La comunicació entre aplicacions és un component fonamental de la majoria de sistemes informàtics moderns. En aquest context, diverses aplicacions - tant en un mateix dispositiu com a través d'una xarxa - intercanvien dades i informació.

Aquesta interacció permet que les aplicacions realitzin funcions complexes, compartint recursos, dades i funcionalitats.

En el procés de comunicació es distingeix:

* Missatge
* Emissor
* Receptor
* Paquet
* Canal de comunicació
* Protocol de comunicacions

### Procés de comunicació

![Procés de comunicació](../img/3_1%20proces%20comunicacio.png)

### Conceptes Bàsics

**Interfície de Programació d'Aplicacions (API)**: Les APIs permeten que diferents programes interactuïn entre si, definint un conjunt de regles i protocols per aquesta interacció. Per exemple, una aplicació de temps pot utilitzar una API per obtenir dades meteorològiques d'un servei extern.

**Protocol de Comunicació**: Els protocols com HTTP, TCP/IP, i WebSocket defineixen les normes per a l'intercanvi de dades. Aquests protocols asseguren que les dades enviades i rebudes siguin enteses per ambdues parts

## 2. Exemples d’arquitectures

Exemples d'arquitectures:

* Arquitectura client-servidor.
* Arquitectura de grup.
* Arquitectura peer-to-peer.

### Rols client i servidor

En la comunicació en xarxa, generalment es parla de dos rols principals: client i servidor. El servidor ofereix recursos o serveis, mentre que el client els consumeix. Per exemple, en una aplicació web, el servidor allotja la web i la base de dades, mentre que el client és el navegador que l'usuari utilitza per accedir a la web.

És a dir, el model client-servidor defineix com dues parts d'un sistema interactuen per completar operacions. Aquest model és una part essencial en la majoria de les aplicacions de xarxa modernes.

#### Definició dels Rols

**Servidor**: És el sistema que proporciona recursos o serveis. Aquest pot ser una màquina física o un programari que s'executa en una màquina. El servidor escolta les peticions dels clients, processa aquestes peticions, i envia una resposta.

**Client**: El client és l'entitat que inicia les peticions cap al servidor. Aquests poden ser usuaris humans interactuant amb una aplicació o altres sistemes informàtics. El client utilitza els serveis o recursos que el servidor posa a disposició.

#### Arquitectura client-servidor

![Arquitectura client-servidor](../img/3_2%20arquitectura%20client%20servidor.png)

### Comunicacions en grup

És l'alternativa més comuna al model client/servidor.

En aquest model no hi ha rols diferenciats.

En la comunicació en grup hi ha un conjunt de dos o més elements (processos, aplicacions, etc.) que cooperen en un treball comú.

Aquest conjunt s'anomena grup, i els elements que el formen es consideren tots iguals, sense rols ni jerarquies definides.

Els missatges es transmeten mitjançant radiat.

#### Arquitectura de grup

![Arquitectura de grup](../img/3_3%20arquitectura%20grup.png)

### Models híbrids

Les aplicacions distribuïdes més avançades solen tenir requisits de comunicacions molt complexos, que requereixen models de comunicacions sofisticats.

En molts casos, els models de comunicacions reals implementats en aquestes aplicacions barregen conceptes del model client/servidor i la comunicació en grup, donant lloc a enfocaments híbrids, com les xarxes peer-to-peer (P2P).

#### Xarxes peer-to-peer

Una xarxa P2P està formada per un grup d'elements distribuïts que col·laboren amb un objectiu comú.

Qualsevol element pot exercir els rols de servidor o client, com si fos un model client/servidor.

Les xarxes P2P puguin oferir serveis de forma similar al model client/servidor.

Qualsevol aplicació es pot connectar a la xarxa com un client, localitzar un servidor i enviar-li una petició.

Si roman a la xarxa P2P, amb el temps aquest mateix client pot fer al seu torn de servidor per a altres elements de la xarxa.

#### Arquitectura peer-to-peer

![Arquitectura peer-to-peer](../img/3_4%20arquitectura%20peer%20to%20peer.png)

## 3. Bases de la comunicació entre aplicacions

La comunicació entre aplicacions és un pilar fonamental en el desenvolupament de software, especialment en entorns de xarxa.

Aquesta secció explora els fonaments d'aquesta comunicació, destacant la importància dels **protocols**, **elements de les xarxes**, **models** i els conceptes clau per entendre com les aplicacions intercanvien informació.

### Protocols de Comunicació

Ja hem xerrat de protocols, però uns exemples són:

* **TCP/IP**: Aquest és un conjunt de protocols que regeixen la majoria de les comunicacions a Internet. TCP (Transmission Control Protocol) assegura la transmissió fiable de dades, mentre que IP (Internet Protocol) s'encarrega de l'enviament de paquets de dades.
* **HTTP/HTTPS**: El protocol HTTP (Hypertext Transfer Protocol) és àmpliament utilitzat en aplicacions web per a la transferència de dades. HTTPS (HTTP Secure) és la versió segura d'HTTP, que utilitza encriptació per protegir les dades.

### Elements de la Xarxa

* **Adreces IP i Ports**: Cada dispositiu connectat a una xarxa té una adreça IP única. Els ports permeten a múltiples serveis operar en un mateix dispositiu, amb cada servei escoltant en un port específic.
* **DNS** (Sistema de Noms de Domini): El DNS tradueix els noms de domini amigables per a humans (com ara <www.example.com>) en adreces IP.

### Models de Xarxa

* **Model OSI**: El Model de Referència OSI (Open Systems Interconnection) divideix les funcions de la xarxa en set capes, des de la capa física fins a l'aplicació. Cada capa té una funció específica en el procés de comunicació.
* **Model TCP/IP**: Aquest model simplifica les capes del model OSI en quatre capes (enllaç de dades, internet, transport, i aplicació) i és el model utilitzat en la pràctica per a Internet.

### Pila de protocols TCP/IP

![Pila de protocols TCP/IP](../img/3_5%20pila%20tcp%20ip.png)

Font: <https://es.wikipedia.org/wiki/Familia_de_protocolos_de_internet>

### Exemples en Java

En Java, la comunicació en xarxa es pot realitzar mitjançant l'ús de sockets TCP (Transmission Control Protocol) o UDP (User Datagram Protocol).

**TCP**: Es basa en connexions, és a dir, abans que dos dispositius comencin a intercanviar dades, estableixen una connexió i mantenen aquesta connexió oberta durant tota la transmissió. És útil per a dades que necessiten fiabilitat i ordre en la transmissió.

```java
// Creació d'un socket client
Socket socket = new Socket("hostname", port);
```

**UDP**: A diferència del TCP, UDP envia paquets sense establir una connexió prèvia, el que pot resultar en una major velocitat però menor fiabilitat.

```java
// Creació d'un socket UDP
DatagramSocket socket = new DatagramSocket();
```

**Utilització de APIs de Xarxa en Java**: Java proporciona diverses classes i interfícies en el paquet java.net per a la gestió de la comunicació en xarxa. Aquestes inclouen classes com URL, URLConnection, Socket, i ServerSocket.

```java
URL url = new URL("<http://example.com>");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
```

## 4. Elements de programació d’aplicacions en xarxa

La programació d’aplicacions en xarxa requereix un conjunt específic de coneixements i eines. Aquestes eines i components permeten a les aplicacions comunicar-se eficientment a través de xarxes, gestionar múltiples clients simultàniament, i assegurar la seguretat de les dades transmeses.

### Sockets en Java

Els sockets són el mecanisme de comunicació bàsic fonamental que es fa servir per fer transferències d'informació entre aplicacions.

Proporcionen una abstracció de la pila de protocols.

Un socket (en anglès, literalment, un endoll) representa l'extrem d'un canal de comunicació establert entre un emissor i un receptor.

En Java, java.net.Socket s'utilitza per a la comunicació TCP, mentre que java.net.DatagramSocket s'utilitza per a la comunicació UDP.

**Creació de Sockets**: Un socket client es crea connectant-se a un servidor en una adreça i port específics. Per altra banda, un socket servidor utilitza ServerSocket per escoltar les peticions entrants.

### Exemple de creació d'un servidor i d’un client

En Java, es pot crear un servidor bàsic utilitzant ServerSocket. Aquest servidor escoltarà les peticions dels clients en un port específic.

```java
ServerSocket serverSocket = new ServerSocket(port);
Socket conexion = serverSocket.accept(); // Espera una connexió del client
```

Un client en Java pot utilitzar la classe Socket per connectar-se a un servidor i enviar/rebre dades.

```java
Socket conexion = new Socket("hostname", port); // Connectar-se al servidor
```

![Sockets](../img/3_6%20sockets.png)

### Multicast Sockets en Java

Els MulticastSocket són una especialització dels sockets UDP per a l'ús en comunicacions de grup. Aquests permeten l'enviament i recepció de dades a grups de multicast, on un sol paquet de dades pot ser rebut per múltiples destinataris simultàniament. Són especialment útils en situacions en què la mateixa informació necessita ser distribuïda a molts receptors.

#### Creació i Ús de Multicast Sockets

**Creació**: Per crear un MulticastSocket, s'ha d'instanciar l'objecte MulticastSocket, opcionalment especificant un port.

**Unir-se a un Grup**: El socket ha de subscriure's a una adreça IP de multicast per a començar a rebre dades enviades a aquest grup.

**Rebre Dades**: El socket pot utilitzar el mètode receive per obtenir dades enviades al grup.

**Enviar Dades**: Similar a DatagramSocket, el MulticastSocket pot enviar dades utilitzant el mètode send, dirigint les dades a una adreça de multicast.

#### Exemple en Java

```java
InetAddress ip = InetAddress.getByName("224.0.0.1");
InetSocketAddress grupo = new InetSocketAddress(ip, 6789);

NetworkInterface interfaz = null;
interfaz = NetworkInterface.getByName("wlp1s0");
MulticastSocket chat = null;
chat = new MulticastSocket(6789);

chat.joinGroup(grupo, interfaz);

// Per rebre dades
byte[] buffer = new byte[1024];
DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
chat.receive(packet);

// Per enviar dades
String missatge = "Hola grup!";
byte[] data = missatge.getBytes();
DatagramPacket sendPacket = new DatagramPacket(data, data.length, grupo);
chat.send(sendPacket);
```

[Torna a la presentació de l'assignatura](README.md)
