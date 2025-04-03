# LEITURA DADOS SEMI ESTRUTURADOS

import pandas as pd

df_json = pd.read_json("dadosSemi.json")

print(df_json)