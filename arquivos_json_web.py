from urllib.request import urlopen
import json

arquivo = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")
leitura = json.loads(arquivo)[0]

print ('Título: ', leitura['title'])
print ('URL: ', leitura['url'])
print ('Duração: ', leitura['duration'])
print ('Número de Visualizações: ', leitura['stats_number_of_plays'])



