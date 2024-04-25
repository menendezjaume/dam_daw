# 4. Generació de serveis en xarxa

## 1. Què és un Servei?

En el context de les xarxes d'ordinadors i Internet, **un servei és una funció o conjunt de funcions que un sistema (servidor) ofereix per a ser utilitzat per altres sistemes (clients)**.

Aquests serveis inclouen, per exemple, la transferència de dades, la comunicació, el processament de sol·licituds i la provisió de recursos.

Els serveis són fonamentals per a l'operativitat d'Internet i de les xarxes privades.

### Característiques d'un Servei

**Distribuït**: El servei sol ser proporcionat per un sistema i utilitzat per un altre a través d'una xarxa.

**Modular**: Pot ser dissenyat com una unitat independent que realitza una funció específica.

**Escalable**: Els serveis poden ser ampliats per gestionar càrregues de treball més grans segons la necessitat.

**Interoperable**: Disposat per interactuar i operar amb altres serveis i aplicacions.

### Tipus de Serveis

**Serveis de Dades**: Com ara bases de dades en xarxa o emmagatzematge en núvol.

**Serveis de Comunicació**: Com el correu electrònic, la missatgeria instantània, i les conferències web.

**Serveis d'Aplicacions**: Serveis que proporcionen funcionalitats específiques d'aplicacions, com ara eines d'ofimàtica en línia o plataformes de comerç electrònic.

**Serveis d'Infraestructura**: Com els serveis de noms de domini (DNS) o els serveis de xarxa virtual privada (VPN).

### Com funcionen els serveis

Els serveis en xarxa funcionen segons el model **client-servidor**, on **el servidor proporciona el servei i el client el consumeix**. La comunicació entre client i servidor es realitza mitjançant protocols de xarxa estàndards.

Els serveis en xarxa són vitals per a la infraestructura d'Internet i per a moltes aplicacions empresarials. Faciliten la comunicació, el comerç, el processament de dades, i molt més, jugant un paper crucial en l'economia digital.

## 2. Serveis i Protocols Estàndards de Comunicació

Els protocols de comunicació en xarxa són conjunts de regles que determinen com es transfereixen i intercanvien les dades entre diferents dispositius en una xarxa.

Aquests protocols són fonamentals per a l'operació d'Internet i les xarxes d'ordinadors privades.

Dos dels components més importants en aquest context són el model TCP/IP i el sistema de noms de domini (DNS).

### El Model TCP/IP

TCP/IP és l'acrònim de Transmission Control Protocol/Internet Protocol. Aquest és un conjunt de protocols que governa la major part de les comunicacions a Internet.

**Transmission Control Protocol (TCP)**: És un protocol orientat a la connexió que s'encarrega de la fiabilitat en la transferència de dades. Garanteix que totes les dades enviades arribin al destinatari en l'ordre correcte i sense errors. TCP divideix el flux de dades en paquets, retransmet els paquets que es perden i assegura que arriben en ordre.

**Internet Protocol (IP)**: S'encarrega de l'adreçament i l'enrutament de paquets de dades entre l'origen i el destí. Cada dispositiu en una xarxa té una adreça IP única, la qual és utilitzada per a la identificació i la localització del dispositiu en la xarxa.

### DNS (Domain Name System)

El DNS és un sistema que tradueix els noms de domini, que són fàcils de recordar per als humans, a les adreces IP numèriques que utilitzen els ordinadors per a localitzar-se entre si en la xarxa.

**Funcionament del DNS**: Quan un usuari introdueix un nom de domini com "www.example.com" en el seu navegador, el DNS s'encarrega de trobar l'adreça IP corresponent perquè el navegador pugui carregar el lloc web desitjat. Això s'aconsegueix a través d'una sèrie de consultes a servidors DNS.

**Importància del DNS**: Sense el DNS, els usuaris haurien de recordar les adreces IP complexes de cada lloc web, cosa que seria impracticable. A més, el DNS juga un paper crucial en l'escalabilitat d'Internet, permetent que els llocs web canviïn les seves adreces IP sense afectar els usuaris finals.

### Aspectes Fonamentals en la Comunicació de Xarxa

**Xifrat i seguretat**: La seguretat en les comunicacions de xarxa es maneja a través de protocols com TLS/SSL, que són utilitzats per a encriptar les dades transferides a través d'Internet, especialment en transaccions sensibles com les bancàries o les compres en línia.

**IPv4 vs IPv6**: Amb l'esgotament de les adreces IPv4, IPv6 s'ha introduït per oferir un espai d'adreçament molt més gran, així com millores en termes de rendiment, seguretat i altres característiques tècniques.

## 3. Serveis de Transferència de Fitxers

Els serveis de transferència de fitxers són essencials en la gestió de la informació i la comunicació en l'era digital. Aquests serveis permeten als usuaris intercanviar dades i fitxers de manera eficient a través de xarxes, inclosa Internet. En aquesta secció, ens centrarem en els protocols FTP, SFTP i SCP, explicant com funcionen, com es configuren i les seves aplicacions més comunes.

### FTP (File Transfer Protocol)

FTP és un dels protocols més antics i més utilitzats per a la transferència de fitxers a través d'una xarxa TCP/IP. Permet als usuaris carregar o descarregar fitxers des d'un servidor FTP.

* **Funcionament**: FTP utilitza dos canals de comunicació, un per a comandes (port 21 per defecte) i un altre per a la transferència de dades. Els usuaris necessiten un client FTP per connectar-se a un servidor FTP, i sovint es requereix autenticació amb un nom d'usuari i una contrasenya.
* **Configuració**: La configuració d'un servidor FTP implica instal·lar el programari del servidor, configurar els usuaris i els permisos, i opcionalment configurar un firewall per permetre el trànsit a través del port 21. Els clients FTP simplement necessiten la informació del servidor per connectar-se.
* **Aplicacions Comunes**: FTP és àmpliament utilitzat per a la distribució de programari, l'intercanvi de fitxers grans i la gestió de llocs web.

### SFTP (SSH File Transfer Protocol)

SFTP és una versió segura de FTP que forma part del protocol SSH (Secure Shell). A diferència d'FTP, SFTP encripta tant les credencials com les dades transferides, proporcionant una transferència segura de fitxers.

* **Funcionament**: SFTP utilitza el port 22 (el mateix que SSH) per a totes les operacions, unificant la transmissió de comandes i dades en un sol canal xifrat. Això evita la necessitat de múltiples canals i millora la seguretat.
* **Configuració**: Per configurar un servidor SFTP, cal instal·lar i configurar un servidor SSH i habilitar l'accés SFTP. Els clients SFTP, similars als clients FTP, necessiten la informació del servidor i les credencials per connectar-se.
* **Aplicacions Comunes**: SFTP és ideal per a transferències segures de dades confidencials, com ara documents financers o persones, en entorns corporatius o d'alta seguretat.

### SCP (Secure Copy Protocol)

SCP és una eina que permet la còpia segura de fitxers entre un host local i un host remot o entre dos hosts remots. Utilitza SSH per a la transferència de dades i ofereix una funcionalitat similar a la comanda "copy" en sistemes UNIX.

* **Funcionament**: SCP és una comanda de línia de comandes que permet transferir fitxers. Encripta les dades transferides i utilitza la mateixa autenticació i seguretat que SSH.
* **Configuració**: No hi ha una configuració específica per a SCP fora de la configuració de SSH.
* **Com Utilitzar SCP**: Per transferir un fitxer, s'utilitza una comanda en la línia de comandes que especifica el fitxer d'origen i el destí. Per exemple, scp origen.txt usuari@hostdestí:/cami/destí copiarà origen.txt al directori especificat en el host destí. Si es transfereix entre hosts remots, es necessiten els detalls d'autenticació per a ambdós hosts.

### Aspectes a Considerar en la Transferència de Fitxers

**Seguretat**: Encara que FTP és àmpliament utilitzat, la seva falta de xifratge en la transferència de dades i credencials pot ser un risc de seguretat. SFTP i SCP proporcionen un nivell superior de seguretat mitjançant l'encriptació.

**Facilitat d'Ús**: FTP i SFTP tenen clients amb interfícies gràfiques d'usuari (GUI) que faciliten la transferència de fitxers, mentre que SCP és generalment utilitzat a través de la línia de comandes.

**Compatibilitat**: Tot i que FTP és universalment suportat, SFTP i SCP requereixen un entorn que suporti SSH.

**Rendiment**: La transferència de fitxers pot ser influenciada per diversos factors, incloent la mida dels fitxers, la velocitat de la xarxa, i la càrrega del servidor. SFTP i SCP, al xifrar les dades, poden ser lleugerament més lents que FTP en algunes situacions.

**Gestió de Fitxers**: Tant SFTP com SCP permeten operacions addicionals de gestió de fitxers, com canviar permisos o propietats dels fitxers, que no estan disponibles en FTP estàndard.

## 4. Serveis de Correu Electrònic

Els serveis de correu electrònic són una part fonamental de la comunicació quotidiana en l'àmbit personal i professional.

Aquesta secció explora el funcionament dels serveis de correu electrònic a nivell de servidor, centrant-se en els protocols SMTP, POP3 i IMAP, i discuteix aspectes de seguretat com el xifratge de correus electrònics.

### SMTP (Simple Mail Transfer Protocol)

SMTP és el protocol estàndard utilitzat per a l'enviament de correus electrònics a través d'Internet.

**Funcionament**: Quan un usuari envia un correu electrònic, el servidor SMTP del seu proveïdor de serveis de correu electrònic (com Gmail o Outlook) pren aquest missatge i el comunica al servidor SMTP del destinatari. Aquest protocol només s'ocupa de l'enviament de correus, no de la seva recepció o emmagatzematge.

**Ports i Seguretat**: Els ports estàndard per a SMTP són el 25, 465 (SMTPS per a connexions segures) i 587. Per augmentar la seguretat, es recomana utilitzar SMTP amb xifratge TLS/SSL.

### POP3 (Post Office Protocol version 3)

POP3 és un protocol utilitzat per a la recepció de correus electrònics des del servidor a un client de correu local.

**Funcionament**: Quan un usuari obre el seu client de correu (com Outlook o Thunderbird), el protocol POP3 descarrega els missatges de correu electrònic des del servidor i els emmagatzema localment en el dispositiu de l'usuari. Després de la descàrrega, els missatges sovint s'esborren del servidor, encara que això pot configurar-se d'altra manera.

**Utilització**: Aquest protocol és útil quan es vol accedir als correus electrònics sense necessitat de connexió a Internet, ja que els missatges es guarden localment. El port estàndard per a POP3 és el 110, i el 995 per a connexions segures (POP3S).

### IMAP (Internet Message Access Protocol)

IMAP és un protocol més modern i flexible per a la recepció de correus electrònics.

**Funcionament**: A diferència de POP3, IMAP permet als usuaris veure i manipular missatges de correu electrònic directament en el servidor. Això significa que els missatges es mantenen en el servidor i es poden accedir des de múltiples dispositius de manera coherent.

**Utilització**: IMAP és ideal per a persones que necessiten accedir al seu correu electrònic des de diversos dispositius, com un telèfon mòbil, un portàtil i un ordinador de taula. El port estàndard per a IMAP és el 143, i el 993 per a connexions segures (IMAPS).

### Aspectes de Seguretat en el Correu Electrònic

**Xifrat de Correus Electrònics**: Per protegir la privadesa i la seguretat de les comunicacions, és essencial utilitzar xifratge. Això es pot aconseguir mitjançant protocols com TLS/SSL, que xifren la connexió entre el client de correu i el servidor.

**Autenticació i Prevenció de Spam**: Mètodes com SPF (Sender Policy Framework) i DKIM (DomainKeys Identified Mail) són utilitzats pels servidors de correu per verificar l'autenticitat dels missatges i reduir el correu brossa.

**Gestió de la Privadesa i dels Drets d'Accés**: És important tenir en compte les polítiques de privadesa i els drets d'accés quan es configura un servidor de correu, especialment en entorns corporatius on la confidencialitat de la informació és clau.

## 5. Servei WWW

El Servei WWW, o World Wide Web, és un sistema de documents d'hipertext interconnectats accessibles a través d'Internet. Utilitzant navegadors web, els usuaris poden veure pàgines web que poden contenir text, ../img, vídeos i altres multimèdia, i navegar entre elles mitjançant hiperenllaços.

Aquesta secció explora el funcionament dels serveis web, incloent el protocol HTTP/HTTPS, la naturalesa sense estat del web, i la seva importància en l'arquitectura moderna d'aplicacions.

### Protocol HTTP/HTTPS

HTTP (Hypertext Transfer Protocol) és el protocol fonamental utilitzat en la transferència de dades del World Wide Web. Defineix com els missatges són formats i transmesos, i com els servidors web i els navegadors han de respondre a aquestes sol·licituds.

**Funcionament del HTTP**: Quan un usuari accedeix a una pàgina web, el seu navegador envia una sol·licitud HTTP al servidor on s'allotja la pàgina. El servidor, després de processar la sol·licitud, envia una resposta HTTP de tornada al navegador, que pot incloure el contingut de la pàgina web (com ara HTML, CSS, ../img).

**HTTPS (HTTP Secure)**: És la versió segura d'HTTP, on les comunicacions són xifrades mitjançant protocols com SSL/TLS. Això proporciona una capa addicional de seguretat, assegurant que la informació enviada i rebuda no pugui ser fàcilment interceptada o manipulada.

### HTTP “stateless”

El protocol HTTP és "sense estat", la qual cosa significa que cada sol·licitud és independent; el servidor no manté cap estat o informació de la sessió entre sol·licituds. Això simplifica el disseny del servidor, però també implica alguns desafiaments, com la gestió de sessions d'usuari.

**Gestió de Sessions**: Per mantenir un estat (com ara l'estat d'inici de sessió d'un usuari) entre diverses sol·licituds HTTP, els serveis web utilitzen tècniques com cookies, tokens de sessió i emmagatzematge local.

### Importància dels Serveis Web en l'Arquitectura Moderna d'Aplicacions

**Aplicacions Basades en el Núvol**: Amb l'avenç de la computació en núvol, cada vegada més aplicacions i serveis es basen en arquitectures web. Això permet una major escalabilitat, accessibilitat des de qualsevol lloc, i facilitat de manteniment.

**APIs Web i Serveis RESTful**: Les APIs web, especialment aquelles basades en l'estil arquitectònic REST (Representational State Transfer), han esdevingut un component clau en la interacció entre diferents aplicacions i serveis en línia, permetent la integració i comunicació eficient entre diferents sistemes i plataformes.

**Aplicacions de Pàgina Única (SPA)**: Les SPA són aplicacions web que carreguen una única pàgina HTML i actualitzen dinàmicament el contingut a mesura que l'usuari interacciona amb l'aplicació, millorant l'experiència de l'usuari i reduint els temps de càrrega.

## 6. Programació d'Aplicacions Client

La programació d'aplicacions client implica el desenvolupament d'aplicacions que interactuen amb els serveis a través d'una xarxa, generalment enviant sol·licituds i rebent respostes dels servidors. Aquests clients poden ser tant simples com un navegador web o tan complexos com una aplicació mòbil o de sobretaula personalitzada.

### Connexió a Serveis

**Establiment de Connexió**: La primera etapa en el desenvolupament d'un client és establir una connexió amb el servidor. Això pot implicar l'especificació d'una URL o una adreça IP i un port, juntament amb el protocol pertinent (com HTTP/S per a serveis web).

**Autenticació**: En molts casos, especialment en aplicacions empresarials o de xarxa privada, els clients han de ser autenticats abans de poder interactuar amb el servidor. Això pot implicar l'ús de tokens, contrasenyes, o altres mecanismes d'autenticació.

### Enviament de Sol·licituds i Recepció de Respostes

**Creació de Sol·licituds**: El client ha de ser capaç de construir sol·licituds ben formades. Això inclou no només l'adreça del recurs sinó també capçaleres adequades, paràmetres i, en el cas de sol·licituds POST o PUT en una API REST, un cos de missatge.

**Gestió de Respostes**: Una vegada enviada la sol·licitud, el client ha d'estar preparat per processar la resposta. Això pot incloure la interpretació de codis d'estat HTTP, l'anàlisi de dades JSON o XML, i la gestió de dades binàries com ../img o arxius.

### Maneig d'Errors

**Tractament d'Errors de Xarxa**: Els errors de xarxa poden ocórrer per moltes raons, incloent-hi problemes de connectivitat, errors del servidor, o sol·licituds mal formades. Els clients han de ser capaços de detectar aquests errors i respondre de manera adequada, potser reintroduint la sol·licitud o informant a l'usuari.

**Logs i Informes**: El registre adequat d'errors i comportaments inusuals és crucial per a la depuració i el manteniment d'aplicacions client.

## 7. Programació de Servidors

La programació de servidors implica la creació de programari que escolta les sol·licituds de la xarxa i respon a elles. Els servidors poden variar des de simples servidors de fitxers fins a complexes aplicacions web que gestionen milers de sol·licituds per segon.

### Gestió de Sol·licituds de Xarxa

**Escolta i Resposta**: Els servidors han d'estar configurats per escoltar en els ports adequats i respondre a les sol·licituds entrants. Això implica analitzar la sol·licitud, processar-la (potser interactuant amb una base de dades o un altre servei), i generar una resposta.

**Rutes i Controladors**: En servidors web, la lògica per a diferents tipus de sol·licituds (com GET, POST, DELETE) i diferents rutes (URLs) és gestionada per controladors específics, organitzant així la lògica de l'aplicació de manera modular i mantenible.

### Multithreading i Gestió de Recursos

**Multithreading**: Amb moltes sol·licituds arribant simultàniament, els servidors freqüentment fan ús del multithreading o models asincrònics per manejar múltiples operacions al mateix temps. Això maximitza l'eficiència i la velocitat de resposta.

**Gestió de Memòria i Recursos**: Els servidors han de ser eficients en l'ús de recursos, incloent-hi la memòria i les connexions de xarxa. El maneig inadequat     d'aquests recursos pot portar a problemes de rendiment o fins i tot a caigudes del servidor.

### Seguretat del Servidor

**Autenticació i Autorització**: Els servidors han de verificar qui està fent la sol·licitud i si tenen permís per realitzar l'acció sol·licitada. Això implica implementar sistemes robustos d'autenticació i autorització.

**Protecció contra Atacs**: Els servidors són objectius freqüents d'atacs, incloent atacs d'injecció SQL, Cross-Site Scripting (XSS), i altres. La programació segura i la validació de dades són essencials per prevenir aquests atacs.

## 8. Implementació de Comunicacions Simultànies

En el món de la programació de xarxes, una de les tasques més complexes és la gestió eficient de múltiples connexions simultànies. Això és especialment important en entorns on un servidor ha de manejar milers o fins i tot milions de sol·licituds al mateix temps. Les tècniques clau per abordar aquest desafiament inclouen el maneig de múltiples fils d'execució i la programació asíncrona.

### Maneig de Múltiples Fils d'Execució

**Fils i processament concurrent**: Una manera de gestionar múltiples connexions simultànies és a través de l'ús de fils (threads). Cada fil pot manejar una sol·licitud o connexió individual. Això permet que un servidor processi diverses sol·licituds al mateix temps, millorant significativament el rendiment i la capacitat de resposta.

**Desafiaments del Multithreading**: Tot i que els fils poden millorar el rendiment, també introdueixen complexitat addicional. Els problemes com la condició de cursa, el bloqueig de recursos, i la sincronització de fils han de ser acuradament gestionats. A més, els fils consumeixen recursos del sistema, de manera que un nombre excessiu de fils pot tenir un impacte negatiu en el rendiment.

**Pool de fils**: Per mitigar alguns dels problemes associats amb el multithreading, sovint es fa ús de "pools de threads", on un nombre fix de fils es reutilitzen per processar sol·licituds. Això ajuda a limitar el consum de recursos i a millorar l'eficiència.

### Programació Asíncrona

La programació asíncrona és una alternativa al multithreading que pot ser més eficient en termes de recursos. En lloc de bloquejar l'espera de les respostes o els recursos, les operacions asíncrones permeten que un procés principal segueixi funcionant mentre les tasques secundàries són gestionades en el fons.

**Callbacks i Promeses**: En molts llenguatges de programació, la programació asíncrona es maneja mitjançant callbacks o promeses. Aquests mecanismes permeten a un programa continuar executant-se i només actuar quan una operació (com una petició de xarxa) ha estat completada.

**Event Loop**: En entorns asíncrons, un event loop corre contínuament i maneja tots els esdeveniments o sol·licituds a mesura que arriben. Aquest model pot ser molt eficient, ja que un sol fil pot manejar múltiples tasques sense bloquejar.

### Desafiaments i Consideracions

**Gestió de l'Estat**: Tant en el multithreading com en la programació asíncrona, la gestió de l'estat pot ser complicada. Mantenir la consistència de les dades entre múltiples fils o operacions asíncrones requereix una planificació i disseny cuidadosos.

**Depuració i Manteniment**: La complexitat introduïda pel multithreading i les operacions asíncrones pot fer que la depuració i el manteniment del codi siguin més difícils. És important utilitzar patrons de disseny sòlids i mantenir el codi ben organitzat i documentat.

**Selecció de l'Enfocament**: La decisió entre utilitzar multithreading, programació asíncrona, o una combinació d'ambdós, depèn de l'aplicació específica, les limitacions de recursos, i les competències de l'equip de desenvolupament.

## 9. RMI de Java (Java Remote Method Invocation)

Java Remote Method Invocation (RMI) és una API que permet a un objecte Java invocar mètodes d'un objecte situat en una altra màquina virtual Java.

Aquesta capacitat és fonamental en el desenvolupament d'aplicacions distribuïdes, ja que facilita la comunicació entre processos en diferents JVMs (Java Virtual Machines), potencialment situades en diferents hosts dins d'una xarxa.

### Concepte de RMI

**Invocació de Mètodes a Distància**: RMI permet a un objecte client invocar mètodes d'un objecte servidor situat en una altra JVM. Aquesta comunicació es realitza a través de la xarxa, fent que la distància física entre els objectes sigui transparent tant per al client com per al servidor.

**Serialització d'Objectes**: Per realitzar aquesta comunicació, els objectes passats i retornats en les crides RMI són serialitzats (convertits en una seqüència de bytes) i després deserialitzats a l'altre extrem. Això permet que l'estat de l'objecte sigui transmès a través de la xarxa.

### Creació de Servidors i Clients RMI

**Definició de la Interfície**: El primer pas en la creació d'una aplicació RMI és definir una interfície que estengui java.rmi.Remote. Aquesta interfície declara els mètodes que poden ser invocats a distància.

**Implementació del Servidor**: El següent pas és implementar aquesta interfície en una classe servidor. Aquesta classe ha d'estendre java.rmi.server.UnicastRemoteObject i implementar els mètodes definits en la interfície.

**Registre de l'Objecte del Servidor**: L'objecte servidor ha de ser registrat en el RMI registry per a que pugui ser trobat pels clients. Això es fa normalment en el mateix codi que implementa l'objecte servidor.

**Creació del Client**: El client RMI localitza l'objecte servidor utilitzant el RMI registry i després invoca els mètodes sobre l'objecte servidor com si fossin locals.

### Comunicació entre Client i Servidor

**Crida Remota**: Quan un client realitza una crida a un mètode d'un objecte servidor, RMI s'encarrega de la comunicació de xarxa. El client i el servidor poden interactuar utilitzant aquests mètodes remots com si fossin mètodes locals.

**Gestió d'Excepcions**: Les crides RMI poden generar excepcions, com java.rmi.RemoteException. Els clients han de manejar aquestes excepcions adequadament, ja que poden indicar problemes de xarxa o errors en el servidor.

## Exemple pràctic

Creem una interficie.

```java
import java.rmi.*;

public interface RMICalcInterface extends Remote {

   public int suma(int a, int b) throws RemoteException;

   public int resta(int a, int b) throws RemoteException;

   public int multip(int a, int b) throws RemoteException;

   public int div(int a, int b) throws RemoteException;

}
```

La implementem al servidor.

```java
import java.rmi.*;
import java.rmi.registry.*;
import java.rmi.server.UnicastRemoteObject;

public class RMICalcServer implements RMICalcInterface {
   public int suma(int a, int b) throws RemoteException {
       return (a + b);
   }

   public int resta(int a, int b) throws RemoteException {
       return (a - b);
   }

   public int multip(int a, int b) throws RemoteException {
       return (a * b);
   }

   public int div(int a, int b) throws RemoteException {
       return (a / b);
   }

   public static void main(String[] args) {
       Registry reg = null;
       try {
           reg = LocateRegistry.createRegistry(5555);
       } catch (Exception e) {
           System.out.println("ERROR: No se ha podido crear el registro");
           e.printStackTrace();
       }
       RMICalcServer serverObject = new RMICalcServer();
       try {
           reg.bind("Calculadora", (RMICalcInterface) UnicastRemoteObject.exportObject(serverObject, 0));
       } catch (Exception e) {
           System.out.println("ERROR: No se ha podido inscribir el objeto servidor.");
           e.printStackTrace();
       }
   }
}
```

Creem un client.

```java
import java.rmi.*;
import java.rmi.registry.*;

public class RMICalcClient {
   public static void main(String[] args) {
       RMICalcInterface calc = null;
       try {
           Registry registry = LocateRegistry.getRegistry("localhost", 5555);
           calc = (RMICalcInterface) registry.lookup("Calculadora");
       } catch (Exception e) {
           e.printStackTrace();
       }
       if (calc != null) {
           try {
               System.out.println("2 + 2 = " + calc.suma(2, 2));
               System.out.println("99 - 45 = " + calc.resta(99, 45));
               System.out.println("125 * 3 = " + calc.multip(125, 3));
               System.out.println("1250 / 5 = " + calc.div(1250, 5));
           } catch (RemoteException e) {
               e.printStackTrace();
           }
       }
   }
}
```

[Torna a la presentació de l'assignatura](README.md)
