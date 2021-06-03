from flask import Flask, request, render_template
from flask import send_file, redirect, send_from_directory
from requests.models import cookiejar_from_dict
from objetos.coordinator import Coordinator

app = Flask(__name__, template_folder='htmls', static_folder="htmls/static/")

coordinator = Coordinator()

@app.route('/')
@app.route('/home')
def retornaTesteHtml():
    return "Servidor De Coordenadas Está Executando"

@app.route('/distancia/<endereco1>/<endereco2>')
def retornarDistancia(endereco1, endereco2):
    cord1 = coordinator.calcularCoordenadas( endereco1 )
    cord2 = coordinator.calcularCoordenadas( endereco2 )

    return str( coordinator.calcularDistancia( cord1, cord2 ) )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='7373')