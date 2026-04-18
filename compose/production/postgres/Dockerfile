FROM docker.io/postgres:18

COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

# Copy schema init script and SQL schema files.
# The script runs on first boot (empty data volume) to create additional
# databases (db_controller, esmart) and load their schemas.
COPY ./compose/production/postgres/init/init_schemas.sh /docker-entrypoint-initdb.d/init_schemas.sh
RUN chmod +x /docker-entrypoint-initdb.d/init_schemas.sh

COPY ./schema/db_controller.sql /docker-entrypoint-initdb.d/schemas/db_controller.sql
COPY ./schema/esmart.sql /docker-entrypoint-initdb.d/schemas/esmart.sql
