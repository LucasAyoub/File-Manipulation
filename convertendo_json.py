import json
dict = {"nome": "Tony Montana",
        "idade": "80",
        "linguagem": "Python"}

for x,y in dict.items():
    print(x,y)

print(json.dumps(dict))
