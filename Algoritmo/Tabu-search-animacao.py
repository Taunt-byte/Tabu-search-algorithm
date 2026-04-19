import random
import matplotlib.pyplot as plt

# -------------------------
# custo da rota
# -------------------------
def custo(solucao, distancias):
    total = 0
    for i in range(len(solucao) - 1):
        total += distancias[solucao[i]][solucao[i+1]]
    total += distancias[solucao[-1]][solucao[0]]
    return total


# -------------------------
# desenho com mais significado
# -------------------------
def desenhar_rota(solucao, melhor_solucao, pos, ax, titulo, info_extra=""):
    ax.clear()

    # nós
    for i, (x, y) in enumerate(pos):
        ax.scatter(x, y, s=200, color="gray")
        ax.text(x, y + 0.05, str(i), ha='center')

    # rota atual (vermelho)
    for i in range(len(solucao)):
        a = solucao[i]
        b = solucao[(i + 1) % len(solucao)]
        ax.plot(
            [pos[a][0], pos[b][0]],
            [pos[a][1], pos[b][1]],
            color="red"
        )

    # melhor rota (verde pontilhada)
    for i in range(len(melhor_solucao)):
        a = melhor_solucao[i]
        b = melhor_solucao[(i + 1) % len(melhor_solucao)]
        ax.plot(
            [pos[a][0], pos[b][0]],
            [pos[a][1], pos[b][1]],
            color="green",
            linestyle="dashed",
            alpha=0.6
        )

    ax.set_title(titulo)
    ax.set_xticks([])
    ax.set_yticks([])

    # texto explicativo dentro do gráfico
    ax.text(
        0.02, 0.95,
        info_extra,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top'
    )


# -------------------------
# Tabu Search animado com narrativa
# -------------------------
def tabu_search(distancias, pos, n_iter=50, tamanho_tabu=5):
    n = len(distancias)
    solucao = list(range(n))
    melhor = solucao[:]
    melhor_custo = custo(solucao, distancias)
    lista_tabu = []

    plt.ion()
    fig, ax = plt.subplots()

    for it in range(n_iter):

        vizinhos = []

        for i in range(n):
            for j in range(i+1, n):
                vizinho = solucao[:]
                vizinho[i], vizinho[j] = vizinho[j], vizinho[i]

                if vizinho not in lista_tabu:
                    vizinhos.append(vizinho)

        vizinho = min(vizinhos, key=lambda s: custo(s, distancias))
        c = custo(vizinho, distancias)

        lista_tabu.append(vizinho)
        if len(lista_tabu) > tamanho_tabu:
            lista_tabu.pop(0)

        solucao = vizinho

        if c < melhor_custo:
            melhor, melhor_custo = vizinho, c
            evento = "🔵 Nova melhor solução encontrada"
        else:
            evento = "🟡 Explorando vizinhança"

        info = (
            f"Iteração: {it+1}\n"
            f"Custo atual: {c}\n"
            f"Melhor custo: {melhor_custo}\n"
            f"Tamanho tabu: {len(lista_tabu)}\n\n"
            f"{evento}"
        )

        desenhar_rota(
            solucao,
            melhor,
            pos,
            ax,
            "Tabu Search em execução",
            info
        )

        plt.pause(0.5)

    plt.ioff()

    desenhar_rota(
        melhor,
        melhor,
        pos,
        ax,
        "FINAL - Melhor solução encontrada",
        f"Custo final: {melhor_custo}"
    )

    plt.show()

    return melhor, melhor_custo


# -------------------------
# dados
# -------------------------
distancias = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

pos = [
    (0, 0),
    (1, 2),
    (2, 0),
    (1, -1)
]

rota, distancia_min = tabu_search(distancias, pos)

print("Melhor rota:", rota)
print("Distância mínima:", distancia_min)