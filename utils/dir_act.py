import os


def mostrar_arvore(caminho):
    tree = []
    for root, dirs, files in os.walk(caminho):
        level = root.replace(caminho, '').count(os.sep)
        indent = ' ' * 4 * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree.append(f"{subindent}{f}")
    return '\n'.join(tree)

# Exemplo de uso
if __name__ == "__main__":   
    caminho = "C:\\Users\\Gabriel\\Documents\\GitHub\\cpy"  # ou qualquer outro caminho desejado
    arvore = mostrar_arvore(caminho)
    print(arvore)