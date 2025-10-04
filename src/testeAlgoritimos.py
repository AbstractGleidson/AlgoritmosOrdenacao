import time
from pathlib import Path
import package_sortlib.sortlib as sortlib
from text_manager.extract_words import extract_words
from create_JSON.create_json import create_json

arq = "nomes500.txt" # Arquivo para ser lido
file = "Downloads"

# Caminho do arquivo
path = Path.home()
path = path / file / arq

save_data = Path.home() / "Programacao" / "python" / "testeAlgoritimosOrdenacao" / "src" / "data_base" / "merge_sort"

for i in range(5):
    words = extract_words(path) # Extrai palavras

    start = time.process_time()
    words = sortlib.merge_sort(words)
    end = time.process_time()

    print(len(words))

    create_json("merge_sort_500", 500, end - start, save_data)