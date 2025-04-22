# criação do app
from flask import Flask # importa o Flask e o render_template do flask 
from flask_sqlalchemy import SQLAlchemy # importa o SQLAlchemy do flask_sqlalchemy
from flask_login import LoginManager # importa o LoginManager do flask_login
from flask_bcrypt import Bcrypt # importa o Bcrypt do flask_bcrypt
      


app = Flask(__name__) # cria uma instância do Flask, __name__ é o nome do módulo atual
# o Flask vai saber onde estão os arquivos estáticos, templates e etc.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' # configura o banco de dados, nesse caso, um sqlite
app.config["SECRET_KEY"] = '245aec28c2caa1919373ab04652ad471' # chave secreta para proteger as sessões do Flask
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts' # pasta onde as fotos serão salvas

database = SQLAlchemy(app) # cria uma instância do SQLAlchemy, passando o app como parâmetro
bcrypt = Bcrypt(app) # cria uma instância do Bcrypt, passando o app como parâmetro
login_manager = LoginManager(app) # cria uma instância do LoginManager, passando o app como parâmetro
login_manager.login_view = "homepage" # define a view de login, que será a homepage


from fakepinterest import routes # importa as rotas do arquivo routes.py