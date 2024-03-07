SETTINGS_DEV=core.settings

# Check for the presence of a pip executable, preferring pip3 if available
PIP_CMD=$(shell command -v pip3 || echo pip)

# Define the Python command to use, preferring python3
PYTHON_CMD=$(shell which python3)

install_requirements:
	@echo "Installing requirements"
	$(PIP_CMD) install -r requirements.txt

run_makemigrations:
	@echo "Making Migration files"
	$(PYTHON_CMD) manage.py makemigrations --settings=$(SETTINGS_DEV)

run_migrations:
	@echo "Running Migrations in Docker"
	docker-compose run --rm todo_api $(PYTHON_CMD) manage.py migrate

build_app_docker:
	@echo "Building API test server with Docker"
	docker-compose build

run_app_docker:
	@echo "Starting API test server with Docker"
	docker-compose up

install_pre_commit: install_requirements
	@echo "Installing pre-commit"
	pre-commit install

run_tests:
	@echo "Running tests in Docker"
	docker-compose run --rm app $(PYTHON_CMD) manage.py test

