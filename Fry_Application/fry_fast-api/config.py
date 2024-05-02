import os


class EnvConfig:
    _instance = None
    DB_HOST = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_NAME = ""
    DB_PORT = ""
    SCHEMA = ""

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnvConfig, cls).__new__(cls)
            cls.DB_HOST = 'localhost'
            cls.DB_USERNAME = 'xxxxx'
            cls.DB_PASSWORD = 'xxxxx'
            cls.DB_NAME = 'postgres'
            cls.DB_PORT = '5432'
            cls.SCHEMA = 'fry'
        return cls._instance

    def get_env_variable(name: str) -> str:
        try:
            return os.environ[name]
        except KeyError:
            message = "Expected environment variable '{}' not set.".format(name)
            raise Exception(message)