import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from core.dir import listar_dir

def print_project_root():
    # Obtém o caminho absoluto do diretório raiz do projeto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    print(f"\n📁 Diretório raiz do projeto: {project_root}")

    # Lista a estrutura do diretório raiz
    estrutura = listar_dir(project_root, max_arquivos=100)
    print(estrutura)

def comit(path):
    # diretorio atual
    pasta1 = print_project_root()

    # diretorio selecionado
    pasta2 = path

    # verificar se a semelhança com algum repositorio existente
    
if __name__ == "__main__":
    print_project_root()