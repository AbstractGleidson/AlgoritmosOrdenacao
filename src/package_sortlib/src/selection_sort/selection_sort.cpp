#include "selection_sort.h"

// Selection Sort para strings
std::vector<std::string> selection_sort(std::vector<std::string> arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; ++i) {
        // Assume que a posição atual possui o menor elemento
        int min_idx = i;

        // Procura o menor elemento na parte não ordenada
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        // Troca o menor elemento para a posição correta
        std::swap(arr[i], arr[min_idx]);
    }

    return arr;  // Retorna o vetor ordenado
}
