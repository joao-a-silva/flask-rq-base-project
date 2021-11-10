import os

class Config(object):
    """
    Common configurations
    """
   
    REDIS_URL = os.getenv('REDIS')
    QUEUES = ['default']
    TIME_OUT = {'QUEUE':'5m', 
                'TASK':500,
                'RESULT_TTL':300
    }

   
class DevelopmentConfig(Config):
    """
    Development configurations
    """

class StagingConfig(Config):
    """
    Development configurations
    """

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}