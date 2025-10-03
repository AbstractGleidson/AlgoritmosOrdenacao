#include "insertion_sort.h"

// Insertion Sort para strings
std::vector<std::string> insertion_sort(std::vector<std::string> arr) {
    int n = arr.size();

    for (int i = 1; i < n; ++i) {
        std::string key = arr[i];
        int j = i - 1;

        // Move elementos maiores que key uma posição à frente
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }

    return arr;  // Retorna o vetor ordenado
}