import random
import time
from collections import defaultdict
import matplotlib.pyplot as plt

class GrafoEuleriano:
    def __init__(self, n):
        self.n = n
        self.grafo = defaultdict(list)
        self.arestas = []

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
        self.arestas.append((u, v))

    def gerar_grafo_euleriano(self, arestas_extras=0):
        # ciclo base
        for i in range(self.n):
            self.adicionar_aresta(i, (i+1) % self.n)

        # arestas extras em pares
        for _ in range(arestas_extras):
            u = random.randint(0, self.n-1)
            v = random.randint(0, self.n-1)
            if u != v:
                self.adicionar_aresta(u, v)
                self.adicionar_aresta(u, v)

    def ciclo_euleriano(self):
        grafo_temp = {u: self.grafo[u][:] for u in self.grafo}
        pilha = [0]
        caminho = []

        while pilha:
            v = pilha[-1]
            if grafo_temp[v]:
                u = grafo_temp[v].pop()
                grafo_temp[u].remove(v)
                pilha.append(u)
            else:
                caminho.append(pilha.pop())

        return caminho[::-1]


# 🔬 Experimento de Escalabilidade
valores_N = [100, 500, 1000, 5000, 10000]
tempos = []

print("\n=== Resultados Experimentais ===")
print(f"{'N':>10} | {'Tempo (s)':>15}")
print("-" * 28)

for N in valores_N:
    g = GrafoEuleriano(N)
    g.gerar_grafo_euleriano(arestas_extras=N//2)

    inicio = time.time()
    g.ciclo_euleriano()
    fim = time.time()

    tempo_execucao = fim - inicio
    tempos.append(tempo_execucao)

    # ✅ Impressão na CLI
    print(f"{N:>10} | {tempo_execucao:>15.6f}")

# 📊 Gráfico
plt.figure()
plt.plot(valores_N, tempos)
plt.xlabel("Número de Nós (N)")
plt.ylabel("Tempo de Execução (s)")
plt.title("Complexidade Experimental do Algoritmo de Hierholzer")
plt.grid(True)
plt.show()
