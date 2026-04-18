#!/bin/bash

# This script runs during PostgreSQL first initialization only (empty data directory).
# It creates the additional databases and loads their schemas.

set -e

# Create additional databases
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE db_controller;
    GRANT ALL PRIVILEGES ON DATABASE db_controller TO "$POSTGRES_USER";

    CREATE DATABASE esmart;
    GRANT ALL PRIVILEGES ON DATABASE esmart TO "$POSTGRES_USER";
EOSQL

# Load schema into db_controller
echo "Loading schema: db_controller"
psql --username "$POSTGRES_USER" --dbname "db_controller" \
    < /docker-entrypoint-initdb.d/schemas/db_controller.sql

# Load schema into esmart
echo "Loading schema: esmart"
psql --username "$POSTGRES_USER" --dbname "esmart" \
    < /docker-entrypoint-initdb.d/schemas/esmart.sql

echo "Schema initialization complete."
