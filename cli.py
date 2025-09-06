import shlex
import shlex

# Terminal interativo do CPY
# Permite executar comandos do controlador de versão de forma simples
def main():
    print('Bem-vindo ao terminal do CPY!')  # Mensagem de boas-vindas
    print('Digite "help" para ver os comandos disponíveis.')
    while True:
        try:
            # Lê o comando do usuário
            cmd = input('cpy > ').strip()

            # Comando para sair do terminal
            if cmd in ('exit', 'quit'):
                print('Saindo do CPY...')
                break

            # Comando de ajuda
            if cmd == 'help':
                print('Comandos:')
                print('  new <nome> [-d "descrição"]  # Cria novo repositório')
                print('  exit/quit                    # Sai do terminal')
                continue

            # Comando para criar novo repositório
            if cmd.startswith('new '):
                args = shlex.split(cmd)  # Divide argumentos como no shell
                name = args[1] if len(args) > 1 else ''  # Nome do repositório
                desc = ''  # Descrição opcional
                if '-d' in args:
                    i = args.index('-d')
                    if i+1 < len(args): desc = args[i+1]
                if name:
                    from core.new_repo import new_repo  # Importa função de criação
                    new_repo(name, desc)
                    print(f'Repositório "{name}" criado!')
                else:
                    print('Uso: new <nome> [-d "descrição"]')
                continue

            # Ignora comandos vazios
            if cmd == '': continue

            # Comando desconhecido
            print(f'Comando desconhecido: {cmd}')
        except (KeyboardInterrupt, EOFError):
            print('\nSaindo do CPY...')
            break

# Executa o terminal se chamado diretamente
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
