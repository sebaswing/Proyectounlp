class Config(object):
    """base config."""

    SECRET_KEY ="secret"
    TESTING = False
    SESSION_TYPE="filesystem"

class ProductionConfig(Config):
    """Production Config"""

    pass

class DevelopmentConfig(Config):
    """Development Configuration"""
    DB_USER="postgres"
    DB_PASSWORD="123"
    DB_HOST="localhost"
    DB_PORT="5432"
    DB_NAME="grupo01"
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    print(SQLALCHEMY_DATABASE_URI)


class TestingConfig(Config):
    """Testging Configuration"""
    TESTING=True

config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}