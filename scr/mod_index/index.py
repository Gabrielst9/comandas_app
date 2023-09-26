from flask import Blueprint, render_template
bp_index = Blueprint('index', __name__, url_prefix="/index", template_folder='templates')

''' rotas dos formulários '''
@bp_index.route('/')
def formListaIndex():
    return render_template('formListaIndex.html'), 200

'''
Rota antiga de app...
@app.route('/')
def formListaIndex():
    # return "<h1>Rota da página Inicial da nossa WEB APP</h1>", 200
    return render_template('formListaIndex.html'), 200
'''