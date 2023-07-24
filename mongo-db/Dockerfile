FROM mongo
COPY ./mongo-db-init-files /docker-entrypoint-initdb.d
ENV MONGO_INITDB_ROOT_USERNAME root
ENV MONGO_INITDB_ROOT_PASSWORD example
EXPOSE 27017