Multi Databases
===============

This solution has a CPF query service that makes available the personal data stored in `MySQL`.<br/>
Each call in this service sends an event to an event queue on `RabbitMQ`.<br/>
A worker processes these events and stores them in `MongoDB` and updates the last record in `Elasticsearch`.

## Given 3 databases

* **Very sensible database** - [MySQL](#mysql)
* **Light sensible database** - [MongoDB](#mongodb)
* **Fast database** - [Elasticsearch](#elasticsearch)

## <a name="mysql"></a>MySQL

It stores accounts data.

## <a name="mongodb"></a>MongoDB

It stores events related data.

## <a name="elasticsearch"></a>Elasticsearch

It stores the latest event associated to an account.

Running
-------

* Create `.env` file

```bash
MYSQL_ROOT_PASSWORD=example
RABBITMQ_DEFAULT_PASS=example
COMPOSE_FILE=docker-compose.yml:whois-api/nested-docker-compose.yml
```

* Run docker-compose

```bash
$ docker-compose up
```

* Run database migration

```bash
$ virtualenv venv
...

$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
...

(venv) $ yoyo apply -p
Password for mysql://root@localhost/secure-database:
... applied
```

* Call [whois-api](https://github.com/luiscoms/whois-api.git) endpoints
