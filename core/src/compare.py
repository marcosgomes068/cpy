import os
import filecmp
from pathlib import Path

def comparar_pastas_simples(caminho1, caminho2):
    """
    Versão simplificada para comparar duas pastas.
    """
    if not os.path.exists(caminho1) or not os.path.exists(caminho2):
        print("Um ou ambos os caminhos não existem.")
        return 0
    
    # Coletar todos os arquivos
    arquivos1 = set()
    for raiz, _, arquivos in os.walk(caminho1):
        for arquivo in arquivos:
            caminho_relativo = os.path.relpath(os.path.join(raiz, arquivo), caminho1)
            arquivos1.add(caminho_relativo)
    
    arquivos2 = set()
    for raiz, _, arquivos in os.walk(caminho2):
        for arquivo in arquivos:
            caminho_relativo = os.path.relpath(os.path.join(raiz, arquivo), caminho2)
            arquivos2.add(caminho_relativo)
    
    # Encontrar arquivos comuns e diferentes
    comuns = arquivos1.intersection(arquivos2)
    exclusivos1 = arquivos1 - arquivos2
    exclusivos2 = arquivos2 - arquivos1
    
    # Verificar quais arquivos comuns são idênticos
    identicos = 0
    diferentes = 0
    
    for arquivo in comuns:
        caminho_completo1 = os.path.join(caminho1, arquivo)
        caminho_completo2 = os.path.join(caminho2, arquivo)
        
        if filecmp.cmp(caminho_completo1, caminho_completo2, shallow=False):
            identicos += 1
        else:
            diferentes += 1
    
    total_arquivos = len(arquivos1.union(arquivos2))
    
    if total_arquivos == 0:
        taxa_semelhanca = 1.0
    else:
        # Calcular taxa de semelhança
        semelhantes = identicos + (diferentes * 0.5)
        taxa_semelhanca = semelhantes / total_arquivos
    
    # Exibir resultados
    print(f"Arquivos idênticos: {identicos}")
    print(f"Arquivos diferentes: {diferentes}")
    print(f"Arquivos exclusivos na pasta 1: {len(exclusivos1)}")
    print(f"Arquivos exclusivos na pasta 2: {len(exclusivos2)}")
    print(f"Taxa de semelhança: {taxa_semelhanca:.2%}")
    
    return taxa_semelhanca

# Exemplo de uso
if __name__ == "__main__":
    taxa = comparar_pastas_simples("pasta1", "pasta2")
    print(f"Taxa de semelhança: {taxa:.2%}")