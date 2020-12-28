# Celery 5.0.2 Docker example

This is a fork of [bstiel/celery-docker](https://github.com/bstiel/celery-docker) updated with poetry.

## Configuration

Edit [docker-compose.yml](docker-compose.yml) file and replace `CELERY_BROKER_URL` with connection string for a queue manager.

Default setting `CELERY_BROKER_URL=amqp://admin:mypass@172.23.0.1:5672` is for Mac running RabbitMQ with

```bash
docker run -d -p 5672:5672 -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=mypass rabbitmq
```

## Launch

```bash
docker-compose up --build
```