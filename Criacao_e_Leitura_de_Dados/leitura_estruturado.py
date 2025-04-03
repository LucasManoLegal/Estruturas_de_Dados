# LEITURA DADOS ESTRUTURADOS

import pandas as pd

df_excel = pd.read_excel("dadosEstruturados.xlsx", sheet_name="Tabela1")

print(df_excel)