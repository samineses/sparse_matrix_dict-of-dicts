from openpyxl import Workbook

wb = Workbook()

# ==========================================================
# --- Função para criar uma aba e preencher dados ----------
# ==========================================================
def criar_planilha(nome, header, rows):
    ws = wb.create_sheet(title=nome)
    ws.append(header)
    for row in rows:
        ws.append(row)

    # Ajuste de largura
    for col in ws.columns:
        length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in col)
        ws.column_dimensions[col[0].column_letter].width = length + 2



# ==========================================================
# --- 1. MATRIZES 10000 x 10000 ----------------------------
# ==========================================================

header_10k = [
    "Esparsidade\nMatrizes 10000x10000",
    "Inserção (ms)",
    "Acesso (ms)",
    "Transposição (ms)",
    "Multiplicação por Escalar (ms)",
    "Soma A+B (ms)",
    "Multiplicação A*B (ms)"
]

rows_10k = [
    ["0.01% e 0.001%", 1.216, 0.097, 0.428, 654.053, 554.765, 9110.217],
    ["0.01% e 0.0001%", "", "", "", "", 171.893, 1086.437],
    ["0.001% e 0.0001%", 0.621, 0.091, 0.474, 52.981, 25.935, 116.140],
    ["0.0001% e 0.0001%", 0.795, 0.155, 0.156, 8.528, "", ""]
]

criar_planilha("10000x10000", header_10k, rows_10k)



# ==========================================================
# --- 2. MATRIZES 100000 x 100000 --------------------------
# ==========================================================

header_100k = [
    "Esparsidade\nMatrizes 100000x100000",
    "Inserção (ms)",
    "Acesso (ms)",
    "Transposição (ms)",
    "Multiplicação por Escalar (ms)",
    "Soma A+B (ms)",
    "Multiplicação A*B (ms)"
]

rows_100k = [
    ["0.01% e 0.001%", 0.175, 1.211, 0.142, 6944.262, 2654.130, 113692.285],
    ["0.001% e 0.0001%", 0.158, 0.194, 0.122, 661.594, 1793.088, 20035.485],
    ["0.0001% e 0.0001%", 0.183, 0.544, 0.105, 79.400, 346.655, 1601.525]
]

criar_planilha("100000x100000", header_100k, rows_100k)



# ==========================================================
# --- 3. MATRIZES 1000000 x 1000000 ------------------------
# ==========================================================

header_1M = [
    "Esparsidade\nMatrizes 1000000x1000000",
    "Inserção (ms)",
    "Acesso (ms)",
    "Transposição (ms)",
    "Multiplicação por Escalar (ms)",
    "Soma A+B (ms)",
    "Multiplicação A*B (ms)"
]

rows_1M = [
    ["0.0001%",   1.232, 0.242, 0.086, "", "", ""],
    ["0.00001%",  0.361, 0.485, 0.076, "", "", ""],
    ["0.000001%", 0.093, 0.870, 0.052, "", "", ""]
]

criar_planilha("1000000x1000000", header_1M, rows_1M)



# ==========================================================
# --- Salvar arquivo ---------------------------------------
# ==========================================================
# Remove a planilha padrão criada automaticamente
del wb["Sheet"]

filename = "tabelas_esparsidade.xlsx"
wb.save(filename)
print(f"Arquivo gerado: {filename}")
