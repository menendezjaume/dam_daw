FROM node:latest

# Instal·lar PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Copiar el script d'inici al contenidor
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Obrir el port 5432
EXPOSE 5432

# Executar el script d'inici
CMD ["/bin/bash", "-c", "/start.sh"]
