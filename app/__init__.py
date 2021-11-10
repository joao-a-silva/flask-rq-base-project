# -*- coding: utf-8 -*-
from flask import Flask
from config import app_config
from flasgger import Swagger
import os
from flask_cors import CORS, cross_origin

print('----------------------------------')
print(os.getenv('FLASK_CONFIG'))

# local imports
from config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[os.getenv('FLASK_CONFIG')])
#app.config.from_pyfile('config.py')
cors = CORS(app)
Swagger(app)
from app import routes

# shell context for flask cli
app.shell_context_processor({"app": app})
