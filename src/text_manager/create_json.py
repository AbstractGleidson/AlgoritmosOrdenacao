# Cria os JSON com os dados
import json
from pathlib import Path

def create_json(algoritmo: str, quantidade: int, tempo_exec: float, save_dir: Path):
    """
    Cria um arquivo JSON com os dados de execução de um algoritmo.

    Args:
        algoritmo (str): Nome do algoritmo.
        quantidade (int): Quantidade de palavras processadas.
        tempo_exec (float): Tempo de execução em segundos.
    """
    dados = {
        "algoritmo": algoritmo,
        "quantidade_palavras": quantidade,
        "tempo": tempo_exec
    }
    
    json_path = save_dir / f"{algoritmo}.json"  # Cria o path do JSON
    
    with open(json_path, "a", encoding="UTF-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)  # Cria arquivo
        file.write(",\n")
    
    print(f"Arquivo JSON criado em: {json_path}")
