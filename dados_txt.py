#importando o os
import os
texto = "Criando texto em Python "
texto = texto + "e ainda adicionando conteúdo "
texto += "ao texto"
print(texto)

arquivo = open(os.path.join("arquivos/criacao.txt"), "w")
for palavra in texto:
    arquivo.write(palavra + " ")
arquivo.close()

arquivo = open("arquivos/criacao.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
