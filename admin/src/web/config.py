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
    
    pass


class TestingConfig(Config):
    """Testging Configuration"""

    TESTING=True

config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}