from flask import Flask, request, jsonify, session
from flask_cors import CORS
from database import (
    init_db, get_users, add_user, delete_user, update_user, check_login,
    add_produto, get_produtos, update_produto, delete_produto
)


app = Flask(__name__)
app.secret_key = 'segredo123'
CORS(app, supports_credentials=True)

init_db()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if check_login(data['email'], data['senha']):
        session['email'] = data['email']
        return jsonify({'success': True})
    return jsonify({'success': False}), 401

@app.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/usuarios', methods=['GET', 'POST', 'PUT', 'DELETE'])
def usuarios():
    if 'email' not in session:
        return jsonify({'error': 'Não autorizado'}), 401

    if request.method == 'GET':
        return jsonify(get_users())
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify(add_user(data['nome'], data['email'], data['senha']))
    elif request.method == 'PUT':
        data = request.get_json()
        return jsonify(update_user(data['id'], data['nome'], data['email'], data['senha']))
    elif request.method == 'DELETE':
        data = request.get_json()
        return jsonify(delete_user(data['id']))

# NOVA ROTA - Produtos
@app.route('/produtos', methods=['GET', 'POST', 'PUT', 'DELETE'])
def produtos():
    if 'email' not in session:
        return jsonify({'error': 'Não autorizado'}), 401

    if request.method == 'GET':
        return jsonify(get_produtos())

    elif request.method == 'POST':
        data = request.get_json()
        return jsonify(add_produto(data['nome'], data['preco']))

    elif request.method == 'PUT':
        data = request.get_json()
        return jsonify(update_produto(data['id'], data['nome'], data['preco']))

    elif request.method == 'DELETE':
        data = request.get_json()
        return jsonify(delete_produto(data['id']))

if __name__ == '__main__':
    app.run(debug=True)
