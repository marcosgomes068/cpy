import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.dir_act import mostrar_arvore

def adicionar_cfg(caminho, nome_repo, descript):
    """Cria arquivo de configuração .mypkg para o repositório"""
    # Garante que a pasta existe
    os.makedirs(caminho, exist_ok=True)

    # Caminho do arquivo .mypkg
    cfg_path = os.path.join(caminho, '.mypkg')

    # Conteúdo padrão do arquivo
    conteudo = f"""# Arquivo de configuração do pacote (.mypkg)

# Use este arquivo para definir propriedades do pacote ou ignorar diretórios.

[{caminho}]
name = {nome_repo}
version = 0.1.0
description = {descript}
"""

    # Cria/escreve o arquivo
    with open(cfg_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"Arquivo criado em: {cfg_path}")

def atualizar_versao(lines):
    """Atualiza a versão no arquivo de configuração"""
    for i, line in enumerate(lines):
        if line.startswith("version ="):
            version = line.split('=')[1].strip()
            major, minor, patch = map(int, version.split('.'))
            
            # Incrementar versão
            patch += 1
            if patch >= 10:
                patch = 0
                minor += 1
            if minor >= 10:
                minor = 0
                major += 1
                
            lines[i] = f"version = {major}.{minor}.{patch}\n"
            return lines
    return lines

def atualizar_campo(lines, campo, novo_valor):
    """Atualiza um campo específico no arquivo de configuração"""
    for i, line in enumerate(lines):
        if line.startswith(f"{campo} ="):
            lines[i] = f"{campo} = {novo_valor}\n"
            return lines
    return lines

def updt_cfg(caminho, nome_repo, descript):
    """Atualiza as configurações do repositório"""
    # Caminho do arquivo .mypkg
    cfg_path = os.path.join(caminho, '.mypkg')

    # Solicitar alterações do usuário
    new_name = input("Deseja alterar o nome do repositório? (Enter para pular): ")
    new_descript = input("Deseja alterar a descrição? (Enter para pular): ")

    if not os.path.isfile(cfg_path):
        print(f"O arquivo {cfg_path} não existe.")
        return

    # Ler e atualizar o arquivo
    with open(cfg_path, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        # Atualizar versão
        lines = atualizar_versao(lines)
        
        # Atualizar nome se fornecido
        if new_name:
            lines = atualizar_campo(lines, "name", new_name)
        
        # Atualizar descrição se fornecida
        if new_descript:
            lines = atualizar_campo(lines, "description", new_descript)
        
        # Escrever alterações
        f.seek(0)
        f.writelines(lines)
        f.truncate()

    print(f"Arquivo atualizado em: {cfg_path}")



# adicionar o ".!"
def adicionar_ign(caminho):
    """Cria arquivo de configuração .! (iginore) para o repositório"""
    # Garante que a pasta existe
    os.makedirs(caminho, exist_ok=True)

    # Caminho do arquivo .!
    ignr_path = os.path.join(caminho, '.!')

    # Conteúdo padrão do arquivo
    conteudo = """__pycache__/
*.py[cod]
.env/
venv/
env/
.venv/
build/
dist/
*.egg-info/
.coverage
.pytest_cache/
.mypy_cache/
.DS_Store
Thumbs.db
"""

    # Cria/escreve o arquivo
    with open(ignr_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"Arquivo .! criado em: {ignr_path}")
    return ignr_path

if __name__ == "__main__":
    adicionar_ign("C:\\CPY\\marcos")

if __name__ == "__main__":
    # Exemplo de uso
    caminho = "C:\\Users\\Gabriel\\Documents\\GitHub\\gitpy\\src\\inga-cfg"
    nome_repo = "teste"
    descript = "teste"
    
    # Criar configuração
    adicionar_cfg(caminho, nome_repo, descript)
    
    # Atualizar configuração
    updt_cfg(caminho, nome_repo, descript)