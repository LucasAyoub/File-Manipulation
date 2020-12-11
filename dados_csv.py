#Importando o csv
import csv

#Abrindo o arquivo com with para escrita
with open("arquivos/numeros.csv", "w") as arquivo:
    escrita = csv.writer(arquivo)
    escrita.writerow(("abacaxi", "uva", "pera"))
    escrita.writerow((12, 47, 68))

#Para evitar linhas em branco, usamos o encoding para leitura e depois imprimimos também o número de colunas
with open('arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)
