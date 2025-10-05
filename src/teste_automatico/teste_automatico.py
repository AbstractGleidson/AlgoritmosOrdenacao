import time
from package_sortlib import sortlib
from text_manager.text_treatment import clear_arq_text
from PySide6.QtCore import QThread, Signal

# Classe que realiza o teste de forma automatica em paralelo
class AutoTeste(QThread):
    # algoritmos para teste 
    algoritmos = {
        "quicksort": sortlib.quick_sort,
        "heapsort":  sortlib.heap_sort,
        "mergesort": sortlib.merge_sort,
        "shellsort": sortlib.shell_sort,
        "insertionsort": sortlib.insertion_sort,
        "selectionsort": sortlib.selection_sort,
        "bubblesort":  sortlib.bubble_sort
    }

    finished = Signal(float)  # sinal que é mandado quando termina a execucao do run

    def __init__(self, algoritmo: str, path: str, parent=None):
        super().__init__(parent)      
        self.algoritmo = algoritmo
        self.path = path

    def run(self):
        tempo_exec = 0.0
        
        # roda 5 vezes e soma os tempos
        for _ in range(5):
            words = clear_arq_text(self.path)

            start = time.process_time()   # mais apropriado para medir wall-clock
            # chama o algoritmo selecionado (sincrono)
            self.algoritmos[self.algoritmo](words)
            end = time.process_time()

            tempo_exec += (end - start)
        
        tempo_exec = tempo_exec / 5
        # ao final, emite o tempo total (Da um gritinho)
        self.finished.emit(tempo_exec)
