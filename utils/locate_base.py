import os
from dotenv import load_dotenv

def verificar_pasta_env():
    load_dotenv()
    folder_path = os.getenv('base')
    if folder_path:
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            return f"A pasta foi criada: {folder_path}"
        return f"A pasta existe: {folder_path}"
    return "A variável base não foi encontrada."
    

# Exemplo de uso
if __name__ == "__main__":
    resultado = verificar_pasta_env()
    print(resultado)
    