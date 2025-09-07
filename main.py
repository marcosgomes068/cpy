import os
from dotenv import load_dotenv

# Configura ambiente - carrega ou cria .env
load_dotenv()
if os.getenv('base') is None:
    with open('.env', 'w') as f:
        f.write('base=./repositorios\n')
    load_dotenv()

# Obtém caminho base
base_path = os.getenv('base')
print(f"Diretório base: {base_path}")

# Lista arquivos se diretório existir
if os.path.exists(base_path) and os.path.isdir(base_path):
    if input("Digite 1 para listar arquivos: ") == "1":

        print("Arquivos encontrados:")
        for i, arquivo in enumerate(os.listdir(base_path), start=1):
            print(f"{i}. {arquivo}")
else:
    print(f"Erro: Diretório '{base_path}' não encontrado")