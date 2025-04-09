from flask import Flask, render_template, request, redirect, url_for
from bigquery import BigQuery
import datetime

app = Flask(__name__)
bq = BigQuery()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inserir", methods=["POST"])
def inserir():
    nome = request.form["nome"]
    raca = request.form["raca"]
    idade = int(request.form["idade"])
    tutor = request.form["tutor"]
    resultado, query = bq.insert_cachorro(nome, raca, idade, tutor)
    return {"mensagem": "Inserido com sucesso!", "query": query}

@app.route("/atualizar", methods=["POST"])
def atualizar():
    nome = request.form["nome"]
    nova_idade = int(request.form["nova_idade"])
    resultado, query = bq.update_cachorro(nome, nova_idade)
    return {"mensagem": "Atualizado com sucesso!", "query": query}

@app.route("/deletar", methods=["POST"])
def deletar():
    nome = request.form["nome"]
    resultado, query = bq.delete_cachorro(nome)
    return {"mensagem": "Deletado com sucesso!", "query": query}

if __name__ == "__main__":
    app.run(debug=True)

