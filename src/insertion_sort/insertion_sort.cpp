// Implementacao do algoritmo de ordenacao insertionsort
#include "insertion_sort.h"

// Função do insertionsort
void insertion_sort(std::vector<int>& arr) {
    int n = arr.size();

    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;

        // Move elementos maiores que key uma posição à frente
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }

    return;  // Retorna o vetor ordenado
}
