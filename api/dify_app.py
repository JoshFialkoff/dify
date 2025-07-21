import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:edcRfv$$5@docker_db_1:5432/dify'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models *after* app is created to avoid circular imports
with app.app_context():
    from models import *
