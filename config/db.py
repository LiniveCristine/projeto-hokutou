import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='postgres', 
            user='postgres',
            password= '123456x',
            host= 'localhost',
            port= '5432'
        )
    
        return conn
    except Exception as e:
        print(f'Erro de conexão {e}')