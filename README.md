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
