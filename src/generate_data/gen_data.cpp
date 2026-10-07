#include <fstream>
#include <iostream>
#include<random>

void gen_data(int n){
    // Configuração para gerar números aleatórios
    static std::random_device rd;
    static std::mt19937 gen(rd());
    for(int i = 1; i <= 1000; i*=10){  
        std::uniform_int_distribution<int> dis(1, i*n);
        std::string nome = "dados"+std::to_string(n)+"-"+std::to_string(i*n)+".txt";
        std::ofstream arquivo(nome);
        if (arquivo.is_open()) {
            for(int i = 0; i < n; i++){
                arquivo << dis(gen) << std::endl;
            }

            arquivo.close();
            std::cout << "Dados gravados com sucesso!" << std::endl;
        } else {
            std::cout << "Erro ao abrir o arquivo." << std::endl;
        }
    }
}

