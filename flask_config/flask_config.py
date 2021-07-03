class TestConfig(object):
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig(object):
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DeploymentConfig(object):
    #TODO should be taken from environment variable
    SECRET_KEY = 'test'
    #TODO should be set to point at the location of the database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False