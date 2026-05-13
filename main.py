from services.user_services import inset_client 




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
            nome = input("\nDigite seu user: ")
            senha= input("Digite sua senha: ")
            data_nsc = input("Digite sua data de nascimento (AAAA-DD-MM): ")

            inset_client(nome, senha, data_nsc)


        elif op == 2:
            pass
    
        else:
            break

    except ValueError:
        print("\n*** Opção invalida!! ***\n")