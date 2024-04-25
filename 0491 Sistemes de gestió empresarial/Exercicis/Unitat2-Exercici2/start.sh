#!/bin/bash
service postgresql start

# Configurar la contrasenya per a l'usuari postgres
su postgres -c "psql -c \"ALTER USER postgres PASSWORD 'novaContrasenya';\""

# Qualsevol altra configuració inicial aquí

# Bucle infinit per mantenir el contenidor en execució
tail -f /dev/null
