from flask import Blueprint, render_template
bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''
@bp_cliente.route('/cliente/')
def formListaCliente():
    return render_template('formListaCliente.html'), 200

'''
Rota antiga de app...
@app.route('/')
def formListaCliente():
    # return "<h1>Rota da página Inicial da nossa WEB APP</h1>", 200
    return render_template('formListaCliente.html'), 200
'''