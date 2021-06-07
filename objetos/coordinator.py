from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class Coordinator():
    ''' Informar o número no endereço ajuda muito na precisão '''
    def __init__(self):
        self.geolocator = Nominatim(user_agent="Coordinator")
    
    def formatarEndereco( self, endereco ):
        endereco = endereco.lower()
        endereco = endereco.replace("r.","rua ")
        return endereco

    def retornarInformacaoEndereco( self, endereco ):
        endereco = self.formatarEndereco( endereco )
        localizacao = self.geolocator.geocode( endereco )
        if localizacao is None:
            print("Endereco ("+endereco+") nao encontrado para obter informacoes")
            return None

        print(localizacao.raw)
        return localizacao.raw
    
    def calcularCoordenadas( self, endereco ):
        endereco = self.formatarEndereco( endereco )
        localizacao = self.geolocator.geocode( endereco )
        if localizacao is None:
            print("Localizacao ("+endereco+") nao encontrada")
            return None

        return (localizacao.latitude, localizacao.longitude)

    def calcularDistancia( self, coordenas1, coordenadas2 ):
        distancia = geodesic(coordenas1, coordenadas2).m
        distancia = str( round( float( distancia), 2) )
        print("Distancia = "+distancia)
        return distancia

#c = Coordinator()
#Todas as palavras devem ser escritar sem abreviação
#c.calcularCoordenadas("kjsbad ,msdl,sjabhdl b") # Se não encontrar endereço
#c.calcularDistancia( (-4.9457, 37.9756), (-4.9230,-37.9794)) # Distancia entre coordenadas
#c.calcularDistancia( c.calcularCoordenadas("Rua José da Costa Celedonio 146, Russas"), c.calcularCoordenadas("Rua Felipe Santiago 411, Russas"))
#google => 2560 / geopy => 2378