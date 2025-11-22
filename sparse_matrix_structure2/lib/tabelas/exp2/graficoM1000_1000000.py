import matplotlib.pyplot as plt

# ---------------- DADOS EXTRAÍDOS DAS TABELAS ----------------

data = {
    "10000X10000": {
        "densities": [0.0001, 0.001, 0.01],   # convertidos para formato uniforme
        "insercao": {
            0.01: 1.216,
            0.001: 0.621,
            0.0001: 0.795
        },
        "acesso": {
            0.01: 0.097,
            0.001: 0.091,
            0.0001: 0.155
        },
        "transposicao": {
            0.01: 0.428,
            0.001: 0.474,
            0.0001: 0.156
        },
        "smult": {
            0.01: 654.053,
            0.001: 52.981,
            0.0001: 8.528
        },
        "soma": {
            # pares: Usamos a densidade da soma A+B correspondente à tabela
            (0.01, 0.001): 554.765,
            (0.01, 0.0001): 171.893,
            (0.001, 0.0001): 25.935
        },
        "mmult": {
            (0.01, 0.001): 9110.217,
            (0.01, 0.0001): 1086.437,
            (0.001, 0.0001): 116.140
        }
    },

    "100000X100000": {
        "densities": [0.0001, 0.001, 0.01],
        "insercao": {
            0.01: 0.175,
            0.001: 0.158,
            0.0001: 0.183
        },
        "acesso": {
            0.01: 1.211,
            0.001: 0.194,
            0.0001: 0.544
        },
        "transposicao": {
            0.01: 0.142,
            0.001: 0.122,
            0.0001: 0.105
        },
        "smult": {
            0.01: 6944.262,
            0.001: 661.594,
            0.0001: 79.400
        },
        "soma": {
            (0.01, 0.001): 2654.130,
            (0.01, 0.0001): 1793.088,
            (0.001, 0.0001): 346.655
        },
        "mmult": {
            (0.01, 0.001): 113692.285,
            (0.01, 0.0001): 20035.485,
            (0.001, 0.0001): 1601.525
        }
    },

    "1000000X1000000": {
        "densities": [0.000001, 0.00001, 0.0001],
        "insercao": {
            0.0001: 1.232,
            0.00001: 0.361,
            0.000001: 0.093
        },
        "acesso": {
            0.0001: 0.242,
            0.00001: 0.485,
            0.000001: 0.870
        },
        "transposicao": {
            0.0001: 0.086,
            0.00001: 0.076,
            0.000001: 0.052
        },
        "smult": {},   # tabela não forneceu estes tempos
        "soma": {},
        "mmult": {}
    }
}



# ---------------- CRIAR GRÁFICOS ----------------

for size_label, vals in data.items():

    densities = vals["densities"]
    insercao = vals["insercao"]
    acesso = vals["acesso"]
    transposicao = vals["transposicao"]
    smult = vals["smult"]
    soma = vals["soma"]
    mmult = vals["mmult"]

    plt.figure(figsize=(10,6))

    # ----- OPERACOES SIMPLES -----
    if insercao:
        plt.plot([d*100 for d in densities],
                 [insercao[d] for d in densities],
                 marker="o", label="Inserção")

    if acesso:
        plt.plot([d*100 for d in densities],
                 [acesso[d] for d in densities],
                 marker="o", label="Acesso")

    if transposicao:
        plt.plot([d*100 for d in densities],
                 [transposicao[d] for d in densities],
                 marker="o", label="Transposição")

    if smult:
        plt.plot([d*100 for d in densities],
                 [smult[d] for d in densities],
                 marker="o", label="Multiplicação por Escalar")

    # ----- OPERACOES DE PARES -----
    if soma:
        pair_x = [(a+b)/2 * 100 for (a,b) in soma.keys()]
        pair_soma_y = list(soma.values())
        plt.plot(pair_x, pair_soma_y,
                 marker="s", linestyle="--",
                 label="Soma A+B (pares)")

    if mmult:
        pair_x2 = [(a+b)/2 * 100 for (a,b) in mmult.keys()]
        pair_mmult_y = list(mmult.values())
        plt.plot(pair_x2, pair_mmult_y,
                 marker="s", linestyle="--",
                 label="Multiplicação A×B (pares)")

    # ----- FINALIZAÇÃO -----
    plt.xlabel("Densidade (%)")
    plt.ylabel("Tempo (ms)")
    plt.title(f"Comparação de Operações — Matriz {size_label}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    fname = f"operacoes_{size_label}.png"
    plt.savefig(fname, dpi=200)
    plt.close()

    print(f"Gráfico salvo: {fname}")
