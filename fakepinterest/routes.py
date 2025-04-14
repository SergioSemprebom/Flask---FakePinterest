#crias as rotas da aplicação
from flask import Flask, render_template, url_for, redirect # importa o Flask, render_template, url_for e redirect do flask
from fakepinterest import app # importa o app do arquivo fakepinterest.py
from fakepinterest.models import Usuario, Foto # importa o modelo Usuario do arquivo models.py
from flask_login import login_required, login_user, logout_user, current_user # importa o login_required do flask_login
from fakepinterest.forms import FormLogin, FormCriarConta# importa os formulários do arquivo forms.py
from fakepinterest import database, bcrypt # importa o banco de dados e o bcrypt do arquivo fakepinterest.py


#cria as rotas da aplicação
@app.route('/', methods=["GET", "POST"]) # rota padrão
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit(): # verifica se o formulário foi enviado e se é válido
        usuario = Usuario.query.filter_by(email=form_login.email.data).first() # busca o usuário no banco de dados pelo email
        if usuario and bcrypt.check_password_hash(usuario.senha,form_login.senha.data): # verifica se o usuário existe e se a senha está correta
            login_user(usuario, remember=True) # faz o login do usuário
            return redirect(url_for("perfil", id_usuario=usuario.id)) # redireciona para a página do perfil do usuário
    return render_template("homepage.html", form=form_login) # renderiza o template homepage.html

@app.route("/criarconta", methods=["GET", "POST"])  # rota para criar conta
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit(): # verifica se o formulário foi enviado e se é válido, se ususer clicou no botao 
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data) # gera o hash da senha
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha, # senha criptografada
                          email=form_criarconta.email.data) # cria um novo usuário com os dados do formulário  
        database.session.add(usuario) # adiciona o usuário ao banco de dados
        database.session.commit() # salva as alterações no banco de dados
        login_user(usuario, remember=True) # login o usuário
        return redirect(url_for("perfil", id_usuario=usuario.id)) # redireciona para a página do perfil do usuário)) # redireciona para a página principal
    return render_template("criarconta.html", form=form_criarconta) # renderiza o template criarconta.html
    


@app.route("/perfil/<id_usuario>") # rota para o perfil
@login_required # verifica se o usuário está logado, se não estiver logado, redireciona para a página de login  
def perfil(id_usuario):
     # busca o usuário no banco de dados pelo id
    if int(id_usuario) == int(current_user.id): # verifica se o usuário é o mesmo que está logado
        # o usuario está venfondo o perfil dele mesmo
        return render_template("perfil.html", usuario=current_user) # renderiza o template perfil.html
           # se o usuário não existe
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return redirect("perfil.html", usuario=usuario) # redireciona para a página do perfil do usuário
    

@app.route("/logout") # rota para fazer logout
@login_required
def logout():
    logout_user() # faz o logout do usuário
    return redirect(url_for("homepage")) # redireciona para a página de login



