import pandas as pd

# com  valores ausentes
dados = {
    "Nome": ["Ana", "Bruno", None, "Daniel"],
    "Idade": [28, None, 32, 25],
    "Cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", None]
}
df = pd.DataFrame(dados)

print("DataFrame original com valores ausentes:")
print(df)

# removendo linhas ou colunas com valores ausentes
df_sem_na = df.dropna()
print("\nDataFrame após remover linhas com valores ausentes:")
print(df_sem_na)

# ou Substituindo valores ausentes por um valor específico.
df_preenchido = df.fillna({"Nome": "Desconhecido", "Idade": 0, "Cidade": "Desconhecida"})
print("\nDataFrame após preencher valores ausentes:")
print(df_preenchido)

# ou identificar e contar valores ausentes
print("\nValores ausentes em cada coluna:")
print(df.isna().sum())