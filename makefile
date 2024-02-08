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
	@echo "  logs-api:     Show the logs of the api container"
	@echo "  ps:           List the docker containers"
	@echo "  login-timescale:  Login to the timescale container"
	@echo "  login-api:    Login to the api container"
	@echo "  db-shell:     Open a psql shell to the timescale container"

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

logs-api:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) logs --tail=100 -f api

ps:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) ps

login-timescale:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) exec timescale /bin/bash

login-api:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) exec api /bin/bash

db-shell:
	docker compose -f $(COMPOSE_FILE_DEFAULT_NAME) exec timescale psql -Upostgres

exec-into:
	docker exec $(container) $(command)

app-exec:
	docker exec container=$(APP_CONTAINER_NAME) command=$(command)

db-sql:
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER_NAME) -W $(DB_NAME) $(DB_PASSWORD)
	