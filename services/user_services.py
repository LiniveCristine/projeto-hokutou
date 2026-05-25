from config.db import criar_conexao
from config.bcrypt import checar_password, criotpgrafar


def inset_client(nome:str, senha:str, data_nsc: str):
    con = None              #Se a conexão falhar isso impede q o sistema trave
    cursor = None
    
    try:
        con= criar_conexao()
        cursor = con.cursor()

        senha = criotpgrafar(senha)

        sql = "INSERT INTO cliente(nome,senha, data_nsc) VALUES(%s,%s,%s)"
        cursor.execute(sql, (nome, senha, data_nsc))

        con.commit()
        print(f"\nCliente {nome} cadastrado\n")

    except Exception as e:
        print(f"\nErro ao inserir cliente: {e}")

    finally:
        if cursor:
            cursor.close()      #previne erro "AttributeError: 'NoneType'" junto com o comentario de cima
        if con:
            con.close()


def login(nome:str, senha:str):
    con = None
    cursor = None

    try:
        con= criar_conexao()
        cursor = con.cursor()

        sql = "SELECT nome, senha, id_cliente FROM cliente WHERE nome=%s"
        cursor.execute(sql,(nome,))
        user = cursor.fetchone()

        hash = bytes(user[1])


        if user and checar_password(senha, hash):
            return user
        
        return None

    except Exception as e:
        print(f"\nErro no login: {e}")

    finally:
            if cursor:
                cursor.close()
            if con:
                con.close()


def buscar_endereco(id_cliente: int):   
    con = None
    cursor = None

    try: 
        con= criar_conexao()
        cursor = con.cursor()

        sql = "SELECT rua, cidade, estado, cep FROM endereco WHERE id_cliente = %s"
        cursor.execute(sql,(id_cliente,))
        endereco = cursor.fetchone() 
        return endereco
        
    except Exception as e:
        print(f"\nErro ao buscar endereço: {e}")

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
    

def cadastrar_endereco(id_cliente: int, rua: str, cidade: str, estado: str, cep: str):
    con = None
    cursor = None

    try:    
        con= criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO endereco (id_cliente, rua, cidade, estado, cep) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(id_cliente, rua, cidade, estado, cep))

        con.commit()
        print("\nEndereço cadastrado com sucesso!")

    except Exception as e:
        print(f"\nErro ao cadastrar endereço: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def buscar_carrinho(id_cliente: int):
    con = None
    cursor = None
    try:
        con = criar_conexao()
        cursor = con.cursor()
        
        sql = """
            SELECT p.nome, iv.quantidade, iv.preco_unitario, c.data_venda
            FROM compra c
            JOIN itens_venda iv ON c.id_venda = iv.id_venda
            JOIN produtos p ON iv.id_produto = p.id_produdo
            WHERE c.id_cliente = %s
            ORDER BY c.data_venda DESC
            """
        cursor.execute(sql, (id_cliente,))
        
        itens = cursor.fetchall() # retorna uma lista de tuplas com todos os produtos
        return itens
        
    except Exception as e:
        print(f"\nErro ao buscar o carrinho: {e}")
        return [] # retorna uma lista vazia para não quebrar o for depois

    finally:
        if cursor: cursor.close()
        if con: con.close()
    