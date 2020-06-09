# webapp-boilerplate

The Dockerfile builds an environment on top of the Debian image wich can be used to run the django-cookiecutter without configuration. Using the instructions below you can get into the container's bash, launch cookiecutter and run the Django server which can then be reached on `localhost:8000`. **At the moment the data inside the container is not persistent.**

1. Build the image with `docker build -t <name>`
2. Get into the container bash with `docker run -it -p 8000:8000 --rm <name> bash` (the `--rm` flag cleans the container after the execution)
3. Run the django-cookiecutter with `cookiecutter .`
4. Get into the project directory and activate the environment with `cd <project-name> && activate`
5. Get into the Django project directory and run the django server with `cd <project-name> && python3 manage.py runserver 0.0.0.0:8000`