# experimento2_safe_v4.py
from lib.sparse_matrix2 import SparseMatrix
import time
import sys
import tkinter as tk
from tkinter import scrolledtext
import math
import itertools

# --------- CONFIGURAÇÃO DE SEGURANÇA ---------
MAX_NNZ_PER_MATRIX = 2_000_000
MMULT_OPS_THRESHOLD = 1e8
REPETITIONS = 3
VALID_SIZES = [100, 1000, 10000, 100000, 1000000]

def ask_size():
    print("Tamanhos válidos:", VALID_SIZES)
    try:
        n = int(input("Digite o tamanho da matriz (ex: 100): ").strip())
    except:
        print("Entrada inválida.")
        sys.exit(1)
    if n not in VALID_SIZES:
        print("Tamanho inválido. Encerrando.")
        sys.exit(1)
    return n

def choose_sparsities(n):
    if n <= 1000:
        return [0.01, 0.05, 0.10, 0.20]
    if n == 10000:
        return [0.0001, 0.001, 0.01]
    if n == 100000:
        return [0.00001, 0.0001, 0.001]
    if n == 1000000:
        return [0.000001, 0.00001, 0.0001]
    return [0.0001]

def estimate_k(n, density):
    return int(n * n * density)

def capped_nnz(n, density):
    k = estimate_k(n, density)
    return min(k, MAX_NNZ_PER_MATRIX)

def estimate_mmult_cost(n, density_A, density_B):
    return (n ** 3) * (density_A * density_B)

def gen_random_sparse_matrix(n, density, cap_nnz):
    mat = SparseMatrix(n, n)
    target = min(int(n * n * density), cap_nnz)
    if target <= 0:
        return mat
    import random
    inserted = 0
    seen = set()
    while inserted < target:
        i = random.randrange(n)
        j = random.randrange(n)
        if (i, j) in seen:
            continue
        seen.add((i, j))
        val = random.uniform(1.0, 10.0)
        mat.insert(i, j, val)
        inserted += 1
    return mat

def time_fn(fn):
    start = time.perf_counter()
    fn()
    end = time.perf_counter()
    return (end - start) * 1000.0

def run_for_size(n):
    sparsities = choose_sparsities(n)
    results = {}
    print(f"Executando para N={n}, densidades={sparsities}, cap_nnz={MAX_NNZ_PER_MATRIX}")

    # gerar matrizes
    mats = {}
    for d in sparsities:
        cap = capped_nnz(n, d)
        mats[d] = gen_random_sparse_matrix(n, d, cap)

    # medir operações básicas
    for d, M in mats.items():
        res = {"insercao": None, "acesso": None, "transposicao": None, "smult": None}
        res["insercao"] = sum(time_fn(lambda: M.insert(0, 0, 1.0)) for _ in range(REPETITIONS)) / REPETITIONS
        res["acesso"] = sum(time_fn(lambda: M.access(0, 0)) for _ in range(REPETITIONS)) / REPETITIONS
        res["transposicao"] = sum(time_fn(lambda: M.transpose()) for _ in range(REPETITIONS)) / REPETITIONS
        res["smult"] = sum(time_fn(lambda: 2 * M) for _ in range(REPETITIONS)) / REPETITIONS
        results[d] = res

    # soma e multiplicação entre diferentes densidades
    results['soma'] = {}
    results['mmult_diff'] = {}
    for d1, d2 in itertools.combinations(sparsities, 2):
        M1 = mats[d1]
        M2 = mats[d2]
        results['soma'][(d1, d2)] = sum(time_fn(lambda: M1 + M2) for _ in range(REPETITIONS)) / REPETITIONS
        est_cost = estimate_mmult_cost(n, d1, d2)
        if est_cost > MMULT_OPS_THRESHOLD or estimate_k(n, d1) > MAX_NNZ_PER_MATRIX or estimate_k(n, d2) > MAX_NNZ_PER_MATRIX:
            results['mmult_diff'][(d1, d2)] = None
        else:
            results['mmult_diff'][(d1, d2)] = sum(time_fn(lambda: M1 * M2) for _ in range(REPETITIONS)) / REPETITIONS

    return results

def montar_texto_global(n, results):
    txt = f"RESULTADOS PARA MATRIZ {n} x {n}\n\n"

    # ---------------- Inserção ----------------
    txt += "Inserção (ms):\n"
    for d, r in results.items():
        if d in ['soma', 'mmult_diff']:
            continue
        txt += f"  Densidade {d*100:.6g}%: {r['insercao']:.6f}\n"
    txt += "\n"

    # ---------------- Acesso ----------------
    txt += "Acesso (ms):\n"
    for d, r in results.items():
        if d in ['soma', 'mmult_diff']:
            continue
        txt += f"  Densidade {d*100:.6g}%: {r['acesso']:.6f}\n"
    txt += "\n"

    # ---------------- Transposição ----------------
    txt += "Transposição (ms):\n"
    for d, r in results.items():
        if d in ['soma', 'mmult_diff']:
            continue
        txt += f"  Densidade {d*100:.6g}%: {r['transposicao']:.6f}\n"
    txt += "\n"

    # ---------------- Multiplicação escalar ----------------
    txt += "Multiplicação escalar (ms):\n"
    for d, r in results.items():
        if d in ['soma', 'mmult_diff']:
            continue
        txt += f"  Densidade {d*100:.6g}%: {r['smult']:.6f}\n"
    txt += "\n"

    # ---------------- Soma de Matrizes ----------------
    if 'soma' in results:
        txt += "Soma de Matrizes (ms):\n"
        for (d1, d2), val in results['soma'].items():
            txt += f"  Soma densidades {d1*100:.6g}% + {d2*100:.6g}%: {val:.6f} ms\n"
        txt += "\n"

    # ---------------- Multiplicação A*B entre densidades diferentes ----------------
    if 'mmult_diff' in results:
        txt += "Multiplicação A*B entre diferentes densidades (ms):\n"
        for (d1, d2), val in results['mmult_diff'].items():
            if val is None:
                txt += f"  Multiplicação {d1*100:.6g}% * {d2*100:.6g}%: NÃO EXECUTADA (estimativa alta)\n"
            else:
                txt += f"  Multiplicação {d1*100:.6g}% * {d2*100:.6g}%: {val:.6f} ms\n"
        txt += "\n"

    return txt

def abrir_janela_resultados(texto):
    janela = tk.Tk()
    janela.title("Resultados dos Experimentos (SAFE)")
    area = scrolledtext.ScrolledText(janela, width=100, height=40, font=("Consolas", 11))
    area.pack(padx=10, pady=10)
    area.insert(tk.END, texto)
    area.configure(state='disabled')
    janela.mainloop()

def main():
    n = ask_size()
    results = run_for_size(n)
    texto = montar_texto_global(n, results)
    print(texto)
    abrir_janela_resultados(texto)

if __name__ == "__main__":
    main()
