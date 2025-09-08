import sys, os
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.inga_cfg.cfg import *
from utils.list import listar_pastas

def updt(caminho):
    # escolher o repositorio
    repositorio = listar_pastas()

    # verificar pasta de entrada
    pasta1 = caminho
    print(f"Diretório atual: {pasta1}")

    # caminho da pasta selecionada
    variavel_ambiente = os.getenv('base')   
    pasta2 = os.path.join(variavel_ambiente, repositorio)
    print(f"Caminho da pasta selecionada: {pasta2}")
    
    # copiar intens da pasta 1 para a pasta 2
    for item in os.listdir(pasta1):
        src_path = os.path.join(pasta1, item)
        dest_path = os.path.join(pasta2, item)
        try:
            if os.path.isdir(src_path):
                # Se for pasta, copiar com copytree (substitui se já existe)
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(src_path, dest_path)
                print(f"Pasta copiada: {src_path} para {dest_path}")
            else:
                # Se for arquivo, copiar/substituir
                shutil.copy2(src_path, dest_path)
                print(f"Arquivo copiado/substituído: {src_path} para {dest_path}")
        except PermissionError as e:
            print(f"Permissão negada ao copiar {src_path}: {e}")
        except Exception as e:
            print(f"Erro ao copiar {src_path}: {e}")

    # procurar arquivo .mypkg
    cfg_path = os.path.join(pasta2, '.mypkg')
    if os.path.isfile(cfg_path):
        print(f"Arquivo de configuração encontrado: {cfg_path}")
        # Atualizar configurações
        updt_cfg(pasta2)
    else:
        nome_repo = input("Digite o nome do repositório: ").strip()
        descript = input("Digite a descrição do repositório: ").strip()
        adicionar_cfg(caminho, nome_repo, descript)



# teste
if __name__ == "__main__":
    updt("C:\\Users\\Gabriel\\Documents\\GitHub\\cpy\\utils")