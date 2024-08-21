### Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
# Cálculo KPI bônus: 1000 + salario * bonus
###   
constante_bonus = 1000
nome_usuario = input("Informa seu nome: ")
salario_usuario = float(input("Informe seu salário: "))
bonus_usuario = float(input("Informe o seu bônus: "))
valor_bonus = constante_bonus + salario_usuario * bonus_usuario

print('Olá {}, seu bônus foi de R$ {}'.format(nome_usuario, valor_bonus))
print(f"{nome_usuario}, o seu bônus será de R${valor_bonus}")
