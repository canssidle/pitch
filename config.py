# import os
# class Config:
#     '''
#     General configuration parent class
#     '''
#     SECRET_KEY = 'canssy'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     UPLOADED_PHOTOS_DEST='app/static/photos'
#     #email configurations

#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     SIMPLEMDE_JS_IIFE = True
#     SIMPLEMDE_USE_CDN = True
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://canssidle:judycharles@localhost/pitches'

  


# class ProdConfig(Config):
#     '''
#     Pruduction  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://canssidle:judycharles@localhost/pitch_test'


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings

#     '''
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://canssidle:judycharles@localhost/pitches'

#     DEBUG =True


    
# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig,
#     'test':TestConfig
# }


