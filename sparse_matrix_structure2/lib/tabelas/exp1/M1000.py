from openpyxl import Workbook

# Criação da planilha
wb = Workbook()
ws = wb.active
ws.title = "Matrizes 1000x1000"

# Cabeçalho
header = [
    "Esparsidade\nMatrizes 1000x1000",
    "Inserção (ms)",
    "Acesso (ms)",
    "Transposição (ms)",
    "Multiplicação por Escalar (ms)",
    "Soma A+B (ms)",
    "Multiplicação A*B (ms)"
]

ws.append(header)

# Dados da tabela
rows = [
    ["1% e 5%",      0.550, 1.244, 0.646, 5.413,    56.213,    219.536],
    ["1% e 10%",     "",    "",    "",    "",        91.629,    461.619],
    ["1% e 20%",     "",    "",    "",    "",       172.599,    891.033],
    ["5% e 10%",     0.162, 0.863, 0.331, 23.708,   106.054,   1939.901],
    ["5% e 20%",     "",    "",    "",    "",       180.597,   3326.672],
    ["10% e 20%",    0.149, 0.160, 0.114, 48.268,   159.780,    145.507],
    ["20%",          0.135, 0.182, 0.499, 99.807,   "",          ""     ]
]

# Escreve as linhas
for row in rows:
    ws.append(row)

# Ajuste opcional de largura das colunas
for col in ws.columns:
    length = max(len(str(cell.value)) for cell in col)
    ws.column_dimensions[col[0].column_letter].width = length + 2

# Salvar o arquivo
filename = "tabela_matrizes_1000x1000.xlsx"
wb.save(filename)

print(f"Arquivo gerado: {filename}")
