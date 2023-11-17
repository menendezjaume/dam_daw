# Instal·lació i configuració de sistemes ERP-CRM

## 1. Introducció a Docker

### 1.1. Conceptes bàsics de Docker

#### Introducció a Docker

Docker és una plataforma de contenidors que permet als desenvolupadors empaquetar aplicacions en contenidors—unitats estàndard de software que embalen el codi i totes les seves dependències.

Els contenidors de Docker permeten que una aplicació s'executi de la mateixa manera en qualsevol entorn, ja que tot el necessari per executar l'aplicació està dins del contenidor.

#### Contenidors vs màquines virtuals

##### Què són els contenidors?

Els contenidors són una abstracció a nivell d'aplicació que agrupen codi i dependències. S'executen de manera aïllada, però comparteixen el mateix OS kernel, inicien més ràpid i utilitzen menys memòria que les màquines virtuals.

##### Diferències amb màquines virtuals

Mentre les màquines virtuals virtualitzen tot un hardware per executar un sistema operatiu complet, els contenidors només virtualitzen el sistema operatiu mateix, permetent un ús més eficient dels recursos.

#### Imatges de Docker

Les imatges són plantilles de sola lectura usades per crear contenidors. Es construeixen a partir de fitxers de text anomenats Dockerfiles. Cada línia en un Dockerfile és una instrucció que construeix una part de la imatge.

#### Contenidors

Quan s'executa una imatge, es crea un contenidor. Un contenidor és una instància executable d'una imatge, que pot ser iniciada, aturada, moguda o eliminada independentment.

#### Docker Hub i repositoris

##### Docker Hub

Docker Hub és un servei basat en la núvol que permet a usuaris i empreses compartir i descarregar imatges de Docker. Funciona com un repositori centralitzat per a la distribució i gestió de contenidors.

##### Treballar amb imatges

Podem cercar imatges disponibles en Docker Hub, descarregar-les al nostre sistema local i utilitzar-les per crear contenidors. També és possible pujar les nostres pròpies imatges personalitzades al Docker Hub per a compartir-les amb altres.

### 1.2. Instal·lació i configuració de docker

Seguirem la documentació oficial per tal d'instal·lar Docker Engine: [Install Docker Engine](https://docs.docker.com/engine/install/)

Recorda visitar [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/), la secció `Manage Docker as a non-root user`, per tal de poder executar Docker sense fer servir un usuari privilegiat.

### 1.3. Primeros passos amb docker

#### Què són els Dockerfiles?

Un Dockerfile és un fitxer de text que conté una llista d'instruccions per construir una imatge de Docker. Cada instrucció en el fitxer afegirà una nova capa a la imatge, permetent personalitzar-la segons les necessitats de l'aplicació.

#### Estructura bàsica d'un Dockerfile

- Instrucció `FROM`: Especifica la imatge base des de la qual es construirà la nova imatge.
- Instruccions `RUN`: Executa comandaments dins de la imatge en construcció.
- Instrucció `COPY`/`ADD`: Afegeix fitxers des del sistema local a la imatge.
- Instrucció `CMD`: Defineix el comandament que s'executarà quan el contenidor sigui iniciat a partir d'aquesta imatge.

#### Exemple d'un Dockerfile simple

Creació d'una imatge personalitzada basada en Ubuntu que instal·la el servidor web Apache:

```Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y apache2
CMD ["apache2ctl", "-D", "FOREGROUND"]
```

Aquest Dockerfile inicia amb una imatge base d'Ubuntu, instal·la Apache i configura el contenidor per executar Apache en primer pla.

#### Comandaments bàsics de docker

`docker run`: Com executar un container.

`docker ps`: Com veure els containers en execució.

`docker stop`: Aturar un container.

`docker rm` i `docker rmi`: Eliminar containers i imatges.

#### Executar un contenidor simple

**Comandament:** `docker run hello-world`

**Descripció:** Aquest comandament executa un contenidor a partir de la imatge `hello-world`. Si l'imatge no es troba en el sistema local, Docker la descarrega automàticament de Docker Hub. Aquesta imatge és una eina de prova bàsica per confirmar que Docker està instal·lat correctament i que pot crear contenidors.

**Resultat:** El contenidor imprimeix un missatge en la línia de comandes confirmant que la seva execució ha estat exitosa.

#### Executar un contenidor avançat

**Comandament:** `docker run -d -p 80:80 nginx`

**Descripció:** Aquest comandament descarrega (si és necessari) i executa un contenidor amb l'imatge `nginx`, un servidor web popular. L'opció -d executa el contenidor en segon pla (desacoplat), i `-p 80:80` mapeja el port 80 del contenidor al port 80 de l'amfitrió.

**Resultat:** Un cop executat, es pot accedir a un servidor web Nginx funcionant accedint a http://localhost des del navegador.

#### Llistar Contenidors amb docker ps

**Comandament:** `docker ps`

**Descripció:** Aquest comandament llista tots els contenidors en execució, mostrant detalls com ID
del contenidor, imatge utilitzada, temps de funcionament, ports i noms. Per veure tots els contenidors, inclosos els aturats, s'utilitza `docker ps -a`.

**Resultat:** Es proporciona una visió general dels contenidors actius en el sistema.

#### Detalls del Contenidor amb docker inspect

**Comandament:** `docker inspect [CONTAINER_ID]`

**Descripció:** Es pot utilitzar aquest comandament per obtenir informació detallada sobre un contenidor específic, incloent la seva configuració, estat, xarxa, volums, etc.

**Resultat:** S'obté una sortida detallada en format JSON que proporciona una visió profunda dels internals del contenidor.

#### Aturar un Contenidor

**Comandament:** `docker stop [CONTAINER_ID]`

**Descripció:** Aquest comandament s'utilitza per aturar un contenidor que està en execució.

**Resultat:** El contenidor s'atura, però es manté en el sistema i es pot reiniciar.

#### Eliminar un Contenidor

**Comandament:** `docker rm [CONTAINER_ID]`

**Descripció:** Després d'aturar un contenidor, es pot utilitzar aquest comandament per eliminar-lo completament del sistema.

**Resultat:** El contenidor s'elimina, alliberant espai i recursos.

#### Executar un Comandament dins d'un Contenidor

**Comandament:** `docker exec -it [CONTAINER_ID] bash`

**Descripció:** Aquest comandament permet entrar en un contenidor en execució i interactuar amb ell a través d'una sessió de shell, útil per a depuració i administració.

**Resultat:** S'obre un shell dins del contenidor, permetent l'execució de comandaments directament dins del seu entorn.

#### Eliminar Contenidors Aturats

**Comandament:** `docker container prune`

**Descripció:** Aquest comandament elimina tots els contenidors aturats, ajudant a mantenir el sistema net i alliberant espai en disc.

**Comandament:** Utilitzar aquest comandament després d'aturar i revisar contenidors no necessaris.

#### Eliminar Imatges No Utilitzades

**Comandament:** `docker image prune`

**Descripció:** Similar a `docker container prune`, aquest comandament elimina les imatges que no estan associades amb cap contenidor, alliberant encara més espai.

**Comandament:** Executar aquest comandament per eliminar imatges obsoletes o innecessàries.

### 1.4. Conceptes avançats

#### Xarxes en Docker

##### Gestió de xarxes en Docker

Docker utilitza xarxes virtuals per connectar contenidors entre ells i amb l'exterior. Això permet que els contenidors comuniquin de manera segura i eficient.

##### Tipus de Xarxes en Docker

- **Xarxa Bridge:** El tipus de xarxa per defecte en Docker, que permet la comunicació entre contenidors i amb l'amfitrió.
- **Xarxa Host:** Aquesta xarxa elimina l'aïllament entre el contenidor i l'amfitrió, permetent que els contenidors accedeixin directament a la xarxa de l'amfitrió.

#### Comandaments Bàsics de Xarxa

- `docker network create`: Crea una nova xarxa.
- `docker network ls`: Llista les xarxes disponibles.
- `docker network connect`: Connecta un contenidor a una xarxa.

#### Volums i Persistència de Dades

##### Volums en Docker

Els volums són el mecanisme preferit per a persistir dades generades i utilitzades pels contenidors de Docker. A diferència de les dades dins del contenidor, els volums són gestionats per Docker i són independents del cicle de vida del contenidor.

##### Creació i gestió de volums

Comandaments:

- `docker volume create`: Crea un nou volum.
- `docker volume ls`: Llista tots els volums existents.
- `docker volume inspect`: Proporciona detalls sobre un volum específic.

Els volums es poden muntar en contenidors utilitzant l'opció `-v` o `--mount` quan s'executa un contenidor.

##### Exemple d'Ús de Volums

Executar un contenidor de MySQL amb un volum per a persistir les dades de la base de dades:

```bash
docker run -d \
  --name my-mysql \
  -e MYSQL_ROOT_PASSWORD=mypassword \
  -v mysql-data:/var/lib/mysql \
  mysql
```

Aquest comandament crea i executa un contenidor MySQL i utilitza un volum anomenat `mysql-data` per a persistir les dades.

## 2. Docker Compose

### 2.1. Introducció a Docker Compose

Docker Compose és una eina que permet definir i executar aplicacions multi-contenidor amb Docker. Utilitza un fitxer YAML per configurar els serveis de l'aplicació, permetent així una fàcil definició, creació i execució de l'entorn de l'aplicació.

#### Beneficis de Docker Compose

- Simplifica el procés de configuració: Amb Docker Compose, pots definir tots els paràmetres dels teus contenidors, xarxes i volums en un sol fitxer.
- Facilita la replicació: Les configuracions són fàcilment replicables, permetent un desplegament consistent en diferents entorns.
- Gestió centralitzada: Amb un sol comandament pots iniciar, aturar i reconstruir tots els serveis de la teva aplicació.

#### Estructura bàsica d'un fitxer `docker-compose.yml`

El fitxer `docker-compose.yml` és un fitxer en format YAML que defineix com Docker Compose ha de construir i executar els contenidors de la teva aplicació.

**Components Clau**:

- **Serveis**: Defineix els diferents contenidors que formen part de la teva aplicació. Cada servei pot usar una imatge de Docker Hub o construir-se a partir d'un Dockerfile.
- **Xarxes**: Defineix les xarxes que connecten els teus contenidors.
- **Volums**: Especifica els volums de dades utilitzats pels teus contenidors.

#### Consideracions importants

**Versió del fitxer `docker-compose.yml`**:

És important especificar la `versió` del format del fitxer `docker-compose.yml` a l'inici del fitxer. Això assegura la compatibilitat amb diferents versions de Docker Compose.

Les versions més recents ofereixen més funcionalitats i millores en la gestió de serveis.

**Ubicació del fitxer `docker-compose.yml`**:

Normalment, el fitxer `docker-compose.yml` es troba a l'arrel del projecte, fent que sigui fàcil iniciar i gestionar l'entorn de l'aplicació des d'allà.

### 2.2. Creació i gestió de serveis amb Docker Compose

Suposem que volem configurar una aplicació web senzilla amb un servidor web i una base de dades. El fitxer `docker-compose.yml` podria semblar això:

```yaml
version: "3"
services:
  web:
    image: nginx
    ports:
      - "80:80"
    networks:
      - webnet
  database:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
    networks:
      - webnet
networks:
  webnet:
```

Aquest fitxer defineix dos serveis: `web` (utilitzant l'imatge `nginx`) i `database` (utilitzant l'imatge `postgres`). També defineix una xarxa anomenada `webnet` que connecta els dos serveis.

#### Definició de serveis en `docker-compose.yml`

Cada servei en Docker Compose es defineix sota la clau `services` en el fitxer `docker-compose.yml`. Aquests serveis representen contenidors que treballaran conjuntament dins de la teva aplicació.

##### Components d'un servei

- **Imatge**: Pots especificar la imatge de Docker que vols utilitzar per aquest servei, que pot ser una imatge preexistent de Docker Hub o una construïda des d'un Dockerfile.
- **Ports**: Configura els ports que vols exposar i mapejar. Per exemple, `ports: - "80:80"` exposa el port 80 del contenidor al port 80 de l'amfitrió.
- **Variables d'Entorn**: Pots definir variables d'entorn específiques per al servei amb `environment` o `env_file`.
- **Volums**: Defineix els volums per a la persistència de dades o per compartir dades entre l'amfitrió i el contenidor.
- **Dependències**: Amb `depends_on`, pots especificar les dependències entre serveis, assegurant que s'inicien en l'ordre correcte.

#### Gestió de serveis amb comandaments de Docker Compose

##### Iniciar els serveis

- **Comandament**: `docker-compose up`
- **Descripció**: Aquest comandament busca el fitxer `docker-compose.yml` en el directori actual i inicia tots els serveis definits. Si s'utilitza l'opció `-d`, els serveis s'iniciaran en el fons (mode desacoplat).
- **Exemple**: Executar `docker-compose up -d` per iniciar tots els serveis definits en el fitxer `docker-compose.yml` sense bloquejar la terminal.

##### Aturar els serveis

- **Comandament**: `docker-compose down`
- **Descripció**: Aquest comandament atura tots els serveis que s'estan executant i elimina els contenidors, xarxes, volums, i imatges creades per `docker-compose up`.
- **Exemple**: Executar `docker-compose down` per netejar tot l'entorn i aturar tots els serveis.

##### Altres comandaments útils

- **Veure Logs**: `docker-compose logs` per veure els logs de tots els serveis.
- **Escalar Serveis**: `docker-compose up --scale service=n` on `service` és el nom del servei i `n` és el nombre d'instàncies que vols executar.

#### Avantatges de la gestió de serveis amb Docker Compose

- **Consistència**: Tots els membres de l'equip treballen amb la mateixa configuració, evitant així els problemes de "funciona en la meva màquina".
- **Simplicitat**: Amb un sol fitxer de configuració i uns quants comandaments, pots gestionar tot un ecosistema d'aplicacions i serveis.

### 2.3. Xarxes en Docker Compose

Docker Compose permet la creació de xarxes personalitzades que faciliten la comunicació entre diferents serveis (contenidors). Aquestes xarxes es defineixen a nivell de top del fitxer `docker-compose.yml` i són utilitzades per a connectar els serveis.

#### Definir xarxes

A la secció `networks` del fitxer `docker-compose.yml`, pots definir una o més xarxes personalitzades. Els serveis poden connectar-se a qualsevol d'aquestes xarxes.

Exemple de configuració de xarxa:

```yaml
networks:
  myapp-network:
    driver: bridge
```

#### connectar serveis a xarxes

Dins de la definició de cada servei, pots especificar a quines xarxes es connectarà. Això permet un alt nivell d'aïllament i control sobre com els serveis interaccionen entre ells.

Exemple de connectar un servei a una xarxa:

```yaml
services:
  myservice:
    image: myimage
    networks:
      - myapp-network
```

#### Aliases i comunicació entre contenidors

Pots assignar aliases a contenidors dins de les xarxes, facilitant la referència i comunicació entre els serveis.

Exemple d'assignació d'alias:

```yaml
services:
  myservice:
    image: myimage
    networks:
      myapp-network:
        aliases:
          - myservicealias
```

#### Exemple Pràctic: Aplicació amb Múltiples Serveis

**Configuració d'una Aplicació Multi-Servei**:

Imaginem una aplicació amb un frontend, un backend, i una base de dades. Cada component pot ser configurat com un servei diferent en Docker Compose, i tots poden comunicar-se a través d'una xarxa interna.

**Fitxer `docker-compose.yml` d'Exemple**:

En aquest exemple, configurem tres serveis: `frontend`, `backend`, i `database`, tots connectats a la xarxa `myapp-network`.

```yaml
version: "3"
services:
  frontend:
    image: myfrontend
    networks:
      - myapp-network
  backend:
    image: mybackend
    networks:
      - myapp-network
  database:
    image: postgres
    networks:
      - myapp-network
networks:
  myapp-network:
    driver: bridge
```

**Comunicació entre els Serveis**:

En aquesta configuració, els serveis `frontend`, `backend`, i `database` poden comunicar-se entre ells usant els noms dels serveis com a hostnames. Per exemple, el `frontend` pot accedir al `backend` utilitzant l'URL `http://backend`.

### 2.4. Persistència de Dades amb Volums

#### Què són els Volums en Docker

Els volums en Docker són una forma de persistir dades generades i utilitzades per contenidors. Són completament gestionats per Docker i viuen independentment del cicle de vida dels contenidors.

#### Què són els Bind Mounts

Els bind mounts enllacen un directori o fitxer del sistema de fitxers de l'amfitrió a un camí dins del contenidor. A diferència dels volums, els bind mounts depenen del sistema de fitxers de l'amfitrió.

#### Diferències Principals

- **Gestió**: Els volums són gestionats per Docker, mentre que els bind mounts són gestionats pel sistema de fitxers de l'amfitrió.
- **Portabilitat**: Els volums són més portàtils i més fàcils de fer còpies de seguretat o transferir entre hosts.
- **Performance**: Els bind mounts poden oferir millor rendiment per a alguns casos d'ús específics on es necessita accés directe als fitxers de l'amfitrió.

#### Definir i Utilitzar Volums en `docker-compose.yml`

##### Configuració de Volums

En Docker Compose, els volums es defineixen dins de la secció `volumes` del fitxer `docker-compose.yml`. Aquesta definició pot incloure detalls sobre el volum com el seu nom.

##### Exemple de Configuració de Volums

Imaginem una aplicació amb una base de dades PostgreSQL que necessita persistir dades. Podem definir un volum per aquesta base de dades en el nostre fitxer `docker-compose.yml`:

```yaml
version: "3"
services:
  database:
  image: postgres
  environment:
    POSTGRES_PASSWORD: example
  volumes:
    - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

En aquest exemple, `db-data` és el nom del volum que hem creat. El camí `/var/lib/postgresql/data` és on PostgreSQL emmagatzema les seves dades dins del contenidor, i ara està muntat en el volum `db-data`.

#### Avantatges de l'Ús de Volums en Docker Compose

- **Independència de Dades**: Les dades persistides en volums són independents del contenidor que les utilitza, fent que la gestió de dades sigui més segura i flexible.
- **Fàcil Backup i Restauració**: Els volums poden ser més fàcilment respaldats, restaurats o traslladats entre diferents entorns o contenidors.
- **Seguretat**: Utilitzar volums redueix el risc de comprometre el sistema de fitxers de l'amfitrió, ja que els contenidors no necessiten accés directe a aquest.

### 2.5. Depuració i Manteniment

#### Veure Logs de Contenidors amb Docker Compose

El comandament `docker-compose logs` permet veure els logs de tots els contenidors associats amb els serveis definits en el fitxer `docker-compose.yml`. És una eina útil per a la depuració, ja que proporciona una visió centralitzada de l'activitat dels contenidors.

**Exemple Pràctic**: Executant `docker-compose logs` es mostren els logs de tots els serveis. Si vols veure els logs d'un servei específic, pots utilitzar `docker-compose logs [nom_del_servei]`. Per exemple, `docker-compose logs web` mostrarà només els logs del servei `web`.

**Opcions Útils**: Pots afegir opcions com `-f` per seguir els logs en temps real o `--tail=50` per veure només les últimes 50 línies.

#### Executar Comandaments dins de Contenidors

Utilitzant el comandament `docker-compose exec`, pots executar comandaments dins d'un contenidor en execució. Això és útil per a realitzar tasques de depuració, manteniment o simplement per explorar l'estat intern del contenidor.

**Exemple Pràctic**: Per accedir al shell d'un contenidor en execució, pots utilitzar `docker-compose exec [nom_del_servei] sh` (o `bash`, depenent de la shell disponible dins del contenidor). Per exemple, `docker-compose exec backend sh` t'obrirà un shell dins del contenidor del servei `backend`.

#### Actualització de Contenidors sense Interrupció

Docker Compose permet actualitzar serveis sense necessitat d'aturar tota l'aplicació. Això es pot fer actualitzant la configuració o les imatges dels serveis i després executant un re-desplegament.

**Exemple Pràctic**: Si has fet canvis en el fitxer `docker-compose.yml` o necessites actualitzar una imatge a la seva última versió, pots utilitzar `docker-compose up -d`. Això recrearà els serveis que han canviat, mantenint els que no han estat modificats.

**Reconstrucció de Contenidors**: En el cas que hagis modificat un Dockerfile i necessitis reconstruir l'imatge, pots utilitzar `docker-compose up -d --build`. Això assegurarà que els serveis amb imatges reconstruïdes siguin actualitzats.

## 3. Projecte Pràctic: Instal·lació d'Odoo amb Docker Compose

### 3.1. Introducció a l'Arquitectura del Projecte

Per aprofundir en el contingut específic de la secció "3.1. Introducció a l'Arquitectura del Projecte" de la teva formació, centrarem-nos en la instal·lació i configuració d'Odoo 16 utilitzant Docker Compose. Aquesta secció cobrirà una visió general d'Odoo com a ERP i la seva arquitectura bàsica de dues capes amb Odoo i PostgreSQL.

### 3.1. Introducció a l'Arquitectura del Projecte

#### Descripció d'Odoo

Odoo és una suite integral d'aplicacions empresarials (ERP) que inclou mòduls per a gestió de vendes, CRM, projectes, magatzem, fabricació, finances, recursos humans, i molt més.

És conegut per la seva flexibilitat i capacitat d'adaptar-se a les necessitats específiques de cada empresa gràcies a la seva arquitectura modular.

#### Necessitats de Serveis i Dependències per a Odoo

Per funcionar eficaçment, Odoo requereix una base de dades robusta, amb PostgreSQL sent la opció recomanada.

Per a la versió 16 d'Odoo, és important assegurar que totes les dependències requerides estiguin disponibles, incloent un entorn de Python adequat i llibreries específiques.

#### Arquitectura de 2 Capes

La instal·lació d'Odoo amb Docker Compose es basa en una arquitectura de dues capes:

- **Capa de Servei Web (Odoo)**: Aquesta capa gestiona la interfície d'usuari d'Odoo, la lògica de l'aplicació, i la interacció amb la base de dades.

- **Capa de Base de Dades (PostgreSQL)**: Responsable de l'emmagatzematge de totes les dades empresarials, configuracions i informació de transaccions.

#### Interacció entre les Capes

El servei web d'Odoo es comunica amb la base de dades PostgreSQL per a l'emmagatzematge i la recuperació de dades.

La configuració amb Docker Compose assegura que aquesta comunicació sigui fluida i segura, mantenint els contenidors ben aïllats i fàcilment gestionables.

### 3.2. Preparació del Fitxer docker-compose.yml

Per aprofundir en el contingut específic de la secció "3.2. Preparació del Fitxer `docker-compose.yml`" de la teva formació en Docker Compose, centrarem-nos en la creació d'un fitxer `docker-compose.yml` per a la configuració d'Odoo 16 i PostgreSQL, incloent les definicions dels serveis, les variables d'entorn necessàries i la configuració dels volums per a la persistència de dades.

### 3.2. Preparació del Fitxer `docker-compose.yml`

#### Definició dels Serveis

##### Configuració del Servei Odoo

En el fitxer `docker-compose.yml`, el primer pas és definir el servei per a Odoo. Especificarem la imatge d'Odoo 16 i els ports per a l'accés web.

Exemple de configuració per a Odoo:

```yaml
version: "3"
services:
  odoo:
    image: odoo:16
    depends_on:
      - db
    ports:
      - "8069:8069"
```

##### Configuració del Servei PostgreSQL

A continuació, definim el servei de la base de dades PostgreSQL, que Odoo utilitzarà per emmagatzemar dades.

Exemple de configuració per a PostgreSQL:

```yaml
db:
  image: postgres:13
  environment:
  POSTGRES_DB: odoodb
  POSTGRES_USER: odoo
  POSTGRES_PASSWORD: odoo
```

#### Variables d'Entorn

##### Variables per a Odoo

Odoo requereix certes variables d'entorn per a la seva configuració, com l'enllaç amb la base de dades.

Exemple de variables d'entorn per a Odoo:

```yaml
odoo:
  environment:
  HOST: db
  USER: odoo
  PASSWORD: odoo
```

##### Variables per a PostgreSQL

Per a PostgreSQL, les variables d'entorn s'utilitzen per establir el nom de la base de dades, l'usuari i la contrasenya.

Aquestes variables ja s'han definit en l'exemple anterior.

#### Volums

##### Persistència de Dades per a PostgreSQL

Per a la base de dades PostgreSQL, és important configurar un volum per a la persistència de les dades.

Exemple de configuració de volum per a PostgreSQL:

```yaml
db:
  volumes:
    - postgres-data:/var/lib/postgresql/data
```

##### Persistència de Dades per a Odoo

Odoo també pot requerir volums per emmagatzemar fitxers addicionals, com arxius de configuració o dades d'usuari.

Exemple de configuració de volum per a Odoo:

```yaml
odoo:
  volumes:
    - odoo-data:/var/lib/odoo
```

##### Definició dels Volums

Al final del fitxer `docker-compose.yml`, definirem els volums que hem utilitzat.

Exemple de definició dels volums:

```yaml
volumes:
  postgres-data:
  odoo-data:
```

### 3.3. Configuració de Xarxes i Seguretat

#### Creació d'una Xarxa Interna en Docker Compose

En el fitxer `docker-compose.yml`, es pot definir una xarxa interna per aïllar el trànsit entre els serveis d'Odoo i PostgreSQL.

Exemple de configuració de la xarxa:

```yaml
networks:
  odoo-network:
  driver: bridge
```

#### Assignació de Serveis a la Xarxa

Assigna els serveis d'Odoo i PostgreSQL a aquesta xarxa per permetre la comunicació entre ells mentre es manté aïllats de qualsevol altre servei de la xarxa.

Exemple d'assignació dels serveis a la xarxa:

```yaml
services:
  odoo:
  networks:
      - odoo-network
  db:
  networks:
      - odoo-network
```

#### Establir Restriccions d'Accés per a PostgreSQL

##### Limitar l'Accés a PostgreSQL

La configuració de xarxa en Docker Compose pot ser utilitzada per restringir l'accés a la base de dades PostgreSQL només des del servei d'Odoo.

En la configuració de PostgreSQL, no s'exposen ports al host, limitant l'accés a la xarxa interna.

##### Exemple de Restricció de Ports

A diferència d'Odoo, on es poden exposar els ports per a l'accés web, per a PostgreSQL no s'especificarà cap port exposat.

Exemple de configuració de PostgreSQL sense ports exposats:

```yaml
db:
  image: postgres:13
  environment:
    POSTGRES_DB: odoodb
    POSTGRES_USER: odoo
    POSTGRES_PASSWORD: odoo
  networks:
    - odoo-network
```

#### Implementació de Mesures de Seguretat Addicionals

##### Variables d'Entorn Segures

És important utilitzar variables d'entorn per a la configuració sensible, com ara contrasenyes, per evitar que siguin hard-coded en el fitxer `docker-compose.yml`.

Aquestes variables es poden definir en fitxers `.env` o de manera segura en l'entorn de desplegament.

##### Actualitzacions Regulars i Patches de Seguretat

Mantenir les imatges d'Odoo i PostgreSQL actualitzades amb les últimes versions per assegurar que totes les correccions de seguretat estiguin aplicades.

### 3.4. Desplegament i Proves del Sistema

Iniciar els Serveis: Executar docker-compose up per iniciar els serveis.

Verificació: Comprovar que l'aplicació Odoo es carrega correctament i es pot connectar a la base de dades PostgreSQL.

### 3.5. Manteniment i Escalabilitat

Actualitzacions: Com actualitzar els serveis sense temps d'inactivitat.

Còpies de Seguretat i Restauració: Pràctiques per a fer còpies de seguretat de les dades i com restaurar-les.

Escalabilitat Bàsica: Discussió sobre com escalar el servei d'Odoo si es necessita.

### 3.6. Documentació i Recursos Addicionals

Guies d'Odoo i PostgreSQL: Enllaços a la documentació oficial i guies d'ús.

Exemples i Plantilles: Repositoris amb exemples de configuracions d'Odoo i PostgreSQL amb Docker Compose.

### 3.7. Projecte Final i Presentació

Desenvolupament d'un Cas d'Ús Personalitzat: Encoratjar els participants a desenvolupar el seu propi projecte utilitzant Odoo i Docker Compose.

Presentació de Projectes: Sessió on els participants presenten els seus projectes i comparteixen aprenentatges.