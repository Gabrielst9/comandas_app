from flask import Blueprint, render_template
bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''
@bp_produto.route('/produto/')
def formListaProduto():
    return render_template('formListaProduto.html'), 200

@bp_produto.route('/form-Produto/', methods=['POST'])
def formProduto():
    return render_template('formProduto.html')

'''
Rota antiga de app...
@app.route('/')
def formListaProduto():
    # return "<h1>Rota da página Inicial da nossa WEB APP</h1>", 200
    return render_template('formListaProduto.html'), 200
'''