from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
    'id': 1,
    'nome': 'Harry Potter',
    'lancamento': 2001
  },
  {
    'id': 2,
    'nome': 'Diário de um banana',
    'lancamento': 2012
  },
  {
    'id':3,
    'nome': 'Aloha',
    'lancamento': 2021
  },
   {
    'id':4,
    'nome': 'Gente Grande',
    'lancamento': 2009
  }
]

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro (id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)

@app.route('/livros',methods=['GET'])
def obter_biblioteca():
  return jsonify(livros)


@app.route('/livros/<int:id>',methods =['PUT'])
def editar_livro (id):
  livro_alterado = request.get_json()
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])
def cadastrar_livro():
  novo_livro =request.get_json()
  livros.append(novo_livro)

  return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]

  
  return jsonify(livros)


app.run(port=8000, host='localhost',debug=True)