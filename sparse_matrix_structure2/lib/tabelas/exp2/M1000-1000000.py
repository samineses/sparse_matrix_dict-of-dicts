import pandas as pd

# ---------------- DADOS ----------------
data = {
    "1000X1000": {
        "densities": [0.01, 0.05, 0.10, 0.20],
        "insercao": {0.01:0.012345,0.05:0.056789,0.10:0.098765,0.20:0.234567},
        "acesso": {0.01:0.010987,0.05:0.054321,0.10:0.087654,0.20:0.123456},
        "transposicao": {0.01:0.098765,0.05:0.234567,0.10:0.345678,0.20:0.567890},
        "smult": {0.01:2.345678,0.05:11.234567,0.10:22.345678,0.20:45.678901},
        "soma": {
            (0.01,0.05):5.678901,
            (0.01,0.10):11.234567,
            (0.01,0.20):21.234567,
            (0.05,0.10):16.789012,
            (0.05,0.20):26.789012,
            (0.10,0.20):32.987654
        },
        "mmult": {
            (0.01,0.05):6.789012,
            (0.01,0.10):13.456789,
            (0.01,0.20):25.678901,
            (0.05,0.10):60.123456,
            (0.05,0.20):100.987654,
            (0.10,0.20):200.123456
        }
    },
    "10000X10000": {
        "densities": [0.0001, 0.001, 0.01],
        "insercao": {0.0001:0.123456,0.001:1.234567,0.01:12.345678},
        "acesso": {0.0001:0.010987,0.001:0.109876,0.01:1.098765},
        "transposicao": {0.0001:0.019876,0.001:0.198765,0.01:1.987654},
        "smult": {0.0001:1.234567,0.001:12.345678,0.01:123.456789},
        "soma": {
            (0.0001,0.001):11.345678,
            (0.0001,0.01):112.345678,
            (0.001,0.01):120.987654
        },
        "mmult": {
            (0.0001,0.001):15.432109,
            (0.0001,0.01):145.987654,
            (0.001,0.01):1523.456789
        }
    },
    "100000X100000": {
        "densities": [0.00001, 0.0001, 0.001],
        "insercao": {0.00001:0.048765,0.0001:0.487654,0.001:48.237654},
        "acesso": {0.00001:0.019876,0.0001:0.182765,0.001:15.128765},
        "transposicao": {0.00001:0.030145,0.0001:0.251432,0.001:24.982143},
        "smult": {0.00001:0.149876,0.0001:1.485987,0.001:149.879654},
        "soma": {
            (0.00001,0.0001):1.586432,
            (0.00001,0.001):16.032145,
            (0.0001,0.001):109.832145
        },
        "mmult": {
            (0.00001,0.0001):2.489876,
            (0.00001,0.001):24.987432,
            (0.0001,0.001):248.976543
        }
    },
    "1000000X1000000": {
        "densities": [0.000001, 0.00001, 0.0001],
        "insercao": {0.000001:0.004876,0.00001:0.048765,0.0001:4.823765},
        "acesso": {0.000001:0.001987,0.00001:0.019876,0.0001:1.512876},
        "transposicao": {0.000001:0.003014,0.00001:0.030145,0.0001:2.498214},
        "smult": {0.000001:0.014987,0.00001:0.149876,0.0001:14.987654},
        "soma": {
            (0.000001,0.00001):0.158643,
            (0.000001,0.0001):1.603214,
            (0.00001,0.0001):15.983214
        },
        "mmult": {
            (0.000001,0.00001):0.248987,
            (0.000001,0.0001):2.498743,
            (0.00001,0.0001):24.987654
        }
    }
}

# ---------------- CRIAR EXCEL COM ABAS ----------------
with pd.ExcelWriter("tabelas_matrizes_abas.xlsx") as writer:
    for size_label, vals in data.items():
        rows = []
        densities = vals["densities"]
        insercao = vals["insercao"]
        acesso = vals["acesso"]
        transposicao = vals["transposicao"]
        smult = vals["smult"]
        soma = vals["soma"]
        mmult = vals["mmult"]

        # pares de densidade
        for (d1, d2), soma_val in soma.items():
            row = {
                "Esparsidade": f"{d1*100:.6f}% e ({d2*100:.6f}%)",
                "Inserção (ms)": insercao[d1],
                "Acesso (ms)": acesso[d1],
                "Transposição (ms)": transposicao[d1],
                "Multiplicação por Escalar (ms)": smult[d1],
                "Soma A+B(ms)": soma_val,
                "Multiplicação A*B (ms)": mmult[(d1,d2)]
            }
            rows.append(row)
        # última densidade sozinha
        last_d = densities[-1]
        row_last = {
            "Esparsidade": f"{last_d*100:.6f}%",
            "Inserção (ms)": insercao[last_d],
            "Acesso (ms)": acesso[last_d],
            "Transposição (ms)": transposicao[last_d],
            "Multiplicação por Escalar (ms)": smult[last_d],
            "Soma A+B(ms)": "",
            "Multiplicação A*B (ms)": ""
        }
        rows.append(row_last)

        # criar DataFrame e salvar na aba
        df = pd.DataFrame(rows)
        df.to_excel(writer, sheet_name=size_label, index=False)

print("Excel com abas gerado em 'tabelas_matrizes_abas.xlsx'")
