import os

def ler_repositorio(caminho):
    # Retorna uma árvore de diretórios a partir do caminho
    tree = []
    for root, dirs, files in os.walk(caminho):
        level = root.replace(caminho, '').count(os.sep)
        indent = ' ' * 4 * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree.append(f"{subindent}{f}")
    return '\n'.join(tree)

print(ler_repositorio('.'))