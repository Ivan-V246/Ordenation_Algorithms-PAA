from pathlib import Path
import json
import matplotlib.pyplot as plt
from manager_data import read_json
import pandas as pd
import seaborn as sns

if __name__ == '__main__':
  base_path = Path(__file__).parent.parent.parent / 'data'
  path_data = base_path / 'mean_times' / 'mean_times.json'

  path_save_graph = Path(__file__).parent.parent.parent / 'results' / 'graphs'

  # dados
  data = read_json(path_data)

  # Transformar o dicionário estruturado em um DataFrame
  rows = []
  for key, time_val in data.items():
    n_str, range_str, algo = key.split('-')
    rows.append(
        {'n': int(n_str), 'range': int(range_str), 'algorithm': algo, 'time': time_val}
    )

  df = pd.DataFrame(rows)

  # Configurar o estilo visual dos gráficos
  sns.set_theme(style='whitegrid')
  plt.rcParams.update({'font.size': 11})

  # ==========================================
  # GRÁFICO 1: Curvas de Crescimento (n == range)
  # ==========================================
  plt.figure(figsize=(10, 6))
  df_growth = df[df['n'] == df['range']]

  sns.lineplot(
      data=df_growth,
      x='n',
      y='time',
      hue='algorithm',
      marker='o',
      linewidth=2.5,
  )

  plt.yscale('log')
  plt.xscale('log')
  plt.title(
      'Desempenho dos Algoritmos de Ordenação por Tamanho (n = range)',
      fontsize=14,
      pad=15,
  )
  plt.xlabel('Tamanho do Array (n) [Escala Log]', fontsize=12)
  plt.ylabel('Tempo Médio de Execução (segundos) [Escala Log]', fontsize=12)

  plt.legend(
      title='Algoritmo',
      title_fontsize='11',
      bbox_to_anchor=(1.02, 1),
      loc='upper left',
  )

  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'comparativo_crescimento.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()

  # ==========================================
  # GRÁFICO 2: Impacto do Range (k) para n Fixo
  # ==========================================
  unique_ns = sorted(df['n'].unique())

  for fixed_n in unique_ns:
    df_range_impact = df[df['n'] == fixed_n]

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df_range_impact,
        x='range',
        y='time',
        hue='algorithm',
        marker='s',
        linewidth=2.5,
    )

    plt.yscale('log')
    plt.xscale('log')
    plt.title(
        f'Impacto do Range dos Valores (k) no Tempo (Para n = {fixed_n:,})',
        fontsize=14,
        pad=15,
    )
    plt.xlabel('Range dos Valores (k) [Escala Log]', fontsize=12)
    plt.ylabel('Tempo Médio de Execução (segundos) [Escala Log]', fontsize=12)

    plt.legend(
        title='Algoritmo',
        title_fontsize='11',
        bbox_to_anchor=(1.02, 1),
        loc='upper left',
    )

    plt.tight_layout()

    filename = f'impacto_range_n_{fixed_n}.png'

    plt.savefig(
        path_save_graph / filename, dpi=300, bbox_inches='tight'
    )
    plt.show()
    plt.close()

  # ==========================================
  # GRÁFICO 3: Mapa de Calor (Heatmap) - Counting Sort
  # ==========================================
  df_counting = df[df['algorithm'] == 'counting_sort']
  pivot_counting = df_counting.pivot(
      index='range', columns='n', values='time'
  )

  plt.figure(figsize=(10, 7))
  sns.heatmap(
      pivot_counting,
      annot=False,
      fmt='.4f',
      cmap='YlOrRd',
      norm=plt.matplotlib.colors.LogNorm(),
      cbar_kws={'label': 'Tempo (s) - Escala Log'},
  )

  plt.title(
      'Mapa de Calor: Tempo de Execução do Counting Sort (n vs Range)',
      fontsize=14,
      pad=15,
  )
  plt.xlabel('Tamanho do Array (n)', fontsize=12)
  plt.ylabel('Range dos Valores (k)', fontsize=12)
  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'heatmap_counting_sort.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()