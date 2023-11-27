# IMPORTAÇÕES   
# ------------------------------------------------------------------------------------------------
import requests
from flask import Blueprint, redirect, render_template, request, url_for, session
from settings import ENDPOINT_LOGIN, HEADERS_API
from funcoes import Funcoes
from functools import wraps
# ------------------------------------------------------------------------------------------------



#BLUEPRINT LOGIN
# ------------------------------------------------------------------------------------------------
bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')
# ------------------------------------------------------------------------------------------------



#ROTAS
# ------------------------------------------------------------------------------------------------

#ROTA DE LOGIN
# ------------------------------------------------------------------------------------------------
@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")
# ------------------------------------------------------------------------------------------------



#ROTA DE VALIDAÇÃO DE LOGIN
# ------------------------------------------------------------------------------------------------
@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        cpf = request.form['usuario']
        senha = Funcoes.cifraSenha(request.form['senha'])

        # limpa a sessão
        session.clear()
    
        if (cpf == "abc" and senha == Funcoes.cifraSenha('Bolinhas')):
            # registra usuário na sessão, armazenando o login do usuário
            session['login'] = cpf

            # abre a aplicação na tela home
            return redirect(url_for('index.formIndex'))
        else:
            raise Exception("Falha de Login! Verifique seus dados e tente novamente!")

    except Exception as e:
        # retorna para a tela de login
        return redirect(url_for('login.login', msgErro=e.args[0]))
# ------------------------------------------------------------------------------------------------



#ROTA DE LOGOFF
# ------------------------------------------------------------------------------------------------
@bp_login.route("/logoff", methods=['GET'])
def logoff():

    # limpa um valor individual da sessão
    session.pop('login', None)

    # limpa a sessão
    session.clear()
    
    # retorna para a tela de login    
    return redirect(url_for('login.login'))
# ------------------------------------------------------------------------------------------------



# VALIDAÇÃO DE SESSÃO
# ------------------------------------------------------------------------------------------------
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:
            # descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login', msgErro='Usuário não logado!'))
        else:
            # retorna os dados copiados da função original
            return f(*args, **kwargs)
    # retorna o resultado do if acima
    return decorated_function
# ------------------------------------------------------------------------------------------------



# VALIDAÇÃO DE GRUPO
# ------------------------------------------------------------------------------------------------
def guardaDadosSessao(result):
    session['login'] = result[0].get('cpf')
    session['nome'] = result[0].get('nome')
    session['grupo'] = result[0].get('grupo')
# ------------------------------------------------------------------------------------------------