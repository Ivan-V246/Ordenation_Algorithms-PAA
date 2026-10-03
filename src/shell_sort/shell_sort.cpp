// Implementacao do algoritmo de ordenacao shellsort
#include "shell_sort.h"

// Shell Sort para números naturais
// Recebe o valor por referência
void shell_sort(std::vector<int>& arr) {
    int n = arr.size();

    // Começa com um gap grande, que vai sendo reduzido
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // Faz uma insertion sort para este gap
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;

            // Move elementos maiores que temp para frente
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }

            arr[j] = temp; // Coloca temp na posição correta
        }
    }

    return;
}
