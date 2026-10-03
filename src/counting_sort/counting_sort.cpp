// Implementacao do algoritmo de ordenacao coutingsort
#include "counting_sort.h"
#include <vector>

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

    //Preenche o novo vetor com os elementos na ordem
    std::vector<int> new_array(n);
    for(int i = 0, j = 0; i <= max_element; i++) 
        for(int k = 0; k < count[i]; k++, j++) 
            new_array[j] = i;

    arr = new_array;
    return;
}
