# IMPORTAÇÕES   
# ------------------------------------------------------------------------------------------------
import requests
from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
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
        # dados enviados via FORM
        cpf = request.form['usuario']
        senha = request.form['senha']
        # monta o JSON para envio a API
        payload = {'id_funcionario': 0, 'nome': '', 'matricula': '', 'cpf': cpf, 'telefone': '', 'grupo': 0, 'senha': senha}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_LOGIN, headers=HEADERS_API, json=payload)
        result = response.json()
        print(cpf,senha)
        # verifica se o retorno da API foi OK   
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
                  
        # limpa a sessão atual e registra usuário na sessão, armazenando o login do usuário
        session.clear()
        session['nome'] = result[0]['nome']
        session['login'] = result[0]['cpf']
        session['grupo'] = result[0]['grupo']
        # abre a aplicação na tela home
        return redirect(url_for('index.formIndex'))
    except Exception as e:
        # retorna para a tela de login
        return redirect(url_for('login.login', msgErro="Falha de Login! Verifique seus dados e tente novamente!", msgException=e.args[0]))

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