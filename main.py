# uso facilitado
from utils.dir_act import mostrar_arvore

def terminal_chat():
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o chat. Até mais!")
            break
        
            print("Comando não reconhecido. Tente novamente.")
        


if __name__ == "__main__":
    terminal_chat()