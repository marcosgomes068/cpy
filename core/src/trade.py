import os
import sys
import shutil



def trade(path_origem, path_destino=None):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    print(f"\n📁 Diretório raiz do projeto: {project_root}")

    # Limpar pasta de destino
    if os.path.exists(path_origem) and os.path.isdir(path_origem):
        try:
            for arquivo in os.listdir(path_origem):
                arquivo_path = os.path.join(path_origem, arquivo)
                if os.path.isfile(arquivo_path) or os.path.islink(arquivo_path):
                    os.remove(arquivo_path)
                    print(f"🗑️ Arquivo excluído: {arquivo_path}")
                elif os.path.isdir(arquivo_path):
                    shutil.rmtree(arquivo_path)
                    print(f"🗑️ Pasta excluída: {arquivo_path}")
            print("✅ Todos os arquivos e pastas foram excluídos da pasta.")
        except Exception as e:
            print(f"❌ Erro ao excluir arquivos: {e}")
    else:
        print("❌ Caminho inválido ou não é uma pasta.")

    # Copiar arquivos, se o destino for fornecido
    if path_destino:
        if os.path.exists(path_origem) and os.path.isdir(path_origem):
            if not os.path.exists(path_destino):
                os.makedirs(path_destino)
            
            try:
                shutil.copytree(path_origem, path_destino, dirs_exist_ok=True)
                print(f"✅ Todos os arquivos foram copiados de {path_origem} para {path_destino}.")
            except Exception as e:
                print(f"❌ Erro ao copiar arquivos: {e}")
        else:
            print("❌ Caminho de origem inválido ou não é uma pasta.")
    


if __name__ == "__main__":
    trade(r"C:\CPY\teste")