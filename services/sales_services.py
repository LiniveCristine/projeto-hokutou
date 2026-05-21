from config.db import criar_conexao

def finalizar_compra_no_banco(carrinho, id_cliente, forma_pgm="Cartão"):
    """Grava a compra e os itens correspondentes respeitando a estrutura do BD."""
    if not carrinho:
        print("\nCarrinho vazio. Operação cancelada.")
        return False

    # Calcula o valor total somando (quantidade * preco_unitario) de cada item do carrinho
    valor_total = sum(item["quantidade"] * item["preco_unitario"] for item in carrinho)

    try:
        con = criar_conexao()
        cursor = con.cursor()

        # 1. Insere na tabela 'compra' 
        sql_compra = """
            INSERT INTO compra (forma_pgm, data_venda, valor_total, status_pgm, id_cliente) 
            VALUES (%s, CURRENT_TIMESTAMP, %s, %s, %s)
            RETURNING id_venda
        """
        
        cursor.execute(sql_compra, (forma_pgm, valor_total, "Pago", id_cliente))
        
        # Pega o id_venda que o banco acabou de gerar automaticamente
        id_venda = cursor.fetchone()[0]

        # 2. Insere os itens na tabela 'itens_venda'
        sql_itens = """
            INSERT INTO itens_venda (id_venda, id_produto, quantidade, preco_unitario) 
            VALUES (%s, %s, %s, %s)
        """
        
        for item in carrinho:
            valores_item = (
                id_venda, 
                item["id_produto"], 
                item["quantidade"], 
                item["preco_unitario"]
            )
            cursor.execute(sql_itens, valores_item)

        con.commit()
        print(f"\n Compra finalizada com sucesso! Cupom nº: {id_venda}")
        return True

    except Exception as e:
        print(f"\nErro ao salvar a compra no banco: {e}")
        con.rollback()
        return False
    finally:
        cursor.close()
        con.close()