# webapp-boilerplate

Experimental Docker-compose Django coookiecutter.

## Dependencies

* cookiecutter
* docker-compose

## Fast Check Instructions

1. `cookiecutter .`
2. `cd <my_project_name>`
3. `docker compose build`
4. `docker compose up`
5. Wait for DB healthchecks and then visit `localhost:8000`

## TODO

* Test DB integration
* Test data persistence
* DB persistence
* Multiple database support (supports mysql and postgresql atm)
* Multiple project template support
* Deploy support (also, change binds to volumes)
* Git integration
* CLI scripts
* (Multiple framework support)