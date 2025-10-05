// Implementacao do algoritmo de ordenacao bubblesort
#include "bubble_sort.h"

std::vector<std::string> bubble_sort(std::vector<std::string> arr) {
    int n = arr.size();
    bool swapped; // Flag para saber se ja esta ordenado

    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {   // Compara strings 
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }

    return arr;  // Retorna o vetor ordenado
}