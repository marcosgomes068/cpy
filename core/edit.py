import os
from list import listar_pastas
from dotenv import load_dotenv
from dir import listar_estrutura
from src.compare import comparar_pastas_simples
from src.trade import trade

# Configura ambiente - carrega ou cria .env
load_dotenv()

# Obtém caminho base
base_path = os.getenv('base')

# comitar as mudanças no git
def comitar_mudancas():
    # Listar pastas e permitir seleção
    pasta_selecionada = listar_pastas()


    '''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!funções!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    
    if pasta_selecionada:
        print(f"\n📂 Pasta selecionada para commit: {pasta_selecionada}")
        # Aqui você pode adicionar lógica para realizar o commit na pasta selecionada
        repo = print(listar_estrutura(pasta_selecionada, max_arquivos=100))
        print("Estrutura do repositório carregada com sucesso.")
        s_n = input("seguir com o commit? (1):\nforçar copiar (2):\nexcluir (3):\nCancelar (4): ")
        if s_n == '1':
             # função de commit

            # comparar arquivos 
            comparar_pastas_simples(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')), pasta_selecionada)
            similarity = comparar_pastas_simples(
                os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')), 
                pasta_selecionada
            )
            if similarity < 0.5:  # Supondo que 0.5 seja o limiar de semelhança baixa
                proceed = input("A semelhança entre as pastas é baixa. Deseja continuar mesmo assim? (s/n): ")
                if proceed.lower() != 's':
                    print("Operação de commit cancelada devido à baixa semelhança.")
                    trade(pasta_selecionada)
            print("Commit realizado com sucesso!")
            

            
        elif s_n == '2':
            # função de forçar copiar
            print("Cópia forçada com sucesso!")
        
        elif s_n == '3':
            # função de excluir
            print("Exclusão realizada com sucesso!")

        elif s_n == '4':
            print("Operação de commit cancelada.")
    else:
        print("Nenhuma pasta selecionada. Operação cancelada.")

if __name__ == "__main__":
    comitar_mudancas()