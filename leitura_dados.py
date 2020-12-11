#Mostrando o caminho do arquivo para a leitura
teste = open("arquivos/dados.txt", "r")
print(teste.read())

#Caso queira saber quantos caracteres o arquivo possui
print(teste.tell())

#Retornar para o começo do arquivo
print(teste.seek(0,0))

#Lendo um número de caracteres específico
print(teste.read(10))