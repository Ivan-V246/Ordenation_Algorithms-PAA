// O modulo pybind faz uma "traducao" dos tipos, retornos e etc do c++ para o python
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

// Incluindo o cabecalho de cada algoritmo
#include "counting_sort/counting_sort.h"
#include "merge_sort/merge_sort.h"
#include "insertion_sort/insertion_sort.h"
#include "radix_sort/radix_sort.h"

namespace py = pybind11;

// Define a base da lib a ser gerada para python
PYBIND11_MODULE(sortlib, m) {
    m.doc() = "Biblioteca de ordenação de strings";

    // Registrando cada função no módulo Python
    m.def("counting_sort", &counting_sort, "Ordena um vetor de strings usando Counting Sort");
    m.def("merge_sort", &merge_sort, "Ordena um vetor de strings usando Merge Sort");
    m.def("insertion_sort", &insertion_sort, "Ordena um vetor de strings usando Insertion Sort");
    m.def("radix_sort", &radix_sort, "Ordena um vetor de strings usando Radix Sort");
}
