#To run
- install docker-compose and docker
- ensure no processes are currently running on ports 8080 or 5432
- from the root of the repository run `docker-compose up`
- Load the file `upload.html` locally in a browser

#Alternative
## Postgres
- Have a postgres instance running on localhost - if you don't, you can do so with docker easily with
`docker run -d -p 5432:5432 --name mypostgres -e POSTGRES_PASSWORD=password postgres`

- Create a database called `customer_purchases`.

    - This database can be changed (for port, etc) in the `base_repository.py` file.

## Server
- Run 

`pip install -r requirements.txt`

`python3 -m swagger_server`

- Load the file `upload.html` locally in a browser (in production host this in nginx)


### Running with Docker
