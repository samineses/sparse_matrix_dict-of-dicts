import csv

filename = "tabela_matrizes_100x100.csv"

header = [
    "Esparsidade\nMatrizes 100X100",
    "Inserção (ms)",
    "Acesso (ms)",
    "Transposição (ms)",
    "Multiplicação\npor Escalar (ms)",
    "Soma A+B(ms)",
    "Multiplicação\nA*B (ms)"
]

# Função para converter float para string com vírgula
def f2s(v):
    if v == '':
        return ''
    return f"{v:.4f}".replace('.', ',')

rows = [
    ["1% e 5%", f2s(0.1476), f2s(0.2394), f2s(1.7136), f2s(1.7454), f2s(67.331), f2s(279.648)],
    ["1% e 10%", '', '', '', '', f2s(100.137), f2s(423.005)],
    ["1% e 20%", '', '', '', '', f2s(170.745), f2s(865.275)],
    ["5% e 10%", f2s(0.1501), f2s(1.4808), f2s(0.1116), f2s(0.4550), f2s(74.475), f2s(1663.829)],
    ["5% e 20%", '', '', '', '', f2s(111.616), f2s(3216.605)],
    ["10% e 20%", f2s(0.1099), f2s(0.2332), f2s(0.0954), f2s(0.9240), f2s(183.950), f2s(147.520)],
    ["20%", f2s(0.2808), f2s(0.0859), f2s(0.0884), f2s(1.6595), '', '']
]

with open(filename, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)

print(f"Tabela gerada em '{filename}' com vírgulas como separador decimal para Excel brasileiro.")
