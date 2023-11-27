#IMPORTAÇÕES
#------------------------------------------------------------------------------------------------
import os
from flask import Flask, session
from datetime import timedelta
from settings import HOST, PORT, DEBUG, TEMPO_SESSION
from flask import Flask, render_template
#------------------------------------------------------------------------------------------------


# import blueprint criado
#------------------------------------------------------------------------------------------------
from mod_funcionario.funcionario import bp_funcionario
from mod_index.index import bp_index
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_erro.erro import bp_erro
from mod_login.login import bp_login
#------------------------------------------------------------------------------------------------



# criação do aplicativo WEB Flask
#------------------------------------------------------------------------------------------------
app = Flask(__name__)
#------------------------------------------------------------------------------------------------



# Gerando uma chave randômica para secret_key
#------------------------------------------------------------------------------------------------
app.secret_key = os.urandom(12).hex()
#------------------------------------------------------------------------------------------------



# configurações do aplicativo WEB Flask
#------------------------------------------------------------------------------------------------
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE='True'
)
#------------------------------------------------------------------------------------------------



# método para renovar o tempo da sessão
#------------------------------------------------------------------------------------------------
@app.before_request
def before_request():
    session.permanent = True
    session['tempo'] = int(TEMPO_SESSION)
    # o padrão é 31 dias...
    app.permanent_session_lifetime = timedelta(minutes=session['tempo'])
#------------------------------------------------------------------------------------------------



# registro das rotas do blueprint
#------------------------------------------------------------------------------------------------
app.register_blueprint(bp_login)
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_index)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_erro)
#------------------------------------------------------------------------------------------------



# Configurações de Host, Porta e Debug
#------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host='0.0.0.0', port=5000, debug=True)
#------------------------------------------------------------------------------------------------
