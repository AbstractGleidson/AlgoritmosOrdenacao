// Implementacao do algoritmo de ordenacao heapsort
#include "heap_sort.h"
#include <vector>
#include <string>
#include <algorithm>

// Função auxiliar para rebalancear o heap
void heapify(std::vector<std::string>& arr, int n, int i) {
    int largest = i; // Raiz
    int l = 2 * i + 1; // Filho esquerdo
    int r = 2 * i + 2; // Filho direito

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

// Função principal de Heap Sort
std::vector<std::string> heap_sort(std::vector<std::string> arr) {
    int n = arr.size();

    // Constroi o heap máximo
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extrai os elementos do heap um por um
    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }

    return arr;
}