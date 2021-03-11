import os


class Config(object):
    JWT_SECRET_KEY = "Dev Key"
    SECRET_KEY = "Dev Key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DATABASE_URL")
        if not value:
            raise ValueError("DATABASE_URL is not set")
        return value


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")
        if not value:
            raise ValueError("JWT Secret Key is not set")

        return value


class TestingConfig(Config):
    TESTING = True
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI_TEST")
        if not value:
            raise ValueError("SQLALCHEMY_DATABASE_URI_TEST is not set")
        return value


environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
