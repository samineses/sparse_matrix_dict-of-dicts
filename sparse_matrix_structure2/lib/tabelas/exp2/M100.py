import pandas as pd

# dados fornecidos
densities = [0.01, 0.05, 0.10, 0.20]

insercao = {0.01: 0.011433, 0.05: 0.006233, 0.10: 0.006667, 0.20: 0.013033}
acesso = {0.01: 0.010367, 0.05: 0.002667, 0.10: 0.002967, 0.20: 0.002967}
transposicao = {0.01: 0.008867, 0.05: 0.001900, 0.10: 0.002167, 0.20: 0.002000}
smult = {0.01: 2.139800, 0.05: 5.334467, 0.10: 7.214567, 0.20: 12.042500}

soma = {
    (0.01, 0.05): 5.218567,
    (0.01, 0.10): 10.655900,
    (0.01, 0.20): 12.882933,
    (0.05, 0.10): 8.671167,
    (0.05, 0.20): 12.862200,
    (0.10, 0.20): 13.142200
}

mmult = {
    (0.01, 0.05): 6.228467,
    (0.01, 0.10): 9.340267,
    (0.01, 0.20): 14.392067,
    (0.05, 0.10): 32.018100,
    (0.05, 0.20): 54.393867,
    (0.10, 0.20): 85.593900
}

# montar linhas da tabela
rows = []
for (d1, d2), soma_val in soma.items():
    row = {
        "Esparsidade\nMatrizes 100X100": f"{int(d1*100)}% e ({int(d2*100)}%)",
        "Inserção (ms)": insercao[d1],
        "Acesso (ms)": acesso[d1],
        "Transposição (ms)": transposicao[d1],
        "Multiplicação\npor Escalar (ms)": smult[d1],
        "Soma A+B(ms)": soma_val,
        "Multiplicação\nA*B (ms)": mmult[(d1, d2)]
    }
    rows.append(row)

# adicionar linha só para a densidade 20% (última sem par)
row_last = {
    "Esparsidade\nMatrizes 100X100": "20%",
    "Inserção (ms)": insercao[0.20],
    "Acesso (ms)": acesso[0.20],
    "Transposição (ms)": transposicao[0.20],
    "Multiplicação\npor Escalar (ms)": smult[0.20],
    "Soma A+B(ms)": "",
    "Multiplicação\nA*B (ms)": ""
}
rows.append(row_last)

# criar DataFrame
df = pd.DataFrame(rows)

# salvar em Excel
df.to_excel("tabela_matrizes.xlsx", index=False)

print("Tabela gerada em 'tabela_matrizes.xlsx'")
