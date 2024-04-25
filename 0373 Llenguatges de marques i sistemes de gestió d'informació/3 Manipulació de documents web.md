# 3. Manipulació de Documents Web

## 1. Introducció als Llenguatges de Script de Client

### Definició i Ús

Els llenguatges de script de client són aquells que s'executen en el navegador de l'usuari, en comptes del servidor. Aquests llenguatges permeten a les pàgines web ser més interactives i dinàmiques, oferint una experiència d'usuari millorada.

1. **Interacció amb l'Usuari**: Mitjançant scripts de client, és possible capturar i respondre a accions de l'usuari com clics, tecles, moviments del ratolí, etc. Això permet crear una interfície d'usuari interactiva i responsiva.

2. **Control del Navegador**: Aquests llenguatges permeten manipular elements del navegador, com la barra d'adreces, la història de navegació, o fins i tot controlar el tamany i la posició de les finestres.

3. **Comunicació Asíncrona**: Una de les capacitats més potents és la possibilitat de realitzar peticions al servidor sense necessitat de recarregar tota la pàgina (conegut com AJAX). Això enriqueix l'experiència de l'usuari permetent actualitzacions de la pàgina "al vol".

4. **Validació de Formularis i Animacions**: Els llenguatges de script de client també són utilitzats per validar dades en formularis abans de ser enviats al servidor, i per crear animacions i efectes visuals en les pàgines web.

### Exemples

- **JavaScript**: És el llenguatge de script de client més utilitzat. És pràcticament omnipresent en el desenvolupament web modern, suportat per tots els navegadors principals. JavaScript és versàtil i pot ser utilitzat tant per a tasques senzilles com per a aplicacions web complexes.

- **VBScript**: Menys comú en l'actualitat, VBScript (Visual Basic Scripting Edition) va ser utilitzat principalment en entorns vinculats a Microsoft, com a part de pàgines web ASP o en aplicacions d'Internet Explorer. Encara que no és tan popular com JavaScript, serveix com a exemple d'un altre llenguatge de script de client.

## 2. Característiques dels llenguatges de script de client

Els llenguatges de script de client, com JavaScript, tenen diverses característiques distintives que els fan especialment adequats per al desenvolupament web. Aquestes característiques permeten als desenvolupadors crear pàgines web dinàmiques i interactives.

### Interpretació vs. Compilació

- **Interpretats**: A diferència dels llenguatges compilats, els llenguatges de script de client són interpretats, és a dir, el codi s'executa línia per línia pel navegador. Això significa que el codi és llegit i executat gairebé simultàniament, permetent una ràpida iteració i desenvolupament.
- **Avantatges i desavantatges**: La interpretació facilita la depuració i el testejament, ja que els canvis poden ser ràpidament revisats. No obstant això, pot ser menys eficient en termes de velocitat d'execució en comparació amb llenguatges compilats.

### Asincronia

- **Execució asíncrona**: Els llenguatges de script de client sovint permeten l'execució asíncrona, és a dir, la capacitat d'executar codi sense bloquejar o esperar que una tasca finalitzi. Això és fonamental en aplicacions web modernes on diverses operacions, com les peticions a un servidor, poden tardar temps variable a completar-se.

- **Exemple**: AJAX (Asynchronous JavaScript and XML) és una tècnica que utilitza aquesta propietat per permetre que les pàgines web sol·licitin dades del servidor i actualitzin la interfície d'usuari sense necessitat de recarregar la pàgina completa.

### Manipulació del DOM

- **Què és el DOM?**: El Document Object Model (DOM) és una representació orientada a objectes del document web. Permet als llenguatges de script de client interactuar i modificar el contingut, l'estructura i l'estil de les pàgines web.

- **Interacció amb el DOM**: A través del DOM, els scripts poden afegir, eliminar o modificar elements HTML, canviar estils CSS i respondre a esdeveniments de l'usuari. Aquesta capacitat transforma documents HTML estàtics en aplicacions web interactives.

- **Exemples d'Ús**: Amb la manipulació del DOM, es poden crear tasques com a actualitzacions dinàmiques de contingut (per exemple, carregar comentaris en un blog sense recarregar la pàgina), controls d'animació, formularis interactius, i molt més.

## 3. Sintaxi Bàsica en Llenguatges de Script de Client

Aquesta secció abordarà els elements fonamentals: variables, tipus de dades, estructures de control i funcions.

### Variables i Tipus de Dades

#### Declaració de Variables

En JavaScript, les variables es poden declarar utilitzant `let`, `const`, o `var` (menys recomanat per la seva àmplia visibilitat). `let` permet declarar variables amb un abast limitat al bloc, declaració o expressió on es fan servir, mentre que `const` es fa servir per a constants, les quals no poden ser reassignades.

```javascript
let nom = "Joan";
const PI = 3.14;
```

#### Tipus de Dades

JavaScript és un llenguatge de tipus dinàmic, però suporta diversos tipus de dades:

- **Nombres**: Inclou tant enters com decimals.
- **Cadenes de Caràcters**: Text envoltat per cometes simples, dobles o backticks.
- **Booleans**: Valors veritables o falsos, útils per a condicions.
- **Objectes**: Col·leccions de propietats, clau-valor.
- **Arrays**: Llistes ordenades de valors.
- **`undefined` i `null`**: Representen un valor 'sense valor' o 'desconegut'.

```javascript
let edat = 30;
let nomUsuari = "Joan";
let esMajorEdat = true;
let usuari = { nom: "Joan", edat: 30 };
let aficions = ["ciclisme", "lectura"];
```

### Estructures de Control

#### If-Else

Permet executar codi basat en condicions.

```javascript
if (edat > 18) {
  console.log("Major d'edat");
} else {
  console.log("Menor d'edat");
}
```

#### Bucles For i While

Utilitzats per a executar un bloc de codi repetidament.

`for`: Comú per a iterar sobre arrays o realitzar un nombre fix de repeticions.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

`while`: Executa un bloc de codi mentre una condició sigui certa.

```javascript
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

#### Switch

Alternativa a múltiples `if-else` per a comprovar múltiples condicions.

```javascript
switch (nomUsuari) {
  case "Joan":
    console.log("Hola Joan");
    break;
  case "Maria":
    console.log("Hola Maria");
    break;
  default:
    console.log("Usuari no reconegut");
}
```

### Funcions

#### Creació i Ús

Les funcions són blocs de codi reutilitzables. Es poden crear utilitzant la paraula clau `function` o com a funcions de fletxa (arrow functions).

```javascript
function suma(a, b) {
  return a + b;
}

let resta = (a, b) => a - b;
```

#### Àmbit de Variables (Scope)

Les variables dins una funció tenen un àmbit local a aquesta funció. No són accessibles fora de la mateixa.

```javascript
function demo() {
  let local = "Només visible dins de demo";
}
console.log(local); // Error: local no està definida
```

#### Closures

Una funció que recorda l'entorn en què va ser creada. Són útils per a encapsular dades i proporcionar una espècie de variables privades.

```javascript
function crearContador() {
  let comptador = 0;
  return () => ++comptador;
}

let meuContador = crearContador();
console.log(meuContador()); // 1
console.log(meuContador()); // 2
```

Aquesta visió general de la sintaxi bàsica dels llenguatges de script de client, com JavaScript, ofereix una comprensió fonamental dels blocs de construcció necessaris per a crear aplicacions web dinàmiques i interactives. Amb una bona comprensió d'aquests conceptes, els desenvolupadors poden començar a explorar funcionalitats més complexes i construir solucions sofisticades en el món del desenvolupament web.

## 4. Estàndards dels Llenguatges de Script de Client

Els llenguatges de script de client, especialment JavaScript, operen dins d'un marc d'estàndards establerts per garantir la seva compatibilitat i funcionament en diferents entorns, com els navegadors web. Aquesta secció explora aquests estàndards, centrant-se en ECMAScript i la compatibilitat entre navegadors.

### ECMAScript: L'Estàndard de JavaScript

#### Què és ECMAScript?

ECMAScript és un estàndard de llenguatge de script creat per l'organització Ecma International. JavaScript, el llenguatge de script de client més utilitzat, segueix l'estàndard ECMAScript. Això assegura que sigui consistent i funcioni de manera previsible en diferents entorns de programació.

#### Evolució i Versions

ECMAScript va ser presentat per primera vegada el 1997, i des de llavors ha passat per múltiples versions. Cada nova edició (com ECMAScript 2015, també coneguda com ES6) introdueix noves funcionalitats i millores. ES6, per exemple, va introduir classes, mòduls, promeses, funcions de fletxa, i moltes altres característiques que modernitzen el llenguatge.

#### Impacte en el Desenvolupament Web

Amb cada nova versió d'ECMAScript, els desenvolupadors disposen de més eines i funcions per escriure codi més eficient, legible i mantenible. L'estàndard ajuda a unificar el comportament del llenguatge en diferents navegadors i plataformes.

### Compatibilitat i Diferències entre Navegadors

#### Desafiaments de la Compatibilitat

Malgrat els estàndards establerts per ECMAScript, diferents navegadors poden interpretar o implementar el JavaScript de maneres lleugerament diferents. Això pot conduir a problemes de compatibilitat, on un codi pot funcionar en un navegador però no en un altre.

#### Detecció de Característiques vs Detecció de Navegadors

Una pràctica comuna per abordar aquestes diferències és la detecció de característiques. En comptes de codificar per a un navegador específic, els desenvolupadors comproven si una característica necessària és suportada pel navegador de l'usuari. Això es prefereix a la detecció de navegadors, que identifica el navegador i canvia el comportament del codi en conseqüència.

#### Polyfills i Transpilers

Per a utilitzar característiques modernes de JavaScript en navegadors antics, es fan servir polyfills i transpilers. Un polyfill és un fragment de codi que afegeix suport per a una característica que el navegador no suporta nadiuament. Un transpiler, com Babel, transforma codi modern de JavaScript en una versió compatible amb navegadors més antics.

#### Frameworks i Biblioteques

Sovint, els desenvolupadors fan servir frameworks i biblioteques com jQuery, React, o Angular, que abstrauen molts dels problemes de compatibilitat. Aquests eines gestionen les diferències entre navegadors, permetent als desenvolupadors concentrar-se en la lògica de l'aplicació.

## 5. Selecció i Accés a Elements

La capacitat de seleccionar i accedir a elements del Document Object Model (DOM) és fonamental en el desenvolupament web, permetent als desenvolupadors manipular la pàgina web de manera dinàmica. Aquesta secció explora com treballar amb el DOM i utilitzar selectors CSS per interactuar amb elements HTML.

### Document Object Model (DOM)

#### Què és el DOM?

El DOM és una representació en arbre de la pàgina web. Cada element HTML, atribut, i text són nodes en aquest arbre, permetent als scripts modificar visualment la pàgina. Quan una pàgina web es carrega, el navegador crea el DOM basat en el HTML.

#### Accedir i Modificar el DOM

JavaScript s'utilitza per interactuar amb el DOM. Pots accedir a elements, modificar-los, afegir o eliminar-los, i canviar els seus estils. Això es fa generalment per millorar la interactivitat de la pàgina, com per exemple actualitzar dinàmicament el contingut, validar formularis, o crear animacions.

#### Mètodes per Accedir a Elements

`getElementById`: Retorna l'element amb l'ID especificat.

```javascript
let element = document.getElementById("meuId");
```

`getElementsByClassName`: Retorna una col·lecció d'elements amb la classe especificada.

```javascript
let elements = document.getElementsByClassName("mevaClasse");
```

`getElementsByTagName`: Retorna elements segons la seva etiqueta.

```javascript
let paragrafs = document.getElementsByTagName("p");
```

#### Modificació d'Elements

Un cop tens accés a un element, pots modificar el seu contingut, atributs i estils.

- Modificar contingut amb `innerHTML` o `textContent`.
- Canviar atributs com `src` en imatges, `href` en enllaços, etc.
- Modificar estils CSS directament.

### Selectors CSS

#### Ús de Selectors CSS en JavaScript

Els selectors CSS són una manera potent de trobar elements en el DOM. En lloc d'utilitzar mètodes com `getElementById`, pots utilitzar `querySelector` i `querySelectorAll`, que permeten utilitzar qualsevol selector CSS.

#### querySelector i querySelectorAll

`querySelector`: Retorna el primer element que coincideix amb el selector CSS.

```javascript
let primerBotó = document.querySelector("button");
```

`querySelectorAll`: Retorna tots els elements que coincideixen amb el selector CSS en forma de NodeList.

```javascript
let totsElsBotons = document.querySelectorAll("button");
```

#### Exemples de Selectors CSS

- Selectors per id: `#meuId`.
- Selectors per classe: `.mevaClasse`.
- Selectors per etiqueta: `p`, `div`.
- Selectors combinats i complexes: `div.mevaClasse`, `#meuId > p`.

## 6. Creació, Modificació i Eliminació d'Elements en el DOM

La manipulació del Document Object Model (DOM) és una part integral del desenvolupament web. Els llenguatges de script de client, especialment JavaScript, proporcionen diverses funcions per crear, modificar i eliminar elements HTML. Aquesta capacitat permet als desenvolupadors construir interfícies d'usuari dinàmiques i interactives.

### Creació d'Elements

#### Document.createElement

Per crear un nou element en el DOM, es fa servir `document.createElement()`. Aquest mètode crea un node element que encara no està lligat al DOM actual.

```javascript
let nouDiv = document.createElement("div");
```

#### Afegir Contingut i Atributs

Després de crear un element, pots afegir-li contingut i atributs. Per exemple, pots utilitzar `textContent` o `innerHTML` per a afegir contingut de text o HTML, i `setAttribute` per a afegir atributs com `class`, `id`, `style`, etc.

```javascript
nouDiv.textContent = "Hola Món!";
nouDiv.setAttribute("class", "meva-classe");
```

#### Inserir l'Element en el DOM

Un cop creat i configurat l'element, necessites inserir-lo en el DOM. Això es fa utilitzant mètodes com `appendChild()` o `insertBefore()`.

```javascript
document.body.appendChild(nouDiv);
```

### Modificació d'Elements

#### Canviar Contingut i Atributs

La modificació d'un element existent és similar a afegir contingut i atributs a un element nou. Pots utilitzar `textContent` o `innerHTML` per modificar el contingut, i `setAttribute` per canviar els seus atributs.

```javascript
let element = document.getElementById("elementId");
element.textContent = "Text actualitzat";
element.setAttribute("style", "color: blue;");
```

#### Modificar Estils CSS

Per canviar els estils d'un element, pots accedir a la propietat `style` de l'element i modificar els seus valors.

```javascript
element.style.backgroundColor = "yellow";
```

### Eliminació d'Elements

#### Eliminar un Element del DOM

Per eliminar un element, primer has de trobar l'element pare i després utilitzar el mètode `removeChild()`.

```javascript
let pare = document.getElementById("pareId");
let fill = document.getElementById("fillId");
pare.removeChild(fill);
```

#### Mètode `remove()`

En versions més recents de JavaScript, pots utilitzar directament el mètode `remove()` en l'element que vols eliminar. Aquest mètode elimina l'element directament sense necessitat d'accedir al seu element pare.

```javascript
let elementAEliminar = document.getElementById("elementAEliminar");
elementAEliminar.remove();
```

## 7. Manipulació d'Estils

La manipulació d'estils és una part essencial del desenvolupament web, permetent als desenvolupadors canviar l'aparença de les pàgines web de manera dinàmica. Això inclou modificar estils en línia i CSS, així com crear animacions i transicions utilitzant JavaScript.

### Estils en línia vs CSS

#### Estils en línia

Els estils en línia s'apliquen directament a elements individuals utilitzant l'atribut `style` en HTML. Amb JavaScript, pots modificar aquests estils accedint a la propietat `style` de l'element.

```javascript
let element = document.getElementById("meuElement");
element.style.color = "blue";
element.style.fontSize = "14px";
```

#### CSS via JavaScript

Més enllà dels estils en línia, JavaScript també pot modificar fulls d'estil CSS. Això es pot fer manipulant les classes CSS de l'element amb `classList`. Per exemple, pots afegir, eliminar o commutar classes, el que permet canviar l'estil de l'element d'acord amb les definicions en els fulls d'estil.

```javascript
element.classList.add("novaClasse");
element.classList.remove("antigaClasse");
element.classList.toggle("alternarClasse");
```

#### Avantatges de l'Ús de Classes CSS

Utilitzar classes CSS en lloc d'estils en línia fa que el codi sigui més net i mantenible. També separa l'estil del contingut, que és una bona pràctica en el disseny web. A més, l'ús de classes CSS facilita l'aplicació d'estils consistents a múltiples elements.

### Animacions i Transicions

#### Transicions CSS

JavaScript pot ser utilitzat per disparar transicions CSS. Les transicions permeten canviar propietats d'estils amb una durada i temporització específiques. Per exemple, pots canviar la mida, el color, o la posició d'un element de manera suau durant un temps definit.

```css
.transicio {
  transition: color 2s, transform 2s;
}
```

```javascript
element.classList.add("transicio");
element.style.color = "red"; // La transició a color vermell serà suau.
```

#### Animacions CSS

A diferència de les transicions, les animacions CSS poden ser més complexes i permeten més control sobre els fotogrames clau (keyframes) i la seqüència de l'animació. JavaScript pot ser utilitzat per iniciar, pausar o detenir aquestes animacions.

```css
@keyframes animacioExemple {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(1.5);
  }
}
.animacio {
  animation: animacioExemple 3s infinite alternate;
}
```

```javascript
element.classList.add("animacio");
```

#### JavaScript per Animacions Complexes

Per a animacions més complexes o que requereixen més control, pots utilitzar JavaScript per animar propietats directament. Això es fa generalment utilitzant `requestAnimationFrame`, que proporciona un mitjà per crear animacions suaus i eficients.

```javascript
function animar() {
    let valor = /* Calcula el valor de l'animació */;
    element.style.transform = `translateX(${valor}px)`;
    requestAnimationFrame(animar);
}
requestAnimationFrame(animar);
```

La manipulació d'estils i la creació d'animacions són eines poderoses en mans dels desenvolupadors web. Permeten no només millorar l'aspecte visual dels llocs web sinó també augmentar la interactivitat i millorar l'experiència d'usuari. Amb la combinació adequada d'HTML, CSS i JavaScript, es poden crear experiències web dinàmiques i atractives.

## 8. Exercicis Pràctics i Exemples

Els exercicis pràctics i els exemples reals són essencials per consolidar els coneixements adquirits en el desenvolupament web. Aquesta secció proporciona exemples d'exercicis i casos d'ús que demostren com aplicar els conceptes de llenguatges de script de client en situacions reals.

### Exercicis de Codificació

Aquests exercicis estan dissenyats per posar a prova i millorar les habilitats en programació amb llenguatges de script de client com JavaScript.

1. **Creació d'un Formulari Dinàmic**:

   - Objectiu: Utilitzar el DOM per crear un formulari amb diversos camps (text, data, selecció, etc.) i un botó per enviar.
   - Desafiament: Afegir validació de dades del costat del client abans d'enviar el formulari.

2. **Galeria d'Imatges Interactiva**:

   - Objectiu: Crear una galeria d'imatges on els usuaris puguin clicar per ampliar les imatges.
   - Desafiament: Afegir funcions per passar a la següent o anterior imatge i tancar la visualització ampliada.

3. **Llista de Tasques (To-Do List)**:
   - Objectiu: Implementar una aplicació de llista de tasques que permeti als usuaris afegir, eliminar i marcar tasques com a completades.
   - Desafiament: Implementar la capacitat de guardar i recuperar les tasques utilitzant `localStorage`.

### Casos d'Ús Reals

Aquests exemples il·lustren com els conceptes de llenguatges de script de client són aplicats en llocs web reals.

1. **Validació de Formularis en un Lloc de Comerç Electrònic**:

   - Descripció: En un lloc web de comerç electrònic, la validació de formularis s'utilitza per verificar la informació de contacte i pagament abans d'enviar les dades al servidor.
   - Implementació: Utilització de JavaScript per validar el format del correu electrònic, la seguretat de la contrasenya i la validesa del número de targeta de crèdit.

2. **Animacions en Llocs Web de Portafolis**:

   - Descripció: En un lloc web de portafolis, les animacions i transicions són utilitzades per millorar la presentació de treballs i projectes.
   - Implementació: JavaScript en combinació amb CSS per crear efectes visuals com fades, desplaçaments suaus i transformacions d'elements.

3. **Interactivitat en Blogs i Llocs de Notícies**:
   - Descripció: Els llocs web de notícies i blogs sovint utilitzen JavaScript per afegir interactivitat, com carregar més articles a mesura que l'usuari es desplaça cap avall (scroll).
   - Implementació: JavaScript per detectar l'scroll de l'usuari i carregar dinàmicament nou contingut sense necessitat de recarregar la pàgina.

Aquests exercicis i casos d'ús ofereixen una visió pràctica de com els conceptes teòrics són aplicats en el desenvolupament web real. La codificació pràctica i l'anàlisi de casos reals són crítics per desenvolupar una comprensió profunda i habilitats efectives en el desenvolupament amb llenguatges de script de client.

[Torna a la presentació de l'assignatura](README.md)
