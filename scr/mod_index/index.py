#IMPORTAÇÕES
# ------------------------------------------------------------------------------------------------
from flask import Blueprint, render_template
from mod_login.login import validaSessao
# ------------------------------------------------------------------------------------------------


# blueprint index
# ------------------------------------------------------------------------------------------------
bp_index = Blueprint('index', __name__, url_prefix="/home", 
template_folder='templates')
# ------------------------------------------------------------------------------------------------



# ROTA DE INDEX
# ------------------------------------------------------------------------------------------------
@bp_index.route('/')
@validaSessao
def formIndex():
    return render_template('formIndex.html'), 200
# ------------------------------------------------------------------------------------------------