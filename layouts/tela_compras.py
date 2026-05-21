from services.products_services import obter_todos_produtos
from services.sales_services import finalizar_compra_no_banco

def exibir_tela_compras(id_cliente):
    # 1. Pega os produtos do serviço
    produtos = obter_todos_produtos()
    
    if not produtos:
        print("\nNão há produtos cadastrados.")
        return

    # 2. Exibe os produtos na tela
    print("\n\t *** PRODUTOS *** \n")
    for produto in produtos:
        print(f"ID Produto: {produto[0]}") # id_produdo
        print(f"Nome: {produto[1]}")       # nome
        print(f"Descrição: {produto[2]}")  # descricao
        print(f"Preço: {produto[3]} reais")# preco
        print(f"Estoque: {produto[4]}")    # qnt_estoque
        print("\n\t***\n")

    print("\n\t *** COMPRAR *** \n")
    print("Digite 0 para voltar ao menu ")
    print("Digite 'F' para finalizar compra ")

    carrinho = []

    # 3. Loop do Carrinho
    while True:
        id_valido = False
        preco_unitario = 0
        
        op = input("\nDigite ID do produto: ").strip()
        
        if op == '0':
            print("\nVoltando para o menu principal...")
            return # Aborta o fluxo de compras e retorna ao menu anterior
            
        if op.upper() == 'F':
            print("\n--- FECHANDO CARRINHO ---")
            break

        try:
            id_produto = int(op)
        except ValueError:
            print("\n*** Entrada inválida! Digite um ID numérico, '0' ou 'F' ***\n")
            continue

        # Validação do ID corrigida (Varre todos e pega o preço se achar)
        for produto in produtos:
            if produto[0] == id_produto:
                id_valido = True
                preco_unitario = produto[3]
                break
            
        if not id_valido:
            print("\n*** ID inválido ***\n")
            continue    
        
        quantidade = int(input("Digite a quantidade: "))
        
        # Monta o dicionário e adiciona no array local
        item_venda = {
            "id_produto": id_produto,
            "quantidade": quantidade,
            "preco_unitario": preco_unitario
        }
        carrinho.append(item_venda)
        print(f"\nItem adicionado! Itens no carrinho atualmente: {len(carrinho)}")

    # 4. Ao sair do loop (pressionou 'F'), envia o carrinho para o banco salvar
    if len(carrinho) > 0:
        # Aqui você pode pedir a forma de pagamento se quiser, ou passar fixo
        forma_pgm = input("Digite a forma de pagamento (Dinheiro/Cartão): ").strip()
        finalizar_compra_no_banco(carrinho, id_cliente, forma_pgm=forma_pgm) # Passei id_cliente=1 como exemplo
    else:
        print("\nNenhum item foi adicionado ao carrinho.")