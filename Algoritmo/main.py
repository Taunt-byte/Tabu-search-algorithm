import random

# Função de custo: soma das distâncias
def custo(solucao, distancias):
    total = 0
    for i in range(len(solucao) - 1):
        total += distancias[solucao[i]][solucao[i+1]]
    total += distancias[solucao[-1]][solucao[0]]  # voltar ao início
    return total

# Tabu Search
def tabu_search(distancias, n_iter=50, tamanho_tabu=5):
    n = len(distancias)
    solucao = list(range(n))   # solução inicial [0,1,2,3,...]
    melhor = solucao[:]
    melhor_custo = custo(solucao, distancias)
    lista_tabu = []
    
    for _ in range(n_iter):
        vizinhos = []
        for i in range(n):
            for j in range(i+1, n):
                vizinho = solucao[:]
                vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
                if vizinho not in lista_tabu:
                    vizinhos.append(vizinho)
        
        # escolhe melhor vizinho
        vizinho = min(vizinhos, key=lambda s: custo(s, distancias))
        c = custo(vizinho, distancias)
        
        # atualiza tabu
        lista_tabu.append(vizinho)
        if len(lista_tabu) > tamanho_tabu:
            lista_tabu.pop(0)
        
        # move para vizinho
        solucao = vizinho
        
        # guarda melhor solução
        if c < melhor_custo:
            melhor, melhor_custo = vizinho, c
    
    return melhor, melhor_custo


# Exemplo de distâncias (matriz simétrica)
distancias = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

rota, distancia_min = tabu_search(distancias)
print("Melhor rota:", rota)
print("Distância mínima encontrada:", distancia_min)
