from flask import Flask
from geek_space.conf.config import ProductionConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(ProductionConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from geek_space import routes
