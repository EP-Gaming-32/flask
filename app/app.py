from flask import Flask, render_template, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

#controle dinamico de erros
@app.errorhandler(HTTPException)

def handle_http_exception(e):
    #armazena o codigo, nome e descricao do erro no dict
    error_data = {
        'code': e.code,
        'name': e.name,
        'description': e.description
    }
    #renderiza o template dinamico e passa os dados descompactados para facil utilização no template
    return render_template('error.html', **error_data), e.code

#rota de teste dinamica
@app.route("/test/error/<code>")

def test_error(code):
    try:
        #converte <code> passado no url de string para int
        status_code = int(code)
        #lista de status validos
        valid_codes = [400, 401, 403, 404, 405, 408, 429, 500, 502, 503, 504]
        # checa se o codigo testado consta na lista
        if status_code not in valid_codes:#caso não conste
            return jsonify({'erro': f'Código de status {status_code} não suportado'}), 400
        abort(status_code)# caso conste na lista, força o status de erro
    except ValueError: 
        # caso tenha erro na conversão de str -> int
        return jsonify({'erro': 'Código de status inválido, deve ser um número'}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
#pode ser usado em crud para performar operacoes com base em id
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)