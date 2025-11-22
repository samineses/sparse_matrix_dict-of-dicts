import matplotlib.pyplot as plt

# ---------------------- DADOS ----------------------
data = {
    "densities_simple": [0.20],  # densidades com apenas uma matriz
    "densities_pairs": [
        (0.01, 0.05),
        (0.01, 0.10),
        (0.01, 0.20),
        (0.05, 0.10),
        (0.05, 0.20),
        (0.10, 0.20)
    ],
    
    # operações simples (valem para 1% e 20%)
    "insercao": {0.20: 0.135},
    "acesso": {0.20: 0.182},
    "transposicao": {0.20: 0.499},
    "smult": {0.20: 99.807},

    # pares
    "soma": {
        (0.01,0.05): 56.213,
        (0.01,0.10): 91.629,
        (0.01,0.20): 172.599,
        (0.05,0.10): 106.054,
        (0.05,0.20): 180.597,
        (0.10,0.20): 159.780
    },

    "mmult": {
        (0.01,0.05): 219.536,
        (0.01,0.10): 461.619,
        (0.01,0.20): 891.033,
        (0.05,0.10): 1_939.901,
        (0.05,0.20): 3_326.672,
        (0.10,0.20): 145.507
    }
}

# ---------------------- PLOT ----------------------

plt.figure(figsize=(10,6))

# ----- operações simples -----
dens_simple = [d*100 for d in data["densities_simple"]]

plt.plot(
    dens_simple,
    [data["insercao"][d] for d in data["densities_simple"]],
    marker="o",
    label="Inserção"
)
plt.plot(
    dens_simple,
    [data["acesso"][d] for d in data["densities_simple"]],
    marker="o",
    label="Acesso"
)
plt.plot(
    dens_simple,
    [data["transposicao"][d] for d in data["densities_simple"]],
    marker="o",
    label="Transposição"
)
plt.plot(
    dens_simple,
    [data["smult"][d] for d in data["densities_simple"]],
    marker="o",
    label="Multiplicação por Escalar"
)

# ----- operações com pares -----
pair_x = [((a+b)/2)*100 for (a,b) in data["densities_pairs"]]

plt.plot(
    pair_x,
    list(data["soma"].values()),
    marker="s",
    linestyle="--",
    label="Soma A+B"
)

plt.plot(
    pair_x,
    list(data["mmult"].values()),
    marker="s",
    linestyle="--",
    label="Multiplicação A×B"
)

# ----- finalização -----
plt.xlabel("Densidade média (%)")
plt.ylabel("Tempo (ms)")
plt.title("Operações em Matrizes Esparsas — 1000×1000")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("operacoes_1000x1000.png", dpi=200)
plt.show()

print("Gráfico salvo: operacoes_1000x1000.png")
