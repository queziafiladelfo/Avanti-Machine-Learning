import pandas as pd

df = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "Idade": [28, 22, 32, 25],
    "Cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", "Curitiba"]
})

# selecionar a coluna 'Idade'
coluna_idade = df["Idade"]
print("Coluna Idade:")
print(coluna_idade)

# filtra as linhas onde a Cidade é 'São Paulo'
filtro_sp = df[df["Cidade"] == "São Paulo"]
print("\nLinhas onde Cidade é São Paulo:")
print(filtro_sp)
