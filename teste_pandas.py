#Import do pandas para manipulação de dados
import pandas as pd

#Chamando o pandas para ler o arquivo a seguir
arquivo1 = "arquivos/salarios.csv"
leitura = pd.read_csv(arquivo1)
leitura.head()