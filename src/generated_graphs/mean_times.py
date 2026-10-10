from pathlib import Path
from manager_data import read_json, write_json

if __name__ == "__main__":
    
    base_path = Path(__file__).parent.parent.parent / 'data'
    
    data_mean = {}
    
    # carrega todos os dados de tempo em data_mean 
    for i in range(0, 5):
        for n in [1000, 2500, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000]:
            for j in [1, 10, 100, 1000]:
                
                path = base_path / 'times' / (f"data_{n}-{n*j}_teste{i}.json")
    
                data = read_json(path)
                
                for algorithm, time in data.items():             
                    try: 
                        data_mean[f"{n}-{n*j}-{algorithm}"] += time
                    except KeyError:
                        data_mean[f"{n}-{n*j}-{algorithm}"] = time
              
    for key, value in data_mean.items():
        data_mean[key] = (value / 5) # tira a média dos 4 teste de execução para cada algoritmo e intervalo
        
    write_json(base_path / 'mean_times' / 'mean_times.json', data_mean) # grava os resultados de tempo médio