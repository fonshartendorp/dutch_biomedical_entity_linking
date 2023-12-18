# Create local .env file
cp .env-example .env

# Set local file paths & MySQL root password in .env

# Set MySQL loading config settings 
vim ./02_ExtractSubset/2022AB/META/populate_mysql_db.sh

MYSQL_HOME=/usr
user=root
password=root
db_name=umls

# Start MySQL container in Docker
docker-compose up -d

# Enter docker container
docker exec -it umls bash

# Execute mysql loading script
cd /src_files/2022AB/META/
bash populate_mysql_db.sh
