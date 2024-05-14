# Here is online information about the MySQL database image:
#   https://hub.docker.com/_/mysql
# I could also have used a Mongo or a Postgres SQL image if I wanted

FROM mysql

# I looked up information online about the MySQL image
# That information tells me that if the container machine starts up
#   and it finds no existing data, it will run any SQL files
#   in the directory /docker-entrypoint-initdb.d
COPY setup.sql /docker-entrypoint-initdb.d


# The online information indicates that the mysql image expects to find
#   a root password for the database system in a certain environment variable

# The ENV command in a dockerfile sets an environment variable

ENV MYSQL_ROOT_PASSWORD=rotmgbestgame

# Port 3306 is the default port used by MySQL
EXPOSE 3306