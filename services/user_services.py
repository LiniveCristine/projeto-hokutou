from config.db import criar_conexao


def inset_client(nome:str, senha:str, data_nsc: str):
    con = None              #Se a conexão falhar isso impede q o sistema trave
    cursor = None
    
    try:
        con= criar_conexao()
        cursor = con.cursor()

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

        sql = "SELECT nome, senha, id_cliente FROM cliente WHERE nome=%s AND senha=%s"
        cursor.execute(sql,(nome,senha))
        user = cursor.fetchone()
        return user

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
    