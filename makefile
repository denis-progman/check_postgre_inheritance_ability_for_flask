.PHONY: help build up start down destroy stop restart logs logs-api ps login-timescale login-api db-shell exec-into app-exec
DEFAULT_GOAL := help
COMPOSE_FILE_DEFAULT_NAME := docker-compose.yml
APP_CONTAINER_NAME := python-app
DB_CONTAINER_NAME := postgre-db
DB_USER_NAME := postgres
DB_NAME := postgres
DB_PASSWORD := pass

help:
	@echo "Makefile for the project"
	@echo "Usage: make [command]"
	@echo "Commands:"
	@echo "  build:        Build the docker containers"
	@echo "  up:           Start the docker containers"
	@echo "  start:        Start the docker containers"
	@echo "  down:         Stop the docker containers"
	@echo "  destroy:      Stop and remove the docker containers"
	@echo "  stop:         Stop the docker containers"
	@echo "  restart:      Restart the docker containers"
	@echo "  logs:         Show the logs of the docker containers"
	@echo "  ps:           List the docker containers"
	@echo "  ex-in:        Execute a command into a running container"
	@echo "  app-ex:       Execute a command into the app container"
	@echo "  db:           Execute a command into the db container"
	@echo "  db-sql:       Open the psql shell"
	@echo "  db-list:      List the databases"
	@echo "  db-tables:    List the tables of the default database"
	@echo "  flask-i:      Initialize the flask migrations"
	@echo "  flask-m:      Create a new flask migration"
	@echo "  flask-u:      Upgrade the flask migrations"


build:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) build $(c)

up:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) up -d $(c)

start:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) start $(c)

down:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) down $(c)

destroy:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) down -v $(c)

stop:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) stop $(c)

restart:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) stop $(c)
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) up -d $(c)

logs:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) logs --tail=100 -f $(c)

ps:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) ps

ex-in:
	docker exec $(container) $(c)

app-ex:
	docker exec $(APP_CONTAINER_NAME) $(c)

db:
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER_NAME) $(DB_NAME) -c "$(c)"

db-sql:
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER_NAME) $(DB_NAME)

db-list:
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER_NAME) $(DB_NAME) -c "\l"

db-tables:
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER_NAME) $(DB_NAME) -c "\dt"

db-del-all-tables:
	rm -rf app/migrations
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER_NAME) $(DB_NAME) -c "DROP SCHEMA public CASCADE;CREATE SCHEMA public;GRANT ALL ON SCHEMA public TO postgres;GRANT ALL ON SCHEMA public TO public;"

flask-i:
	docker exec $(APP_CONTAINER_NAME) flask db init

flask-m:
	docker exec $(APP_CONTAINER_NAME) flask db migrate

flask-u:
	docker exec $(APP_CONTAINER_NAME) flask db upgrade

flask-dg:
	docker exec $(APP_CONTAINER_NAME) flask db downgrade
	