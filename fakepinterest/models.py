# cria a estrtura do banco de dados
from fakepinterest import database, login_manager # importa o banco de dados do arquivo fakepinterest
from datetime import datetime # importa o datetime para usar na data de criação das fotos
from flask_login import UserMixin # importa o UserMixin para usar na autenticação do usuário
from flask_login import UserMixin

@login_manager.user_loader # função que carrega o usuário
def load_usuario(id_usuario): # função para carregar o usuário pelo id
    return Usuario.query.get(int(id_usuario)) # retorna o usuário com o id passado como parâmetro

# cria a classe Usuario que herda de database.Model e UserMixin
# UserMixin é uma classe que fornece métodos e atributos para autenticação de usuários
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True) # cria a coluna id, do tipo inteiro, e define como chave primária
    username = database.Column(database.String, nullable=False) # cria a coluna username, do tipo string, e define como não nula
    email = database.Column(database.String, nullable=False, unique=True) # cria a coluna email, do tipo string, e define como não nula e única
    senha = database.Column(database.String, nullable=False) # cria a coluna senha, do tipo string, e define como não nula
    fotos = database.relationship("Foto", backref="usuario", lazy=True)
    
class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True) # cria a coluna id, do tipo inteiro, e define como chave primária
    imagem = database.Column(database.String, default="default.png") # cria a coluna imagem, do tipo string, e define como padrão "default.png"
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow) # cria a coluna data_criacao, do tipo datetime, e define como não nula e padrão como a data atual
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False) # cria a coluna id_usuario, do tipo inteiro, e define como chave estrangeira da tabela usuario, e define como não nula