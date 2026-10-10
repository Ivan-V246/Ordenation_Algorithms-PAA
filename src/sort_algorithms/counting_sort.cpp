// Implementacao do algoritmo de ordenacao coutingsort
#include <sort_algorithms.hpp>

// Função do countingsort 
void counting_sort(std::vector<int>& arr) {
    //Extrai o tamanho do vetor
    int n = arr.size();

    //Armazena o maior elemento do vetor
    int max_element = arr[0];
    for(int i = 1; i < n; i++) 
        if(arr[i] > max_element) max_element = arr[i];

    //Contabiliza a frequência de cada valor
    std::vector<int> count(max_element+1, 0);
    for(int i = 0; i < n; i++) count[arr[i]]++;

    //Calcula a soma de prefixo
    for(int i = 1; i <= max_element; i++) count[i] += count[i-1]; 

    //Preenche o novo vetor
    std::vector<int> new_array(n);
    for(int i = n-1; i >= 0; i--) 
        new_array[--count[arr[i]]] = arr[i];

    arr = new_array;
    return;
}
