import pandas as pd


def listar_colunas(arquivo_xls):
    df = pd.read_excel(arquivo_xls)
    print(df.columns)


# Substitua 'meuarquivo.xlsx' pelo caminho do seu arquivo .xlsx
arquivo_xls = 'meuarquivo.xlsx'
listar_colunas(arquivo_xls)
