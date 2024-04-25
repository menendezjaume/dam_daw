const express = require("express");
const { Pool } = require("pg");

const app = express();
const port = 3001;

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "postgres",
  password: "novaContrasenya",
  port: 5432,
});

app.get("/", async (req, res) => {
  const client = await pool.connect();
  const result = await client.query("SELECT NOW()");
  client.release();
  res.send(`Hola Món - La hora actual és: ${result.rows[0].now}`);
});

app.listen(port, () => {
  console.log(`Servidor escoltant al port http://localhost:${port}`);
});
