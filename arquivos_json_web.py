#Importação
from urllib.request import urlopen
import json

#Foi colocado a URL do arquivo que desejamos usar
arquivo = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")
leitura = json.loads(arquivo)[0]

#De acordo com o arquivo colocamos as palavras chaves para obter os dados do mesmo
print ('Título: ', leitura['title'])
print ('URL: ', leitura['url'])
print ('Duração: ', leitura['duration'])
print ('Número de Visualizações: ', leitura['stats_number_of_plays'])

