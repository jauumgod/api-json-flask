from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os
import pymysql


pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config.from_object('config')

ma = Marshmallow(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


#PRECISA SER IMPORTADO AQUI DE FROM VIEWS E MODELS PARA EXECUTAR OS COMANDOS DE MIGRATIONS;

from .views import curso_views, formacao_views
from .models import curso_model, formacao_model
 