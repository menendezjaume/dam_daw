# 2. Instal·lació i ús d’entorns de desenvolupament

## 1. Instal·lació d'un entorn de desenvolupament integrat (IDE)

Instal·lació d'un entorn de desenvolupament integrat (IDE)
El procés d'instal·lació pot variar segons l'entorn de desenvolupament que es vulgui utilitzar i el sistema operatiu en què s'instal·larà. 
Aquí es descriurà com a exemple el procés d'instal·lació de Visual Studio Code i la Instal·lació d'IntelliJ IDEA, en un sistema operatiu Windows.

### Visual Studio Code

Pas 1: Descàrrega del Programa
Obre el navegador web i visita la pàgina oficial de Visual Studio Code: https://code.visualstudio.com/
Cerca el botó de descàrrega, que normalment detecta automàticament el teu sistema operatiu i mostra l'opció adequada. Per a Windows, faràs clic en "Download for Windows".
Guarda l'arxiu executable (.exe) en una carpeta del teu ordinador.
Pas 2: Execució de l'Instal·lador
Navega fins a la carpeta on has descarregat l'instal·lador i fes doble clic en l'arxiu executable per iniciar el procés d'instal·lació.
Segueix les instruccions que apareixen a la pantalla. Això pot incloure acceptar els termes de la llicència, triar la carpeta de destinació per a la instal·lació, i seleccionar opcions addicionals com crear una icona d'accés directe a l'escriptori o afegir Visual Studio Code al PATH (això últim permet obrir l'IDE des de la línia de comandes).
Fes clic en "Install" per començar la instal·lació.
Pas 3: Configuració Inicial i Comprovació de la Instal·lació
Un cop finalitzada la instal·lació, selecciona l'opció per obrir Visual Studio Code si no està ja seleccionada, i fes clic en "Finish".
Visual Studio Code s'obrirà, mostrant la pantalla d'inici.
Si desitges, pots explorar les opcions de configuració i personalitzar l'entorn segons les teves preferències. Això pot incloure canviar el tema de colors, instal·lar extensions, configurar dreceres de teclat, entre altres.
Pas 4: Instal·lació d'Extensions (Opcional)
Visual Studio Code té una àmplia comunitat i un gran catàleg d'extensions que pots instal·lar per afegir funcionalitats addicionals. Per exemple, si vols desenvolupar en un llenguatge de programació específic, pot ser útil buscar i instal·lar una extensió que proporcioni suport per a aquest llenguatge.
Fes clic a la icona d'extensions a la barra lateral esquerra.
Cerca l'extensió que vols instal·lar en la barra de cerca.
Fes clic a "Install" a l'extensió desitjada.

### IntelliJ Idea

1. Descàrrega del Programa
Obre el navegador web i visita la pàgina oficial de JetBrains: https://www.jetbrains.com/idea/download/
Trobaràs dues versions d'IntelliJ IDEA: Community i Ultimate. La versió Community és gratuïta i ofereix funcionalitats bàsiques, mentre que la versió Ultimate és de pagament i inclou funcionalitats addicionals. Selecciona la versió que prefereixis.
Fes clic en "Download" a la versió seleccionada per Windows. L'arxiu executable (.exe) es descarregarà a una carpeta del teu ordinador.
2. Execució de l'Instal·lador
Navega fins a la carpeta on has descarregat l'instal·lador i fes doble clic en l'arxiu executable per iniciar el procés d'instal·lació.
Segueix les instruccions que apareixen a la pantalla. Això pot incloure acceptar els termes de la llicència, triar la carpeta de destinació per a la instal·lació, i seleccionar opcions addicionals com crear una icona d'accés directe a l'escriptori o associar determinats tipus d'arxiu amb IntelliJ IDEA.
Fes clic en "Install" per començar la instal·lació.
3. Configuració Inicial i Comprovació de la Instal·lació
Un cop finalitzada la instal·lació, fes clic en "Finish" per obrir IntelliJ IDEA.
En obrir-se, et pot demanar que configures les teves preferències de configuració, com el tema de colors, les configuracions del teclat, i altres opcions de desenvolupament.
Pots crear un nou projecte, obrir-ne un d'existent, o importar configuracions si és necessari.

## 2. Funcions d'un entorn de desenvolupament integrat (IDE)

Un entorn de desenvolupament integrat (IDE) és un programari que proporciona eines i facilitats per ajudar els desenvolupadors de programari durant el procés de creació d'aplicacions. A continuació es detallen les funcions principals d'un IDE:
Editor de Codi: Permet als desenvolupadors escriure i editar el codi font dels seus programes. Ofereix funcionalitats com el ressaltat de sintaxi, que destaca diferents parts del codi amb colors per facilitar la seva lectura, i l'autocompletat, que suggerix completaments per a noms de variables, funcions i altres elements del codi.
Compilador/Intèrpret: Tradueix el codi font escrit pel desenvolupador a codi màquina o a un llenguatge intermedi que pot ser executat per una màquina virtual. Això depèn del llenguatge de programació utilitzat.
Depurador: Proporciona eines per trobar i solucionar errors (bugs) en el codi. Permet als desenvolupadors executar el seu programa pas a pas, inspeccionar valors de variables, i establir punts d'aturada (breakpoints) per analitzar el flux d'execució.
Gestor de Projectes: Ajuda a organitzar els diferents arxius i recursos que formen part d'un projecte de programari. Això inclou arxius de codi, imatges, biblioteques, entre altres.

Integració amb Sistemes de Control de Versions: Permet als desenvolupadors fer seguiment dels canvis en el codi font al llarg del temps, col·laborar amb altres desenvolupadors, i gestionar diferents versions del seu projecte.
Terminal o Consola Integrada: Ofereix una interfície per executar comandes directament des de l'IDE, el que pot ser útil per compilar i executar aplicacions, gestionar sistemes de control de versions, entre altres tasques.
Suport per a Múltiples Llenguatges de Programació: Molts IDEs proporcionen suport per a diferents llenguatges de programació, oferint ressaltat de sintaxi, autocompletat, i altres funcionalitats específiques per a cada llenguatge.
Eines de Refactorització: Proporcionen maneres automatitzades per canviar l'estructura del codi sense canviar el seu comportament, amb l'objectiu de fer-lo més net, eficient, i fàcil de mantenir.
15

Visualització de Codi: Ofereix representacions gràfiques de l'estructura del codi, com arbre de dependències, diagrames de classes, entre altres, per ajudar els desenvolupadors a comprendre millor el seu codi.
Integració amb Eines Externes: Permet integrar i utilitzar eines de desenvolupament externes directament des de l'IDE, com bases de dades, servidors web, contenidors, entre altres.
Assistència en la Codificació: Proporciona suggeriments, correccions automàtiques, i altres ajudes per millorar la qualitat del codi i la productivitat del desenvolupador.
Automatització de Tasques: Ofereix eines per automatitzar tasques repetitives com la compilació, execució de tests, desplegament d'aplicacions, entre altres.
16

3. Ús Bàsic d'un Entorn de
Desenvolupament Integrat (IDE)
17

Ús Bàsic d'un Entorn de Desenvolupament Integrat (IDE)
Un Entorn de Desenvolupament Integrat (IDE) és una aplicació que proporciona eines per ajudar els programadors a desenvolupar programari de manera més eficient. A continuació es descriuen algunes de les funcionalitats bàsiques que es poden trobar en la majoria dels IDEs.
18

Creació i Gestió de Projectes
Creació de Nou Projecte: Els IDEs permeten crear nous projectes a partir de plantilles, facilitant la configuració inicial.
Importació de Projectes Existents: Si ja tens un projecte creat, pots importar-lo al teu IDE per començar a treballar amb ell.
Navegació per l'Estructura del Projecte: Un IDE ofereix una vista estructurada dels arxius i carpetes del teu projecte, permetent-te navegar fàcilment entre ells.
19

Edició de Codi
Editor de Text: Pots escriure i editar el codi font directament a l'IDE.
Ressaltat de Sintaxi: L'IDE ressalta la sintaxi del teu codi, facilitant la lectura i comprensió del codi.
Autocompletament: Aquesta funcionalitat et suggerirà automàticament fragments de codi o noms de variables mentre escrius.
Refactorització: L'IDE et pot ajudar a reestructurar el codi sense canviar el seu comportament, com per exemple renombrar variables o moure codi a una funció.
20

Compilació i Execució
Compilació del Codi: Pots compilar el teu codi directament des de l'IDE. Si hi ha errors, l'IDE els mostrarà i et permetrà anar directament a la línia de codi que els ha causat.
Execució d'Aplicacions: Després de compilar, pots executar la teva aplicació directament des de l'IDE.
Depuració: L'IDE proporciona eines de depuració que et permeten executar el teu codi pas a pas, inspeccionar variables i avaluar expressions en temps d'execució.
21

Gestió de Versions
Integració amb Sistemes de Control de Versions: Els IDEs sovint suporten la integració amb sistemes de control de versions com Git, permetent-te realitzar commits, pushes, pulls, i altres operacions directament des de l'IDE.
22

Ajudes i Documentació
Suggeriments i Avisos: Mentre escrius codi, l'IDE pot oferir suggeriments, avisos i advertències per millorar la qualitat del codi o corregir errors potencials.
Accés a la Documentació: Pots accedir a la documentació de les llibreries i frameworks que estàs utilitzant directament des de l'IDE.
23

4. Personalització de l'Entorn de Desenvolupament
24

Personalització de l'Entorn de Desenvolupament
La personalització de l'entorn de desenvolupament (IDE) és una part crucial per optimitzar la productivitat i la comoditat durant la programació. Cada desenvolupador té les seves preferències personals, i els IDEs moderns ofereixen una àmplia varietat d'opcions de personalització per satisfer aquestes necessitats.
25

Temes i Aparença
Temes de Colors: Pots canviar els colors de l'editor, les finestres i altres elements de l'IDE. Això inclou tant el mode clar com el mode fosc.
Fonts i Mida de Text: Ajusta la font i la mida del text de l'editor per adaptar-ho a les teves preferències visuals.
Icones i Bars d'Eines: Configura quines icones i bars d'eines vols que es mostrin, i on vols que estiguin situades.
26

Configuració de l'Editor
Estils de Codificació: Estableix les regles d'estil de codificació, com l'indentació, l'ús de tabulacions o espais, i altres convencions de codi.
Inspeccions de Codi: Personalitza els nivells d'advertència o error per diferents tipus d'inspeccions de codi.
Plugins i Extensions: Afegeix funcionalitats addicionals a l'IDE mitjançant l'instal·lació de plugins o extensions. Això pot incloure suport per a altres llenguatges de programació, eines de productivitat, temes visuals, entre d'altres.
27

Configuració de la Navegació
Dreceres de Teclat: Personalitza o aprèn les dreceres de teclat per accedir ràpidament a funcionalitats comuns de l'IDE.
Vistes i Panells: Configura com vols que es mostrin les diferents vistes i panells de l'IDE, com l'explorador de projectes, la consola, el depurador, etc.
28

Configuració del Compilador i l'Executor
Configuració de Compilació: Estableix les opcions del compilador, com les banderes de compilació, les versions del llenguatge, etc.
Configuració d'Execució: Configura els paràmetres d'execució per a les teves aplicacions, com els arguments de la línia de comandes, les variables d'entorn, etc.
29

Suport per a Control de Versions
Integració amb Repositoris: Configura l'accés als teus repositoris de control de versions, com Git, SVN, etc.
Opcions de Commit i Push: Personalitza les opcions disponibles quan fas commits o pushes, com la inclusió automàtica de fitxers, la signatura de commits, etc.
30

5. Edició de Programes
31

Edició de Programes
L’edició de programes és una part fonamental del procés de desenvolupament de software. Els IDEs moderns proporcionen una sèrie d’eines i funcionalitats per fer aquesta tasca més eficient i intuïtiva. 
32

Editor de Codi
Sintaxi Resaltada: Els IDEs ressalten diferents parts del codi (com ara variables, funcions, paraules clau) amb colors diferents, facilitant la lectura i comprensió del codi.
Autocompletament de Codi: Aquesta funció suggereix automàticament noms de variables, funcions i altres fragments de codi mentre l’usuari està escrivint, accelerant el procés d’escriptura del codi.
Snippet de Codi: Permet als desenvolupadors inserir blocs de codi predefinits ràpidament.
33

Navegació i Cerca
Cerca Ràpida: Permet buscar ràpidament dins del codi font, amb suport per a expressions regulars i cerques sensibles a majúscules.
Navegació entre Arxius i Funcions: Funcionalitats per saltar ràpidament a definicions de funcions, classes, o a altres arxius del projecte.
Vista d'Estructura: Mostra una vista estructurada del codi font actual, facilitant la navegació entre diferents parts del codi.
34

Refactorització i Format de Codi
Refactorització de Codi: Eines per reorganitzar el codi sense canviar-ne el funcionament, inclòs el canvi de noms de variables, la extracció de codi a funcions, etc.
Format de Codi: Funcionalitat per reformatejar automàticament el codi segons un conjunt d’estils i convencions predefinides.
35

Integració amb Control de Versions
Històric de Canvis: Permet visualitzar i revertir canvis anteriors en el codi font.
Diferències de Codi: Mostra les diferències entre diferents versions del codi o entre diferents branques en un sistema de control de versions.
36

Suport per a Múltiples Llenguatges i Frameworks
Suport per a Diversos Llenguatges de Programació: Els IDEs sovint suporten múltiples llenguatges de programació, proporcionant ressaltat de sintaxi, autocompletament i altres funcionalitats per a cadascun.
Integració amb Frameworks: Suport específic per a diferents frameworks, proporcionant plantilles, eines i assistents per facilitar el desenvolupament.
37

Depuració i Anàlisi de Codi
Eines de Depuració: Permeten executar el programa pas a pas, inspeccionar variables i avaluar expressions en temps d’execució.
Anàlisi de Codi: Identifica possibles errors, punts dèbils o àrees de millora en el codi font.
38

6. Generació d'executables
en diferents entorns
39

Generació d'executables en diferents entorns
La generació d'executables és un pas crític en el desenvolupament de software, ja que converteix el codi font escrit pels desenvolupadors en un programa que pot ser executat en una màquina. Aquest procés pot variar depenent de l'entorn i el llenguatge de programació utilitzat. Els IDEs moderns ofereixen eines per facilitar aquest procés en diferents entorns. 
40

Compilació
Selecció del Compilador: Depenent del llenguatge de programació, hauràs de seleccionar el compilador adequat. Per exemple, GCC per C/C++, javac per Java, etc.
Configuració del Compilador: Estableix les opcions del compilador, com les banderes de compilació, les versions del llenguatge, les biblioteques d'enllaç, entre d'altres.
Compilació Creuada: Per generar executables per a diferents plataformes (Windows, Linux, MacOS) des d'una única plataforma de desenvolupament.
41

Enllaç
Enllaçador: Després de la compilació, l'enllaçador combina els objectes compilats i les biblioteques necessàries per crear l'executable.
Biblioteques Estàtiques i Dinàmiques: Configura si vols utilitzar biblioteques estàtiques (incloses a l'executable) o dinàmiques (carregades en temps d'execució).
42

Generació d'Arxius Executables
Arxius Executables: L'IDE generarà l'arxiu executable (.exe en Windows, .out en Linux, etc.) que pot ser executat en la màquina objectiu.
Paquets d'Instal·lació: Per a aplicacions més complexes, pots generar paquets d'instal·lació que inclouran l'executable juntament amb qualsevol dependència i arxiu de configuració necessari.
43

Proves en Diferents Entorns
Màquines Virtuals o Contenidors: Utilitza màquines virtuals o contenidors (com Docker) per provar l'executable en diferents entorns i assegurar-te que funciona correctament.
Emuladors: En el cas de desenvolupament per a dispositius mòbils o altres plataformes especialitzades, utilitza emuladors per provar l'aplicació.
44

Automatització de la Generació d'Executables
Eines de Construcció: Utilitza eines com Make, Maven, Gradle, etc., per automatitzar el procés de compilació, enllaç i generació d'executables.
Integració Contínua (CI): Configura un sistema de CI per a generar automàticament executables cada cop que es faci un canvi al codi font.
45

Distribució
Plataformes de Distribució: Utilitza plataformes específiques per a distribuir l'aplicació, com les botigues d'aplicacions per a mòbils, repositoris de programari per a Linux, o llocs web per a aplicacions de PC.
46

7. Eines de gestió i automatització 
de projectes de Software
47

Què són?
Maven i Gradle són eines de gestió de construcció i dependències per a projectes de programació. Principalment s'utilitzen en projectes Java, però també suporten altres llenguatges de programació.
Aquestes eines ajuden els desenvolupadors a automatitzar processos repetitius relacionats amb la construcció de programari, com ara compilar codi font, empaquetar codi en fitxers executables o llibreries, gestionar biblioteques externes i moltes altres tasques. Penseu en elles com a "assistents" que fan tasques tècniques per al desenvolupador.
En termes senzills, aquestes eines ajuden els desenvolupadors a "construir" el seu programari de manera més eficient, gestionant les parts complexes i repetitives. Això permet als desenvolupadors centrar-se més en escriure codi i menys en tasques tècniques associades.
48

És una eina que ajuda a organitzar, construir i gestionar dependències en projectes de programari.
Per a què es fa servir?: Simplifica molts processos, com ara descarregar biblioteques necessàries automàticament o seguir una estructura estàndard de projecte que fa més fàcil treballar amb equips grans.
Per què va sorgir?: Va ser creat per proporcionar una manera més estructurada i centralitzada de gestionar projectes de programari, en comparació amb altres eines que existien en aquell moment.
Què és Maven?
49

Què és Gradle?
Una eina més moderna que Maven, que també ajuda en la construcció i gestió de projectes de programari.
Per a què es fa servir?: Ofereix més flexibilitat que Maven, permetent als desenvolupadors definir com volen construir els seus projectes de manera més detallada. També pot ser més ràpid en algunes situacions gràcies a la seva capacitat de construcció incremental.
Per què va sorgir?: Va ser dissenyat per superar algunes de les limitacions de Maven i altres eines, oferint una eina més potent i flexible.
50

Maven vs. Gradle
Maven:
Basat en XML: Usa pom.xml per definir el projecte i les seves dependències.
Convenció sobre Configuració: Té una estructura i un cicle de vida estàndard, el que pot simplificar la configuració.
Maduresa i Estabilitat: Ha estat utilitzat durant molt de temps i té una gran base d'usuaris.
Menys Flexibilitat: Degut a la seva naturalesa basada en convencions, pot ser menys flexible en escenaris complexes.
Gradle:
Basat en Groovy/Kotlin: Originalment utilitzava scripts Groovy, però ara també suporta Kotlin amb Kotlin DSL.
Configuració sobre Convenció: Tot i que té convencions, és més configurable que Maven.
Més Ràpid: Gràcies a la seva capacitat d'execució incremental i la gestió de dependències més eficient.
Més Flexibilitat: Pots escriure scripts personalitzats i funcions dins dels teus scripts de construcció.
51

Raons per utilitzar Maven:
Simplicitat: Si estàs començant o el teu projecte no té requisits de construcció complicats, la convenció de Maven pot ser suficient.
Maduresa: Maven ha estat al voltant de molts anys, i moltes empreses el fan servir per a la seva estabilitat i maduresa.
Gran Ecosistema: Hi ha molts plugins disponibles i una gran comunitat darrere.
Per a què utilitzar Maven o Gradle?
Raons per utilitzar Gradle:
Flexibilitat: Ideal per a projectes amb requisits de construcció personalitzats o complicats.
Rendiment: Construcció més ràpida, especialment en projectes grans.
Diversitat de llenguatges: A part de Java, suporta nombrosos llenguatges com Kotlin, Groovy, Scala, etc.
Kotlin DSL: Si estàs treballant amb Kotlin, aquesta pot ser una raó natural per escollir Gradle.
52

[Torna a la presentació de l'assignatura](README.md)