#include <manager_numbers.hpp>
#include <cmath>
#include <cstring>

// converte uma string em inteiro 
int string_to_int(const std::string &s) {
    int number = 0;
    for (char c : s) {
        number = number * 10 + (c - '0');
    }
    return number;
}

void read_data(std::vector<int> &numbers, std::string &save_dir, int size, int interval){

    std::string name_file = save_dir + "/dados"+std::to_string(size)+"-"+std::to_string(interval)+".txt";

    // cria arquivo
    std::ifstream file(name_file);

    std::string line;

    // tenta abrir o arquivo
    if (file.is_open()) {
        while(std::getline(file, line))
        {
            numbers.push_back(string_to_int(line));
        }

        file.close();

        std::cout << "Arquivo lido: " << name_file << std::endl;
    } else {
        std::cout << "Erro ao abrir o arquivo: " << name_file << std::endl;
    }
}