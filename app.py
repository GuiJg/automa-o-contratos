from flask import Flask, render_template, request, jsonify
from docx import Document
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_contract', methods=['POST'])
def generate_contract():
    data = request.json

    # Lógica para gerar o contrato usando os dados recebidos
    nome = data.get('name')
    # Adicione lógica para outros campos conforme necessário

    # Código para gerar o contrato (semelhante ao que você já tem)

    # Retorne uma resposta para o cliente (por exemplo, um link para download)
    response = {'download_link': 'http://example.com/contrato.docx'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
