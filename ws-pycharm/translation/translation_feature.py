import pandas as pd
import os

def criar_translation_feature(arquivo_xls, pasta_saida):
    # Lendo o arquivo Excel, especificando apenas a coluna desejada (por exemplo, coluna 'A')
    df = pd.read_excel(arquivo_xls)

    # Criando o conteúdo do arquivo translation.feature usando somente a coluna 'A'
    conteudo = ""
    coluna = df.columns[0]  # Obtém o nome da primeira coluna

    # Adiciona o nome da coluna apenas na primeira linha
    conteudo += f"{coluna}"
    for valor in df['Feature ']:
        conteudo += f"{valor}\n\n"  # Adiciona duas quebras de linha (\n\n) para criar uma linha em branco

    # Escrevendo no arquivo translation.feature na pasta de saída
    with open(os.path.join(pasta_saida, 'translation.feature'), 'w') as file:
        file.write(conteudo)

# Substitua 'meuarquivo.xlsx' pelo caminho do seu arquivo .xlsx e 'pasta_saida' pela pasta de saída desejada
arquivo_xls = 'meuarquivo.xlsx'
pasta_saida = 'pasta_saida'

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

criar_translation_feature(arquivo_xls, pasta_saida)
