#IMPORTAÇÕES
#------------------------------------------------------------------------------------------------
import requests
from settings import HEADERS_API, ENDPOINT_FUNCIONARIO
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from funcoes import Funcoes
from mod_login.login import validaSessao


bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')
#------------------------------------------------------------------------------------------------


# ROTAS DOS FORMULÁRIOS
#------------------------------------------------------------------------------------------------

# ROTA DE LISTAGEM DE FUNCIONÁRIOS
#------------------------------------------------------------------------------------------------
@bp_funcionario.route('/', methods=['GET', 'POST'])
@validaSessao
def formListaFuncionario():
    try:
        response = requests.get(ENDPOINT_FUNCIONARIO, headers=HEADERS_API)
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result[0])
        return render_template('formListaFuncionario.html', result=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
#------------------------------------------------------------------------------------------------



# ROTA DE CADASTRO DE FUNCIONÁRIOS
#------------------------------------------------------------------------------------------------
@bp_funcionario.route('/form-Funcionario/', methods=['POST'])
@validaSessao
def formFuncionario():
    return render_template('formFuncionario.html')
#------------------------------------------------------------------------------------------------



# ROTA DE INSERÇÃO DE FUNCIONÁRIOS
#------------------------------------------------------------------------------------------------
@bp_funcionario.route('/insert', methods=['POST'])
@validaSessao
def insert():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])

        # monta o JSON para envio a API
        payload = {
                    'id_funcionario': id_funcionario, 
                    'nome': nome, 
                    'matricula': matricula, 
                    'cpf': cpf,
                    'telefone': telefone,
                    'grupo': grupo,
                    'senha': senha
                   }
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_FUNCIONARIO, headers=HEADERS_API, json=payload)
        result = response.json()

        print(result) # [{'msg': 'Cadastrado com sucesso!', 'id': 13}, 200]
        print(response.status_code) # 200

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        
        #return render_template('formListaFuncionario.html', msg=result[0])
        return redirect(url_for('funcionario.formListaFuncionario', msg=result[0]))
    
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
#------------------------------------------------------------------------------------------------



# ROTA DE EDIÇÃO DE FUNCIONÁRIOS
#------------------------------------------------------------------------------------------------
@bp_funcionario.route("/form-edit-funcionario", methods=['POST'])
@validaSessao
def formEditFuncionario():
    try:
		# ID enviado via FORM
        id_funcionario = request.form['id']
		# executa o verbo GET da API buscando somente o funcionário 	selecionado,
		# obtendo o JSON do retorno
        response = requests.get(ENDPOINT_FUNCIONARIO + id_funcionario,headers=HEADERS_API)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
		# renderiza o form passando os dados retornados
        return render_template('formFuncionario.html', result=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])

@bp_funcionario.route('/edit', methods=['POST'])
@validaSessao
def edit():
	try:
		# dados enviados via FORM
		id_funcionario = request.form['id']
		nome = request.form['nome']
		matricula = request.form['matricula']
		cpf = request.form['cpf']
		telefone = request.form['telefone']
		grupo = request.form['grupo']
		senha = Funcoes.cifraSenha(request.form['senha'])
		# monta o JSON para envio a API
		payload = {'id_funcionario': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone': telefone, 'grupo': grupo, 'senha': senha}

		# executa o verbo PUT da API e armazena seu retorno
		response = requests.put(ENDPOINT_FUNCIONARIO + id_funcionario, headers=HEADERS_API, json=payload)
		result = response.json()
		if (response.status_code != 200 or result[1] != 201):
			raise Exception(result[0])
		return redirect( url_for('funcionario.formListaFuncionario', msg=result[0]) )
	except Exception as e:
		return render_template('formListaFuncionario.html', msgErro=e.args[0])
#------------------------------------------------------------------------------------------------



#ROTA DE EXCLUÇÃO DE FUNCIONÁRIOS
#------------------------------------------------------------------------------------------------
@bp_funcionario.route('/delete', methods=['POST'])
@validaSessao
def delete():
	try:
		# dados enviados via FORM
		id_funcionario = request.form['id_funcionario']
          
		# executa o verbo DELETE da API e armazena seu retorno
		response = requests.delete(ENDPOINT_FUNCIONARIO  + id_funcionario, headers=HEADERS_API)
		result = response.json()
        
		if (response.status_code != 200 or result[1] != 201):
			raise Exception(result[0])
		#{'msg': 'Excluído com sucesso!', 'id': 4}
		return jsonify(erro=False, msg=result[0])
     
	except Exception as e:
		#return render_template('formListaFuncionario.html', msgErro=e.args[0])
		return jsonify(erro=True, msgErro=e.args[0])
#------------------------------------------------------------------------------------------------