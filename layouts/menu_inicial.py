from services.products_services import obter_todos_produtos
from layouts.tela_compras import exibir_tela_compras
from services.user_services import buscar_endereco, cadastrar_endereco, buscar_carrinho

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
                print("\n\t*** MINHAS COMPRAS ***\n")
                
             
                itens_comprados = buscar_carrinho(id_user)

                if not itens_comprados:
                    print("**Carrinho vazio!.")
                else:
                    total_gasto = 0
                                    
                    print(f"{'DATA':<12} | {'PRODUTO':<20} | {'QTD':<5} | {'PREÇO':<10} | {'SUBTOTAL'}")
                    print("-" * 65)
                                      
                    for item in itens_comprados:

                        nome, quantidade, valor_unitario, data_compra = item 
                        
                        subtotal = quantidade * valor_unitario
                        total_gasto += subtotal
                        
                        data_str = str(data_compra)
                        
                        print(f"{data_str:<12} | {nome:<20} | {quantidade:<5} | R$ {valor_unitario:<7.2f} | R$ {subtotal:.2f}")
                    
                    print("-" * 65)
                    print(f"TOTAL: R$ {total_gasto:.2f}\n")
                    
                # pra poder ler antes de sair do carrinho
                input("Pressione ENTER para voltar ao menu...")
                    
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
                    atualizar = input("Deseja voltar ao menu? (S/N): ").strip().upper()
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

            elif op == 4:                  
                print("SAINDO DO SISTEMA!")
                break
            else:
               
                pass

        except ValueError:
            print("\n*** Opção invalida!! ***\n")
