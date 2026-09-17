# Flask Docker Starter

## Run the Flask and Apache Jena containers

```sh
FUSEKI_PASSWORD=change-me docker compose up --build
```

The Flask app is available at <http://localhost:5000>, and the Apache Jena
Fuseki UI and SPARQL endpoint are available at <http://localhost:3030>.
The configured dataset is `ds`; its endpoint is
<http://localhost:3030/ds/query>.

Stop the services with `docker compose down`. Add `-v` to remove the persisted
Jena data volume as well.

## Run with Docker

```sh
docker build -t flask-starter .
docker run --rm -p 5000:5000 flask-starter
```

Then open <http://localhost:5000/health>.

## Run locally

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```