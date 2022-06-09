1. Download postgresql image
  ```
  docker pull postgres
  ```
2. Create a volume to store the data
  ```
  docker volume create pgdata
  ```
3. Run container
  ```
  docker run --name postgresqldb \
  -e POSTGRES_USER=<username> \
  -e POSTGRES_PASSWORD=<password> \
  -p 5432:5432 \
  --mount source=pgdata,target=/var/lib/postgresql/data \
  -d postgres
  ```
 4. Start container
  ```
  docker start postgresqldb
  ```
