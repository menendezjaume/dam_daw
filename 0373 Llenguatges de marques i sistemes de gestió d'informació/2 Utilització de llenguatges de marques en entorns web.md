# 2. Utilització de Llenguatges de Marques en Entorns Web

## Llenguatges per a la visualització de informació

En l'era digital actual, la informació es presenta i es consumeix predominantment a través de mitjans electrònics, com ara llocs web, aplicacions mòbils, publicacions digitals, entre d'altres. Per garantir que aquesta informació sigui accessible i comprensible per a l'usuari, s'utilitzen llenguatges de presentació.

### Concepte de llenguatges de presentació

Un llenguatge de presentació és un llenguatge utilitzat per descriure com s'ha de visualitzar o presentar la informació a l'usuari. Aquests llenguatges no determinen quina informació es mostra, sinó com es mostra. CSS (Cascading Style Sheets) és un exemple prevalent d'un llenguatge de presentació utilitzat en el desenvolupament web.

### Necessitat dels llenguatges de presentació

**Separació del contingut i la presentació**: Permet als desenvolupadors i dissenyadors treballar de manera independent i assegura que els canvis en el disseny no afectin el contingut subjacent o la lògica de negoci.

**Reutilització i consistència**: Amb els llenguatges de presentació, els estils i les temàtiques poden ser definits una sola vegada i aplicats a múltiples parts o pàgines, assegurant una aparença i sensació coherents.

**Adaptabilitat**: A través de mètodes com les media queries en CSS, els llenguatges de presentació permeten la creació de dissenys responsius que s'adaptin a diferents mides de pantalla i dispositius.

**Accessibilitat**: Amb els estils adequats, es pot garantir que la informació sigui accessible per a tots els usuaris, inclosos aquells amb discapacitats visuals o altres necessitats especials.

### Exemples de llenguatges de presentació

**CSS**: Com s'ha esmentat anteriorment, CSS és el llenguatge de presentació estàndard per a la web. Controla aspectes com colors, tipografies, espaiat i més.

**XSL**: Extensible Stylesheet Language, utilitzat principalment per transformar i presentar documents XML.

**TeX**: Un llenguatge de marcat ampliament utilitzat en la tipografia d'alta qualitat, especialment en matemàtiques, ciències i enginyeria.

### Diferència entre llenguatges d'estructura i de presentació

En el món del desenvolupament i disseny web, es fa ús de diversos llenguatges amb finalitats específiques. D'aquests, dues categories predominants són els llenguatges d'estructura i els de presentació. Encara que estan estretament relacionats i sovint es complementen entre si, tenen funcions distintes.

### Llenguatges d'estructura

Definició: Els llenguatges d'estructura es fan servir per descriure l'estructura o l'esquelet d'una pàgina web o document. Defineixen com es disposen i organitzen les dades.

Exemples:

- **HTML (Hypertext Markup Language)**: Utilitzat per estructurar contingut a la web, definint elements com paràgrafs, enllaços, imatges, llistes, etc.
- **XML (Extensible Markup Language)**: Un llenguatge de marcat que defineix un conjunt de regles per codificar documents de manera que tant humans com màquines puguin llegir-les.

Característiques:

- No estan orientats a l'aparença visual.
- Determinen l'ordre i la jerarquia del contingut.
- Es poden comparar amb l'estructura d'un edifici, on es defineixen les parets, les habitacions i la disposició general.

### Llenguatges de presentació

Definició: Els llenguatges de presentació descriuen com s'ha de mostrar o estilitzar el contingut. No afecten l'estructura subjacent, sinó que determinen com es veurà i se sentirà per a l'usuari.

Exemples:

- **CSS (Cascading Style Sheets)**: El llenguatge estàndard per estilitzar pàgines web, controlant aspectes com colors, tipografies, espaiat i més.
- **XSL (Extensible Stylesheet Language)**: Utilitzat per estilitzar i transformar documents XML.

Característiques:

- Centrats en l'aparença visual i l'experiència de l'usuari.
- Permeten la separació del contingut i el disseny, possibilitant dissenys reutilitzables i temes canviants.
- Poden ser comparats amb la decoració d'un edifici, incloent-hi la pintura, el mobiliari i la il·luminació.

### Diferències

Mentre que els llenguatges d'estructura estableixen la base i l'organització d'un document o pàgina web, els llenguatges de presentació determinen com es presenta aquesta estructura a l'usuari final. La capacitat de separar l'estructura del disseny és una pràctica essencial en el desenvolupament web modern, ja que permet una major flexibilitat, mantenibilitat i accessibilitat en el disseny i la distribució de contingut digital.

## Llenguatges d'estructura

### Història i evolució d'HTML

HTML (Hypertext Markup Language) és la pedra angular del web. Es tracta d'un llenguatge de marcat estàndard utilitzat per crear i dissenyar pàgines web. Al llarg dels anys, HTML ha passat per diverses revisions i ha evolucionat considerablement des de la seva concepció.

**1990 - HTML com a concepte**: Tim Berners-Lee, un científic informàtic britànic, va proposar un nou sistema per a la publicació i recuperació automàtica d'informació, que més tard es convertiria en el World Wide Web. Va introduir el concepte d'HTML com a manera d'estructurar documents i enllaçar-los entre si.

**1995 - HTML 2.0**: La primera versió estàndard d'HTML. Aquesta versió formalitzava les etiquetes ja existents i establia la base per al desenvolupament posterior d'HTML.

**1997 - HTML 3.2**: Va introduir moltes funcions noves, com ara taules, scripts i més etiquetes de format, tot expandint considerablement les capacitats del llenguatge.

**1999 - HTML 4.01**: Aquesta versió es va concentrar en la separació entre estructura i presentació, empentant el desenvolupament de CSS com a llenguatge de presentació independent. HTML 4.01 va ser un pas important cap a un web més estandaritzat i accessible.

**2000 - XHTML 1.0**: XHTML va ser una reformulació d'HTML com a aplicació de XML. Va requerir un codi més net i ben formatat, amb l'esperança d'assegurar una major compatibilitat i interoperabilitat.

**2008 - 2014 - HTML5**: Desenvolupat per la WHATWG i més tard per la W3C, HTML5 va ser una resposta a la necessitat d'un llenguatge de marcat més modern que pogués manejar el contingut multimèdia modern i ser més semàntic i accessible. Va introduir etiquetes com `<video>`, `<audio>`, `<canvas>` i molts altres elements que permeten la creació de pàgines web riques sense la necessitat de plugins externs com Flash.

### Estat actual i futur

Amb l'arribada d'HTML5 i la seva adopció generalitzada, el desenvolupament principal d'HTML s'ha estabilitzat. Tot i això, les especificacions continuen evolucionant amb l'afegiment de funcions més fines i optimitzacions basades en les necessitats emergents del web.

La comunitat de desenvolupadors i les organitzacions estàndard continuen treballant conjuntament per millorar l'accessibilitat, la interoperabilitat i la seguretat d'HTML.

### Estructura bàsica d’un HTML

Una pàgina web HTML té una estructura específica que la defineix. Aquesta estructura permet als navegadors interpretar correctament el contingut i presentar-lo a l'usuari. Tres components essencials d'aquesta estructura són `<!DOCTYPE>`, `<head>` i `<body>`.

### `<!DOCTYPE>`

La declaració <!DOCTYPE> defineix la versió d'HTML utilitzada en el document. No és una etiqueta HTML per se, sinó una instrucció per al navegador sobre com interpretar el codi de la pàgina.

Aquesta declaració serveix per garantir que el navegador sàpiga quina versió d'HTML s'està utilitzant i pugui renderitzar la pàgina correctament. Això pot ajudar a evitar problemes de compatibilitat.

Exemple:

Per a HTML5, la declaració seria:

```html
<!DOCTYPE html>
```

### `<head>`

L'element <head> conté metadades sobre el document, és a dir, informació sobre la pàgina que no es mostra directament a l'usuari.

Components típics:

- `<meta charset="UTF-8">`: Defineix l'encoding de caràcters utilitzat.
- `<title>`: Estableix el títol de la pàgina, que apareix a la pestanya del navegador.
- `<link>`: Utilitzat principalment per enllaçar fulls d'estil externs, com ara CSS.
- `<script>`: Pot enllaçar o contindre codi JavaScript.
- `<meta name="description" content="Descripció del lloc web">`: Proporciona una descripció breu de la pàgina per als motors de cerca.

Exemple:

```html
<head>
  <meta charset="UTF-8" />
  <title>Títol de la pàgina</title>
  <link rel="stylesheet" href="estils.css" />
</head>
```

### `<body>`

L'element `<body>` conté el contingut visible de la pàgina web. Tot el que es veu en una pàgina web (textos, imatges, enllaços, etc.) està dins de l'etiqueta <body>.

L'element `<body>`pot contenir una gran varietat d'elements, com `<h1>`, `<p>`, `<a>`, `<img>`, `<div>`, entre molts altres.

Exemple:

```html
<body>
  <h1>Benvinguts al meu lloc web</h1>
  <p>Aquest és un paràgraf introductori.</p>
  <a href="pagina2.html">Enllaç a una altra pàgina</a>
</body>
```

### Elements i atributs comuns en HTML

Els documents HTML estan formats per elements, que a la seva vegada poden tenir atributs. Mentre que els elements defineixen l'estructura i el contingut del document, els atributs proporcionen informació addicional sobre aquests elements.

#### Elements comuns

`<h1>`, `<h2>`, ... `<h6>`: Són les etiquetes d'encapçalament, amb `<h1>` sent l'encapçalament de més alt nivell i `<h6>` el de més baix.

```html
<h1>Títol Principal</h1>
<h2>Subtítol</h2>
```

`<p>`: Representa un paràgraf de text.

```html
<p>Aquest és un paràgraf d'exemple.</p>
```

`<img>`: Utilitzada per inserir imatges.

```html
<img src="imatge.jpg" alt="Descripció de la imatge" />
```

`<a>`: Etiqueta d'enllaç. Utilitzada per enllaçar a altres pàgines o recursos.

```html
<a href="https://exemple.com">Visita aquest lloc</a>
```

- Enllaços a IDs dins de la mateixa pàgina:

  Pots fer referència a qualsevol element de la pàgina que tingui un atribut id assignat utilitzant el prefix # seguit de l'ID de l'element al qual vols enllaçar.

  ```html
  <!-- Definició d'un lloc d'ancoratge amb l'ID "seccio1" -->
  <h2 id="seccio1">Títol de la Secció 1</h2>
  <p>Contingut de la Secció 1...</p>
  <!-- Més avall o a d'altres parts de la pàgina -->
  <a href="#seccio1">Torna a la Secció 1</a>
  ```

`<ul>` i `<li>`: Representen llistes no ordenades i els seus elements, respectivament.

```html
<ul>
  <li>Element 1</li>
  <li>Element 2</li>
</ul>
```

`<ol>` i `<li>`: Representen llistes ordenades i els seus elements.

```html
<ol>
  <li>Primer element</li>
  <li>Segon element</li>
</ol>
```

`<div>`: És un contenidor genèric que sol ser utilitzat amb CSS i JavaScript per agrupar altres elements i aplicar estils o comportaments específics.

`<span>`: Semblant a `<div>`, però es tracta d'un element en línia utilitzat per agrupar o aplicar estils a fragments específics dins d'un text.

#### Atributs comuns

`href`: Utilitzat amb l'element `<a>` per especificar l'URL de l'enllaç.

```html
<a href="https://exemple.com">Visita aquest lloc</a>
```

`src`: Especifica la ruta de la font d'un element, com ara `<img>` o `<script>`.

```html
<img src="imatge.jpg" />
```

`style`: Permet afegir estils CSS directament a un element específic.

```html
<p style="color: blue;">Aquest text és blau.</p>
```

`alt`: Proporciona una descripció textual de les imatges amb l'element `<img>`, útil per a l'accessibilitat.

```html
<img src="imatge.jpg" alt="Descripció de la imatge" />
```

`class` i `id`: Són identificadors utilitzats per referenciar elements específics amb CSS o JavaScript. Mentre que `class` pot ser utilitzat per múltiples elements, `id` ha de ser únic dins d'una pàgina.

```html
<div class="classe-exemple"></div>
<div id="identificador-exemple"></div>
```

#### Formularis en HTML: creació i processament

Els formularis són una eina essencial en el desenvolupament web, permetent la interacció de l'usuari amb el lloc web. Es fan servir per recopilar dades dels usuaris, com ara informació de contacte, preferències, dades d'inici de sessió, entre altres.

##### Creació de formularis

L'element `<form>`: És el contenidor principal de tots els components d'un formulari. Defineix on s'enviaran les dades del formulari quan s'enviïn.

```html
<form action="/ruta-del-processament" method="post">
  <!-- Elements del formulari aquí -->
</form>
```

##### Elements d'entrada comuns

`<fieldset>` i `<legend>`: L'element `<fieldset>` es fa servir per agrupar elements relacionats dins d'un formulari. Acompanyat de l'element `<legend>`, proporciona un títol per a aquest grup.

```html
<fieldset>
  <legend>Informació de contacte</legend>
  <label for="nomUsuari">Nom:</label>
  <input type="text" id="nomUsuari" name="nom" />
  <label for="correuUsuari">Correu electrònic:</label>
  <input type="email" id="correuUsuari" name="email" />
</fieldset>
```

`<input>`: Un element versàtil que pot prendre diferents formes basades en l'atribut type.

```html
<!-- Text: -->
<input type="text" name="nom" />
<!-- Password: -->
<input type="password" name="contrasenya" />
<!-- Email: -->
<input type="email" name="correu" />
<!-- Date: -->
<input type="date" name="data_naixement" />
<!-- Number: -->
<input type="number" name="edat" min="0" />
<!-- Range (slider): -->
<input type="range" name="volum" min="0" max="10" />
<!-- Color picker: -->
<input type="color" name="color_preferit" />
<!-- File upload: -->
<input type="file" name="foto_perfil" />
<!-- Hidden: -->
<input type="hidden" name="usuari_id" value="12345" />
```

`<input type="checkbox">`: Els checkboxes permeten que l'usuari seleccioni múltiples opcions d'un conjunt. A diferència dels botons de ràdio, no són exclusius entre si.

En aquest exemple, un usuari pot marcar ambdues opcions si vol rebre tant notícies com promocions.

```html
<input type="checkbox" id="opc1" name="preferencies" value="noticies" />
<label for="opc1">Vull rebre notícies</label>
<input type="checkbox" id="opc2" name="preferencies" value="promocions" />
<label for="opc2">Vull rebre promocions</label>
```

`<input type="radio">`: Els botons de ràdio permeten que l'usuari seleccioni una única opció d'un conjunt. Si tens diversos botons de ràdio amb el mateix valor per a l'atribut name, s'asseguren que només una opció pugui ser seleccionada alhora.

En aquest exemple, encara que hi hagi dos botons de ràdio, l'usuari només pot seleccionar una de les dues opcions (Home o Dona) gràcies a que comparteixen el mateix nom d'atribut name.

```html
<input type="radio" id="gen1" name="genere" value="home" />
<label for="gen1">Home</label>
<input type="radio" id="gen2" name="genere" value="dona" />
<label for="gen2">Dona</label>
```

`<textarea>`: Una àrea de text multi-línia.

```html
<textarea name="missatge" rows="4" cols="50"></textarea>
```

`<select>` i `<option>`: Una llista desplegable d'opcions.

```html
<select name="pais">
  <option value="es">Espanya</option>
  <option value="fr">França</option>
</select>
```

`<button>`: Un botó que pot ser utilitzat per a l'enviament del formulari o altres interaccions.

```html
<button type="submit">Enviar</button>
```

#### Atributs útils per formularis

`placeholder`: Text d'ajuda mostrat a l'element d'entrada abans que l'usuari introdueixi dades.

`required`: Obliga a l'usuari a omplir un camp específic abans d'enviar el formulari.

`disabled`: Desactiva un element d'entrada, evitant que l'usuari interactuï amb ell.

#### Processament de formularis

Acció i mètode: Els atributs `action` i method de l'element `<form>` determinen on i com s'enviaran les dades del formulari.

- `action`: Especifica l'URL on es processaran les dades del formulari.
- `method`: Determina el mètode HTTP utilitzat per enviar les dades. Els més comuns són `GET` (per enviar dades via `URL`) i `POST` (per enviar dades a través del cos de la petició).

**Llenguatges de programació del costat del servidor**: Una vegada que les dades són enviades, un llenguatge de programació del costat del servidor, com PHP, Python, Ruby o Node.js, es fa càrrec de processar aquestes dades, realitzar operacions com ara inserir-les en una base de dades o enviar un correu electrònic.

## Llenguatges de presentació

### Definició de CSS

CSS és l'acrònim de `Cascading Style Sheets` (en català: Fulls d'Estil en Cascada). És un llenguatge de marques utilitzat per descriure l'aspecte i la formatació d'un document escrit en HTML o XML. CSS defineix com han de ser mostrats els elements en les pàgines web, incloent-hi el disseny, colors, espaisatges, tipus de lletra, etc.

### Història de CSS

La necessitat d'una eina com CSS va sorgir amb l'expansió del web. Al principi, HTML estava dissenyat només per a estructurar informació. No obstant això, amb el temps, els desenvolupadors van començar a utilitzar HTML per a controlar també l'aspecte visual dels llocs web. Això va fer que els documents HTML es tornessin més complexos i difícils de mantenir. CSS va ser creat per separar el contingut (HTML) de la presentació (CSS), permetent una gestió més eficient i organitzada dels llocs web.

### Per què és important CSS?

**Separació de contingut i presentació**: CSS permet que el contingut (HTML) i la presentació (CSS) estiguin separats. Això facilita la manteniment, ja que podem canviar l'estil sense alterar el contingut, i viceversa.

**Flexibilitat i control**: CSS proporciona un gran control sobre l'aspecte de les pàgines web, permetent als desenvolupadors crear dissenys atractius i adaptatius.

**Dissenys responsius**: Amb CSS, es pot crear dissenys que s'adapten a diferents mides de pantalla, des de mòbils fins a pantalles d'ordinador de gran resolució.

**Eficiència**: Un full d'estil pot ser aplicat a múltiples pàgines, cosa que significa que un canvi en aquest full afectarà totes les pàgines associades. Això permet actualitzacions ràpides i consistents en tot el lloc web.

**Accessibilitat**: Utilitzant CSS, es pot millorar l'accessibilitat dels llocs web per a persones amb discapacitats, ajustant per exemple el contrast o la mida del text.

### Com funciona CSS

Quan un **navegador** carrega una pàgina web, **primer carrega l'HTML**, que defineix l'estructura de la pàgina. **A continuació, carrega el CSS** associat, que defineix com han de ser mostrats els elements. **El navegador combina aquesta informació** per a mostrar la pàgina final a l'usuari.

CSS és una eina poderosa i essencial en el desenvolupament web modern. Permet als desenvolupadors crear pàgines web atractives, eficients i accessibles, millorant l'experiència d'usuari i facilitant la gestió i manteniment dels llocs web.

### Incloure CSS a fitxers HTML

Incloure CSS a un fitxer HTML pot fer-se de tres maneres diferents:

- estils en línia (inline)
- estils interns (dins de l'etiqueta `<head>` del document)
- estils externs (utilitzant un fitxer CSS separat). Anem a veure cada mètode amb detall i amb exemples.

#### Estils en línia (Inline Styles)

Aquests estils s'apliquen directament a una etiqueta específica utilitzant l'atribut style. Són útils quan volem estilizar un element específic sense afectar altres elements similars en la pàgina.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Exemple d'estils en línia</title>
  </head>
  <body>
    <p style="color: blue">Aquest text és blau gràcies als estils en línia.</p>
  </body>
</html>
```

#### Estils interns (Internal Styles)

Aquests estils es defineixen dins de l'etiqueta `<style>` que es troba dins del `<head>` del document. Afecten a tot el document HTML.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Exemple d'estils interns</title>
    <style>
      p {
        color: red;
      }
    </style>
  </head>
  <body>
    <p>Aquest text és vermell gràcies als estils interns.</p>
  </body>
</html>
```

#### Estils externs (External Styles)

Aquest és el mètode més comú i organitzat. Els estils es guarden en un fitxer separat amb extensió `.css`. Aquest fitxer s'enllaça des del document HTML utilitzant l'etiqueta `<link>`.

Fitxer `estils.css`:

```css
p {
  color: green;
}
```

Fitxer `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Exemple d'estils externs</title>
    <link rel="stylesheet" type="text/css" href="estils.css" />
  </head>
  <body>
    <p>Aquest text és verd gràcies als estils externs.</p>
  </body>
</html>
```

#### Recomanació

Encara que pots utilitzar qualsevol dels tres mètodes segons les teves necessitats, **els estils externs són els més recomanats** per a llocs web de gran envergadura. Això es deu al fet que permeten **una millor organització, reutilització d'estils i manteniment més fàcil**.

Estils en línia poden ser útils per a ajustos específics, però poden fer que el codi HTML es torni desordenat si s'usen en excés.

### Sintaxi bàsica: selectors, propietats i valors

Per entendre com estilitzar elements en una pàgina web amb CSS, és crucial comprendre la seva sintaxi bàsica. La sintaxi CSS consta de tres components principals: selectors, propietats i valors.

Els selectors, propietats i valors són components fonamentals de la sintaxi CSS. En combinar-los de diferents maneres, podem crear estils complexos i atractius per als nostres llocs web.

```css
selector {
  propietat: valor;
}
```

#### Selectors

Els selectors determinen quins elements del document HTML seran estilitzats. Aquests elements poden ser seleccionats de diverses maneres:

- Selector d'etiqueta
- Selector de classe
- Selector d'ID

I hi ha molts altres selectors més avançats com selectors de fills, selectors d'atributs, pseudo-classes, entre d'altres.

##### Selector d'etiqueta

Selecciona tots els elements d'una determinada etiqueta.

Aquest exemple selecciona tots els elements `<p>` i els fa de color vermell.

```css
p {
  color: red;
}
```

##### Selector de classe

Selecciona tots els elements que tenen un atribut class específic.

Aquest exemple selecciona tots els elements amb la classe "destacat" i els fa en lletra negreta.

```css
.destacat {
  font-weight: bold;
}
```

##### Selector d’ID

Selecciona un element específic que té un atribut id determinat.

Aquest exemple selecciona l'element amb l'ID "titolPrincipal" i canvia la seva mida de lletra a 24px.

```css
#titolPrincipal {
  font-size: 24px;
}
```

#### Propietats

Les propietats són els aspectes específics que volem canviar en els elements seleccionats. Algunes propietats comunes inclouen `color`, `font-size`, `margin`, `padding`, `border`, etc.

Per exemple, en el codi `font-size: 24px;`, `font-size` és la propietat que estem especificant.

#### Valors

Els valors són les configuracions específiques que assignem a una propietat. En l'exemple anterior, 24px és el valor assignat a la propietat `font-size`.

Un altre exemple seria `color: blue;`, on `blue` és el valor assignat a la propietat color.

### Unitats CSS

Quan es tracta de definir dimensions, marges, i altres propietats en CSS, és essencial entendre les diferents unitats que es poden utilitzar.

Les unitats CSS es poden classificar en dues categories principals: **absolutes** i **relatives**.

#### Unitats CSS absolutes

Les unitats absolutes són fixes i no canvien segons el context en què s'utilitzen. Les més comunes inclouen:

- Pixels (`px`): La unitat més bàsica i comuna, representa un píxel a la pantalla.
- Punts (`pt`): Tradicionalment utilitzada en la impressió; 1pt = 1/72 de polzada.
- Polsades (`in`): Una unitat de mesura en polzades.
- Centímetres (`cm`): Una unitat de mesura en centímetres.
- Mil·límetres (`mm`): Una unitat de mesura en mil·límetres.

#### Unitats CSS relatives

Les unitats relatives s'ajusten en funció d'altres valors com la mida de lletra del pare o la mida de la finestra de visualització. Aquestes inclouen:

- Percentatge (`%):` Es basa en les dimensions de l'element pare.
- Em (`em`): Relacionat amb la mida de lletra de l'element. 1em és equivalent a la mida de lletra de l'element pare.
- Rem (`rem`): Similars a les em, però sempre es relacionen amb la mida de lletra de l'element arrel (habitualment el `<html>`).
- Viewport Width (`vw`): 1vw és igual a l'1% de l'amplada de la finestra de visualització.
- Viewport Height (`vh`): 1vh és igual a l'1% de l'alçada de la finestra de visualització.
- Viewport Minimum (`vmin`)/Viewport Maximum (`vmax`): `1vmin` és igual a l'1% de la mida més petita de la finestra de visualització, mentre que `1vmax` és igual a l'1% de la mida més gran.

#### Quan Utilitzar Cada Unitat

**Unitats Absolutes**: Utilitza-les quan necessitis que un element tingui una mida fixa que no canviï, com ara per a imatges o elements interactius específics.

**Unitats Relatives**: Són més flexibles i s'adapten millor a diferents mides de pantalla i configuracions. Són especialment útils per a dissenys responsius.

### Box model: margin, border, padding, content

Un dels conceptes fonamentals en CSS és el model de caixa o "Box Model". Tots els elements a una pàgina web es poden considerar com caixes rectangulars, i aquest model defineix com aquestes caixes són estructurades i interactuen entre elles. El Box Model està compost de quatre components principals:`content` (contingut), `padding` (rellenat) , `border` (vora) i`margin` (marge).

![Box model](https://upload.wikimedia.org/wikipedia/commons/7/7a/Boxmodell-detail.png)

_Font: https://en.wikipedia.org/wiki/CSS_box_model_

#### Content (Contingut)

És la part central del model de caixa, on es mostra el contingut real de l'element, com ara text, imatges o altres elements interns. La mida del contingut es pot controlar amb les propietats width i height.

```css
div {
  width: 200px;
  height: 150px;
}
```

#### Padding (Rellenat)

El padding es troba directament al voltant del contingut i dins de la vora. Representa l'espai entre el contingut i la vora. El rellenat pot ser definit per als quatre costats de la caixa (superior, dret, inferior, esquerre) utilitzant propietats específiques (padding-top, padding-right, padding-bottom, padding-left) o una única propietat per definir tots (padding).

```css
div {
  padding: 10px 15px 10px 15px; /* Superior, dret, inferior, esquerre */
}
```

#### Border (Vora)

La vora envolta el padding (si existeix) i el contingut. Es pot definir en termes d'amplada, estil i color. Similar al padding, la vora pot ser especificada per cada costat individualment (border-top, border-right, border-bottom, border-left) o amb propietats agrupades.

```css
div {
  border: 2px solid black; /* Amplada, estil i color */
}
```

#### Margin (Marge)

El marge es troba a l'exterior de la vora i separa un element d'altres elements. Com amb el padding i la vora, el marge pot ser definit per cada costat individualment (margin-top, margin-right, margin-bottom, margin-left) o amb una única propietat.

```css
div {
  margin: 20px 25px; /* Superior/inferior, dret/esquerre */
}
```

### Posicionament i layout: float, flexbox i grid

Un dels desafiaments més grans en disseny web és organitzar i posicionar elements de manera eficient i responsiva. CSS proporciona eines potents com Flexbox i Grid per a ajudar els desenvolupadors a crear layouts complexos amb més facilitat i flexibilitat.

Tot i això, abans que es desenvolupessin les tecnologies modernes de disposició com Flexbox i Grid, el posicionament basat en float era una tècnica estàndard per crear dissenys web. Encara que ara es considera més tradicional i ha estat en gran part substituït per tècniques més modernes, és útil entendre com funciona float, ja que encara es pot trobar en codi més antic i pot ser útil en certes situacions.

#### Float

La propietat `float` es fa servir per col·locar un element a l'esquerra o a la dreta d'un contenidor, permetent que el contingut flueixi al seu voltant.

```css
.element-esquerra {
  float: left;
}

.element-dreta {
  float: right;
}
```

Aquí hi ha alguns punts clau per entendre sobre float:

1. **Desplaçament del flux normal**: Quan es fa servir float en un element, aquest es desplaça fora del flux normal de la pàgina i es mou a l'esquerra o a la dreta, depenent del valor que se li doni (left o right).
2. **Clearing Floats**: Els elements flotants poden causar problemes de disposició si no es "netegen". Per això, sovint es fa servir la propietat clear per assegurar-se que cap element es col·loca al costat d'un element flotant.

   ```css
   .element-netejar {
     clear: both; /* Pot ser 'left', 'right', o 'both' */
   }
   ```

3. **Ús amb moderació**: Encara que float pot ser útil en algunes situacions, sovint pot portar a complicacions i problemes inesperats en el disseny, especialment en dissenys responsius. Les tècniques més modernes com Flexbox i Grid ofereixen més control i són més predictibles.

Exemple de necessitat de `clear`:

```html
<aside>
  <p>Aquesta és la barra lateral.</p>

  <p>Aquesta és la barra lateral.</p>
</aside>

<main>
  <p>Aquest és el contingut principal.</p>
</main>

<footer>
  <p>Aquest és el peu de pàgina.</p>
</footer>
```

```css
aside {
  float: left;
  width: 200px;
  background-color: #eee;
}

main {
  background-color: #ddd;
}

footer {
  /* clear: both; */
  background-color: #ccc;
}
```

#### Flexbox (Flexible Box)

Flexbox és un model de disseny unidimensional que permet organitzar elements en forma de columna o fila dins d'un contenidor, fent-ho amb una gran flexibilitat.

Per utilitzar Flexbox, primer s'ha d'establir un **contenidor flex** amb la propietat `display: flex;` o `display: inline-flex;` (si volem que el contenidor es comporti com un element en línia).

```css
.contenidor-flex {
  display: flex;
}
```

Propietats comunes del contenidor flex:

- `flex-direction`: Defineix la direcció principal (fila o columna).
- `justify-content`: Alinea els elements al llarg de l'eix principal.
- `align-items`: Alinea els elements al llarg de l'eix creuat.
- `flex-wrap`: Determina si els elements han d'embolicar-se o no quan no hi ha suficient espai.

Propietats dels elements flex:

- `flex-grow`: Defineix la capacitat de creixement d'un element respecte als altres.
- `flex-shrink`: Estableix com un element es reduirà respecte als altres.
- `flex-basis`: Defineix la mida base d'un element abans que es distribueixin espais lliures.

#### Grid (Reixeta)

CSS Grid és un model de disseny bidimensional que permet crear layouts amb files i columnes, oferint un major control sobre la disposició dels elements.

Per utilitzar Grid, s'ha d'establir un **contenidor grid** amb la propietat `display: grid;` o `display: inline-grid;`.

```css
.contenidor-grid {
  display: grid;
}
```

Propietats comuns del contenidor grid:

- `grid-template-columns` i `grid-template-rows`: Defineixen la mida i el nombre de columnes i files.
- `grid-gap`: Estableix l'espaiat entre columnes i files.
- `grid-template-areas`: Defineix zones de la reixeta per a col·locar elements.

Propietats dels elements grid:

- `grid-column` i `grid-row`: Determinen on comença i acaba un element dins de la reixeta.
- `grid-area`: Assigna un element a una zona específica definida en grid-template-areas.

#### Diferències

Tant Flexbox com Grid ofereixen eines poderoses per a la creació de layouts.

Mentre que Flexbox és ideal per a layouts unidimensionals (com ara barres de navegació o columnes d'imatges), Grid és perfecte per a dissenys bidimensionals amb estructures més complexes.

La clau està en entendre les necessitats específiques del projecte i utilitzar l'eina més adequada per a la tasca. Moltes vegades, Flexbox i Grid es poden utilitzar conjuntament per a obtenir el millor dels dos mons.

### Responsive design amb media queries

El disseny responsiu es refereix a l'adaptació d'un lloc web perquè es visualitzi de manera òptima en diferents dispositius, des de telèfons mòbils fins a pantalles d'ordinador de gran resolució. Amb l'augment de l'ús de dispositius mòbils per navegar per la web, és essencial que els llocs web s'adaptin a diferents mides de pantalla i condicions d'ús. Les "media queries" de CSS són una eina essencial per a aconseguir aquesta adaptabilitat.

#### Què són les Media Queries?

Les media queries permeten aplicar estils basats en determinades condicions, com ara la mida de pantalla, la resolució o altres característiques del dispositiu. Amb elles, es pot canviar l'aparença i la disposició del contingut depenent de les característiques del dispositiu en què es visualitza el lloc web.

#### Sintaxi bàsica de Media Queries

La sintaxi bàsica d'una media query implica especificar el tipus de mitjà (com ara screen per a pantalles) i després definir una o més condicions.

En l'exemple anterior, el fons del cos es canviarà a blau clar per a dispositius amb una amplada de pantalla de 600px o menys.

```css
@media screen and (max-width: 600px) {
  /* Estils per a pantalles amb una amplada màxima de 600px */

  body {
    background-color: lightblue;
  }
}
```

#### Punts de trencament (Breakpoints)

Els punts de trencament són les mides específiques on es decideix canviar la disposició o l'estil d'un lloc web per adaptar-se millor a una determinada mida de pantalla. En seleccionar punts de trencament, és comú utilitzar mides que corresponen a dispositius comuns, com ara telèfons mòbils, tauletes i escriptoris.

```css
/* Estil per defecte per a escriptoris i pantalles grans */
body {
  font-size: 16px;
}

/* Estil per a tablets*/
@media screen and (max-width: 768px) {
  body {
    font-size: 14px;
  }
}

/* Estil per a telèfons mòbils */
@media screen and (max-width: 480px) {
  body {
    font-size: 12px;
  }
}
```

#### Altres condicions en Media Queries

A més de la mida de pantalla, es poden utilitzar altres condicions en media queries, com ara la resolució (resolution), l'orientació (orientation), la relació d'aspect (aspect-ratio), entre d'altres.

[Torna a la presentació de l'assignatura](README.md)
