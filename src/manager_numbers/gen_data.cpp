#include <manager_numbers.hpp>

void gen_data(int n, std::string &save_dir){
    // Configuração para gerar números aleatórios
    static std::random_device rd;
    static std::mt19937 gen(rd());

    for(int i = 1; i <= 1000; i*=10){  
        std::uniform_int_distribution<int> dis(1, i*n);
        std::string name_file = save_dir + "/dados"+std::to_string(n)+"-"+std::to_string(i*n)+".txt";

        // cria arquivo
        std::ofstream file(name_file);

        // tenta abrir o arquivo
        if (file.is_open()) {
            for(int i = 0; i < n; i++){
                file << dis(gen) << std::endl;
            }

            file.close();
            std::cout << "Dados gravados com sucesso!" << std::endl;
        } else {
            std::cout << "Erro ao abrir o arquivo: " << name_file << std::endl;
        }
    }
}

