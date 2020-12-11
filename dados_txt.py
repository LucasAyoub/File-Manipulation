#Importando o os
import os

#Criando o texto
texto = "Criando texto em Python "
texto = texto + "e ainda adicionando conteúdo "
texto += "ao texto"
print(texto)

#Mostrando o caminho do arquivo para escrita
arquivo = open(os.path.join("arquivos/criacao.txt"), "w")
for palavra in texto:
    arquivo.write(palavra + " ")
arquivo.close()

#Mostrando o caminho do arquivo para leitura
arquivo = open("arquivos/criacao.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
