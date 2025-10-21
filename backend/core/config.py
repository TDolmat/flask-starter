import os
from typing import NamedTuple


class Config(NamedTuple):
    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool


def _get_config(environment: str) -> Config:
    if environment == 'development':
        return Config(
            # Add development config here
            SECRET_KEY='dev-secret-key',
            # TODO: Change [app_name] to the name of your app
            SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost:5432/[app_name]_development',
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    elif environment == 'testing':
        return Config(
            # Add testing config here
            SECRET_KEY='test-secret-key',
            # TODO: Change [app_name] to the name of your app
            SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost:5432/[app_name]_testing',
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    elif environment == 'production':
        return Config(
            # Add production config here
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

env = os.getenv('FLASK_ENV') or 'development'
CONFIG = _get_config(env)
