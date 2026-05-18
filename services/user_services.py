from config.db import criar_conexao


def inset_client(nome:str, senha:str, data_nsc: str):
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
        cursor.close()
        con.close()


def login(nome:str, senha:str):
    try:
        con= criar_conexao()
        cursor = con.cursor()

        sql = "SELECT nome, senha FROM cliente WHERE nome=%s AND senha=%s"
        cursor.execute(sql,(nome,senha))
        user = cursor.fetchone()
        return user

    except Exception as e:
        print(f"\nErro no login: {e}")

    finally:
        cursor.close()
        con.close()


