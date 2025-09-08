import os

def get_emoji_arquivo(nome_arquivo):
    # Retorna emoji baseado na extensão do arquivo
    extensoes_emojis = {
    # Código
    '.py': '🐍', '.js': '📜', '.ts': '🔵', '.html': '🌐', '.css': '🎨',
    '.json': '📋', '.xml': '🗂️', '.yml': '⚙️', '.yaml': '⚙️',
    '.java': '☕', '.c': '🔣', '.cpp': '💠', '.cs': '🖥️', '.go': '🐹',
    '.php': '🐘', '.rb': '💎', '.sh': '🐚', '.bat': '📟',
    '.rust': '🦀', '.kt': '🟣', '.swift': '🧡', '.dart': '🎯', '.scala': '🔴',
    '.r': '📊', '.matlab': '🟠', '.lua': '🌙', '.perl': '🐪', '.vue': '🟢',

    # Texto & Docs
    '.txt': '📄', '.md': '📝', '.csv': '📊', '.xlsx': '📈',
    '.docx': '📘', '.pdf': '📕', '.rtf': '📑',
    '.log': '📋', '.readme': '📖', '.license': '📜', '.gitignore': '🙈',

    # Imagens
    '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️', '.gif': '🖼️', '.svg': '🔲',
    '.ico': '🔹', '.psd': '🎨', '.ai': '🖌️',
    '.webp': '🌈', '.tiff': '🖼️', '.bmp': '🟨', '.raw': '📷',

    # Áudio & Vídeo
    '.mp3': '🎵', '.wav': '🔊', '.flac': '🎶',
    '.mp4': '🎬', '.avi': '🎥', '.mkv': '📀', '.mov': '🎞️',
    '.ogg': '🔊', '.aac': '🎧', '.m4a': '🎼', '.webm': '🌐',

    # Banco de Dados
    '.sql': '🗄️', '.db': '💾', '.sqlite': '💽', '.mdb': '🗃️',

    # Compactados
    '.zip': '📦', '.rar': '📦', '.7z': '📦', '.tar': '📦', '.gz': '📦',
    '.bz2': '🟤', '.xz': '🟡',

    # Executáveis & Sistema
    '.exe': '⚙️', '.dll': '🔧', '.sys': '🛠️', '.deb': '📦', '.rpm': '📦',
    '.apk': '📱', '.iso': '💿', '.dmg': '🍎', '.msi': '🪟',

    # Fontes & Design
    '.ttf': '🔤', '.otf': '✒️', '.woff': '🔡', '.sketch': '✏️', '.fig': '🎨',

    # Configuração
    '.ini': '🔧', '.conf': '⚙️', '.cfg': '🛠️', '.env': '🌱', '.toml': '🔩',

    # Web
    '.sass': '💗', '.scss': '💜', '.less': '💙', '.jsx': '⚛️', '.tsx': '🔷',
    '.php': '🟣', '.asp': '🔵', '.jsp': '☕'

    }
    ext = os.path.splitext(nome_arquivo)[1].lower()
    return extensoes_emojis.get(ext, '📄')

def navegador_arquivos():
    path = os.getcwd()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"📁 Pasta: {path}\n'c' confirmar\n'q' sair\n")
        
        items = sorted(os.listdir(path))
        dirs = [d for d in items if os.path.isdir(os.path.join(path, d))]
        files = [f for f in items if f not in dirs]
        
        # Listar diretórios
        for i, d in enumerate(dirs, 1):
            print(f"{i}. 📁 {d}")
        
        # Listar arquivos com emojis
        for i, f in enumerate(files, len(dirs) + 1):
            emoji = get_emoji_arquivo(f)
            print(f"{i}. {emoji} {f}")
            
        # Input do usuário
        op = input(f"\n{len(dirs)}📁 {len(files)}📄 | Nº:abrir | 'b' voltar ").lower()

        # Processar comandos
        if op == 'c': return path
        if op == 'q': 
            print("Saindo do navegador de arquivos...")
            return None
        if op == 'b': path = os.path.dirname(path) if os.path.dirname(path) != path else path
        if op.isdigit() and (num := int(op)) <= len(dirs): path = os.path.join(path, dirs[num-1])

# Exemplo de uso
if __name__ == "__main__":
    caminho = navegador_arquivos()
    print(f"\n Caminho selecionado: {caminho}")