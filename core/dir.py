import os
from pathlib import Path

def obter_emoji_arquivo(nome_arquivo):
    """Retorna emoji baseado na extensão do arquivo"""
    extensao = os.path.splitext(nome_arquivo)[1].lower()
    
    emojis = {
        '.py': '🐍', '.js': '🟨', '.ts': '🔷', '.html': '🌐', '.css': '🎨',
        '.json': '📋', '.xml': '📰', '.yaml': '⚙️', '.yml': '⚙️', '.sql': '🗄️',
        '.md': '📖', '.txt': '📝', '.pdf': '📄', '.jpg': '🖼️', '.png': '🖼️',
        '.gif': '🎬', '.svg': '🎨', '.zip': '🗜️', '.rar': '🗜️', '.exe': '⚙️',
        '.sh': '🐚', '.java': '☕', '.cpp': '⚡', '.php': '🐘', '.rb': '💎',
    }
    
    return emojis.get(extensao, '📄')

def listar_estrutura(base_path='.', **kwargs):
    # Configurações padrão
    config = {
        'ignorar': {'.git', '__pycache__', '.idea', '.vscode'},
        'max_arquivos': 5,
        'mostrar_ocultos': False
    }
    config.update(kwargs)
    
    base_path = Path(base_path).resolve()
    
    if not base_path.exists():
        return f"❌ Diretório não encontrado: {base_path}"
    
    if not base_path.is_dir():
        return f"❌ Não é um diretório: {base_path}"
    
    resultado = []
    resultado.append(f"\n📁 Estrutura de: {base_path}")
    resultado.append("─" * 50)
    
    for root, dirs, files in os.walk(base_path):
        root_path = Path(root)
        
        # Filtrar diretórios
        dirs[:] = [d for d in dirs 
                  if (config['mostrar_ocultos'] or not d.startswith('.')) 
                  and d not in config['ignorar']]
        
        # Filtrar arquivos
        files = [f for f in files 
                if config['mostrar_ocultos'] or not f.startswith('.')]
        
        # Calcular nível
        try:
            level = len(root_path.relative_to(base_path).parts)
        except ValueError:
            level = 0
        
        # Adicionar pasta ao resultado
        indent = '    ' * level
        emoji_pasta = "📂" if level > 0 else "📁"
        linha_pasta = f"{indent}├── {emoji_pasta} {os.path.basename(root)}/"
        resultado.append(linha_pasta)
        
        # Adicionar arquivos ao resultado
        file_indent = '    ' * (level + 1)
        for file in files[:config['max_arquivos']]:
            emoji = obter_emoji_arquivo(file)
            resultado.append(f"{file_indent}├── {emoji} {file}")
        
        # Indicador de mais arquivos
        if len(files) > config['max_arquivos']:
            resultado.append(f"{file_indent}└── 📄 ...({len(files) - config['max_arquivos']} mais)")
    
    return '\n'.join(resultado)

# Função de conveniência para uso rápido
def listar_dir(caminho='.', max_arquivos=3):
    """Lista rápida de um diretório"""
    return listar_estrutura(caminho, max_arquivos=max_arquivos)

