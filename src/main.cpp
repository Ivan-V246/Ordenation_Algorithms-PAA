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

    // Intervalo de n escolhidos 
    int interval_n[] = {100, 500, 1000, 5000, 10000};

    // Gera os aquivos com os dados númericos
    for(auto n: interval_n)
    {
        gen_data(n, BASE_SAVE_PATH);
    }

    // // Cabeçalho base de uma função de ordenação
    using sort_functions = void(*)(std::vector<int>&);

    // Mapeamento das funções de ordnação
    std::map<std::string, sort_functions> sorts = {
        //{"shell_sort", shell_sort},
        {"radix_sort", radix_sort},
        {"merge_sort", merge_sort},
        {"insertion_sort", insertion_sort},
        {"counting_sort", counting_sort}
    };

    // ler arquivos 
    for(auto n: interval_n){
        for(int i = 1; i <= 1000; i*=10){ 

            // Map para escrever o json
            std::map<std::string, double> data = {};

            // Executa cada algoritmo de ordenação e calcula o tempo de execução salvando-o em data
            for (auto const& [nome, algoritmo] : sorts) {
                std::vector<int> numbers = {};
                read_data(numbers, BASE_SAVE_PATH, n, n * i);
            
                // Medição de tempo
                auto start_time = std::chrono::high_resolution_clock::now();

                algoritmo(numbers); // Executa o algoritmo de ordenação atual do loop

                auto end_time = std::chrono::high_resolution_clock::now();
                
                auto duration = std::chrono::duration<double, std::milli>(end_time - start_time);
                double execution_time = duration.count() / 1000.0; // Convertendo para segundos
                
                // Salva o tempo correspondente de cada algoritmo em segundos
                data[nome] = execution_time; 
                
                std::cout << nome << " executado em: " << execution_time << " s\n";
            }

            std::string save_path = "data/times/data" "_" + std::to_string(n) + "-" + std::to_string(i*n) + ".json";
            
            // salva dados no arquivo JSON
            bool response = write_json(save_path, data);

            if (response) {
                std::cout << "\nDados escritos com sucesso em " << save_path << std::endl;
            } else {
                std::cout << "\nErro ao escrever dados!" << std::endl;
            }

        }   
    }

    return 0;
}
