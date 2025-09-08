import os
import shutil

def delete(caminho):
    # Verifica se o caminho existe
    if not os.path.exists(caminho):
        print(f"O caminho '{caminho}' não existe.")
        return
    # deletar arquivo ou pasta facilmente
    try:
        if os.path.isfile(caminho):
            os.remove(caminho)
            print(f"Arquivo '{caminho}' deletado com sucesso.")
        elif os.path.isdir(caminho):
            shutil.rmtree(caminho)
            print(f"Pasta '{caminho}' deletada com sucesso.")
        else:
            print(f"O caminho '{caminho}' não é um arquivo ou pasta válido.")
    except Exception as e:
        print(f"Erro ao deletar '{caminho}': {e}")