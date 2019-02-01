import os

# Note, it's very important that keys read from the environment have the same name as in the config

class Config(object):
  pass

class ProdConfig(Config):
  ENV = 'production'

class DevConfig(Config):
  ENV = 'development'
  DEBUG = True
