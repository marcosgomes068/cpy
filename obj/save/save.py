import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.list import listar_pastas
from dotenv import load_dotenv
from utils.dir_act import mostrar_arvore
import shutil

load_dotenv()

def save():
    # Código para atualizar os diretórios
    variavel_ambiente = os.getenv('base')
    print(f"{variavel_ambiente=}")

    # diretorio atual
    pasta1 = os.getcwd()
    print(f"Diretório atual: {pasta1}")
    mostrar_arvore(pasta1)

    # Escolher um repositório
    pasta2 = (listar_pastas())

    # Caminho da pasta selecionada
    pasta_repo = os.path.join(variavel_ambiente, pasta2)
    print(f"Caminho da pasta selecionada: {pasta_repo}")

    # Limpar pasta2 antes de atualizar os diretórios
    for item in os.listdir(pasta_repo):
        item_path = os.path.join(pasta_repo, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

    # copiar arquivos de pasta1 para pasta2
    print(f"teste da pasta1 ",os.listdir(pasta1))
    print(f"teste da pasta2 ",os.listdir(pasta_repo))

    #logica de copia
    os.makedirs(pasta_repo, exist_ok=True)
    
    for root, dirs, files in os.walk(pasta1):  # percorre arquivos, pastas e subpastas
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(root, pasta1)
            dest_dir = os.path.join(pasta_repo, rel_path)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(src_file, dest_dir)  # mantém metadata
        # Não copie o diretório raiz diretamente!



if __name__ == "__main__":
    save()