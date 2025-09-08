import os
import json
import shutil
from inga_cfg.cfg import adicionar_ign

def clear_ignr(caminho):
    ignr_path = os.path.join(caminho, '!.json')
    if not os.path.exists(ignr_path):
        adicionar_ign(caminho)
    
    try:
        with open(ignr_path, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        pastas = dados.get('pastas', [])
        arquivos = dados.get('arquivos', [])
    except (json.JSONDecodeError, FileNotFoundError):
        print("Erro ao ler arquivo !.json - usando configuracao padrao")
        pastas = ["__pycache__", "venv", "env", ".venv", "build", "dist", ".pytest_cache", ".mypy_cache"]
        arquivos = [".coverage", ".DS_Store", "Thumbs.db", "*.db"]
    
    pastas_encontradas, arquivos_encontrados = [], []
    
    for root, dirs, files in os.walk(caminho):
        for pasta in pastas:
            pasta_nome = pasta.rstrip('/') if pasta.endswith('/') else pasta
            for dir_name in dirs:
                if pasta_nome in dir_name or dir_name == pasta_nome:
                    pasta_completa = os.path.join(root, dir_name)
                    if pasta_completa not in pastas_encontradas:
                        pastas_encontradas.append(pasta_completa)
        
        for arquivo in arquivos:
            for file_name in files:
                if (arquivo.startswith('*') and file_name.endswith(arquivo[1:])) or file_name == arquivo:
                    arquivo_completo = os.path.join(root, file_name)
                    if arquivo_completo not in arquivos_encontrados:
                        arquivos_encontrados.append(arquivo_completo)
    
    total = len(pastas_encontradas) + len(arquivos_encontrados)
    print(f"Itens encontrados: {total} ({len(pastas_encontradas)} pastas, {len(arquivos_encontrados)} arquivos)")
    
    if total > 0:
        pastas_excluidas, arquivos_excluidos = 0, 0
        
        for pasta in pastas_encontradas:
            try:
                shutil.rmtree(pasta)
                pastas_excluidas += 1
            except Exception as e:
                print(f"Erro ao excluir pasta {pasta}: {e}")
        
        for arquivo in arquivos_encontrados:
            try:
                os.remove(arquivo)
                arquivos_excluidos += 1
            except Exception as e:
                print(f"Erro ao excluir arquivo {arquivo}: {e}")
        
        print(f"Exclusao concluida: {pastas_excluidas}/{len(pastas_encontradas)} pastas e {arquivos_excluidos}/{len(arquivos_encontrados)} arquivos removidos")
    else:
        print("Nenhum item encontrado para exclusao.")
    
    return pastas_encontradas, arquivos_encontrados

if __name__ == "__main__":
    caminho = "C:\\Users\\Gabriel\\Documents\\GitHub\\cpy"
    clear_ignr(caminho)