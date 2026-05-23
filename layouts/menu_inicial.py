from services.products_services import obter_todos_produtos
from layouts.tela_compras import exibir_tela_compras
from services.user_services import buscar_endereco, cadastrar_endereco

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

                endereco_atual = buscar_endereco(id_user)

                if endereco_atual:

                    rua, cidade, estado, cep,  = endereco_atual
                    print(f"\nEndereço de entrega atual:")
                    print(f"Rua: {rua}")                        #retirado o numero pq não tinha no banco
                    print(f"Cidade: {cidade} | CEP: {cep}\n")
                    print(f"Estado: {estado}")
                    
                    # Opcional: Perguntar se quer atualizar
                    atualizar = input("Deseja atualizar este endereço? (S/N): ").strip().upper()
                    if atualizar != 'S':
                        continue
                else:
                    print("\nVocê ainda não possui um endereço cadastrado.")
                    cadastrar = input("Deseja cadastrar agora? (S/N): ").strip().upper()
                    if cadastrar != 'S':
                        continue
                    else:   
                        print("\n** Preencha os dados do endereço **")
                        rua =  input ("Digite sua rua:")
                        cidade = input ("Digite sua cidade:")
                        estado = input ("Digite seu estado:")
                        cep = input ("Digite seu CEP:")

                        cadastrar_endereco(id_user, rua,cidade,estado,cep)
                


                pass

            elif op == 4:                   #opção 4 pra sair colocada, meio que serve como logout(?)
                print("SAINDO DO SISTEMA!")
                break
            else:
                #como fazer logout do usuário??
                pass

        except ValueError:
            print("\n*** Opção invalida!! ***\n")
