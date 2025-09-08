# ponto de partida do programa
from colorama import Fore, Style
from cli.cmd import cmd

if __name__ == "__main__":
    print(f"{Fore.GREEN}Iniciando o programa...{Style.RESET_ALL}")
    cmd()