from services.products_services import listar_produtos

def menu_inicial():
    while True:         #While adicionado

        try:
            print('''

            \t*** MENU INICIAL ***\n
            1- Listar Produtos\n
            2- Carrinho\n
            3- Endereço Cadastrado\n
            4- Sair\n

            ''')

            op =int(input("* Digite a opção: "))

            if op == 1:
                listar_produtos()
                

            elif op == 2:
                print("\n\t*** CARRINHO ***\n")
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
