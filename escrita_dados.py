#Localizando o arquivo e abrindo para escrita
teste = open("arquivos/dados2.txt", "w")
teste.write("Testando a escrita de arquivos em Python \n")
teste.close()

#Caso precise adicionar alguma informação adicional, abrimos novamente para append
teste = open("arquivos/dados2.txt", "a")
teste.write("Adicionando mais uma anotação para o arquivo")
teste.close()

#Lendo o arquivo
teste = open("arquivos/dados2.txt", "r")
print(teste.read())


