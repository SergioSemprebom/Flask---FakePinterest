# criar os formularios no nosso site
from flask_wtf import FlaskForm # importa o FlaskForm para criar os formulários
from wtforms import StringField, PasswordField, SubmitField # importa os campos que vamos usar nos formulários
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError  # importa os validadores que vamos usar nos formulários
from fakepinterest.models import Usuario # importa o modelo Usuario para validar o email e o username


# cria o formulário de login com os campos email, senha e botão de confirmação
class FormLogin(FlaskForm):
    email=StringField("E-mail", validators=[DataRequired(), Email()])
    senha=PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao=SubmitField("Fazer login")
    

class FormCriarConta(FlaskForm):
    email=StringField("E-mail", validators=[DataRequired(), Email()])
    username=StringField("Nome de usuário", validators=[DataRequired()])
    senha=PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=20)])
    confirmacao_senha=PasswordField("Confirmação de senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao=SubmitField("Criar conta")

    def validate_email(self, email):
        usuario=Usuario.query.filter_by(email=email.data).first() # verifica se o email já existe no banco de dados
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar" ) # se o email já existe, lança um erro de validação com a mensagem "E-mail já cadastrado, faça login para continuar"