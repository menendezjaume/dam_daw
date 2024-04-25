# Enunciat

Integració d'una Base de Dades dins d'un Únic Contenidor Docker

## Pas 1: Creació del Dockerfile Modificat

1. **Elecció de la Base de Dades:**

   - Decideix quina base de dades vols integrar (en el nostre exemple farem servir PosgreSQL).

2. **Modificació del Dockerfile:**
   - Inclou les instruccions per instal·lar la base de dades dins del mateix contenidor que el servidor.
   - Afegeix qualsevol script d'inicialització de la base de dades necessari.
   - Assegura't que tot el software necessari per a la base de dades estigui instal·lat i configurat dins del contenidor.

## Pas 2: Configuració de la Connexió a la Base de Dades

1. **Modificació del Codi del Servidor:**

   - Actualitza el teu servidor perquè utilitzi la base de dades integrada.
   - Configura el servidor per connectar-se a la base de dades local dins del contenidor.

2. **Gestió de la Configuració:**
   - Utilitza variables d'entorn o fitxers de configuració per gestionar la connexió a la base de dades.
   - Assegura't que el codi del servidor pot accedir a aquestes configuracions correctament.

## Pas 3: Creació i Inicialització de la Base de Dades

1. **Scripts d'Inicialització:**
   - Prepara scripts SQL o qualsevol altra eina necessària per inicialitzar la base de dades amb l'esquema i dades de prova.
   - Afegeix instruccions en el Dockerfile per a executar aquests scripts durant la construcció del contenidor.

## Pas 4: Construcció i Execució del Contenidor

1. **Construcció de la Imatge Docker:**

   - Utilitza `docker build` per a construir la imatge del teu projecte, incloent el servidor i la base de dades.

2. **Execució del Contenidor:**
   - Inicia el contenidor amb la imatge creada i verifica que tant el servidor com la base de dades estan funcionant correctament.

## Pas 5: Proves i Validació

1. **Proves Funcionals:**
   - Realitza peticions al teu servidor per assegurar que respon correctament i que pot interactuar amb la base de dades.
   - Verifica que les operacions de lectura i escriptura a la base de dades funcionen com s'espera.

# Resolució

Per resoldre l'exercici de combinar un servidor Node.js amb una base de dades PostgreSQL dins d'un únic contenidor Docker, seguirem els passos detallats a continuació:

### Pas a Pas per a l'Exercici

#### Pas 1: Preparar el Projecte Node.js

1. **Crea un nou projecte Node.js** si encara no tens un. Això es pot fer amb `npm init` dins d'un nou directori.

2. **Instal·la el mòdul `pg`** per a connectar-te a PostgreSQL des de Node.js. Pots fer-ho executant `npm install pg` en la teva línia de comandes.

#### Pas 2: Escriure el Codi del Servidor

1. **Crea un fitxer JavaScript** (per exemple, `server.js`) per al teu servidor. Aquest fitxer haurà de configurar un servidor web bàsic amb Node.js i connectar-se a PostgreSQL.

2. **Exemple de codi per a `server.js`**:

```javascript
const express = require("express");
const { Pool } = require("pg");
const app = express();
const port = 3000;

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "postgres",
  password: "password",
  port: 5432,
});

app.get("/", async (req, res) => {
  const client = await pool.connect();
  const result = await client.query("SELECT NOW()");
  client.release();
  res.send(`Hola Món - La hora actual és: ${result.rows[0].now}`);
});

app.listen(port, () => {
  console.log(`Servidor escoltant al port ${port}`);
});
```

Aquest codi crea un servidor web bàsic que connecta a PostgreSQL i retorna l'hora actual a qualsevol petició GET a la ruta base (`/`).

#### Pas 3: Crear el Dockerfile

1. **Crea un Dockerfile** en la mateixa carpeta del teu projecte Node.js.

2. **Exemple de Dockerfile**:

```Dockerfile
FROM node:latest

# Instal·lar PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Copiar els fitxers del projecte
WORKDIR /usr/src/app
COPY . .

# Instal·lar dependències del projecte Node.js
RUN npm install

# Obrir el port 3000
EXPOSE 3000

# Comandes per a iniciar PostgreSQL i el servidor Node.js
CMD service postgresql start && node server.js
```

   Aquest Dockerfile configura un entorn amb Node.js i PostgreSQL, copia els teus fitxers del projecte, instal·la les dependències i estableix el commandament per iniciar tant PostgreSQL com el servidor Node.js.

#### Pas 4: Construir i Executar el Contenidor

1. **Construeix la imatge Docker**. En la carpeta del teu projecte, executa:

   ```bash
   docker build -t node-postgres-app .
   ```

2. **Executa el contenidor Docker**:

   ```bash
   docker run -p 3000:3000 node-postgres-app
   ```

   Això mapeja el port 3000 del contenidor al port 3000 de l'amfitrió, permetent-te accedir al servidor Node.js a través del navegador.

#### Pas 5: Provar el Servidor

1. **Obre el teu navegador** i ves a `http://localhost:3000`. Hauries de veure un missatge amb l'hora actual, indicant que el servidor Node.js està connectat i interactuant amb PostgreSQL.

#### Nota:

Aquest exemple és bàsic i per a propòsits educatius. En un entorn de producció, hauries de gestionar les contrasenyes i les variables d'entorn de manera segura, optimitzar la configuració del servidor PostgreSQL, i considerar aspectes com la persistència de dades i la gestió d'errors.
