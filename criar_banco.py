from fakepinterest import database, app #importa o app do arquivo fakepinterest
from fakepinterest.models import Usuario, Foto #importa os modelos do banco de dados do arquivo models

with app.app_context(): # cria um contexto de aplicação, para poder usar o banco de dados
    database.create_all() # cria todas as tabelas do banco de dados
    print("Banco de dados criado com sucesso!") # imprime uma mensagem de sucesso


