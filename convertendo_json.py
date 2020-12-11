#Importamos json
import json

#Criando um dicionario
dict = {"nome": "Tony Montana",
        "idade": "80",
        "linguagem": "Python"}

#Printando os itens na tela e depois convertendo para json
for x,y in dict.items():
    print(x,y)

print(json.dumps(dict))

