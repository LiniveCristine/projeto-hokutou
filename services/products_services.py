from config.db import criar_conexao

def listar_produtos():
    try:
        con= criar_conexao()
        cursor = con.cursor()

        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        produtos = cursor.fetchall()

        print("\n\t *** PRODUTOS *** \n")

        for produto in produtos:
            print(f"ID Produto: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Descrição: {produto[2]}")
            print(f"Preço: {produto[3]} reais")
            print(f"Estoque: {produto[4]}")
            print("\n\t***\n")


    except Exception as e:
        print(f"\nErro ao listar produtos: {e}")

    finally:
        cursor.close()
        con.close()