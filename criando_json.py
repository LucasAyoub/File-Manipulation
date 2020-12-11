#Importando json
import json

#Criando um dicionario
dict = {"nome": "Tony Montana",
        "idade": "80",
        "linguagem": "Python"}

#Abrimos um arquivo criado no programa e convertemos o conteudo para json
with open("arquivos/produtos.json", "w") as arquivo:
    arquivo.write(json.dumps(dict))

#Abrimos o arquivo para leitura após converter ele para json
with open("arquivos/produtos.json", "r") as arquivo:
    leitura = arquivo.read()
    data = json.loads(leitura)
    print(leitura)

#Imprimindo uma informação específica
print(data["linguagem"])
