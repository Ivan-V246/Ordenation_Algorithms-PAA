#include <string>
#include <map>
#include <fstream>
#include <stdint.h>
#include <json.hpp>

using json = nlohmann::json; 

template<typename K, typename V> // para aceitar qualquer tipo base do c++
uint8_t write_json(const std::string& path, const std::map<K, V> &data)
{
    json json_file = data; // converte o map em objeto json

    std::ofstream file(path); // cria arquivo para salva dados

    if(file.is_open())
    {
        file << json_file.dump(4);
        file.close();
        return 1; // dados escritos com sucesso
    }

    else{
        return 0; // erro ao abrir arquivo     
    }
}