import csv

with open("arquivos/numeros.csv", "w") as arquivo:
    escrita = csv.writer(arquivo)
    escrita.writerow(("abacaxi", "uva", "pera"))
    escrita.writerow((12, 47, 68))

with open('arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)