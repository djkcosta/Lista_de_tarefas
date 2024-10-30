from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_wtf import CSRFProtect

import os

load_dotenv('.env')

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrigido o erro de digitação
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Inicializa extensões
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

# Importa rotas e modelos
from app import controller
from app import models
