###
""" 
Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
Cálculo KPI bônus: 1000 + salario * bonus

Desafio - Refatorar o projeto da aula anterior evitando Bugs: aula01/kpi.py
Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos
para salário e bônus, você pode modificar o código diretamente. 
Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos
 """
###
constante_bonus = 1000
try:
    print("Desafio KPI Aula01 - Refatoração")
    nome_usuario = input("Informe seu nome: ")
    salario_usuario = float(input("Informe seu salário: "))
    bonus_usuario = float(input("Informe o seu bônus: "))
    msg_erro = ""
    if salario_usuario <= 0 or bonus_usuario <= 0 or len(nome_usuario) == 0:
        if len(nome_usuario) == 0:
            # print('Informe nome de usuário. \n')
            msg_erro = 'Informe nome de usuário. \n'
        if salario_usuario <= 0:
            #print(f'Salário informado {salario_usuario} deve ser maior que zero')
            msg_erro = msg_erro + f'Salário informado {salario_usuario} deve ser maior que zero \n'
        if bonus_usuario <= 0:
            msg_erro = msg_erro + f'Bonus informado {bonus_usuario} deve ser maior que zero \n'
            #print(f'Bonus informado {bonus_usuario} deve ser maior que zero')
        if len(msg_erro) > 0:
            print(msg_erro)
    elif any(char.isdigit() for char in nome_usuario):
        msg_erro = f'Nome informado: {nome_usuario}. Nome usuário não deve conter números.'
        print(msg_erro)
    else:
        valor_bonus = (constante_bonus + salario_usuario * bonus_usuario) - salario_usuario
        print(f'Prezado(a) {nome_usuario}.  Seu salário é de R${salario_usuario:.2f} e seu bônus final será de R${valor_bonus:.2f}')
except ValueError:
    print("Erro! Verifique salário e bonus informados.")
