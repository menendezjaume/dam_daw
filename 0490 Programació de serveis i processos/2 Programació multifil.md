# 2. Programació multifil

## Introducció a la Programació Multifil

La programació multifil es refereix a la capacitat d'un programa d'executar múltiples tasques o subprogrames, coneguts com a "fils", de manera simultània. Aquesta simultaneïtat pot ser aprofitada per a millorar l'eficiència i el rendiment dels programes, especialment en sistemes amb múltiples nuclis o processadors.

## Definició i conceptes bàsics

Fil (Thread): És la unitat més petita de processament que pot ser programada i gestionada per un sistema operatiu. A diferència d'un procés complet, un fil comparteix recursos i espai de memòria amb altres fils dins del mateix procés.

Multitasking: És la capacitat d'un sistema operatiu d'executar múltiples tasques o programes al mateix temps. La programació multifil es considera una forma de multitasking més granular on diverses operacions s'executen dins d'un sol procés.

Concurrença vs Paral·lelisme: La concurrença es refereix a la capacitat d'un sistema de gestionar múltiples tasques al mateix temps (potser no necessàriament s'executen al mateix instant). El paral·lelisme es refereix a l'execució real i simultània de múltiples tasques o fils. En sistemes amb un sol nucli, la concurrença pot ser realitzada a través de la commutació ràpida entre tasques, mentre que el paral·lelisme real requereix múltiples nuclis o processadors.

## És a dir…

![Fils](imatges/2_1%20fils.png)

## Diferència entre fils i processos

||Processos|Fils|
|-|-|-|
|Definició|Són programes en execució que tenen el seu propi espai d'adreça en emòria. Cada procés és completament independent i corre en el seu propi context.|Són unitats més petites dins d'un procés. Tots els fils dins d'un rocés comparteixen el mateix espai d'adreça, però tenen el seu propi registre i pila.|
|Recursos|Tenen recursos independents (memòria, registres, etc.).|Comparteixen recursos dins d'un procés (memòria heap, arxius oberts, tc.), però tenen la seva pròpia pila.|
|Creació i terminació|Són més costosos de crear i destruir.|Són més lleugers i, per tant, més ràpids de crear i destruir.|
|Comunicació|La comunicació entre processos (IPC) pot ser més complexa i lenta.|La comunicació entre fils és més ràpida degut a la memòria compartida, erò pot portar a condicions de carrera si no es gestiona adequadament.|

## Tornant al multitasking…

La capacitat d'executar múltiples tasques simultàniament en un sistema s'anomena multitasking. Hi ha dos tipus principals:

* **Multitasking Preemptiu**: El sistema operatiu decideix quan canviar de tasca basant-se en prioritats o altres factors.
* **Multitasking Cooperatiu**: Cada tasca decideix quan cedir el control a una altra tasca.

Quan es treballa amb diversos fils, de vegades cal pensar en la seva planificació, per assegurar-se que cada fil té una oportunitat justa d’executar-se. És per això que els fils poden tenir diferents prioritats durant el seu cicle de vida.

## Característiques dels fils

Capacitat de resposta. Els fils permeten als processos continuar atenent peticions de l'usuari encara que alguna de les tasques (fil) que estigui fent el programa sigui molt llarga.

Compartició de recursos. Per defecte, els threads comparteixen la memòria i tots els recursos del procés a què pertanyen.

La creació de nous fils no suposa cap reserva addicional de memòria per part del sistema operatiu.

Paral·lelisme real. La utilització de threads permet aprofitar l'existència de més d'un nucli al sistema en arquitectures multicore.

## Per tant…

|Avantatges|Desavantatges|
|-|-|
|**Eficiència en el rendiment**: En dispositius amb múltiples nuclis o processadors, els fils poden executar-se en paral·lel, augmentant així el rendiment global.|**Complexitat**: La gestió de múltiples fils pot complicar el codi, especialment quan es tracta de sincronització i comunicació entre fils.|
|**Responsivitat millorada**: Per aplicacions d'interfície d'usuari, un fil pot gestionar la interfície mentre un altre fil efectua operacions més llargues en segon pla, mantenint així l'aplicació responsiva.|**Condicions de carrera**: Es produeixen quan dos o més fils intenten accedir o modificar una variable compartida al mateix temps, el que pot donar lloc a resultats inesperats.|
|**Compartició de recursos**: Dins d'un mateix procés, els fils comparteixen l'espai de memòria, la qual cosa pot facilitar la comunicació i el passatge d'informació entre fils.|**Deadlocks**: Succeeixen quan dos o més fils esperen indefinidament per un recurs que és utilitzat per un altre fil.|
||**Sobrecàrrega**: Crear un nombre excessiu de fils pot causar una sobrecàrrega en el sistema, la qual cosa pot reduir l'eficiència global.|

## Estats d’un fil

Aquest són els estats d'un fil:

* **NEW**: Quan es crea el fil però encara no s'ha iniciat.
* **RUNNABLE**: El fil està actiu i potser està executant-se o està en cua esperant el seu torn per executar-se.
* **RUNNING**: El fil s’està executant.
* **BLOCKED**: El fil està esperant un recurs per continuar.
* **WAITING**: El fil està esperant indefinidament per una altra acció per continuar.
* **TIMED_WAITING**: Està esperant per una altra acció durant un temps determinat.
* **TERMINATED**: El fil ha finalitzat la seva execució.

![Estats d'un fil](imatges/2_2%20estats%20fils.png)

## Recursos compartits pels fils

Dins d'un procés, els fils comparteixen diversos recursos:

* **Espai d'adreça de memòria**: Això inclou la memòria heap, que pot ser accedida per qualsevol fil.
* **Arxius oberts**: Si un fil obre un arxiu, aquest pot ser accedit per altres fils.
* **Variables globals**: Les variables globals d'un programa estan disponibles per a tots els fils.
* **Instruccions del programa**: El codi que s'executa.

Tot i que aquests recursos compartits permeten una ràpida i eficient comunicació entre fils, també introdueixen desafiaments en termes de sincronització i condicions de carrera.

![Esquema visual de recursos compartits pels fils](imatges/2_3%20esquema%20recursos%20compartits.png)

## Fils en Java

Quan comencem un programa en Java hi ha un fil en execució, el fil principal, que és creat pel mètode `main()`. Aquest fil és important, ja que és l’encarregat, si cal, de crear la resta de fils del programa. S’ha de programar l’aplicació perquè el fil principal sigui l’últim en acabar la seva execució. Això s’aconsegueix fent esperar els fils creats pel fil principal que aquest últim finalitzi.

### Creació i gestió de fils

En Java, hi ha dues maneres principals de crear fils:

* Estenent la classe Thread.
* Implementant la interfície Runnable.

#### Estenent la classe Thread

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Aquest és un fil en execució.");
    }
}

public class Test {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start(); // Inicia l'execució del fil
    }
}
```

#### Implementant la interfície Runnable

```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Aquest és un fil en execució.");
    }
}

public class Test {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable());
    t.start(); // Inicia l'execució del fil
    }
}
```

#### Quan fem servir cadascun?

Implementar Runnable és generalment preferit perquè Java no permet l'herència múltiple, cosa que significa que pots estendre una altra classe si necessites.

Si no necessites herència, pots fer servir la classe Thread, ja que és més completa. De fet, la classe Thread implementa la classe Runnable.

### Mètodes principals de la classe Thread

* `start()`: Inicia l'execució del fil, cridant al mètode run().
* `run()`: És el mètode que conté el codi que el fil ha d'executar. Ha de ser sobreposat.
* `sleep(long millis)`: Intenta fer que el fil actual dormi (cessi d'executar) pel temps especificat en mil·lisegons.

    ```java
    try {
        Thread.sleep(1000); // Dorm el fil per 1 segon
    } catch (InterruptedException e) {
        // Gestionem l’excepció
    }
    ```

* `join()`: Fa que el fil en el qual es crida esperi que el fil al qual s'aplica aquest mètode acabi la seva execució.
* `interrupt()`: Interrumpeix el fil.
* `isAlive()`: Retorna true si el fil encara s'està executant; false en cas contrari.

```java
Thread t1 = new Thread(new MyRunnable());
t1.start();
try {
    t1.join(); // Espera que t1 acabi la seva execució
} catch (InterruptedException e) {
    // Gestionem l’excepció
}
```

### Prioritats

Pots assignar una prioritat a un fil utilitzant `setPriority(int)`. Els valors poden estar entre `Thread.MIN_PRIORITY` i `Thread.MAX_PRIORITY`, sent `Thread.NORM_PRIORITY` el valor per defecte.

### Sincronització

La sincronització és una de les àrees més crítiques i desafiantes de la programació multifil. Com que múltiples fils poden accedir a les mateixes estructures de dades o recursos de manera simultània, és fonamental garantir que aquest accés sigui controlat i consistent. Sense una sincronització adequada, es poden produir condicions de carrera, inconsistències en les dades i resultats imprevisibles.

> *Condicions de carrera*
>
> *Una condició de carrera ocorre quan dos o més fils accedeixen simultàniament a una eina compartida o a una variable, i almenys un d'aquests acessos és una escriptura. Si els fils es realitzen en un ordre específic, es pot produir un comportament indeterminat.*
>
> *La solució a les condicions de carrera sol ser la introducció de mecanismes de sincronització que garanteixen que només un fil pot accedir a l'eina compartida a la vegada.*

Mètodes de sincronització:

* Semàfors.
* Bloquejos (Locks).
* Mètodes o sentencies sincronitzades (synchronized en Java).
* Variables condicionals.

#### Semàfors

És un *comptador* que permet a un nombre específic de fils accedir a un recurs. Això és útil quan es vol limitar el nombre de fils que poden utilitzar un recurs particular.

Java proporciona la classe Semaphore dins del paquet `java.util.concurrent`.

#### Bloquejos (Locks)

Un bloqueig és un mecanisme que permet a un fil "bloquejar" un recurs, impedint que altres fils hi accedeixin fins que el primer fil el "desbloqueja".

En Java, es pot utilitzar l'objecte ReentrantLock del paquet `java.util.concurrent.locks`.

#### Mètodes o sentencies sincronitzades (synchronized en Java)

Es tracta d'una paraula clau que pot ser utilitzada per garantir que només un fil pot executar un mètode o bloc específic al mateix temps.

```java
public synchronized void myMethod() {
    // codi sincronitzat
}
```

#### Variables condicionals

Són útils quan un fil ha d'esperar fins que es compleixi una condició específica.

En Java, es poden utilitzar juntament amb `ReentrantLock`.

### Problemes: Deadlocks

Un deadlock ocorre quan **dos o més fils estan esperant indefinidament per un conjunt de recursos bloquejats, i cap d'ells pot continuar fins que l'altre alliberi els recursos**.

Algunes estratègies per **prevenir** deadlocks inclouen:

* Assegurar-se que els fils adquireixen bloquejos en el mateix ordre.
* Utilitzar timeouts quan s'intenta adquirir un bloqueig.
* Detectar la situació de deadlock i interrompre un dels fils.

Algunes eines i tècniques permeten **detectar** deadlocks en temps d'execució o durant les proves, facilitant la correcció del problema.

[Torna a la presentació de l'assignatura](README.md)
