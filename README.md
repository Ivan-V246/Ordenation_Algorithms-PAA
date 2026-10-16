# Comparação de Algoritmos de Ordenação

Trabalho prático da disciplina de Projeto e Análise de Algoritmos da UFPI. A ideia é implementar e comparar empiricamente quatro algoritmos de ordenação — **Insertion Sort**, **Merge Sort**, **Counting Sort** e **Radix Sort** — medindo o tempo de execução real em diferentes tamanhos de entrada e intervalos de valores, e confrontando esses resultados com a teoria de complexidade.

**Autores:** Antônio Gemesson Sousa, Gleidson Luan Sena, Ivan Vitor Dias

---

## O que foi feito

Cada algoritmo foi rodado sobre vetores de inteiros gerados aleatoriamente com distribuição uniforme. Os tamanhos testados foram `n ∈ {1000, 5000, 10000, 50000, 100000}`, e para cada `n` foram usados quatro intervalos de valores: `[0, n]`, `[0, 10n]`, `[0, 100n]` e `[0, 1000n]`.

Para garantir resultados confiáveis, foram gerados **5 vetores distintos** por configuração e cada algoritmo foi executado **5 vezes por vetor**. O tempo reportado é a média de todas as execuções. No total, o projeto gerou mais de 2700 arquivos de dados.

---

## Estrutura do projeto

```
.
├── src/
│   ├── main.cpp                      # Ponto de entrada: gera dados e roda os algoritmos
│   ├── sort_algorithms/
│   │   ├── insertion_sort.cpp
│   │   ├── merge_sort.cpp
│   │   ├── counting_sort.cpp
│   │   └── radix_sort.cpp
│   ├── manager_numbers/
│   │   ├── read_data.cpp             # Leitura dos vetores de entrada
│   │   └── write_data.cpp            # Escrita dos resultados ordenados
│   └── generated_graphs/
│       ├── genereted_graphs.py       # Geração de todos os gráficos
│       ├── manager_data.py           # Leitura e organização dos JSONs de tempo
│       └── mean_times.py             # Cálculo das médias por configuração
│
├── include/
│   ├── sort_algorithms.hpp
│   ├── manager_numbers.hpp
│   ├── write_data.hpp
│   └── json.hpp                      # nlohmann/json para salvar os tempos
│
├── data/
│   ├── numbers/                      # Vetores de entrada gerados (numbers1..5)
│   │   └── numbersX/
│   │       └── dadosN-K.txt          # Vetor de tamanho N com valores no intervalo [0, K]
│   ├── times/                        # Tempos de execução por teste (JSON)
│   │   └── dataX/
│   │       └── data_N-K_testeY.json  # Tempo de cada algoritmo para aquele vetor/execução
│   ├── results/                      # Vetores após a ordenação (para verificação)
│   └── mean_times/
│       └── mean_times.json           # Médias finais consolidadas
│
├── results/
│   ├── graphs/                       # Todos os gráficos gerados
│   └── report/                       # Relatório em LaTeX (SBC)
│
├── bin/
│   └── app.exe                       # Executável compilado
│
└── compile.sh                        # Script de compilação
```

O nome dos arquivos de dados segue o padrão `dadosN-K.txt`, onde `N` é o tamanho do vetor e `K` é o valor máximo dos elementos. Os arquivos de tempo seguem `data_N-K_testeY.json`, onde `Y` é o índice do vetor (0 a 4).

---

## Como compilar e rodar

```bash
# Compilar
bash compile.sh

# Executar (gera os dados e roda todos os algoritmos)
./bin/app.exe
```

Depois de rodar o C++, gere os gráficos com Python:

```bash
pip install -r requirements.txt # Instala as bibliotecas 

cd src/generated_graphs
python mean_times.py          # Cálcula as médias em mean_times.json
python genereted_graphs.py    # Gera todos os gráficos em results/graphs/
```

**Dependências Python:** `matplotlib`, `numpy`, `pandas`, `seaborn`

---

## Ambiente usado nos experimentos

| Item | Detalhe |
|---|---|
| Linguagem | C++ |
| Compilador | GCC 15.3.1 (Red Hat 15.3.1-1) |
| Sistema | Linux Fedora |
| Processador | Intel Core i5-13420H (13ª geração) |
| Memória RAM | 8 GB DDR5 5200 MHz |

---

## Resultados em destaque

Alguns números que saíram dos experimentos e valem mencionar:

**Com `k = n` (melhor caso para algoritmos lineares):**

| Algoritmo | n = 1.000 | n = 100.000 |
|---|---|---|
| Counting Sort | ~0,000025 s | ~0,0023 s |
| Radix Sort | ~0,000062 s | ~0,0087 s |
| Merge Sort | ~0,00031 s | ~0,040 s |
| Insertion Sort | ~0,0020 s | ~19,7 s |

A diferença entre o Counting Sort e o Insertion Sort para `n = 100.000` é de **~8.400×**. Dá pra ver por que escolher o algoritmo certo importa.

**O ponto problemático do Counting Sort:** quando `k` cresce mantendo `n` fixo, ele degrada rapidamente. Para `n = 1.000`:
- Em `k = 1.000` é o algoritmo mais rápido (~0,000025 s)
- Em `k = 100.000` já perdeu para o Merge Sort
- Em `k = 1.000.000` é o **mais lento de todos**, incluindo o Insertion Sort

**O Radix Sort se sai bem nos dois mundos:** sofre pouco com o aumento de `k` (apenas ~1,8× mais lento quando `k` aumenta 1000×) e mantém boa vantagem sobre o Merge Sort em todas as configurações testadas.

---

## Gráficos gerados

Todos os gráficos ficam em `results/graphs/`. Os principais são:

- `comparativo_crescimento.png` — comparativo log-log com `k = n`
- `comparativo_media_geral_n.png` — comparativo log-log com média de todos os intervalos
- `escala_real_insertion_sort.png` — curva parabólica do Insertion Sort em escala linear
- `escala_real_nlog_lineares.png` — Merge, Radix e Counting em escala linear com `k = n`
- `escala_real_*_media_ranges.png` — versões com média de todos os intervalos de `k`
- `heatmap_counting_sort.png` — mapa de calor do Counting Sort variando `n` e `k`
- `impacto_range_n_X.png` — sensibilidade ao intervalo `k` para cada valor de `n` fixo

---