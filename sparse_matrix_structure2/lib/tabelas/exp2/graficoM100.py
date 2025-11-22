import matplotlib.pyplot as plt

# ===========================
# Dados fornecidos
# ===========================

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

# ===========================
# Preparação para plotar tudo em um só gráfico
# ===========================

plt.figure(figsize=(10,6))

# ---- Operações simples (densidade única) ----
plt.plot(
    [d*100 for d in insercao.keys()],
    insercao.values(),
    marker="o",
    label="Inserção"
)

plt.plot(
    [d*100 for d in acesso.keys()],
    acesso.values(),
    marker="o",
    label="Acesso"
)

plt.plot(
    [d*100 for d in transposicao.keys()],
    transposicao.values(),
    marker="o",
    label="Transposição"
)

plt.plot(
    [d*100 for d in smult.keys()],
    smult.values(),
    marker="o",
    label="Multiplicação por Escalar"
)

# ---- Operações de pares (usar densidade média para plot) ----
pair_x = [(a+b)/2 * 100 for (a,b) in soma.keys()]
pair_soma_y = list(soma.values())
pair_mmult_y = list(mmult.values())

plt.plot(
    pair_x,
    pair_soma_y,
    marker="s",
    linestyle="--",
    label="Soma A+B (pares)"
)

plt.plot(
    pair_x,
    pair_mmult_y,
    marker="s",
    linestyle="--",
    label="Multiplicação A×B (pares)"
)
3
# ===========================
# Finalização
# ===========================

plt.xlabel("Densidade (%)")
plt.ylabel("Tempo (ms)")
plt.title("Comparação de Todas as Operações em Função da Densidade")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("todas_operacoes_juntas.png", dpi=200)
plt.close()

print("Gráfico salvo como 'todas_operacoes_juntas.png'")
