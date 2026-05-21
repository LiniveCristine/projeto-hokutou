from services.products_services import obter_todos_produtos
from layouts.tela_compras import exibir_tela_compras

def menu_inicial(id_user:int):
    while True:         

        try:
            print('''

            \t*** MENU INICIAL ***\n
            1- Listar Produtos\n
            2- Minhas compras\n
            3- Endereço Cadastrado\n
            4- Sair\n

            ''')

            op =int(input("* Digite a opção: "))

            if op == 1:
                exibir_tela_compras(id_user)
                

            elif op == 2:
                print("\n\t*** CARRINHO ***\n")
                #chamar a lista carrinho e fazer um for
                pass


            elif op == 3:
                print("\n\t*** ENDEREÇO CADASTRADO ***\n")
                pass

            elif op == 4:                   #opção 4 pra sair colocada, meio que serve como logout(?)
                print("SAINDO DO SISTEMA!")
                break
            else:
                #como fazer logout do usuário??
                pass

        except ValueError:
            print("\n*** Opção invalida!! ***\n")
