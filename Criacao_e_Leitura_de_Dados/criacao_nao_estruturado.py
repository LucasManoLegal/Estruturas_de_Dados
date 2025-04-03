# DADOS NÃO ESTRUTURADOS - CRIAÇÃO
# CSV

import pandas as pd

dados_csv = {
    "Nome": ["Antonio", "Thomas", "Walter", "Vito"],
    "Idade": [32, 30, 50, 62],
    "Cidade": ["Cuba", "Birmingham", "Albuquerque", "Sicília"]
}

# CRIA O DATAFRAME
df_csv = pd.DataFrame(dados_csv)

# SALVA EM CSV

df_csv.to_csv("dadosNao.csv", index=False)
