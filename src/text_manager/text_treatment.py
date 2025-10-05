import re
import unicodedata

# Função que remove acentos
def remover_acentos(txt):
    # Separa as letras dos acentos: á = 'a', '´'
    decomposto = unicodedata.normalize("NFD", txt)
    
    # Remove os caracteres de acento (categoria Mn = acentos)
    # unicodedata.category retorna a categoria do caracter c
    # se for diferente de Mn implica que nao e um acento
    return "".join([c for c in decomposto if unicodedata.category(c) != "Mn"])

def clear_arq_text(path_read) -> list[str]:
    
    try:
        # Abre o arquivo
        with open(path_read, "r", encoding="utf-8") as file:
            texto = file.read()

        # Remove símbolos e números, utilizando expressao regular
        texto_limpo = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto) 

        # Remove acentos
        texto_sem_acentos = remover_acentos(texto_limpo)
        
        # Deixa em minusculo as palavras 
        texto_sem_acentos = texto_sem_acentos.lower()

        return texto_sem_acentos.split()
    
    except Exception:
        return ['']


def clear_arq_save(path_read, path_write):
    
    try:
        # Abre o arquivo
        with open(path_read, "r", encoding="utf-8") as file:
            texto = file.read()

        # Remove símbolos e números, utilizando expressao regular
        texto_limpo = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto) 

        # Remove acentos
        texto_sem_acentos = remover_acentos(texto_limpo)
        
        # Deixa em minusculo as palavras 
        texto_sem_acentos = texto_sem_acentos.lower()

        # Salva no novo arquivo
        with open(path_write, "w", encoding="utf-8") as file:
            file.write(texto_sem_acentos)
            
        print("Arquivo salvo")
    except Exception:
        print("Error ao abrir o aquivo")
