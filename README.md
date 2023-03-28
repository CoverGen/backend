# Ticket App

Ticket App is a Django project that provides a platform for creating events and managing virtual tickets.

## Getting Started

Follow the instructions below to set up the local development environment and run the project.

### Prerequisites

- Python 3.10
- Poetry (dependency manager)(It will be installed later)

### Installation

1. Clone the repository:

```
git clone https://gitlab.com/covergen/backend.git
cd ticket_app
```

2. Install Poetry, if you haven't already:

```
curl -sSL https://install.python-poetry.org | python3 -
```
For other installation methods, refer to the official documentation.

3. Install the project dependencies and set up the virtual environment:

```
poetry install
```

4. Apply the database migrations:

```
poetry run python manage.py migrate --settings=ticket_app.settings.development
```

5. (Optional) Load initial data or fixtures, if necessary:

```
poetry run python manage.py loaddata fixture_file.json --settings=ticket_app.settings.development
```
Replace fixture_file.json with the name of your fixture file.

### Running the Development Server

To start the development server, run:

```
make run-dev
```

This command will start the Django development server with development settings. You can access the application at http://127.0.0.1:8000/.

### Linting and Formatting

This project uses Flake8 for linting and Black for code formatting. To lint the code, run:

```
make lint
```

To format the code, run:

```
make format
```

To check if the code is formatted correctly, run:

```
make check-format
```

### Pre-Commit Hooks

This project uses pre-commit hooks to automatically lint and format the code before committing changes. To set up the pre-commit hooks, run:

```
poetry run pre-commit install
```

After setting up the pre-commit hooks, any time you commit changes, the hooks will automatically run the lint and formatting checks. If any issues are found, the commit will be blocked, and you'll need to fix the issues and try committing again. It's very neccessary to run this command before start to coding
