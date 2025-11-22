import matplotlib.pyplot as plt

labels = ["1% e 5%", "1% e 10%", "1% e 20%", "5% e 10%", "5% e 20%", "10% e 20%", "20%"]

insercao = [0.1476, None, None, 0.1501, None, 0.1099, 0.2808]
acesso =   [0.2394, None, None, 1.4808, None, 0.2332, 0.0859]
transp =   [1.7136, None, None, 0.1116, None, 0.0954, 0.0884]
smult =    [1.7454, None, None, 0.4550, None, 0.9240, 1.6595]
soma =     [67.331, 100.137, 170.745, 74.475, 111.616, 183.950, None]
mmult =    [279.648, 423.005, 865.275, 1663.829, 3216.605, 147.520, None]

# Remove valores None (matplotlib ignora automaticamente)
plt.plot(labels, insercao, marker='o', label="Inserção (ms)")
plt.plot(labels, acesso, marker='o', label="Acesso (ms)")
plt.plot(labels, transp, marker='o', label="Transposição (ms)")
plt.plot(labels, smult, marker='o', label="Mult. Escalar (ms)")
plt.plot(labels, soma, marker='o', label="Soma A+B (ms)")
plt.plot(labels, mmult, marker='o', label="Mult. A*B (ms)")

plt.xlabel("Par de Esparsidades")
plt.ylabel("Tempo (ms)")
plt.title("Tempos por Operação – Matrizes 100×100")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)

plt.show()
