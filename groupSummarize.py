# Calcular a média da idade para cada sexo
resumo = df.groupby('sexo')['idade'].mean()

print(resumo)
