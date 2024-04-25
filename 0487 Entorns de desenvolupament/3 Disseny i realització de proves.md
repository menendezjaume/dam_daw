# 3. Disseny i realització de proves

## 1. Planificació de Proves

Aquesta secció proporcionauna base sòlida per comprendre com estructurar i gestionar el procés de prova dins del cicle de vida del desenvolupament de software, amb un èmfasi especial en la importància de la planificació anticipada i l'adaptabilitat.

### Introducció a la Planificació de Proves

La planificació de proves és un procés crític en el desenvolupament de software que implica determinar què provar, com provar-ho i quan. Es basa en la identificació de funcionalitats i components crítics del software per garantir la seva correcta execució.

La planificació eficaç de proves és fonamental per detectar errors, prevenir fallades, assegurar la qualitat del producte i reduir els costos a llarg termini.

Els principals objectius inclouen assegurar la cobertura de tots els requisits del software, identificar anticipadament els requisits de recursos, establir criteris clars per l'inici i la finalització de les proves, i definir mètriques per a l'avaluació dels resultats de les proves.

### Estratègies de Planificació

- **Determinació de Proves a Realitzar**: Aquesta fase implica l'anàlisi dels requisits de software, el disseny del sistema i el codi font per identificar les àrees clau on es centraran les proves. Es consideren factors com la complexitat del codi, les funcionalitats crítiques per a l'usuari i els components amb majors canvis des de la darrera versió.
- **Planificació Temporal**: És crucial determinar el calendari de les proves, incloent quan començaran, quan se suposa que finalitzaran, i com s'ajustarà aquesta planificació en resposta als imprevistos.
- **Selecció de Tècniques de Prova**: Decidir quines tècniques de prova (com proves unitàries, d'integració, de sistema, etc.) seran més adequades per a cada part del software.

### Gestió de Recursos i Temps

- **Assignació de Recursos**: Això implica determinar quants i quins recursos (humans, tecnològics, financers) seran necessaris per a la realització eficaç de les proves. Això inclou la selecció de l'equip de proves, l'assignació de tasques específiques a cada membre i la provisió dels equips i eines necessaris.
- **Planificació del Temps**: Establir un cronograma realista és essencial. Això inclou la definició dels terminis per a cada fase de prova, l'establiment de marges per a l'anàlisi i correcció d'errors, i l'adaptació a possibles retards.
- **Monitorització i Ajustament**: La planificació de proves és un procés dinàmic. Cal monitoritzar constantment el progrés respecte al pla i fer ajustaments segons sigui necessari, per exemple, reassignant recursos o redefinint terminis en resposta a desafiaments inesperats.

## 2. Tipus de Proves

Cada un d'aquests tipus de proves té un paper fonamental en el procés de garantia de qualitat del software. Les proves funcionals asseguren que el software fa el que se suposa que ha de fer, les proves estructurals validen la integritat i la qualitat del codi intern, i les proves de regressió protegeixen contra l'introducció involuntària de nous errors en el software ja existent. La combinació d'aquests tipus de proves ajuda a crear un software robust i fiable.

### Proves Funcionals

- **Definició i Objectiu**: Les proves funcionals es centren en comprovar si el programari compleix amb les especificacions i requisits definits. L'objectiu principal és validar la funcionalitat del software per assegurar-se que realitza les tasques per a les quals va ser dissenyat.
- **Implementació**: Aquest tipus de prova implica l'execució de casos de prova que simulen accions i entrades d'usuaris reals, amb l'objectiu d'observar si la sortida o comportament del software és el desitjat. Es poden utilitzar dades de prova reals o simulades per aquest propòsit.
- **Tècniques Comunes**:
  - **Proves de Caixa Negra**: Es centren en la funcionalitat sense considerar la construcció interna del codi. Es basen únicament en els requisits i especificacions.
  - **Proves d'Acceptació**: Realitzades per validar si el sistema compleix amb les expectatives del client o usuari final.
  - **Proves de Sistema**: Comproven que tots els components del sistema funcionen conjuntament com s'espera.

### Proves Estructurals

- **Definició i Objectiu**: També conegudes com a proves de caixa blanca, les proves estructurals avaluen la construcció interna del codi. L'objectiu és assegurar que tots els elements del codi (bucles, condicions, branques, etc.) han estat adequadament testejats.
- **Implementació**: Aquestes proves requereixen coneixement del codi font. Es dissenyen casos de prova per cobrir condicions específiques, branques, camins d'execució i bucles dins del codi.
- **Tècniques Comunes**:
  - **Anàlisi de Cobriment de Codi**: Mesura quant del codi s'ha executat durant les proves, amb l'objectiu de cobrir un percentatge significatiu del codi font.
  - **Proves de Bucles i Condicionals**: Especialment enfocades en la validació dels diferents camins lògics dins del codi.

### Proves de Regressió

- **Definició i Objectiu**: Les proves de regressió són crucials per assegurar que els canvis recents (com ara correccions de bugs, actualitzacions o millores) no afecten les funcionalitats existents del software. L'objectiu és detectar regressions, o sigui, errors introduïts involuntàriament a parts del programari que abans funcionaven correctament.
- **Implementació**:
  - **Selecció de Casos de Prova**: Es trien casos de prova rellevants del conjunt existent, especialment aquells que testegen funcionalitats que podrien haver estat afectades pels canvis recents.
  - **Automatització de Proves**: Les proves de regressió són ideals per a l'automatització, ja que sovint es necessita re-executar els mateixos casos de prova després de cada canvi significatiu.
- **Pràctiques Recomanades**:
  - **Proves Continues**: Realitzar proves de regressió de manera regular, especialment després de cada canvi major en el codi.
  - **Integració amb CI/CD (Continuous Integration/Continuous Deployment)**: La integració de les proves de regressió en els processos de CI/CD pot ajudar a detectar i resoldre problemes més ràpidament.

### Quines treballarem a classe?

#### El "unit testing" (proves unitàries)

El "unit testing" (proves unitàries) és un tipus de prova de software que es centra en verificar la correcta funcionalitat de les unitats més petites i independents d'un codi, com poden ser funcions, mètodes o classes. En les proves unitàries, cada component es prova de forma aïllada dels altres per garantir que funciona correctament de forma independent.

Aquest tipus de prova es pot considerar una combinació de proves funcionals i estructurals, tot i que està més a prop de les proves estructurals:

- **Com a Prova Funcional**: Les proves unitàries verifiquen si una unitat específica compleix amb el seu comportament esperat, similar a com es verificarien les funcionalitats en les proves funcionals. En aquest context, es posa a prova la funcionalitat de petites parts del codi, com ara una funció o mètode, per veure si realitzen les seves tasques com s'espera.

- **Com a Prova Estructural**: D'altra banda, les proves unitàries també tenen una gran rellevància en el context de les proves estructurals, ja que permeten als desenvolupadors inspeccionar el funcionament intern de petites unitats del codi, ajudant a identificar problemes específics dins de la lògica interna del codi.

Les proves unitàries són una part fonamental de molts processos de desenvolupament de software, especialment en entorns que practiquen la programació orientada a tests (TDD, Test-Driven Development). En aquests entorns, es comença pel disseny i implementació de les proves unitàries abans de desenvolupar el codi que ha de passar aquestes proves, garantint així un major enfocament en la qualitat i la robustesa del codi des de les primeres etapes del seu desenvolupament.

## 3. Procediments i Casos de Prova

La creació i execució de casos de prova, especialment en el marc del unit testing, són parts integrals del procés de desenvolupament de software. Asseguren que cada part del codi no només compleix amb els seus requisits específics sinó que també funciona correctament dins del sistema més gran. Aquest enfocament metodològic i disciplinat cap a les proves promou un codi de major qualitat i una major confiança en la robustesa i fiabilitat del software desenvolupat.

### Creació de Casos de Prova

La creació de casos de prova és un procés meticulós que implica definir condicions específiques sota les quals es comprovarà si una porció de codi funciona com s'espera. Aquesta tasca és crucial tant en proves generals com en unit testing.

- **Identificació de Requisits**: El primer pas en la creació de casos de prova és entendre els requisits del sistema o component que es prova. En el context del unit testing, això significa identificar el comportament esperat de cada unitat (funció, mètode o classe).
- **Definició de Casos de Prova**: Un cop identificats els requisits, es procedeix a definir casos de prova que cobreixin tots els possibles escenaris d'ús. Això inclou:
  - **Casos de Prova Positius**: Situacions on s'espera que el sistema o unitat funcioni correctament.
  - **Casos de Prova Negatius**: Condicions on s'espera que el sistema o unitat falli de manera controlada, com ara entrades no vàlides o condicions anormals.
  - **Casos de Prova de Límits**: Provar els límits dels rangs d'entrada acceptables.
- **Documentació**: Cada cas de prova hauria d'estar ben documentat, incloent la descripció del cas, els passos per executar-lo, les condicions d'entrada, i el resultat esperat.

#### Documentació de Casos de Prova

La documentació és un element fonamental en el procés de creació i execució de casos de prova. Una documentació clara i completa assegura que les proves siguin reproductibles, comprensibles i útils tant per a l'equip de desenvolupament actual com per a qualsevol persona que pugui treballar amb el codi en el futur. A continuació, es detallen els components clau que hauria d'incloure la documentació de cada cas de prova:

##### Descripció del Cas de Prova

- **Propòsit i Context**: Explica què s'està provant i per què és important. Per exemple, en una prova unitària, es podria descriure quina funcionalitat específica o cas d'ús està sent testejat.
- **Identificació**: Assigna un identificador únic a cada cas de prova. Això facilita la referència i la traçabilitat.

##### Passos per Executar-lo

- **Procediment Detallat**: Enumera els passos específics per executar el cas de prova. Això inclou la configuració inicial, les accions específiques que cal realitzar, i com revertir qualsevol canvi després de la prova.
- **Automatització**: Si el cas de prova està automatitzat (com és comú en unit testing), proporciona els scripts o comandes necessaris per executar la prova, així com qualsevol configuració de l'entorn necessària.

##### Condicions d'Entrada

- **Dades de Prova**: Detalla les dades d'entrada que s'utilitzaran en la prova. Això pot incloure valors específics, tipus de dades, o fins i tot l'estat del sistema necessari per a la prova.
- **Precondicions**: Descriu qualsevol estat o configuració del sistema que ha de ser present abans de començar la prova, com per exemple, que certes funcions hagin estat executades o que certes condicions de l'entorn estiguin establertes.

##### Resultat Esperat

- **Expectatives Clares**: Defineix clarament el resultat esperat de la prova. Això hauria d'incloure no només el resultat desitjat sinó també com verificar aquest resultat.
- **Criteris de Èxit i Fallada**: Estableix criteris clars per determinar si la prova ha estat exitosa o ha fallat. Això pot incloure descripcions de sortides esperades, canvis en l'estat del sistema, o missatges d'error específics.

##### Informació Addicional

- **Notes i Advertències**: Qualsevol observació addicional que pugui ser rellevant per a la persona que executa la prova, com ara possibles problemes coneguts o advertències sobre el comportament inesperat del sistema.
- **Referències**: Enllaços a documents relacionats, com requisits de software, especificacions de disseny, o informes d'errors que la prova ajuda a validar o verificar.

Una documentació ben elaborada per a cada cas de prova no només facilita l'execució i revisió de les proves sinó que també serveix com a registre valuós per a futures referències, ajudant a mantenir la qualitat i consistència del procés de desenvolupament de software a llarg termini.

### Execució i Seguiment

L'execució i el seguiment de les proves són tan importants com la seva planificació i creació. Aquesta fase assegura que els casos de prova es realitzen com s'ha previst i que els resultats es registren i analitzen adequadament.

- **Preparació per a l'Execució**: Abans de començar les proves, és essencial preparar l'entorn de prova. Això pot incloure la configuració dels sistemes, la preparació de les dades de prova, i l'assegurament que totes les dependències necessàries estan disponibles.
- **Execució de Casos de Prova en Unit Testing**:
  - En el context del unit testing, l'execució de casos de prova sovint es realitza de manera automatitzada, utilitzant eines com JUnit per a Java o PyTest per a Python.
  - Els tests unitaris s'executen de forma aïllada per verificar la correcta funcionalitat de cada unitat individual.
  - Les proves es poden integrar en processos de integració contínua per a la seva execució automàtica en cada canvi de codi.
- **Monitorització i Registre**: Durant l'execució de les proves, és crucial monitoritzar el procés i registrar els resultats. Això inclou el seguiment dels casos de prova que han passat, els que han fallat, i qualsevol comportament inesperat.
- **Anàlisi dels Resultats**: Un cop completades les proves, s'analitzen els resultats. Això implica revisar els casos de prova fallits, identificar les causes dels errors, i determinar si es necessiten més proves o correccions en el codi.

#### Execució de Casos de Prova en Unit Testing

L'execució de casos de prova en el context del unit testing és un component crític del desenvolupament de software. A continuació, es descriu de forma pràctica com s'executen aquests tests, amb un èmfasi especial en l'ús d'eines com JUnit per a Java i PyTest per a Python, així com la seva integració en processos de integració contínua.

##### Utilització d'Eines d'Automatització

###### JUnit per a Java

- **Preparació**: Instal·la JUnit com a dependència en el teu projecte Java. Això normalment es fa a través de gestors de dependències com Maven o Gradle.
- **Escriptura de Tests**: Crea una classe de test per a cada classe de codi que vols provar. Utilitza anotacions com `@Test` per marcar mètodes com a tests unitaris.
- **Execució de Tests**: Pots executar els tests unitaris directament des de l'entorn de desenvolupament integrat (IDE) o mitjançant una línia de comandes. JUnit proporcionarà un informe dels resultats dels tests.

Clarament! A continuació, proporcionaré exemples senzills de com s'utilitzen JUnit per a Java i PyTest per a Python per a l'execució de tests unitaris.

###### Exemple de JUnit per a Java

Suposem que tenim una classe simple en Java anomenada `Calculadora` que té un mètode per sumar dos números. Aquí tens un exemple de com es podria escriure un test unitari per a aquest mètode utilitzant JUnit:

###### Classe `Calculadora`:

```java
public class Calculadora {
    public int suma(int a, int b) {
        return a + b;
    }
}
```

###### Classe de Test Utilitzant JUnit:

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculadoraTest {

    @Test
    public void testSuma() {
        Calculadora calc = new Calculadora();
        int resultat = calc.suma(5, 3);
        assertEquals(8, resultat);
    }
}
```

En aquest exemple, `assertEquals` es fa servir per verificar que el resultat de la suma és el que esperem. Si el resultat és diferent, el test fallarà.

#### Execució dels Tests:

Per executar els tests unitaris en JUnit, normalment es fa des de l'entorn de desenvolupament integrat (IDE) o mitjançant una línia de comandes utilitzant una eina de construcció com Maven o Gradle.

###### PyTest per a Python

- **Preparació**: Instal·la PyTest utilitzant pip, l'eina de gestió de paquets de Python.
- **Escriptura de Tests**: Crea fitxers de test per les teves funcions i classes Python. Les funcions de test en PyTest comencen amb el prefix `test_`.
- **Execució de Tests**: Executa PyTest des de la línia de comandes per executar tots els tests. PyTest detectarà automàticament i executarà els tests, proporcionant informació detallada sobre el seu èxit o fracàs.

###### Exemple de PyTest per a Python

Anem a veure un exemple similar en Python. Suposa que tenim una funció `suma` en un mòdul `calculadora.py`:

###### Mòdul `calculadora.py`:

```python
def suma(a, b):
    return a + b
```

###### Fitxer de Test Utilitzant PyTest:

Anomenem aquest fitxer `test_calculadora.py`. PyTest identificarà automàticament els fitxers i funcions de test que comencin amb `test_`.

```python
from calculadora import suma

def test_suma():
    assert suma(5, 3) == 8
```

En aquest cas, utilitzem l'afirmació `assert` per comprovar si la funció `suma` retorna el resultat esperat. Si l'expressió dins de `assert` es valora com a `False`, el test fallarà.

#### Execució dels Tests:

Per executar PyTest, pots simplement executar `pytest` des de la línia de comandes en el directori que conté els fitxers de test, i PyTest buscarà i executarà automàticament tots els tests.

##### Execució Aïllada

- **Principi d'Aïllament**: Cada test unitari hauria de ser independent dels altres. Això significa que no ha de dependre de l'estat creat per altres tests, i no hauria de canviar l'estat que pugui afectar altres tests.
- **Gestió d'Estat**: Utilitza mètodes de configuració i neteja (com `setUp` i `tearDown` en JUnit, o fixtures en PyTest) per establir un entorn de test consistent per a cada cas de prova.

##### Integració en CI/CD

- **Configuració de CI/CD**: Integrar els tests unitaris en un sistema de integració contínua (CI/CD) com Jenkins, Travis CI, o GitHub Actions. Això permet que els tests s'executin automàticament cada cop que es realitza un canvi en el codi.
- **Automatització de l'Execució de Tests**: Configura el teu sistema CI/CD per executar els tests unitaris cada cop que es realitzen canvis en el codi, com ara en fer push a un repositori o fusionar pull requests.
- **Monitorització de Resultats**: Utilitza eines de CI/CD per monitoritzar els resultats dels tests. Si un test falla, el sistema pot alertar els desenvolupadors i, en alguns casos, fins i tot impedir la integració del codi fins que els problemes siguin resolts.

##### Beneficis de l'Automatització i Integració en CI/CD

- **Detecció Ràpida d'Errors**: L'execució automàtica de tests unitaris ajuda a identificar ràpidament problemes en el codi, permetent als desenvolupadors abordar-los abans que avancin massa en el procés de desenvolupament.
- **Qualitat de Codi Millorada**: Els tests unitaris regulars i automatitzats asseguren que el codi manté un alt nivell de qualitat a mesura que es desenvolupa i manté.
- **Confiança en el Desenvolupament**: Amb tests unitaris executant-se de manera consistent, els equips de desenvolupament poden sentir-se més segurs en fer canvis i actualitzacions al codi, sabent que qualsevol regressió serà ràpidament detectada.

La pràctica de l'execució de casos de prova en unit testing mitjançant eines d'automatització i la seva integració en processos de CI/CD és fonamental per assegurar la qualitat i la fiabilitat en el desenvolupament de software modern. Aquest enfocament no només optimitza el procés de testejament sinó que també promou una cultura de qualitat i eficiència dins dels equips de desenvolupament.

## 4. Proves de Codi

- **Cobriment de Codi**: Tècniques per assegurar que tot el codi s'ha provat.
- **Proves de Valors Límit i Classes d'Equivalència**: Identificar i provar els casos límit.
- **Anàlisi Estàtica i Dinàmica**: Eines i tècniques per a l'anàlisi de codi.

## 5. Proves Unitàries i Eines d'Automatització

- **Introducció a les Proves Unitàries**: Principis bàsics i importància.
- **Eines d'Automatització**: JUnit per a Java, PyTest per a Python, entre d'altres.
- **Integració amb Entorns de Desenvolupament**: Com integrar aquestes eines amb IDEs com Eclipse o PyCharm.

## 6. Documentació de les Incidències

- **Registre i Seguiment d'Incidències**: Eines i metodologies.
- **Anàlisi i Resolució**: Com analitzar i resoldre les incidències documentades.

## 7. Dobles de Prova

- **Concepte i Tipus**: Mocks, Stubs, i altres dobles de prova.
- **Característiques i Utilització**: Com i quan utilitzar dobles de prova en l'entorn de DAM.

Cadascun d'aquests punts hauria de ser desenvolupat amb detall, incloent exemples pràctics, especialment enfocats en l'ús de Java i Python, per facilitar la comprensió i l'aplicació dels conceptes per part dels estudiants. A més, seria recomanable incloure activitats pràctiques, com exercicis de codi i casos d'estudi, per reforçar l'aprenentatge.

[Torna a la presentació de l'assignatura](README.md)
