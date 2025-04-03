# DADOS ESTRUTURADOS - CRIAÇÃO
# EXCEL
# COMANDOS UTILIZADOS
# - pip install pandas
# - pip install openpyxl

import pandas as pd

# ESTRUTURA DE DICIONÁRIO
dados_planilha1 = {
    "Nome": ["Antonio", "Thomas", "Walter", "Vito"],
    "Idade": [32, 30, 50, 62],
    "Cidade": ["Cuba", "Birmingham", "Albuquerque", "Sicília"]
}

dados_planilha2 = {
    "Nome": ["A", "T", "W", "V"],
    "Idade": [32, 30, 50, 62],
    "Cidade": ["C", "B", "A", "S"]
}

df_planilha1 = pd.DataFrame(dados_planilha1)

df_planilha2 = pd.DataFrame(dados_planilha2)

# SALVAR NO EXCEL
with pd.ExcelWriter(r'dadosEstruturados.xlsx') as writer:
    df_planilha1.to_excel(writer, sheet_name="Tabela1", index=False)
    print('Arquivo salvo com sucesso')
    df_planilha2.to_excel(writer, sheet_name="Tabela2", index=False)
    print('Arquivo salvo com sucesso')
