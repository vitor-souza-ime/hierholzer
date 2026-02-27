# Hierholzer Algorithm – Experimental Complexity Analysis

Implementação do **Algoritmo de Hierholzer** para construção de ciclos eulerianos em grafos não direcionados, incluindo análise experimental de escalabilidade.

---

## 📌 Objetivo

Este projeto implementa o algoritmo clássico de Hierholzer e realiza uma análise empírica de sua complexidade computacional para diferentes tamanhos de grafos.

---

## 🧠 Fundamentação Teórica

Um grafo não direcionado é **euleriano** se:

1. É conexo  
2. Todos os vértices possuem grau par  

O algoritmo de Hierholzer constrói um ciclo euleriano com complexidade:

T(N) = O(N + M)

onde:
- N = número de vértices
- M = número de arestas

No experimento realizado:

M ≈ 2N

Logo, espera-se crescimento aproximadamente linear:

T(N) ≈ O(N)

---

## 🔬 Experimento Realizado

Valores testados:

N = [100, 500, 1000, 5000, 10000]

Para cada N:

- Geração automática de grafo euleriano
- Execução do algoritmo
- Medição de tempo com `time.time()`
- Plotagem de gráfico Tempo × N

---

## 📊 Resultados Obtidos

Saída na CLI:

```

=== Resultados Experimentais ===
N |       Tempo (s)
-------------------

```
   100 |        0.000000
   500 |        0.001000
  1000 |        0.002000
  5000 |        0.007078
 10000 |        0.015859
```

```

---

## 📈 Análise dos Resultados

Observações:

- Para N pequenos, o tempo é praticamente desprezível (limite de resolução do clock).
- O crescimento é aproximadamente linear.
- Para N = 10000, o tempo permanece baixo (~0.016s), indicando boa escalabilidade.
- Não há evidência de crescimento quadrático.

Relação aproximada observada:

Tempo ≈ k · N

O que confirma empiricamente o comportamento linear previsto pela teoria.

---

## 📊 Interpretação do Gráfico

O gráfico Tempo × N apresenta:

- Curva crescente quase linear
- Ausência de crescimento exponencial ou quadrático
- Escalabilidade consistente com O(N)

---

## 🛠 Dependências

- Python 3.x
- matplotlib

Instalação:

```

pip install matplotlib

```

---

## 🎓 Aplicações Acadêmicas

Este repositório pode ser utilizado em:

- Teoria dos Grafos
- Estruturas de Dados
- Análise de Algoritmos
- Estudo experimental de complexidade
- Ensino de algoritmos clássicos

---

## 🔎 Possíveis Melhorias

- Utilizar `time.perf_counter()` (maior precisão)
- Executar múltiplas rodadas e calcular média/desvio padrão
- Análise log-log
- Comparação com algoritmo de Fleury
- Implementação com matriz de adjacência (para contraste O(N²))

---

## 👨‍🏫 Autor

Prof. Vitor Amadeu  

---

## 📜 Licença

MIT License
