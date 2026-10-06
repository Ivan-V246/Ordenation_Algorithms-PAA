// Implementacao do algoritmo de ordenacao radixsort
#include <sort_algorithms.hpp>

// Função do radixsort
void radix_sort(std::vector<int>& arr) {
    //Extrai o tamanho do vetor 
    int n = arr.size();
    
    //Encontra o maior elemento do vetor
    int max_element = arr[0];
    for(int i = 1; i < n; i++) 
        if(arr[i] > max_element) max_element = arr[i];

    for(int exp = 1; max_element/exp > 0 ; exp*=10) {
        //Contabiliza a frequência de cada dígito atual
        std::vector<int> count(10, 0);
        for(int i = 0; i < n; i++) 
            count[(arr[i]/exp)%10]++;

        //Realiza uma soma de prefixos da contagem
        for(int i = 1; i < 10; i++) 
            count[i] = count[i]+count[i-1];

        //Preenche o novo array com os valores ordenados pelo dígito atual
        std::vector<int> new_array(n);
        for(int i = n-1; i >= 0; i--) 
            new_array[--count[(arr[i]/exp)%10]] = arr[i];

        arr = new_array;
    }
    return;
}
