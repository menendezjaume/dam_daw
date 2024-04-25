# 1. Programació multiprocés

Un cuiner que tingui intenció de fer un plat molt elaborat, amb salses i guarnicions diferents, probablement farà servir diferents paelles per cuinar cada element que necessiti utilitzar per elaborar el plat. Tindrà una paella amb la salsa, una altra preparant la guarnició i en una altra cuinarà el plat principal. Tot això ho farà alhora i, finalment, quan acabi totes aquestes tasques les ajuntarà en un únic plat.

Aquesta analogia ens serveix per introduir el terme multiprocés. El cuiner està executant diferents processos a la vegada: cuina la salsa, la guarnició i el plat principal, seguint un ordre d’execució per arribar a un resultat que esperava, un bon plat.

## Procés, sistemes monoprocessador-multiprocessador

Un programa és un element estàtic, un conjunt d’instruccions, unes línies de codi escrites en un llenguatge de programació, que descriuen el tractament que cal donar a unes dades inicials (d’entrada) per aconseguir el resultat esperat (una sortida concreta).

En canvi, un procés és dinàmic, és una instància d’un programa en execució, que realitza els canvis indicats pel programa a les dades inicials i obté una sortida concreta. El procés, a més de les instruccions, requerirà també de recursos específics per a l’execució com ara el comptador d’instruccions del programa, el contingut dels registres o les dades.

El sistema operatiu és l’encarregat de la gestió de processos. Els crea, els elimina i els proveeix d’instruments que en permetin l’execució i també la comunicació entre ells.

Quan s’executa un programa, el sistema operatiu crea una instància del programa: el procés. Si el programa es tornés a executar es crearia una nova instància totalment independent a l’anterior (un nou procés) amb les seves pròpies variables, piles i registres.

Imaginem un ordinador en el qual tenim instal·lat un programa d’edició de text. Posem per cas que volem escriure diversos textos a la vegada executant l’editor.

Cada instància del programa és un procés totalment independent als altres. Cada procés té unes dades d’entrada i per tant diferents sortides. A cada editor (el procés) s’escriurà el seu text.

![Processos](../img/1_1%20processos.png)

Un sistema monoprocessador és aquell que està format únicament per un processador.

Un sistema multiprocessador està format per més d’un processador.

![Placa](../img/1_2%20placa.png)

## Programació concurrent

De forma genèrica anomenarem els processos que s’executin a la vegada, ja sigui de forma real o simulada, processos concurrents.

L’execució de processos concurrents, encara que sigui de forma simulada, fa augmentar el rendiment del sistema informàtic ja que aprofita més el temps del processador. És el sistema operatiu l’encarregat de gestionar l’execució concurrent de diferents processos contra un mateix processador.

![Programació concurrent](../img/1_3%20programacio%20concurrent.png)

## Programació paral·lela

Quan la programació concurrent es realitza en un sistema multiprocessador parlem de programació paral·lela.

El principal desavantatge de la programació paral·lela són els controls que hem d’afegir per tal que la comunicació i sincronització dels processos que s’executen concurrentment siguin correctes.

Dos processos s’han de sincronitzar o comunicar quan un procés necessita alguna dada que està processant l’altre o bé un d’ells ha d’esperar la finalització de l’altre per poder continuar la seva execució.

![Programació paralela](../img/1_4%20programacio%20paralela.png)

## Programació distribuïda

Un tipus especial de programació paral·lela és l’anomenada programació distribuïda. Aquesta programació es dona en sistemes informàtics distribuïts.

Un sistema distribuït està format per un conjunt d’ordinadors que poden estar situats en llocs geogràfics diferents units entre ells a través d’una xarxa de comunicacions.

Un exemple de sistema distribuït pot ser el d’un banc amb moltes oficines al món, amb un ordinador central per oficina per guardar els comptes locals i fer les transaccions locals. Aquest ordinador es pot comunicar amb els altres ordinadors centrals de la xarxa d’oficines. Quan es fa una transacció no importa on es troba el compte o el client.

![Programació distribuïda](../img/1_5%20programacio%20distribuida.png)

## Processos i serveis

Un servei és un tipus de procés que no té interfície amb l’usuari.

Poden ser, depenent de la seva configuració, inicialitzats pel sistema de forma automàtica, en el qual van realitzant les seves funcions sense que l’usuari se n’assabenti o bé es poden mantenir a l’espera que algú els faci una petició per fer una tasca en concret.

Depenent de com s’estan executant, els processos es classificaran com a processos en primer pla (foreground, en anglès) i processos en segon pla (background).

Els processos en primer pla mantenen una comunicació amb l’usuari, ja sigui informant de les accions realitzades o esperant les seves peticions per mitjà d’alguna interfície d’usuari.

En canvi, els que s’executen en segon pla no es mostren explícitament a l’usuari, bé perquè no els cal la seva intervenció o bé perquè les dades requerides no s’incorporen a través d’una interfície d’usuari. Aquest també és conegut com a DAEMON.

Els serveis són processos executats en segon pla. Servei és una nomenclatura utilitzada en Windows. En sistemes Linux s’anomenen també processos deamon.

A Linux el nom dels daemons sempre acaben amb la lletra d, com ara httpd, el daemon de l’http.

## Fils i processos

Els processos són anomenats entitats pesades perquè estan a espais de direccionament de memòria independents, de creació i de comunicació entre processos, cosa que consumeix molts recursos de processador.

En canvi, ni la creació de fils ni la comunicació consumeixen gaire temps de processador. Per aquest motiu els fils s’anomenen entitats lleugeres.

Procés amb un únic fil en execució i procés amb diversos fils en execució

![Fils i processos](../img/1_6%20fils%20i%20processos.png)

## Gestió de processos

Un del objectius del sistema operatiu és proporcionar als processos els recursos necessaris per la seva execució. Ha d’aconseguir una política de planificació que determini quin procés farà ús del processador. El sistema operatiu és, doncs, l’encarregat de decidir quin procés cal executar i durant quant de temps cal fer-ho.

Tots els sistemes operatius disposen d’un planificador de processos encarregat de repartir l’ús del processador de la forma més eficient possible i assegurant que tots els processos s’executin en algun moment. Per realitzar la planificació, el sistema operatiu es basarà en l’estat dels processos per saber quins necessitaran l’ús del processador. Els processos en disposició de ser executats s’organitzaran en una cua esperant el seu torn.

## Estats d’un procés

![Estats d'un procés](../img/1_7%20estats%20proces.png)

## Arbre de processos

El sistema operatiu és l'encarregat de crear els nous processos seguint les directrius de l'usuari.

* La posada en execució d'un nou procés es produeix pel fet que hi ha un procés en concret que està demanant la seva creació en nom o en nom de l'usuari.
* Qualsevol procés en execució (procés fill) sempre depèn del procés que el va crear (procés pare), establint-se un vincle entre tots dos. Alhora, el nou procés pot crear nous processos, formant-se el que s'anomena un arbre de processos.

### Exercici

Obre el controlador de processos i identifica algun arbre de processos.

## Operacions bàsiques

Creació de processos. Quan es crea un nou procés fill, tots dos processos, pare i fill s'executen concurrentment.

* Ambdós processos comparteixen la CPU i s'aniran intercanviant processos comparteixen la CPU i s'aniran intercanviant seguint la política de planificació del
* Si el procés pare necessita esperar fins que el fill acabi la seva execució, ho pot fer mitjançant l'operació ho pot fer mitjançant l'operació wait.
* Els processos són independents i tenen el seu propi espai de memòria assignat, anomenat imatge de memòria.

Terminació de processos. En acabar l'execució d'un procés, cal avisar el sistema operatiu de la seva terminació per alliberar els recursos que tingui assignats.

* En general, és el mateix procés el que indica al sistema mitjançant l'operació èxit que vol acabar, podent aprofitar per enviar informació de la finalització al pare.

## Creació de processos a Java

La classe que representa un procés en Java és la classe Process.

> Els mètodes de ProcessBuilder.start() i Runtime.exec() creen un procés nadiu al sistema operatiu subjacent i tornen una de la classe Process que pot ser utilitzat per controlar aquest procés.

El mètode start() inicia un procés nou procés utilitzant els atributs indicats a l'objecte. El nou procés executa l'ordre i els arguments indicats al mètode command(), executant-se al directori de treball especificat per directory(), utilitzant les variables d'entorn definides en environment()

El mètode exec(cmdarray, envp, dir) executa l'ordre especificada i arguments especificats a cmdarray en un procés fill independent amb l'entorn envp i el directori de treball especificat en dir

```java
public class CreateProcess {
    public static void main(String[] args) throws Exception {
        var processBuilder = new ProcessBuilder();
        processBuilder.command("notepad.exe");
        var process = processBuilder.start();
        var exitCode = process.waitFor();
        System.out.printf("Program exited with code: %d", exitCode);
    }
}
```

## Terminació de processos

El procés fill realitzarà la seva execució completa acabant i el procés fill realitzarà la seva execució completa acabant i alliberant els seus recursos en finalitzar.

Això es produeix quan el fill realitza l'operació èxit per finalitzar la seva execució.

Un procés pare pot a més acabar de forma abrupta un procés fill que va crear mitjançant l'operació destroy

* Aquesta operació elimina el procés fill indicat alliberant els seus recursos al sistema operatiu subjacent.
* A Java, els recursos corresponents els eliminarà el garbage collector quan consideri.

## Comunicació entre processos

Un procés rep informació, la transforma i produeix resultats mitjançant:

* Entrada estàndard (stdin): lloc d'on el procés llegeix les dades d'entrada que requereix per executar-lo. Normalment és el teclat.
* Sortida estàndard (stdout): lloc on el procés escriu els resultats que obté. Normalment és la pantalla.
* Sortida d'errors (stderr): lloc on el procés envia els missatges d'error. Habitualment és el mateix que la sortida estàndard, però es pot especificar que sigui un altre lloc, com un fitxer.

En Java, el procés fill no té la seva pròpia interfície de comunicació, de manera que l'usuari no pot comunicar-se amb ell directament.

Stdin, stdout i stderr estan redirigides al procés pare a través dels fluxos de dades:

* OutputStream: flux de sortida del procés fill. El stream està connectat per un pipe a l'entrada estàndard (stdin) del procés fill.
* InputStream: flux d'entrada del procés fill. El stream està connectat per un pipe a la sortida estàndard (stdout) del procés fill.
* ErrorStream: flux d'error del procés fill. El stream està connectat per un pipe a la sortida estàndard (stderr) del procés fill. Per defecte, està connectat al mateix lloc que stdout.

## Redirecció dels streams del fill

El pare, podrà redirigir els streams del fill a voluntat. Per això, el ProcessBuilderE té uns mètodes que són el redirectOutput, redirectInput i redirectError; i fan servir la subclasse ProcessBuilder.Redirect.

Redirect representa una font d'entrada o una destinació de la sortida del subprocés. Cada instància de Redirect és una de les següents:

* el valor especial Redirect.PIPE
* el valor especial Redirect.INHERIT
* el valor especial Redirect.DISCARD
* una redirecció per llegir des d'un fitxer, creada per una invocació de Redirect.from(File)
* una redirecció per escriure a un fitxer, creada per una invocació de Redirect.to(File)
* una redirecció per afegir a un fitxer, creada per una invocació de Redirect.appendTo(File)

## Sincronització entre processos

Els mètodes de comunicació de processos es poden considerar com a mètodes de sincronització, ja que permeten al procés pare portar el ritme d'enviament i de recepció de missatges.

A més de la utilització de fluxos de dades es pot esperar per la finalització del procés fill mitjançant l'operació wait.

* Bloqueja el procés pare fins que el fill finalitza la seva execució mitjançant exit.
* Com a resultat el pare rep la informació de finalització del procés fill, és a dir, l'exit code.

```java
Process p = Runtime.getRuntime().exec("notepad.exe");

InputStream in = p.getInputStream();

for (int i = 0; i < in.available(); i++) {

   System.out.println("" + in.read());

}
```

## La classe process

|Métode|Tipus de retorn|Descripció|
|-|-|-|
|getOutputStream()|OutputStream|Obté el flux de sortida del procés fill connectat al stdin|
|getInputStream()|InputStream|Obté el flux d'entrada del procés fill connectat a l'stout del procés ill|
|getErrorStream()|InputStream|Obté el flux d'entrada del procés fill connectat al sterr del procés ill|
|destroy()|void|Implementa l'operació destroy|
|waitFor()|int|Implementa l'operació wait|
|exitValue()|int|Obté el valor de retorn del procés fill|

[Torna a la presentació de l'assignatura](README.md)
