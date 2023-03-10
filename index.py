from flask import Flask, jsonify, make_response, request
import mysql.connector

myDB = mysql.connector.connect(
  host='localhost',
  user='MainUser',
  password='MainPassword',
  database='livros'
)
app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False

@app.route('/livros',methods=['POST'])
def cadastrar_livro():
  novo_livro =request.get_json()

  my_cursor = myDB.cursor()
  sql = f"INSERT INTO livros(nome, lancamento) VALUES('{novo_livro['nome']}',{novo_livro['lancamento']})"
  my_cursor.execute(sql)

  return make_response(jsonify(
    mensagem = 'Livro cadastrado com sucesso!'
    )
  )

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro (id):

  my_cursor = myDB.cursor()
  my_cursor.execute('SELECT * FROM livros')
  meus_livros = my_cursor.fetchall()

  livros = list()
  for livro in meus_livros:
    livros.append({
      'id': livro[0],
      'nome': livro[1],
      'lancamento': livro[2]
    })

  for livro in livros:
    if livro.get('id') == id:
      return make_response(
        jsonify(
          mensage= 'O livro procurado localizado!',
          dados=livros
        )
      )

@app.route('/livros',methods=['GET'])
def obter_biblioteca():
  my_cursor = myDB.cursor()
  my_cursor.execute('SELECT * FROM livros')
  meus_livros = my_cursor.fetchall()
  return jsonify(meus_livros)


@app.route('/livros/<int:id>',methods =['PUT'])
def editar_livro (id):
  livro_alterado = request.get_json()

  my_cursor = myDB.cursor()
  my_cursor.execute('SELECT * FROM livros')
  livros = my_cursor.fetchall()
  for livro in livros:
    if livro.get('id') == id:

     sql = f"UPDATE INTO livros(nome, lancemento) VALUES('{livro_alterado.nome}', '{livro_alterado.lancamento}')"
     my_cursor.execute(sql)

    return make_response(jsonify(mensagem='Livro editado com sucesso!'))

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
  my_cursor=myDB.cursor()
  my_cursor.execute('SELECT * FROM livros')
  livros = my_cursor.fetchall()

  for livro in livros:
    if livro.get('id') == id:
      sql = f"DELETE * FROM livros WHERE (id) VALUES('{id}')"
      my_cursor.execute(sql)

      return make_response(jsonify(
        mensagem = 'Livro deletado com sucesso!'
      ))  


app.run(port=8000, host='localhost',debug=True)