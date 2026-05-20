from services.user_services import inset_client, login 
from layouts.menu_inicial import menu_inicial
from datetime import datetime
import getpass


while True:
    print('''

        \t*** BEM VINDO AO HOKUTOU **\n
          1- Cadastre-se\n
          2- login\n
          3- Sair\n

    ''')

    try:

        op =int(input("* Digite a opção: "))

        if op == 1:
            print("\n\t*** CADASTRO ***\n")
            nome = input("\nDigite seu user: ")
            senha= getpass.getpass("Digite sua senha: ")
            data_input = input("Digite sua data de nascimento (AAAA-DD-MM): ")

            if(nome and senha and data_input):
                try:
                    data_valida = datetime.strptime(data_input, "%Y-%d-%m")
                    data_nsc = data_valida.strftime("%Y-%m-%d")
                    inset_client(nome, senha, data_nsc)
                
                except ValueError:
                    print("\n*** Erro: Formato de data inválido! Use o padrão AAAA-DD-MM. ***\n")
            
            else:
                print("\n*** Valores inválidos ***\n")


        elif op == 2:
            print("\n\t*** LOGIN ***\n")
            nome = input("\nDigite seu user: ")
            senha= getpass.getpass("Digite sua senha: ")

            if(nome and senha):
                user_validado = login(nome, senha)


                #while dentro do while?

                if(user_validado):
                    print(f"\n\t*** Bem vindo {user_validado[0]} ***\n")
                    menu_inicial(user_validado[2])


                else:
                    print("\n*** Usuário ou senha invalidos ***\n")

            else:
                print("\n*** Valores inválidos ***\n")

        else:
            break

    except ValueError:
        print("\n*** Opção invalida!! ***\n")