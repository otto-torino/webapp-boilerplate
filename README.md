# webapp-boilerplate

Experimental Docker-Compose Django cookiecutter.

## Dependencies

* cookiecutter
* docker-compose

## Fast Check Instructions

1. `python3 cli.py`
2. `cd <project_name>`
3. `docker-compose build`
4. `docker-compose up`
5. Wait for DB healthchecks and then visit `localhost:8000`

## TODO

* Test DB integration
* Test data persistence
* DB persistence
* Multiple database support (supports mysql and postgresql atm)
* Multiple project template support
* Deploy support (change binds to volumes among the other things)
* Git integration
* CLI scripts
* (Multiple framework support)