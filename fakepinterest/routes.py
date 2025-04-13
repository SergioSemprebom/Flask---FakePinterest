#crias as rotas da aplicação
from flask import Flask, render_template, url_for, redirect # importa o Flask, render_template, url_for e redirect do flask
from fakepinterest import app # importa o app do arquivo fakepinterest.py
from fakepinterest.models import Usuario, Foto # importa o modelo Usuario do arquivo models.py
from flask_login import login_required, login_user, logout_user # importa o login_required do flask_login
from fakepinterest.forms import FormLogin, FormCriarConta# importa os formulários do arquivo forms.py


#cria as rotas da aplicação
@app.route('/', methods=["GET", "POST"]) # rota padrão
def homepage():
    formlogin = FormLogin()
    if form_login.validade_on_submit(): # verifica se o formulário foi enviado e se é válido
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first() # busca o usuário no banco de dados pelo email
        if usuario: # se o usuário existir
            bcrypt.check_password_hash(Usuario.senha,form_login.senha.data) # verifica se a senha está correta
            
    return render_template("homepage.html", form=formlogin) # renderiza o template homepage.html

@app.route("/criarconta", methods=["GET", "POST"])  # rota para criar conta
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit(): # verifica se o formulário foi enviado e se é válido, se ususer clicou no botao 
        senha = brcypt.generate_password_hash(form_criarconta.senha.data) # gera o hash da senha

        usuario = usuario(username=form_criarconta.username.data,
                          senha=senha, # senha criptografada
                          email=form_criarconta.email.data) # cria um novo usuário com os dados do formulário  
        database.session.add(usuario) # adiciona o usuário ao banco de dados
        database.session.commit() # salva as alterações no banco de dados
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", usuario=form_criarconta.username)) # redireciona para a página do perfil do usuário)) # redireciona para a página principal
    return render_template("criarconta.html", form=form_criarconta) # renderiza o template criarconta.html
    


@app.route("/perfil/<usuario>") # rota para o perfil
@login_required # verifica se o usuário está logado, se não estiver logado, redireciona para a página de login  
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario) # renderiza o template perfil.html