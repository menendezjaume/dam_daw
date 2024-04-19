# 5. Utilització de tècniques de programació segura

## Definicions

**Criptografia**: Art d'escriure amb clau secreta o d'una manera enigmàtica.

Ciència que tracta de conservar els secrets o fins i tot l'art d'enviar missatges en clau secreta aplicant-se a tota mena d'informació, tant escrita com digital, la qual es pot emmagatzemar a un ordinador o enviar a través de la xarxa.

**Xifrar**: Acció de protegir la informació mitjançant la modificació utilitzant una clau.

### Aplicacions de la Criptografia

**Identificació i autenticació**. Identificar un individu o validar l'accés a un servidor.
**Certificació**. Esquema mitjançant el qual agents fiables validen la identitat d'agents desconeguts (com a usuaris reals).
**Seguretat de les comunicacions**. Permet establir canals segurs per a aplicacions que operen sobre xarxes que no són segures.
**Comerç electrònic**. L'ús de canals segurs i mecanismes d'identificació permet que les empreses i els usuaris tinguin garanties que les operacions no seran espiades ni modificades, reduint-se el risc de fraus.

### Característiques dels serveis de seguretat

**Confidencialitat**: es tracta d'assegurar que la comunicació només pugui ser vista pels usuaris autoritzats, evitant que cap altre no pugui llegir el missatge. Sol anar acompanyada de l'autenticació dels usuaris que hi participen.
**Integritat de la informació**: es tracta d'assegurar que el missatge no hagi estat modificat de cap manera per terceres persones durant la transmissió.
**Disponibilitat**: es tracta d’assegurar-se que tots els sistemes i operacions que s'ocupen de les dades funcionen sense problemes i prendre mesures com eliminar servidors redundants o assegurar-se que les actualitzacions es produeixen a temps.
**No repudi**: es tracta d'evitar que la persona que envia el missatge o realitza una acció negui haver-ho fet davant de tercers. Com la característica de confidencialitat, necessita l'autenticació de l'origen de la informació.

### Estructura d'un sistema secret

Un sistema secret actual està definit per dues funcions:

* Funció de xifrat.
* Funció de desxifrat.

La clau és el paràmetre que especifica una transformació concreta dins de totes les possibles substitucions que es podrien realitzar amb la funció de xifrat.

![Estructura d'un sistema secret](imatges/5_1%20sistema%20secret.png)

## Tipus de sistemes de xifrat

La seguretat depèn tant de l'algorisme de xifrat com del nivell de secret que es doni a la clau.

Sistemes de xifrat simètric

* Les claus de xifrat i desxifrat són la mateixa.
* El problema és com transmetre la clau perquè l'emissor (que xifra la informació) i el receptor de la informació (desxifra) tinguin tots dos la mateixa clau.
* Donen lloc a què s'anomena **model de clau privada**.

Sistemes de xifrat asimètric

* Les claus de xifrat i desxiframent són diferents i estan relacionades d'alguna manera.
* Donen lloc al **model de clau pública**.

## Sistemes de xifrat simètric

**El mecanisme de xifrat per antonomàsia**, usat des de la invenció de la criptografia en temps pretèrits, és l’anomenat mecanisme de clau simètrica. En aquest, **existeix un secret, la clau**, que és compartida entre tots aquells que han de ser capaços de llegir les dades. Només qui en té possessió és capaç de xifrar-les i desxifrar-les correctament.

**És com disposar d’un cofre indestructible**, protegit amb un pany de tancament automàtic, on es pot desar un missatge. Només qui té una còpia de la clau del pany pot obrir el cofre i desar-hi coses, o obrir-lo i recuperar el que hi ha a dins. Per tant, es donarà una còpia de la clau a qui es vulgui que pugui obrir el cofre. Encara que un intrús s’apoderi del cofre i se’l quedi, serà incapaç d’obtenir el seu contingut a menys que tingui la clau correcta.

**En el cas d’un missatge de dades**, és clar, **no existeix tal cofre**. La clau no és més que un conjunt de dades, també.

**En l’antiguitat, la clau era simplement una contrasenya en text, però en el cas d’un ordinador, pot ser qualsevol seqüència de bits**. No cal ni que sigui representable com a text llegible.

L’algorisme de xifrat combina les dades originals en clar amb la clau per generar com a resultat un conjunt de dades incomprensibles. **Per recuperar el missatge original i desfer el procés d’ofuscació cal aplicar l’algorisme de desxifrat usant una còpia de la clau usada durant el procés de xifrat**. Si no s’usa la clau correcta, el resultat seran també dades incomprensibles i, per tant, el missatge original romandrà protegit.

**En el cas d’un intercanvi de missatges a dues bandes**, abans de poder procedir a l’enviament de les dades, **caldrà que les parts implicades acordin quina ha de ser la clau secreta**.

Normalment, la part interessada, ja sigui l’emissor o el receptor, és qui tria la clau i se la fa saber a l’altre. Ara bé, aquest pas és extremadament delicat, ja que cal tenir en compte que el procés d’enviament de la clau també és susceptible de ser interceptat. Per tant, cal fer-ho garantint que es duu a terme de manera segura. Això se sol fer en persona o mitjançant un missatger fiable.

Actualment, existeixen diferents algorismes de xifrat simètric en ús dins del context de les aplicacions informàtiques. Nosaltres farem les pràctiques amb l’algorisme anomenat **AES** (Advanced Encryption Standrad), que és el que es considera més segur i l’estàndard en algorismes de xifrat.

Aquest algoritme va ser creat per Joan Daemen i Vincent Rijmen i va guanyar el seu estatus d’estàndard després de participar en un concurs molt exigent a nivell internacional.

Tot i així, cal tenir en compte que existeixen altres algorismes que encara estan en ús. Per exemple, l’anterior estàndard, el **DES** (Data Encryption Standrard) o el **TripleDES**.

![Sistema de xifrat simètric](imatges/5_2%20xifrat%20simetric.png)

### Generació de claus simètriques

Abans de plantejar-se l’execució d’un algorisme de xifrat, primer cal una condició indispensable: decidir quina serà la clau mitjançant la qual es protegirà la informació. Per tant, aquest és el primer pas a resoldre. Tothom qui tingui accés a aquesta clau serà capaç de generar dades xifrades i de desxifrar-les posteriorment.

Des del punt de vista d’un algorisme de xifrat que ha de ser executat per un ordinador, una clau simètrica, no és més que una seqüència aleatòria de bits d’una llargària determinada. Les llargàries vàlides vindran donades exclusivament pel tipus d’algorisme que es vol executar. A part d’això, no cal complir cap altra condició.

El JCE, però, no treballa normalment amb seqüències de bytes a l’hora de gestionar claus, sinó amb instàncies de la classe javax.crypto.SecretKey. Les biblioteques del JCE ofereixen una classe auxiliar capaç de generar per si mateixa claus segures per diferents tipus d’algorismes de xifrat.

```java
public SecretKey keygenKeyGeneration(int keySize) throws NoSuchAlgorithmException {
    SecretKey sKey = null;
    if ((keySize == 128)||(keySize == 192)||(keySize == 256)) {
        KeyGenerator kgen = KeyGenerator.getInstance("AES");
        kgen.init(keySize);
        sKey = kgen.generateKey();
      }
    return sKey;
  }
```

### Procés de xifrat simètric

```java
public byte[] encryptData(SecretKey sKey, byte[] data) throws Exception {
    byte[] encryptedData = null;
      Cipher cipher = Cipher.getInstance("AES");
      cipher.init(Cipher.ENCRYPT_MODE, sKey);
      encryptedData =  cipher.doFinal(data);
    return encryptedData;
  }
```

### Procés de desxifrat simètric

Per desxifrar les dades, el procés és exactament igual que el xifrat, amb la única diferència que el mode de l’objecte `Cipher` és `Cipher.DECRYPT_MODE`.
En aquest cas, l’entrada seran les dades xifrades.

## Funció de hash

Una funció hash és un **algorisme matemàtic que resumeix el contingut d'un missatge** en una quantitat d'informació fixa menor.

És una pràctica habitual representar els valors hash com a cadenes **hexadecimals** perquè consten de caràcters del 0 al 9 i de la a a la f, cosa que els fa més fàcils d'utilitzar.

Convertir el hash en una cadena hexadecimal pot ser útil per diverses raons, com ara quan necessiteu mostrar o transmetre el valor hash com a text, o quan necessiteu comparar valors hash. També és una manera típica d'emmagatzemar valors hash a bases de dades o altres sistemes d'emmagatzematge.

Un **algorisme de hash**, o resum (digest, en anglès), és una transformació criptogràfica que es pot aplicar a un conjunt de dades de manera que compleix sempre un seguit de condicions.

Primer de tot, que la relació entre possibles entrades i sortides sigui bijectiva. O sigui, que **donada una mateixa entrada, sempre resulti en exactament la mateixa sortida i que dues sortides diferents vinguin sempre d’entrades diferents**.

D’altra banda, **no ha de ser reversible**. A partir només d’un resultat, ha de ser pràcticament impossible endevinar quina ha estat l’entrada original que l’ha generat.

En l’actualitat, hi ha diversos algorismes de hash. Tot i així, el més utilitzat avui en dia, i el que es considera un estàndard, és l’algorisme **SHA-256** (Secure Hash Algoritm, o Algorisme Segur de Hash). Aquest, a partir d’una entrada de dades de mida arbitrària, genera un resultat de 256 bits.

Si es desitja una sortida de més longitud, existeix una versió millorada, més segura, tot i que no tan popular: el SHA-3, una nova versió encara millor i més segura.

El SHA-1, tot i que encara s’utilitza, no està recomanat, ja que s’ha demostrat senzill de rompre.

L’MD5, està completament romput i no recomanat.

Funció de hash (cont.)

Farem servir la classe MessageDigest.

A continuació, serà necessari transformar aquest array de bytes a un String amb format hexadecimal.

Funció de hash a Java

MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] hash = md.digest(palabra.getBytes());

Claus simètriques basades en contrasenya
Una clau simètrica ha de poder ser intercanviada. Una possibilitat és desar-la en un fitxer o escriure els seus bytes, però això seria feixuc per les persones. Una manera de facilitar la gestió de claus criptogràfiques és generar-les a partir d’una contrasenya llegible. Que trieu una contrasenya fàcil o difícil d’endevinar ja és un altre tema.
Un exemple de generació i compartició de clau amb contrasenya es troba a l'activació del xifrat als encaminadors ADSL domèstics.

Claus simètriques basades en contrasenya (cont.)
Per fer-ho podeu aprofitar la particularitat que qualsevol seqüència de bytes de la mida correcta pot servir com una clau simètrica. Només cal, partint de la contrasenya, generar tants bytes com sigui necessari, però de manera que, donada una contrasenya, només aquesta generi una seqüència de bytes donada. I que mai sigui possible, o si més no extremadament improbable, que dues contrasenyes diferents arribin a generar la mateixa clau.
Aquesta tasca presenta algunes complexitats inherents. Per començar, hi ha el problema de la mida de la contrasenya. Idealment, la contrasenya hauria de tenir exactament la mateixa longitud que la clau que volem generar. Si la contrasenya és més llarga del necessari, ens veurem obligats a eliminar alguns dels seus caràcters; si és més curta, haurem d'afegir-ne. Aquest requisit de tenir una longitud específica i exacta pot ser molest, especialment quan el que busquem és millorar la usabilitat, com ara en el cas d'una clau AES de 128 bits, que requereix 16 caràcters en l'alfabet llatí. A més, si es permet l'ús de contrasenyes de qualsevol longitud sense prendre les mesures adequades, es podria donar el cas que dues contrasenyes diferents produeixin la mateixa clau, el que definitivament volem evitar.
Una manera correcta de resoldre aquest problema és usant un algorisme criptogràfic de hash sobre la contrasenya per generar la clau.

Generació de claus simètriques basades en contrasenya

Farem servir la funció de la diapositiva 15, però, en lloc de generar una clau de forma aleatoria, la clau serà l’output de calcular el hash d’un input de l’usuari.
Has de tenir en compte que AES supports key sizes of 128, 192, and 256 bits. Per tant, haurem d'usar una funció de hash l'output del qual sigui de la mateixa mida.

Sistemes de xifrat asimètric
Al contrari que amb les claus simètriques, els parells de claus asimètriques no són un conjunt arbitrari de bytes que es poden generar de qualsevol manera.
Donades les particularitats del xifrat asimètric, perquè el sistema funcioni, tant la clau pública com la clau privada han de tenir un conjunt de propietats matemàtiques molt concretes. Si no es compleixen aquestes propietats, o no funcionarà l’algorisme, o serà molt fàcil d’endevinar la clau privada a partir de la clau pública. Aquestes propietats varien depenent de l’algorisme.

Sistemes de xifrat asimètric (cont.)
Ara bé, els esquemes de xifrat simètric tenen un seguit de problemes. Per això, a finals del segle XX sorgeixen el sistemes de clau asimètrica.
Aquests replantegen l’escenari del cofre protegit amb pany d’una manera certament innovadora. Imagineu-vos que aquest cofre ara té dos panys, cadascun depenent d’una clau totalment diferent.
Una de les claus permet obrir una escletxa per on únicament es pot fer entrar el missatge, però no permet treure’l de dins. Aquesta serà l’anomenada clau pública. L’altre pany obre el cofre i permet treure els missatges desats a dins. Aquesta s’anomenarà la clau privada.

Sistemes de xifrat asimètric (cont.)
En aquest escenari, el receptor disposa d’una clau de cada tipus i s’encarrega de distribuir una còpia de la clau pública a tothom de qui vulgui rebre missatges secrets.
L’avantatge fonamental és que si un espia intercepta una còpia de la clau pública, li servirà de ben poc. Només podrà desar missatges dins el cofre, però mai obrir el cofre, que és el que realment vol.
Per tant, aquesta clau no cal que es transmeti de manera segura. De fet, com més fàcil sigui que el màxim de gent en tingui una còpia, millor i tot. Per això aquests sistemes també s’anomenen de clau pública.

Sistemes de xifrat asimètric (cont.)
Descrit a nivell general, en un sistema basat en clau pública cada usuari disposa d’un parell de claus: la seva clau privada i la seva clau pública.
Cada usuari genera personalment el seu parell de claus d’acord a un procediment molt concret. Al contrari que el sistema de clau simètrica, aquestes dues claus han de complir unes condicions matemàtiques molt especials, que no s’entrarà a explicar.
El resultat és que no val qualsevol seqüència de bits per generar-les, el procés és força més complex i una mica més lent. Llavors, cadascú s’encarrega de distribuir a tothom la seva clau pública, sense haver de preocupar-se de si algú intercepta la transmissió.
Per exemple, la pot penjar a la seva plana web. La clau privada se la guarda de manera segura, de manera que ningú altre la sàpiga mai. Cada clau privada només la coneix el seu creador i ningú més.

Sistemes de xifrat asimètric (cont.)

Firma digital
Inicialment, l’ús dels termes criptografia i xifrat eren pràcticament intercanviables.
L’aplicació d’aquesta disciplina tradicionalment ha estat per assolir la privadesa en l’intercanvi de missatges.
Però amb la popularitat d’Internet i la proliferació en l’intercanvi telemàtic de missatges o documents, es fa patent la necessitat de disposar d’altres serveis de seguretat més enllà del de la privadesa. Principalment, els següents:
Integritat: poder identificar si un document ha estat manipulat. Cal fer palès que aquest servei no evita la manipulació, només fa possible que sempre pugui ser detectada pel receptor.
Autenticació: poder garantir quina és la identitat de l’autor del document, evitant que sigui suplantat.
No-repudi: evitar que l’autor pugui negar que ell ha generat el document. El receptor pot demostrar a un tercer la identitat de qui ha emès realment el missatge.

Aquests serveis, si es contemplen tots tres junts, són els que us permeten dur a terme intercanvis fiables de dades, com ara realitzar transaccions o la venda de productes, fer la declaració de la renda telemàticament o connectar-vos a la banca en línia.
També permeten garantir que si s’emmagatzema un document a un ordinador, ningú l’haurà modificat quan es torni a obrir sense que la manipulació no es faci patent.
La firma digital és el mecanisme criptogràfic que trasllada totes les propietats de la firma manuscrita del món físic a la informació en format digital.

![Firma digital](imatges/5_5%20firma%20digital.png)

[Torna a la presentació de l'assignatura](README.md)
