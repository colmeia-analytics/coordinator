from flask import Flask, request, render_template, Response
from flask import send_file, redirect, send_from_directory
from requests.models import cookiejar_from_dict
from objetos.coordinator import Coordinator

app = Flask(__name__, template_folder='htmls', static_folder="htmls/static/")

coordinator = Coordinator()

@app.route('/')
@app.route('/home')
def retornaTesteHtml():
    return '''Servidor De Coordenadas Está Executando\n
               \n
               Rotas: /distancia/endereco1/endereco2    => Distancia de em metros\n
                      /informacao/endereco                => Informações disponiveis do endereço\n
                '''

@app.route('/distancia/<endereco1>/<endereco2>')
def retornarDistancia(endereco1, endereco2):
    cord1 = coordinator.calcularCoordenadas( endereco1 )
    cord2 = coordinator.calcularCoordenadas( endereco2 )
    if cord1 == None:
        return "Endereço 1 não encontrado"

    if cord2 == None:
        return "Endereço 2 não encontrado"

    return str( coordinator.calcularDistancia( cord1, cord2 ) )

@app.route('/informacao/<endereco>')
def retornarInformacao(endereco):
    return Response(str( {'endereco':'hendrickélindo'}), content_type='application/json')
    #return Response(str( coordinator.retornarInformacaoEndereco( endereco )), content_type='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='7373')
