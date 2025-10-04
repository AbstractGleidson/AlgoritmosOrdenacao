// Implementacao do algoritimo de ordenacao quicksort
#include "quick_sort.h"
#include <algorithm>  // para std::swap

// Função de partição para strings
int partition(std::vector<std::string>& arr, int low, int high) {
    std::string pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Função recursiva do Quick Sort
void quick_sort_rec(std::vector<std::string>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort_rec(arr, low, pi - 1);
        quick_sort_rec(arr, pi + 1, high);
    }
}

// Função principal chamada do Python
std::vector<std::string> quick_sort(std::vector<std::string> arr) {
    quick_sort_rec(arr, 0, arr.size() - 1);
    return arr;
}