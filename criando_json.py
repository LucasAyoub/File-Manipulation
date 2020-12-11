import json
dict = {"nome": "Tony Montana",
        "idade": "80",
        "linguagem": "Python"}

with open("arquivos/produtos.json", "w") as arquivo:
    arquivo.write(json.dumps(dict))

with open("arquivos/produtos.json", "r") as arquivo:
    leitura = arquivo.read()
    data = json.loads(leitura)
    print(leitura)

print(data["linguagem"])
