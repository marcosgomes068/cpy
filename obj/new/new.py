import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.locate_base import verificar_pasta_env
from src.inga_cfg.cfg import *

# Configuração do path
load_dotenv()

def new_repo(nome_repo):
    """Cria um novo repositório na pasta base"""
    base_path = os.getenv('base')
    caminho = os.path.join(base_path, nome_repo)
    os.makedirs(caminho, exist_ok=True)
    print(f"Repositório '{nome_repo}' criado em: {caminho}")
    return caminho

def create():
    """Função principal para criação de repositório"""
    # Verifica se a pasta base existe
    folder_path = verificar_pasta_env()
    print(folder_path)

    # Solicita nome do novo repositório
    nome_repo = input("Digite o nome do novo repositório: ")
    
    # Pergunta sobre configurações adicionais
    ign_cfg = input("adicionar .! e .mypkg ? (s/n): ")
    
    if ign_cfg.lower() == "s":
        # Cria repositório com arquivos de configuração
        caminho = new_repo(nome_repo)
        descript = input("Digite a descrição do repositório: ")
        adicionar_cfg(caminho, nome_repo, descript)
        adicionar_ign(caminho)

    else:
        # Cria repositório básico
        new_repo(nome_repo)

if __name__ == "__main__":
    create()