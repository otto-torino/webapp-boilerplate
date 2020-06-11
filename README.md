# webapp-boilerplate

Basic docker-compose Django coookiecutter

## Dependencies

* cookiecutter
* docker-compose

## Instructions

1. `cookiecutter .`
2. `cd <my_project_name>`
3. `docker compose build`
4. `docker compose up`
5. Wait for DB healthchecks and then visit `localhost:8000`

## TODO

* Test DB integration
* Test data persistence
* DB persistence
* Multiple database support
* Multiple project template support
* Deploy support
* Git integration
* CLI scripts
* (Multiple framework support)