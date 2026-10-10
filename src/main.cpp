#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <chrono>
#include <write_data.hpp>
#include <sort_algorithms.hpp>
#include <manager_numbers.hpp>

using json = nlohmann::json;

std::string BASE_SAVE_PATH = "data/numbers"; // caminho base para salvar dados

int main() {

    // n escolhidos 
    int interval_n[] = {1000, 2500, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000};

    // Gera os aquivos com os dados númericos
    for(auto n: interval_n)
    {
        gen_data(n, BASE_SAVE_PATH);
    }

    // // Cabeçalho base de uma função de ordenação
    using sort_function = void(*)(std::vector<int>&);

    // Mapeamento das funções de ordnação
    std::map<std::string, sort_function> sorts = {
        {"radix_sort", radix_sort},
        {"merge_sort", merge_sort},
        {"insertion_sort", insertion_sort},
        {"counting_sort", counting_sort}
    };

    for(int i = 0; i < 5; i++){

        for(auto n: interval_n){

            for(int j = 1; j <= 1000; j *= 10){ 

                // Map para escrever o json
                std::map<std::string, double> data = {};

                // Executa cada algoritmo de ordenação e calcula o tempo de execução salvando-o em data
                for (auto const& [nome, algoritmo] : sorts) {
                    std::vector<int> numbers = {};

                    read_data(numbers, BASE_SAVE_PATH, n, n * j); // ler cada arquivo com os dados numericos
                
                    // Medição de tempo
                    auto start_time = std::chrono::high_resolution_clock::now();

                    algoritmo(numbers); // Executa o algoritmo de ordenação atual do loop

                    auto end_time = std::chrono::high_resolution_clock::now();
                    
                    auto duration = std::chrono::duration<double, std::milli>(end_time - start_time);
                    double execution_time = duration.count() / 1000.0; // Convertendo para segundos
                    
                    // Salva o tempo correspondente de cada algoritmo em segundos
                    data[nome] = execution_time; 
                    
                    std::cout << nome << " executado em: " << execution_time << " s\n";
                    
                    // caminho para salvar os resultados da ordenação
                    std::string save_path_results = "data/results/data" "_" + std::to_string(n) + "-" + std::to_string(j*n) + "_teste_" + std::to_string(i) + "_" + nome + ".txt";
                    write_results(numbers, save_path_results);
                }

                // caminho para salvar os dados de tempo
                std::string save_path = "data/times/data" "_" + std::to_string(n) + "-" + std::to_string(j*n) + "_teste" + std::to_string(i) + ".json";
                
                // salva dados no arquivo JSON
                bool response = write_json(save_path, data);

                if (response) {
                    std::cout << "\nDados escritos com sucesso em " << save_path << std::endl;
                } else {
                    std::cout << "\nErro ao escrever dados!" << std::endl;
                }
            }   
        }
    }

    return 0;
}
