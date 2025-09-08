import colorama
colorama.init(autoreset=True)
from colorama import Fore, Style
import os
import sys

# Adiciona o diretório raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# modulos internos
from obj.new.new import create

# Importações
try:
    from obj.objt import novo_repositorio
    from obj.objt import salvar_projeto
    from obj.objt import atualizar_repositorio
    from cli.prcs_cmd import navegador_arquivos
    from obj.objt import excluir_arquivos
    IMPORT_SUCCESS = True
except ImportError as e:
    print(f"{Fore.RED}Erro ao importar: {e}")
    IMPORT_SUCCESS = False

def mostrar_ajuda_principal():
    """Mostra ajuda do menu principal"""
    print(f"{Fore.CYAN}Comandos disponíveis:")
    print(f"{Fore.YELLOW}- Digite um caminho de pasta válido para trabalhar nela")
    print(f"{Fore.YELLOW}- 'novo' {Fore.RESET}para criar um novo repositório")
    print(f"{Fore.YELLOW}- 'buscar' {Fore.RESET}para navegar e buscar pastas facilmente")
    print(f"{Fore.YELLOW}- 'help' {Fore.RESET}para mostrar esta ajuda")
    print(f"{Fore.YELLOW}- 'sair' {Fore.RESET}para encerrar o terminal")

def mostrar_ajuda_path():
    """Mostra ajuda quando um path válido está selecionado"""
    print(f"{Fore.CYAN}Comandos disponíveis:")
    print(f"{Fore.YELLOW}- 'salvar' {Fore.RESET}para salvar o projeto atual")
    print(f"{Fore.YELLOW}- 'voltar' {Fore.RESET}para voltar ao menu principal")
    print(f"{Fore.YELLOW}- 'help' {Fore.RESET}para mostrar esta ajuda")
    print(f"{Fore.YELLOW}- 'update' {Fore.RESET}para atualizar o repositório")
    print(f"{Fore.YELLOW}- 'deletar' {Fore.RESET}para deletar o repositório")

def cmd():
    print(f"{Fore.CYAN}Terminal cpy iniciado. Digite 'help' para ver os comandos.")
    
    while True:
        green_cmd = Fore.GREEN + Style.BRIGHT + "cpy" + Style.RESET_ALL + " > "
        entrada = input(green_cmd).strip()
        
        # Comandos do menu principal
        if entrada.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o terminal. Até mais!")
            break

            
        if entrada.lower() == 'help':
            mostrar_ajuda_principal()
            continue
            
        if entrada.lower() == 'novo':
            novo_repositorio()
            continue
            
        if entrada.lower() == 'buscar':
            if IMPORT_SUCCESS:
                caminho_selecionado = navegador_arquivos()
                if caminho_selecionado:
                    print(f"{Fore.GREEN}Pasta selecionada: {caminho_selecionado}")
                    entrada = caminho_selecionado  # Define entrada para processar como caminho
                else:
                    print(f"{Fore.YELLOW}Nenhuma pasta selecionada.")
                    continue
            else:
                print(f"{Fore.RED}Funcionalidade não disponível")
                continue
            
            
        # Verifica se é um caminho válido
        if os.path.exists(entrada):
            print(f"O caminho '{entrada}' é válido.")
            path = os.path.abspath(entrada)
            print("Digite 'help' para ver os comandos disponíveis.")
            
            # Loop para comandos específicos do path
            while True:
                comando = input(green_cmd).strip().lower()
                
                if comando == 'help':
                    mostrar_ajuda_path()
                    
                elif comando == 'salvar':             
                    salvar_projeto(entrada)

                elif comando == 'update':
                    atualizar_repositorio(entrada)

                elif comando == 'deletar':
                    print("deletando")
                    excluir_arquivos(entrada)

                elif comando == 'voltar':
                    break
                    
                else:
                    print("Comando desconhecido. Digite 'help' para ajuda.")


if __name__ == "__main__":
    cmd()