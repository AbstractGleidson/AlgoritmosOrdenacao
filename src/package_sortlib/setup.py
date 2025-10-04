# Arquivo que dita como o pacote deve ser compilados
# As pastas que devem ser compiladas e arquivos
# Aqui tambem consta algumas informacoes importantes do pacote como nome e discricao
from setuptools import setup, Extension

# Caminho dos arquivos que devem ser compilados
sources = [
    "src/bubble_sort/bubble_sort.cpp",
    "src/selection_sort/selection_sort.cpp",
    "src/insertion_sort/insertion_sort.cpp",
    "src/shell_sort/shell_sort.cpp",
    "src/merge_sort/merge_sort.cpp",
    "src/quick_sort/quick_sort.cpp",
    "src/heap_sort/heap_sort.cpp"
]

# Lista de diretórios que devem ser incluidos
include_dirs = [
    "src/bubble_sort",
    "src/selection_sort",
    "src/insertion_sort",
    "src/shell_sort",
    "src/merge_sort",
    "src/quick_sort",
    "src/heap_sort"
]

# Criação da extensão
ext_modules = [
    Extension(
        'sortlib',                      # nome do módulo Python
        [str(s) for s in sources],      # passa todos os aquivos
        include_dirs=include_dirs,      # diretorios incluidos
        language='c++',
    ),
]

# Setup do pacote
setup(
    name='sortlib', 
    description='Biblioteca de algoritmos de ordenação em C++ para Python',
    ext_modules=ext_modules,
)
