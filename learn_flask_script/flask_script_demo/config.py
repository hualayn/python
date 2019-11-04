import os

DEBUG = True

# HOST = '0.0.0.0'
#
# SECRET_KEY = 'dev'

# TEMPLATE_AUTO_RELOAD = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\python\learn_flask_script\\flask_script_demo\db\database.db'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.dirname(os.path.dirname(__file__)) + '/db/database.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db\database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False