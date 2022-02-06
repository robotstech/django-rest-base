# django-rest-base-project
Main => ![ci workflow](https://github.com/LibertytechX/django-rest-base-project/actions/workflows/ci.yml/badge.svg?branch=main) <br>
Dev ==> ![ci workflow](https://github.com/LibertytechX/django-rest-base-project/actions/workflows/ci.yml/badge.svg?branch=dev) <br>
InDev => ![ci workflow](https://github.com/LibertytechX/django-rest-base-project/actions/workflows/ci.yml/badge.svg?branch=indev) <br>
Template project for all Django Rest services developed

## Tools and Resources
1. Python 3.8 [link](https://www.python.org/downloads/release/python-387/)
1. Virtualenv
1. Postgresql 
    1. Download the application [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). 
    2. Install Postgresql and set up root (postgres). [linux link](https://www.postgresql.org/download/linux/ubuntu/) [windows link](https://www.postgresqltutorial.com/install-postgresql/)
    3. Create __base__ database.

## Setup
*__Note__**: *Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions below*

1. Create the virtual environment.
```shell script
virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

1. Set up `.env` file by duplicating the `.example.env` file(and editing if required).

1. Activate the environment and install dependencies.
    - #### Linux
    ```shell script
    source /path/to/venv/bin/activate
    pip install -r requirements.txt
    ```

    - #### Windows
    ```cmd
    ./path/to/venv/bin/activate
    pip install -r requirements.txt
    ```
1. Launch the app
    ```shell script
    python manage.py runserver localhost:8000
    ```

## Test Project
- Run all tests
    ```shell script
    pytest
    ```

## Development
1. launch app with docker compose
   ```shell
   docker-compose up --build --remove-orphans
   ```
   
## REFERENCES
- [Django](https://www.djangoproject.com/start/)
- [DRF](https://www.django-rest-framework.org/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [Django Storages](https://django-storages.readthedocs.io/en/latest/), for [AWS S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
- [Pytest](https://docs.pytest.org/en/latest/) for [Django](https://pytest-django.readthedocs.io/en/latest/) including [coverage](https://github.com/pytest-dev/pytest-cov)
- [Python Decouple: Strict separation of settings from code](https://github.com/henriquebastos/python-decouple/)
- [Gunicorn](https://gunicorn.org/)
- [The Twelve Factor App](https://12factor.net/)