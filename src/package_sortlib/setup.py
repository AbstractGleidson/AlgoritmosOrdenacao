from setuptools import setup, Extension
import pybind11
from pathlib import Path
import sys

# Diretório base do código
src_dir = Path("src")

# Pega todos os arquivos .cpp recursivamente
sources = list(src_dir.rglob("*.cpp"))

# Lista de diretórios de include (incluindo subpastas)
include_dirs = [pybind11.get_include()]
for folder in src_dir.iterdir():
    if folder.is_dir():
        include_dirs.append(str(folder))

# Criação da extensão
ext_modules = [
    Extension(
        'sortlib',                      # nome do módulo Python
        [str(s) for s in sources],      # todos os .cpp
        include_dirs=include_dirs,
        language='c++',
    ),
]

# Setup do pacote
setup(
    name='sortlib',
    description='Biblioteca de algoritmos de ordenação em C++ para Python',
    ext_modules=ext_modules,
)
