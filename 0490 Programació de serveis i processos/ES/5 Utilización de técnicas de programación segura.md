# 5. Utilización de técnicas de programación segura

## Definiciones

**Criptografía**: Arte de escribir con clave secreta o de forma enigmática.

Ciencia que trata de conservar los secretos o incluso el arte de enviar mensajes en clave secreta aplicándose a todo tipo de información, tanto escrita como digital, la cual se puede almacenar en un ordenador o enviar a través de la red.

**Cifrar**: Acción de proteger la información mediante la modificación utilizando una clave.

### Aplicaciones de la Criptografía

**Identificación y autenticación**. Identificar a un individuo o validar el acceso a un servidor.
**Certificación**. Esquema mediante el cual agentes fiables validan la identidad de agentes desconocidos (como usuarios reales).
**Seguridad de las comunicaciones**. Permite establecer canales seguros para aplicaciones que operan sobre redes no seguras.
**Comercio electrónico**. El uso de canales seguros y mecanismos de identificación permite que las empresas y usuarios tengan garantías de que las operaciones no serán espiadas ni modificadas, reduciéndose el riesgo de fraudes.

### Características de los servicios de seguridad

**Confidencialidad**: se trata de asegurar que la comunicación sólo pueda ser vista por los usuarios autorizados, evitando que ningún otro pueda leer el mensaje. Suele ir acompañada de la autenticación de los usuarios que participan.
**Integridad de la información**: se trata de asegurar que el mensaje no haya sido modificado en modo alguno por terceras personas durante la transmisión.
**Disponibilidad**: se trata de asegurarse de que todos los sistemas y operaciones que se ocupan de los datos funcionan sin problemas y tomar medidas como eliminar servidores redundantes o asegurarse de que las actualizaciones se producen a tiempo.
**No repudio**: se trata de evitar que la persona que envía el mensaje o realiza una acción niegue haberlo hecho ante terceros. Como la característica de confidencialidad, necesita la autenticación del origen de la información.

### Estructura de un sistema secreto

Un sistema secreto actual está definido por dos funciones:

* Función de cifrado.
* Función de descifrado.

La clave es el parámetro que especifica una transformación concreta dentro de todas las posibles sustituciones que podrían realizarse con la función de cifrado.

![Estructura de un sistema secreto](../img/5_1%20sistema%20secret.png)

## Tipo de sistemas de cifrado

La seguridad depende tanto del algoritmo de cifrado como del nivel de secreto que se dé en la clave.

Sistemas de cifrado simétrico

* Las claves de cifrado y descifrado son la misma.
* El problema es cómo transmitir la clave para que el emisor (que cifra la información) y el receptor de la información (descifra) tengan ambos la misma clave.
* Dan lugar a lo que se llama **modelo de clave privada**.

Sistemas de cifrado asimétrico

* Las claves de cifrado y desciframiento son diferentes y están relacionadas de alguna manera.
* Dan lugar al **modelo de clave pública**.

## Sistemas de cifrado simétrico

**El mecanismo de cifrado por antonomasia**, usado desde la invención de la criptografía en tiempos pretéritos, es el llamado mecanismo de clave simétrica. En éste, **existe un secreto, la clave**, que es compartida entre todos aquellos que deben ser capaces de leer los datos. Sólo quien tiene posesión es capaz de cifrarlas y descifrarlas correctamente.

**Es como disponer de un cofre inquebrantable**, protegido con una cerradura de cierre automático, donde se puede guardar un mensaje. Sólo quien tiene una copia de la llave de la cerradura puede abrir el cofre y guardar cosas, o abrirlo y recuperar lo que hay dentro. Por tanto, se dará una copia de la llave a quien se quiera que pueda abrir el cofre. Aunque un intruso se apodere del cofre y se le quede, será incapaz de obtener su contenido a menos que tenga la clave correcta.

**En el caso de un mensaje de datos**, por supuesto, **no existe tal cofre**. La clave no es más que un conjunto de datos también.

**En la antigüedad, la clave era simplemente una contraseña en texto, pero en el caso de un ordenador, puede ser cualquier secuencia de bits**. No hace falta que sea representable como texto legible.

El algoritmo de cifrado combina los datos originales en claro con la clave para generar como resultado un conjunto de datos incomprensibles. **Para recuperar el mensaje original y deshacer el proceso de ofuscación es necesario aplicar el algoritmo de descifrado usando una copia de la clave usada durante el proceso de cifrado**. Si no se usa la clave correcta, el resultado serán también datos incomprensibles y, por tanto, el mensaje original permanecerá protegido.

**En el caso de un intercambio de mensajes a dos bandas**, antes de poder proceder al envío de los datos, **será necesario que las partes implicadas acuerden cuál debe ser la clave secreta**.

Normalmente, la parte interesada, ya sea el emisor o el receptor, es quien elige la clave y se la hace saber al otro. Ahora bien, este paso es extremadamente delicado, ya que debe tenerse en cuenta que el proceso de envío de la clave también es susceptible de ser interceptado. Por tanto, hay que hacerlo garantizando que se lleva a cabo de forma segura. Esto suele hacerse en persona o mediante un mensajero fiable.

Actualmente, existen distintos algoritmos de cifrado simétrico en uso dentro del contexto de las aplicaciones informáticas. Nosotros realizaremos las prácticas con el algoritmo llamado **AES** (Advanced Encryption Standrad), que es el que se considera más seguro y el estándar en algoritmos de cifrado.

Este algoritmo fue creado por Joan Daemen y Vincent Rijmen y ganó su estatus de estándar después de participar en un concurso muy exigente a nivel internacional.

Sin embargo, hay que tener en cuenta que existen otros algoritmos que todavía están en uso. Por ejemplo, el anterior estándar, el **DES** (Data Encryption Standrard) o el **TripleDES**.

![Sistema de cifrado simétrico](../img/5_2%20xifrat%20simetric.png)

### Generación de claves simétricas

Antes de plantearse la ejecución de un algoritmo de cifrado, primero es necesaria una condición indispensable: decidir cuál será la clave mediante la cual se protegerá la información. Por tanto, éste es el primer paso a resolver. Todo el que tenga acceso a esta clave será capaz de generar datos cifrados y de descifrarlos posteriormente.

Desde el punto de vista de un algoritmo de cifrado que debe ser ejecutado por un ordenador, una clave simétrica, no es más que una secuencia aleatoria de bits de determinada longitud. Las longitudes válidas vendrán dadas exclusivamente por el tipo de algoritmo que se desea ejecutar. Aparte de esto, no es necesario cumplir ninguna otra condición.

Sin embargo, JCE no trabaja normalmente con secuencias de bytes a la hora de gestionar claves, sino con instancias de la clase javax.crypto.SecretKey. Las bibliotecas del JCE ofrecen una clase auxiliar capaz de generar por sí misma claves seguras por distintos tipos de algoritmos de cifrado.

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
````

### Proceso de cifrado simétrico

```java
public byte[] encryptData(SecretKey sKey, byte[] data) throws Exception {
     byte[] encryptedData = null;
       Cipher cipher = Cipher.getInstance("AES");
       cipher.init(Cipher.ENCRYPT_MODE, sKey);
       encryptedData = cipher.doFinal(fecha);
     return encryptedData;
   }
````

### Proceso de descifrado simétrico

Para descifrar los datos, el proceso es exactamente igual que el cifrado, con la única diferencia de que el modo del objeto `Cipher` es `Cipher.DECRYPT_MODE`.
En este caso, la entrada serán los datos cifrados.

## Función de hash

Una función hash es un **algoritmo matemático que resume el contenido de un mensaje** en una cantidad de información fija menor.

Es una práctica habitual representar los valores hash como cadenas **hexadecimales** porque constan de caracteres del 0 al 9 y de la a a la f, lo que los hace más fáciles de utilizar.

Convertir el hash en una cadena hexadecimal puede ser útil por varias razones, como cuando necesita mostrar o transmitir el valor hash como texto, o cuando necesita comparar valores hash. También es una forma típica de almacenar valores hash en bases de datos u otros sistemas de almacenamiento.

Un **algoritmo de hash**, o resumen (digesto, en inglés), es una transformación criptográfica que se puede aplicar a un conjunto de datos de forma que cumple siempre una serie de condiciones.

Ante todo, que la relación entre posibles entradas y salidas sea biyectiva. O sea, que **dada una misma entrada, siempre resulte en exactamente la misma salida y que dos salidas distintas vengan siempre de entradas distintas**.

Por otra parte, **no debe ser reversible**. A partir de sólo un resultado, debe ser prácticamente imposible adivinar cuál ha sido la entrada original que la ha generado.

En la actualidad, existen varios algoritmos de hash. Sin embargo, el más utilizado hoy en día, y lo que se considera un estándar, es el algoritmo **SHA-256** (Secure Hash Algoritm, o Algoritmo Seguro de Hash). Éste, a partir de una entrada de datos de tamaño arbitrario, genera un resultado de 256 bits.

Si se desea una salida de mayor longitud, existe una versión mejorada, más segura, aunque no tan popular: el SHA-3, una nueva versión aún mejor y más segura.

El SHA-1, aunque todavía se utiliza, no está recomendado, puesto que se ha demostrado sencillo de romper.

El MD5 está completamente roto y no recomendado.

Función de hash (cont.)

Utilizaremos la clase MessageDigest.

A continuación, será necesario transformar este array de bytes en un String con formato hexadecimal.

Función de hash en Java

```java
MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] hash = md.digest(palabra.getBytes());
```

Claves simétricas basadas en contraseña
Una clave simétrica debe poder ser intercambiada. Una posibilidad es guardarla en un archivo o escribir sus bytes, pero esto sería pesado para las personas. Una forma de facilitar la gestión de claves criptográficas es generarlas a partir de una contraseña legible. Que elija una contraseña fácil o difícil de adivinar ya es otro tema.

Un ejemplo de generación y compartición de clave con contraseña se encuentra en la activación del cifrado en los enrutadores ADSL domésticos.

Para ello puede aprovechar la particularidad de que cualquier secuencia de bytes del tamaño correcto puede servir como una clave simétrica. Sólo es necesario, partiendo de la contraseña, generar tantos bytes como sea necesario, pero de forma que, dada una contraseña, sólo ésta genere una secuencia de bytes dada. Y que nunca sea posible, o al menos extremadamente improbable, que dos contraseñas distintas lleguen a generar la misma clave.

Esta labor presenta algunas complejidades inherentes. Para empezar, existe el problema del tamaño de la contraseña. Idealmente, la contraseña debería tener exactamente la misma longitud que la clave que deseamos generar. Si la contraseña es más larga de lo necesario, nos veremos obligados a eliminar algunos de sus caracteres; si es más corta, deberemos añadirlas. Este requisito de tener una longitud específica y exacta puede ser molesto, especialmente cuando lo que buscamos es mejorar su usabilidad, como en el caso de una clave AES de 128 bits, que requiere 16 caracteres en el alfabeto latino. Además, si se permite el uso de contraseñas de cualquier longitud sin tomar las medidas adecuadas, podría darse el caso de que dos contraseñas diferentes produzcan la misma clave, lo que definitivamente queremos evitar.

Una forma correcta de resolver este problema es usando un algoritmo criptográfico de hash sobre la contraseña para generar la clave.

Generación de claves simétricas basadas en contraseña

Utilizaremos la función de la diapositiva 15, pero en lugar de generar una clave de forma aleatoria, la clave será el output de calcular el hash de un input del usuario.
Debes tener en cuenta que AES supports key sizes of 128, 192, and 256 bits. Por tanto, deberemos usar una función de hash cuyo output sea del mismo tamaño.

Sistemas de cifrado asimétrico
Al contrario que con las claves simétricas, los pares de claves asimétricas no son un conjunto arbitrario de bytes que pueden generarse de cualquier modo.

Dadas las particularidades del cifrado asimétrico, para que el sistema funcione, tanto la clave pública como la clave privada deben tener un conjunto de propiedades matemáticas muy concretas. Si no se cumplen estas propiedades, o no funcionará el algoritmo, o será muy fácil adivinar la clave privada a partir de la clave pública. Estas propiedades varían dependiendo del algoritmo.

Sin embargo, los esquemas de cifrado simétrico tienen una serie de problemas. Por eso, a finales del siglo XX surgen los sistemas de clave asimétrica.

Estos replantean el escenario del cofre protegido con cerradura de forma ciertamente innovadora. Imagínese que este cofre ahora tiene dos cerraduras, cada una dependiendo de una llave totalmente diferente.

Una de las claves permite abrir una brecha por la que únicamente se puede hacer entrar el mensaje, pero no permite sacarlo de dentro. Ésta será la llamada clave pública. La otra cerradura abre el cofre y permite sacar los mensajes guardados dentro. Ésta se llamará la clave privada.

En este escenario, el receptor dispone de una clave de cada tipo y se encarga de distribuir una copia de la clave pública a todo aquel que quiera recibir mensajes secretos.

La ventaja fundamental es que si un espía intercepta una copia de la clave pública, le servirá de poco. Sólo podrá guardar mensajes en el cofre, pero nunca abrir el cofre, que es lo que realmente quiere.

Por tanto, esta clave no es necesario que se transmita de forma segura. De hecho, cuanto más fácil sea que el máximo de gente tenga una copia, mejor. Por eso estos sistemas también se llaman de clave pública.

Descrito a nivel general, en un sistema basado en clave pública cada usuario dispone de un par de claves: su clave privada y su clave pública.

Cada usuario genera personalmente su par de claves de acuerdo a un procedimiento muy concreto. Al contrario que el sistema de clave simétrica, estas dos claves deben cumplir unas condiciones matemáticas muy especiales, que no se entrará a explicar.

El resultado es que no vale cualquier secuencia de bits para generarlas, el proceso es bastante más complejo y algo más lento. Entonces, cada uno se encarga de distribuir a todo el mundo su clave pública, sin tener que preocuparse de si alguien intercepta la transmisión.

Por ejemplo, puede colgarla en su página web. La clave privada se la guarda de forma segura, de modo que nadie la sepa nunca. Cada clave privada sólo la conoce su creador y nadie más.


Firma digital
Inicialmente, el uso de los términos criptografía y cifrado eran prácticamente intercambiables.
La aplicación de esta disciplina ha sido tradicionalmente para alcanzar la privacidad en el intercambio de mensajes.
Sin embargo, con la popularidad de Internet y la proliferación en el intercambio telemático de mensajes o documentos, se hace patente la necesidad de disponer de otros servicios de seguridad más allá del de la privacidad. Principalmente, los siguientes:
Integridad: poder identificar si un documento ha sido manipulado. Hay que poner de manifiesto que este servicio no evita la manipulación, sólo hace posible que siempre pueda ser detectada por el receptor.
Autenticación: poder garantizar cuál es la identidad del autor del documento, evitando su suplantación.
No repudio: evitar que el autor pueda negar que él ha generado el documento. El receptor puede demostrar a un tercero la identidad de quien realmente ha emitido el mensaje.

Estos servicios, si se contemplan los tres juntos, son los que le permiten llevar a cabo intercambios fiables de datos, como realizar transacciones o la venta de productos, hacer la declaración de la renta telemáticamente o conectarse a la banca online.
También permiten garantizar que si se almacena un documento en un ordenador, nadie lo habrá modificado cuando se vuelva a abrir sin que la manipulación no se haga patente.
La firma digital es el mecanismo criptográfico que traslada todas las propiedades de la firma manuscrita del mundo físico a la información en formato digital.

![Firma digital](../img/5_5%20firma%20digital.png)

[Vuelve a la presentación de la asignatura](README.md)