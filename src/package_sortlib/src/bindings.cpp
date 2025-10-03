#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

// Incluindo o cabecalho de cada algoritmo
#include "bubble_sort/bubble_sort.h"
#include "selection_sort/selection_sort.h"
#include "insertion_sort/insertion_sort.h"
#include "quick_sort/quick_sort.h"
#include "merge_sort/merge_sort.h"
#include "shell_sort/shell_sort.h"
#include "heap_sort/heap_sort.h"

namespace py = pybind11;

PYBIND11_MODULE(sortlib, m) {
    m.doc() = "Biblioteca de ordenação de strings";

    // Registrando cada função no módulo Python
    m.def("bubble_sort", &bubble_sort, "Ordena um vetor de strings usando Bubble Sort");
    m.def("selection_sort", &selection_sort, "Ordena um vetor de strings usando Selection Sort");
    m.def("insertion_sort", &insertion_sort, "Ordena um vetor de strings usando Insertion Sort");
    m.def("quick_sort", &quick_sort, "Ordena um vetor de strings usando Quick Sort");
    m.def("merge_sort", &merge_sort, "Ordena um vetor de strings usando Merge Sort");
    m.def("shell_sort", &shell_sort, "Ordena um vetor de strings usando Shell Sort");
    m.def("heap_sort", &heap_sort, "Ordena um vetor de strings usando Heap Sort");
}
