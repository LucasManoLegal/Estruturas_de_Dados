# DADOS SEMI ESTRUTURADOS - CRIAÇÃO
# JSON

import pandas as pd

dados_json = {
    "Nome": ["Antonio", "Thomas", "Walter", "Vito"],
    "Idade": [32, 30, 50, 62],
    "Cidade": ["Cuba", "Birmingham", "Albuquerque", "Sicilia"]
}

# CRIAR DATAFRAME (LINHAS E COLUNAS)
df_json = pd.DataFrame(dados_json)

# SALVAR EM JSON

df_json.to_json("dadosSemi.json", orient="records")


