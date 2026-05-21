from config.db import criar_conexao

def obter_todos_produtos():
    """Busca a lista de produtos diretamente do banco de dados."""
    try:
        con = criar_conexao()
        cursor = con.cursor()
        
        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        produtos = cursor.fetchall()
        return produtos
    except Exception as e:
        print(f"\nErro ao buscar produtos no banco: {e}")
        return []
    finally:
        cursor.close()
        con.close()


