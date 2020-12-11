#Pedimos para a pessoa criar o nome do arquivo
fileName = input("Digite o nome do arquivo: ")
fileName = fileName + ".txt"

#Abrimos o arquivo para escrita
arquivo = open(fileName, "w")
arquivo.write("Criando texto no arquivo criado")
arquivo.close()

#Abrimos o arquivo para leitura
arquivo = open(fileName, "r")
print(arquivo.read())
arquivo.close()