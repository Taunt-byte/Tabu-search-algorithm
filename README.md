# Tabu search algorithm

## 🔎 O que é o **Tabu Search**?

O **Tabu Search (Busca Tabu)** é um **metaheurístico** usado para resolver problemas de otimização complexos, onde não é fácil (ou é impossível) encontrar a solução ótima exata em pouco tempo.

A ideia é:

* Começar com uma solução inicial qualquer.
* Procurar por **vizinhos** dessa solução (pequenas mudanças).
* Escolher o melhor vizinho **mesmo que ele não seja melhor que o atual** (isso ajuda a escapar de mínimos locais).
* Usar uma **lista tabu** (memória) para guardar os movimentos ou soluções recentes, evitando voltar sempre para os mesmos lugares (ficar preso em ciclos).
* Depois de várias iterações, chega-se a uma solução muito boa (não garantidamente a ótima, mas próxima).

---

## ⚙️ Exemplo simples (Problema do Caixeiro Viajante - TSP)

Imagine um vendedor que precisa visitar 5 cidades e voltar à cidade inicial.
Objetivo: encontrar a ordem que **minimiza a distância total**.

### Como o Tabu Search ajudaria:

1. **Solução inicial**: começa com uma rota qualquer, ex: `A → B → C → D → E → A`.
2. **Vizinhança**: troca duas cidades de lugar, por exemplo: `A → C → B → D → E → A`.
3. **Avaliação**: calcula a distância total da nova rota.
4. **Lista Tabu**: se já testou essa troca recentemente, não deixa repetir (tabu).
5. **Melhor vizinho permitido**: escolhe o vizinho que dá a menor distância sem quebrar a regra do tabu.
6. Repete o processo até atingir o **número de iterações** ou **critério de parada**.


Esse código roda o Tabu Search para um **TSP com 4 cidades**.
Ele faz trocas de cidades, evita repetições com a **lista tabu**, e tenta achar uma rota curta.

