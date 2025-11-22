import matplotlib.pyplot as plt

# ==========================================================
# --- DADOS DAS TABELAS (SEM CSV) --------------------------
# ==========================================================

# ========= MATRIZES 10000 x 10000 =========
dens_10k = ["0.01% e 0.001%", "0.01% e 0.0001%", "0.001% e 0.0001%", "0.0001% e 0.0001%"]

insert_10k = [1.216, "", 0.621, 0.795]
access_10k = [0.097, "", 0.091, 0.155]
transp_10k = [0.428, "", 0.474, 0.156]
scalar_10k = [654.053, "", 52.981, 8.528]
soma_10k   = [554.765, 171.893, 25.935, ""]
mult_10k   = [9110.217, 1086.437, 116.140, ""]


# ========= MATRIZES 100000 x 100000 =========
dens_100k = ["0.01% e 0.001%", "0.001% e 0.0001%", "0.0001% e 0.0001%"]

insert_100k = [0.175, 0.158, 0.183]
access_100k = [1.211, 0.194, 0.544]
transp_100k = [0.142, 0.122, 0.105]
scalar_100k = [6944.262, 661.594, 79.400]
soma_100k   = [2654.130, 1793.088, 346.655]
mult_100k   = [113692.285, 20035.485, 1601.525]


# ========= MATRIZES 1.000.000 x 1.000.000 =========
dens_1M = ["0.0001%", "0.00001%", "0.000001%"]

insert_1M = [1.232, 0.361, 0.093]
access_1M = [0.242, 0.485, 0.870]
transp_1M = [0.086, 0.076, 0.052]
scalar_1M = ["", "", ""]
soma_1M   = ["", "", ""]
mult_1M   = ["", "", ""]


# ==========================================================
# --- Função de normalização para remover strings vazias ---
# ==========================================================
def norm(x):
    return [v if v != "" else None for v in x]


# ==========================================================
# --- Função para gerar gráficos ----------------------------
# ==========================================================
def plot_operacao(titulo, label_y, x1, y1, x2, y2, x3, y3, filename):

    plt.figure(figsize=(12, 6))
    plt.title(titulo)
    plt.xlabel("Esparsidade")
    plt.ylabel(label_y)

    # Série 10000x10000
    plt.plot(x1, norm(y1), marker="o", label="10000×10000")

    # Série 100000x100000
    plt.plot(x2, norm(y2), marker="o", label="100000×100000")

    # Série 1000000x1000000
    plt.plot(x3, norm(y3), marker="o", label="1000000×1000000")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()


# ==========================================================
# --- GERAR TODOS OS GRÁFICOS ------------------------------
# ==========================================================

plot_operacao("Inserção vs Esparsidade", "Tempo (ms)",
              dens_10k, insert_10k,
              dens_100k, insert_100k,
              dens_1M, insert_1M,
              "grafico_insercao.png")

plot_operacao("Acesso vs Esparsidade", "Tempo (ms)",
              dens_10k, access_10k,
              dens_100k, access_100k,
              dens_1M, access_1M,
              "grafico_acesso.png")

plot_operacao("Transposição vs Esparsidade", "Tempo (ms)",
              dens_10k, transp_10k,
              dens_100k, transp_100k,
              dens_1M, transp_1M,
              "grafico_transposicao.png")

plot_operacao("Multiplicação por Escalar vs Esparsidade", "Tempo (ms)",
              dens_10k, scalar_10k,
              dens_100k, scalar_100k,
              dens_1M, scalar_1M,
              "grafico_escalar.png")

plot_operacao("Soma A+B vs Esparsidade", "Tempo (ms)",
              dens_10k, soma_10k,
              dens_100k, soma_100k,
              dens_1M, soma_1M,
              "grafico_soma.png")

plot_operacao("Multiplicação A*B vs Esparsidade", "Tempo (ms)",
              dens_10k, mult_10k,
              dens_100k, mult_100k,
              dens_1M, mult_1M,
              "grafico_multiplicacao.png")

print("Gráficos gerados com sucesso!")
