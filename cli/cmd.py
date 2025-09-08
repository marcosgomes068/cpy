import colorama
colorama.init(autoreset=True)
from colorama import Fore, Style
import os
import sys

# Adiciona o diretório utils ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

# Importações
try:
    from obj.objt import novo_repositorio
    from obj.objt import salvar_projeto
    IMPORT_SUCCESS = True
except ImportError as e:
    print(f"{Fore.RED}Erro ao importar: {e}")
    IMPORT_SUCCESS = False

def mostrar_ajuda_principal():
    """Mostra ajuda do menu principal"""
    print(f"{Fore.CYAN}Comandos disponíveis:")
    print(f"{Fore.YELLOW}- Digite um caminho de pasta válido para trabalhar nela")
    print(f"{Fore.YELLOW}- 'novo' {Fore.RESET}para criar um novo repositório")
    print(f"{Fore.YELLOW}- 'help' {Fore.RESET}para mostrar esta ajuda")
    print(f"{Fore.YELLOW}- 'sair' {Fore.RESET}para encerrar o terminal")

def mostrar_ajuda_path():
    """Mostra ajuda quando um path válido está selecionado"""
    print(f"{Fore.CYAN}Comandos disponíveis:")
    print(f"{Fore.YELLOW}- 'salvar' {Fore.RESET}para salvar o projeto atual")
    print(f"{Fore.YELLOW}- 'voltar' {Fore.RESET}para voltar ao menu principal")
    print(f"{Fore.YELLOW}- 'help' {Fore.RESET}para mostrar esta ajuda")
    print(f"{Fore.YELLOW}- 'update' {Fore.RESET}para atualizar o repositório (em breve)")
    print(f"{Fore.YELLOW}- 'deletar' {Fore.RESET}para deletar o repositório (em breve)")

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
            if IMPORT_SUCCESS:
                try:
                    novo_repositorio()
                except Exception as e:
                    print(f"{Fore.RED}Erro ao criar repositório: {e}")
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
                    if IMPORT_SUCCESS:
                        try:
                            salvar_projeto()
                        except Exception as e:
                            print(f"{Fore.RED}Erro ao salvar projeto: {e}")
                    else:
                        print(f"{Fore.RED}Funcionalidade não disponível")
                        
                elif comando == 'update':
                    print("Funcionalidade de update ainda não implementada.")

                elif comando == 'deletar':
                    print("Funcionalidade de deletar ainda não implementada.")

                

                elif comando == 'voltar':
                    break
                    
                else:
                    print("Comando desconhecido. Digite 'help' para ajuda.")
                    
        else:
            print(f"O caminho '{entrada}' não é válido. Digite 'help' para ajuda.")

if __name__ == "__main__":
    cmd()