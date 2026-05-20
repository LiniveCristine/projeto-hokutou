from config.db import criar_conexao

def listar_produtos(id_produto:int):
    try:
        con= criar_conexao()
        cursor = con.cursor()

        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        produtos = cursor.fetchall()

        carrinho = []
        

        print("\n\t *** PRODUTOS *** \n")

        for produto in produtos:
            print(f"ID Produto: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Descrição: {produto[2]}")
            print(f"Preço: {produto[3]} reais")
            print(f"Estoque: {produto[4]}")
            print("\n\t***\n")

        print("\n\t *** COMPRAR *** \n")
        print("\nDigite 0 para sair ")

        while True:
            id_valido = False
            
            id_produto = int(input("\nDigite ID do produto: "))
            if(id_produto==0):
                break

            else:
                for produto in produtos:
                    if produto[0] == id_produto:
                        id_valido = True
                
                if id_valido == False:
                    print("\n*** ID inválido ***\n")
                    continue    
            
            quantidade = int(input("Digite a quantidade: "))
            for produto in produtos:
                if produto[0] == id_produto:
                    preco_unitario = produto[3]
                    break
            
                
                

            item_venda={
                "id_produto":id_produto,
                "quantidade": quantidade,
                "preco_unitario":preco_unitario
            }

            carrinho.append(item_venda)

            print(carrinho)





    except Exception as e:
        print(f"\nErro ao listar produtos: {e}")

    finally:
        cursor.close()
        con.close()