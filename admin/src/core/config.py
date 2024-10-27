from os import environ
class Config(object):
    """base config."""

    SECRET_KEY ="secret"
    TESTING = False
    SESSION_TYPE="filesystem"

class ProductionConfig(Config):
    """Production Config"""
    MINIO_SERVER= environ.get("MINIO_SERVER")
    MINIO_ACCESS_KEY= environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY= environ.get("MINIO_SECRET_KEY")
    MINIO_SECURE   = True
    pass

class DevelopmentConfig(Config):
    """Development Configuration"""
    #minio
    MINIO_SERVER= environ.get("MINIO_SERVER")
    MINIO_ACCESS_KEY= environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY= environ.get("MINIO_SECRET_KEY") 
    MINIO_SECURE   = False
    #database
    DB_USER=environ.get("DB_USER")
    DB_PASSWORD= environ.get("DB_PASSWORD")
    DB_HOST=environ.get("DB_HOST")
    DB_PORT= environ.get("DB_PORT")
    DB_NAME= environ.get("DB_NAME") 
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