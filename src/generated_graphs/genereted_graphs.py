from pathlib import Path
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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

  all_ns = sorted(df['n'].unique())

  # ==========================================
  # GRÁFICO 1: Curvas de Crescimento (n == range) [Log-Log]
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
  plt.xlabel('Tamanho do Array (n) [Escala Log]', fontsize=12)
  plt.ylabel('Tempo Médio de Execução (segundos) [Escala Log]', fontsize=12)
  plt.legend(title_fontsize='11')
  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'comparativo_crescimento.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()
  plt.close()

  # ==========================================
  # GRÁFICO 2: Impacto do Range (k) para n Fixo [Log-Log]
  # ==========================================
  for fixed_n in all_ns:
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
    plt.xlabel('Range dos Valores (k) [Escala Log]', fontsize=12)
    plt.ylabel('Tempo Médio de Execução (segundos) [Escala Log]', fontsize=12)
    plt.legend(title_fontsize='11')
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

  plt.xlabel('Tamanho do Array (n)', fontsize=12)
  plt.ylabel('Range dos Valores (k)', fontsize=12)
  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'heatmap_counting_sort.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()
  plt.close()

  # ==========================================
  # GRÁFICO 4: Escala Real (Linear) - Insertion Sort
  # ==========================================
  plt.figure(figsize=(10, 6))
  df_insertion = df[(df['algorithm'] == 'insertion_sort') & (df['n'] == df['range'])]

  sns.lineplot(
      data=df_insertion,
      x='n',
      y='time',
      hue='algorithm',
      marker='o',
      linewidth=2.5,
      palette=['#fc8d62']
  )

  plt.xlabel('Tamanho do Array (n)', fontsize=12)
  plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
  
  ax = plt.gca()
  formatter = ticker.ScalarFormatter(useMathText=True)
  formatter.set_scientific(True)
  formatter.set_powerlimits((0, 0))
  ax.xaxis.set_major_formatter(formatter)

  plt.legend(title_fontsize='11')
  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'escala_real_insertion_sort.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()
  plt.close()

  # ==========================================
  # GRÁFICO 5: Escala Real (Linear) - Merge, Radix e Counting Sort
  # ==========================================
  plt.figure(figsize=(10, 6))
  algos_proximos = ['merge_sort', 'radix_sort', 'counting_sort']
  df_fast = df[(df['algorithm'].isin(algos_proximos)) & (df['n'] == df['range'])]

  sns.lineplot(
      data=df_fast,
      x='n',
      y='time',
      hue='algorithm',
      marker='o',
      linewidth=2.5,
  )

  plt.xlabel('Tamanho do Array (n)', fontsize=12)
  plt.ylabel('Tempo de Execução (segundos)', fontsize=12)

  ax = plt.gca()
  formatter = ticker.ScalarFormatter(useMathText=True)
  formatter.set_scientific(True)
  formatter.set_powerlimits((0, 0))
  ax.xaxis.set_major_formatter(formatter)

  plt.legend(title_fontsize='11')
  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'escala_real_nlog_lineares.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()
  plt.close()

  # ==========================================
  # GRÁFICO 6: Média Geral por n (Desconsiderando os diferentes ranges) [Log-Log]
  # ==========================================
  plt.figure(figsize=(10, 6))
  
  # Agrupa valores de acordo com o n
  df_mean_by_n = df.groupby(['n', 'algorithm'])['time'].mean().reset_index()

  sns.lineplot(
      data=df_mean_by_n,
      x='n',
      y='time',
      hue='algorithm',
      marker='o',
      linewidth=2.5,
  )

  plt.yscale('log')
  plt.xscale('log')
  plt.xlabel('Tamanho do Array (n) [Escala Log - Média de Todos os Ranges]', fontsize=12)
  plt.ylabel('Tempo Médio Geral de Execução (segundos) [Escala Log]', fontsize=12)
  
  plt.legend(title='Algoritmo', title_fontsize='11')
  plt.tight_layout()
  plt.savefig(
      path_save_graph / 'comparativo_media_geral_n.png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.show()
  plt.close()