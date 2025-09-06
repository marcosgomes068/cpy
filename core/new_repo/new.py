import argparse
import os
import json

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Criar um novo repositório CPY')
    parser.add_argument('name', help='Nome do repositório')
    parser.add_argument('-d', '--description', help='Descrição do repositório', default='')
    return parser.parse_args()

def new_repo(name, description=''):
    """Cria um novo repositório local com o nome fornecido."""
    # Cria o diretório base se não existir
    os.makedirs('C:/CPY', exist_ok=True)
  
    # Cria o novo repositório
    repo_path = f'C:/CPY/{name}'
    os.makedirs(repo_path, exist_ok=True)
    
    # Criar o arquivo CPY.ignore a partir do template
    cpy_ignore_path = os.path.join(repo_path, 'CPY.ignore')
    template_path = os.path.join(os.path.dirname(__file__), 'ignore_template.txt')
    with open(template_path, 'r', encoding='utf-8') as template_file:
        ignore_content = template_file.read()
    with open(cpy_ignore_path, 'w', encoding='utf-8') as ignore_file:
        ignore_file.write(ignore_content)
    
    # Criar o json de configuração do repositório
    config_path = os.path.join(repo_path, f'{name}.json')
    with open(config_path, 'w', encoding='utf-8') as config_file:
        config_data = {
            "repository_name": name,
            "created_at": "",
            "version": 0.1,
            "description": description,
            "author": "",
            "files": [],
        }
        json.dump(config_data, config_file, indent=4, ensure_ascii=False)

# Exemplo de uso via linha de comando:
# python new.py teste -d "teste de repositório"
if __name__ == "__main__":
    args = parse_arguments()
    new_repo(args.name, args.description)