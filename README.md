# Flask Starter 🧪🚀

A production-ready Flask starter template with modern best practices and essential features for rapid development.

## Features 🔧

- **Database Integration**: SQLAlchemy ORM with PostgreSQL support
- **Database Migrations**: Alembic integration for schema management
- **Blueprint Architecture**: Modular API structure with blueprints
- **Configuration Management**: Environment-based configuration with `.env` support
- **RESTful API**: Example endpoints demonstrating CRUD operations
- **Development Ready**: Debug mode, hot reload, and development-friendly setup

## Project Structure 📦

```
backend/
├── api/                # API blueprints and endpoints
├── core/               # Core application configuration
│   ├── config.py       # Application configuration
│   ├── models.py       # Database models
│   └── blueprints.py   # Blueprint registration
├── migrations/         # Database migration files
├── tests/              # Test files
├── utils/              # Utility functions
├── app.py              # Application factory
└── requirements.txt    # Python dependencies
```

## Setup Instructions 📝

1. Change `app_name` to the name of your app in the core/config.py file.
2. Change `.env.example` to `.env`.
3. Create a new database in your PostgreSQL instance:
    ```bash
    psql postgres -c 'CREATE DATABASE app_name_development;'
    ```
4. Run the migrations:
    ```bash
    flask db migrate -m "Initial migration"

    flask db upgrade
    ```
5. Run the app:
    ```bash
    flask run --debug
    ```
6. Test the endpoints specified in the `api/example.py` file.

## Initial Setup 🔨

### (Optional) Python Version Management with pyenv

If you don't have pyenv installed, you can install it from: https://github.com/pyenv/pyenv#installation

#### Basic pyenv Commands

- **List all available Python versions**:
  ```bash
  pyenv install --list
  ```

- **Install a specific Python version**:
  ```bash
  pyenv install 3.11.0
  ```

- **List installed Python versions**:
  ```bash
  pyenv versions
  ```

- **Set Python version for current directory or globally** 
  ```bash
  pyenv local 3.12.0 # creates .python-version file
  pyenv global 3.12.0
  ```

- **Show currently active Python version and the executable path**:
  ```bash
  pyenv version
  pyenv which python
  ```

- **Show which Python executable is being used**:
  ```bash
  which python
  python --version
  ```

### Creating Virtual Environment

After selecting your Python version with pyenv, create a virtual environment:

```bash
python -m venv .venv
```
or using direct python path:
```bash
/Users/username/.pyenv/versions/3.12.0/bin/python -m venv .venv
```

### Activating and Deactivating Virtual Environment

- **Activate the virtual environment**:
  ```bash
  source .venv/bin/activate
  ```

- **Deactivate the virtual environment** (when you're done working):
  ```bash
  deactivate
  ```

After activating the virtual environment, install dependencies:
```bash
pip install -r requirements.txt
```
