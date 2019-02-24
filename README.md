## Postgres
Have a postgres instance running on localhost - if you don't, you can do so with docker easily with
`docker run -d -p 5432:5432 --name mypostgres -e POSTGRES_PASSWORD=password postgres`

Create a database called `customer_purchases`.

This database can be changed (for port, etc) in the `base_repository.py` file.

## Server
Run either with docker (below), or locally with

`pip install -r requirements.txt`

`python3 -m swagger_server`

Load the file `upload.html` locally in a browser (in production host this in nginx)


### Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```