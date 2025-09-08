import os
from dotenv import load_dotenv

load_dotenv()

def listar_pastas():
    """Lista todas as pastas no diretório base com emojis e permite selecionar uma."""
    base_path = os.getenv('base', './repositorios')
    
    if not os.path.exists(base_path):
        print("❌ Diretório não encontrado")
        return None
    
    if not os.path.isdir(base_path):
        print("❌ Não é um diretório válido")
        return None
    
    pastas = [item for item in os.listdir(base_path) 
              if os.path.isdir(os.path.join(base_path, item))]
    pastas.sort()
    
    print(f"\n📁 Pastas em {base_path}:")
    print("─" * 40)
    
    for i, pasta in enumerate(pastas, 1):
        print(f"{i:2d}. 📂 {pasta}")
    
    print("─" * 40)
    print(f"📊 Total: {len(pastas)} pastas")

    if pastas:
        while True:
            try:
                escolha = int(input("\nDigite o número da pasta desejada: "))
                if 1 <= escolha <= len(pastas):
                    pasta_selecionada = os.path.join(base_path, pastas[escolha - 1])
                    print(f"\n📂 Caminho da pasta selecionada: {pasta_selecionada}")
                    return pasta_selecionada
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
    return None

if __name__ == "__main__":
    listar_pastas()