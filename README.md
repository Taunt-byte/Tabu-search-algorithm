# 🧠 Tabu Search Visualizado – Problema do Caixeiro Viajante (TSP)

Projeto em Python que implementa o algoritmo de otimização **Tabu Search**, aplicado ao clássico **Problema do Caixeiro Viajante (TSP)**, com foco em **visualização dinâmica da busca em tempo real**.

📺 Demonstração do projeto rodando:
https://youtu.be/zMOBDpqVJt4

---

## 🚀 Objetivo do projeto

O objetivo deste projeto é entender na prática como funciona um **algoritmo metaheurístico de busca**, visualizando:

- A evolução das soluções ao longo das iterações
- O comportamento da exploração do espaço de busca
- O impacto da lista tabu na prevenção de ciclos
- A melhoria progressiva da solução encontrada

---

## 🧠 O que é o Tabu Search?

O **Tabu Search (Busca Tabu)** é uma técnica de otimização baseada em busca local com memória.

Diferente de métodos simples de melhoria local, ele evita ficar preso em ótimos locais usando uma estrutura chamada **lista tabu**, que impede revisitar soluções recentes.

### 🔁 Funcionamento básico:

- Parte de uma solução inicial
- Gera vizinhos por pequenas modificações (swap de cidades)
- Seleciona o melhor vizinho possível
- Usa uma lista tabu para evitar ciclos
- Repete até atingir o número de iterações

---

## ⚙️ Aplicação no Problema do Caixeiro Viajante (TSP)

O problema consiste em encontrar a menor rota possível que visite todas as cidades exatamente uma vez e retorne ao ponto inicial.

### 📍 Passos do algoritmo:

1. Gera uma solução inicial aleatória
2. Produz vizinhos trocando posições entre cidades
3. Calcula o custo total da rota (distância percorrida)
4. Aplica restrição da lista tabu
5. Escolhe a melhor solução disponível
6. Atualiza a melhor solução global encontrada
7. Repete o processo

---

## 🎨 Diferencial do projeto

Este projeto não apenas implementa o algoritmo, mas também inclui **visualização interativa da busca**:

- 🔴 Rota atual sendo explorada
- 🟢 Melhor solução encontrada até o momento
- 📊 Evolução da otimização em tempo real
- 🧠 Representação clara do comportamento da busca tabu

---

## 🛠 Tecnologias utilizadas

- Python 🐍
- Matplotlib 📊
- Algoritmos de Otimização (Metaheurísticas)
- Tabu Search

---

## 📚 Conceitos aplicados

- Otimização combinatória
- Busca local
- Metaheurísticas
- Problema do Caixeiro Viajante (TSP)
- Estruturas de memória (lista tabu)
- Visualização de algoritmos

---

## 🎯 Aprendizados

Este projeto ajudou a entender:

- Como algoritmos de busca exploram espaços de solução
- Como evitar mínimos locais usando memória (tabu)
- A importância da visualização para compreensão de algoritmos
- Como transformar um algoritmo teórico em uma simulação observável

---

## 📌 Observação

Este projeto tem caráter educacional, com foco em aprendizado de algoritmos de otimização e visualização de processos computacionais.

---

## 📺 Demonstração

👉 https://youtu.be/zMOBDpqVJt4