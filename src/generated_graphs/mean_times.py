from pathlib import Path
from manager_data import read_json, write_json

if __name__ == "__main__":
    base_path = Path(__file__).parent.parent.parent / 'data'
    
    data_mean = {}
    counts = {}
    
    # Valores de N
    interval_n = [1000, 5000, 10000, 50000, 100000]
    
    # Percorre as 5 pastas de dados geradas (data1 a data5)
    for k in range(1, 6):
        
        # Percorre os 5 testes de execução
        for i in range(0, 5):
            
            # percorre para cada n
            for n in interval_n:
                # multiplicador para cada intervalo
                for j in [1, 10, 100, 1000]:
                    
                    # caminho dos json
                    path = base_path / 'times' / f"data{k}" / f"data_{n}-{n*j}_teste{i}.json"
                    
                    # verificação de segurança para a existência do dir
                    if not path.exists():
                        continue
                    
                    data = read_json(path)
                    
                    # gera o dict com os dados
                    for algorithm, time in data.items():
                        
                        key = f"{n}-{n*j}-{algorithm}" # chave para cada intervalo, vetores e testes
                        
                        try: 
                            data_mean[key] += time # dados de tempo 
                            counts[key] += 1 # quantidade de incrementos
                            
                        except KeyError:
                            data_mean[key] = time # dados de tempo
                            counts[key] = 1 # quantidade de incrementos
              
    # Calcula a média geral dividindo pelo total de arquivos somados (5 pastas * 5 testes = 25 execuções) para cada intervalo
    for key, value in data_mean.items():
        data_mean[key] = value / counts[key]
        
    path_save_file = base_path / 'mean_times' / 'mean_times.json', data_mean # gera o path para salvamento
    write_json(path_save_file)  # salva dados em um .json
    
    print(f"Médias calculadas e salvas com sucesso, salvo em: {path_save_file}")