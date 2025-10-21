# SETUP INSTRUCTIONS:

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
