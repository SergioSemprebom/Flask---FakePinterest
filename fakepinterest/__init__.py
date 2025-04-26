from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os # Certifique-se que 'os' está importado

app = Flask(__name__)

# Carrega a URL do banco de dados do ambiente
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("Variável de ambiente DATABASE_URL não definida.")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Carrega a Chave Secreta do ambiente
secret_key = os.getenv("SECRET_KEY")
if not secret_key:
    raise ValueError("Variável de ambiente SECRET_KEY não definida.")
app.config["SECRET_KEY"] = secret_key

app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

# Importante: Faça o commit dessa alteração no seu repositório Git!
# git add fakepinterest/__init__.py
# git commit -m "Carrega SECRET_KEY a partir de variável de ambiente"
# git push

from fakepinterest import routes