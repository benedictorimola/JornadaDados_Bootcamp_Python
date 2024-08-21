print('#####  Exercícios - NÚMEROS INTEIROS  #####')
print('Exercício 1 - soma dois números inteiros inseridos pelo usuário')
#valor_1 = int(input("Informe o valor 1 inteiro: "))
#valor_2 = int(input("Informe o valor 2 inteiro: "))
valor_1 = int(32)
valor_2 = int(10)
valor_total = valor_1 + valor_2
print(f'{valor_1} + {valor_2} = {valor_total}')
print("\n")

print('Exercício 2 - recebe um número do usuário e calcule o resto da divisão desse número por 5.')
# valor = int(input("Informe o valor inteiro: "))
valor = int(18)
resultado_calculo = valor % 5 
print(f'Valor informado: {valor}')
print(f'O resultado : {resultado_calculo}')
print("\n")

print("Exercício 3 - multiplica dois números fornecidos pelo usuário e mostre o resultado")
#valor_1 = int(input("Informe o primeiro núnero inteiro: "))
#valor_2 = int(input("Informe o segundo número inteiro : "))
valor_1 = int(20)
valor_2 = int(5)
resultado_calculo = valor_1 * valor_2
print(f'{valor_1} x {valor_2} = {resultado_calculo}')
print("\n")

print("Exercício 4 - programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo")
#valor_1 = int(input("Informe o primeiro número inteiro: "))
#valor_2 = int(input("Informe o segundo número inteiro : "))
valor_1 = int(27)
valor_2 = int(5)
resultado_calculo = valor_1 // valor_2
print(f'{valor_1} / {valor_2} = {resultado_calculo}')
print("\n")

print("Exercicio 5 - programa que calcule o quadrado de um número fornecido pelo usuário")
#valor_1 = int(input("Informe um número inteiro: "))
valor_1 = int(9)
potenciacao = int(2)
resultado_calculo = valor_1 ** potenciacao
print(f"{valor_1} elevado a {potenciacao} = {resultado_calculo}")
print("\n")


print('#####  Exercícios - NÚMEROS PONTO FLUTUANTE  #####')
print("Exercício 6 - programa que receba dois números flutuantes e realize sua adição")
#valor_1 = float(input("Informe o primeiro número com ponto flutuante: "))
#valor_2 = float(input("Informe o segundo número com ponto flutuante : "))
valor_1 = float(15.6)
valor_2 = float(22.85)
resultado_calculo = valor_1 + valor_2
print(f'{valor_1} + {valor_2} = {resultado_calculo}')
print("\n")

print("Exercício 7 -  programa que calcule a média de dois números flutuantes fornecidos pelo usuário.")
#valor_1 = float(input("Informe o primeiro número com ponto flutuante: "))
#valor_2 = float(input("Informe o segundo número com ponto flutuante : "))
valor_1 = float(10.8)
valor_2 = float(12.2)
resultado_calculo = (valor_1 + valor_2) / 2
print(f'A média dos números {valor_1} + {valor_2} é {resultado_calculo}')
print("\n")
 
print("Exercício 8 -  programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).")
#valor_base = float(input("Informe o valor base com ponto flutuante: "))
#valor_expoente = float(input("Informe o expoenete com ponto flutuante : "))
valor_base = float(5)
valor_expoente = float(3)
resultado_calculo = valor_base ** valor_expoente
print(f' {valor_base} elevado a {valor_expoente} = {resultado_calculo}')
print("\n")


print("Exercício 9 -   programa que converta a temperatura de Celsius para Fahrenheit.).")
#valor_celsius = float(input("Informe o valor em celsius: "))
valor_celsius = float(40)
valor_fahrenheit = (valor_celsius * 9/5) + 32
print(f' {valor_celsius} graus celsius =  {valor_fahrenheit} Fahrenheit')
print("\n")

print("Exercício 10 - programa que calcule a área de um círculo, recebendo o raio como entrada.")
import math
#valor_raio = float(input("Informe o valor do raio: "))
valor_raio = float(2)
constante_pi = math.pi
area_circulo = constante_pi * (valor_raio ** 2)
print(f' àrea do círculo com raio igual a {valor_raio} é {area_circulo:.2f} ')
print("\n")

print('#####  Exercícios - STRINGS  #####')
print("Exercício 11 - programa que receba uma string do usuário e a converta para maiúsculas")
# nome = str(input("Informe seu nome: ")).upper()
nome = str("Benedicto").upper()
print(nome) 
print("\n") 

print("Exercício 12 - programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas")
# nome = str(input("Informe seu nome: ")).lower()
nome = str("Benedicto Rimola").lower()
print(nome)
print("\n")

print("Exercício 13 - programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.")
# frase = str(input("Digite uma frase: ")).strip()
frase = str("   Estou praticando python.   ").strip()
print(frase)
print("\n")

print("Exercício 14 - programa que peça ao usuário para digitar uma data no formato dd/mm/aaaa e, em seguida, imprima o dia, o mês e o ano separadamente.")
#data_informada = str(input("Digite uma data no formato dd/mm/aaaa: ")).split(sep="/")
data_informada = str("19/08/2024").split(sep="/") 
print(data_informada[0], data_informada[1], data_informada[2])  
print("\n") 

print("Exercício 15 - programa que concatene duas strings fornecidas pelo usuário.")
#palavra_1 = str(input("Digite uma palavra: "))
#palavra_2 = str(input("Digite uma palavra: "))
palavra_1 = str("Jornada")
palavra_2 = str("Dados")
palavra = palavra_1 + palavra_2
print(palavra)
print("\n")


print('#####  Exercícios - BOOLEANOS  #####')
valor_1 = True
valor_2 = False


print("Exercício 16 - programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.")
# Exemplo de entrada
resultado_and = valor_1 and valor_2
print("Resultado do AND lógico:", resultado_and)
print("\n")

print("Exercício 17 - programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.")
resultado_or = valor_1 or valor_2
print("Resultado do OR lógico:", resultado_or)
print("\n")


print("Exercício 18 - programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.")
resultado_not = not valor_1
print("Resultado do NOT lógico:", resultado_not)
print("\n")


print("Exercício 19 - programa que compare se dois números fornecidos pelo usuário são iguais.")
num_1 = 5
num_2 = 5
resultado_igualdade = (num_1 == num_2)
print("Resultado da igualdade:", resultado_igualdade)
print("\n")


print("Exercício 20 - programa que verifique se dois números fornecidos pelo usuário são diferentes.")
resultado_diferenca = (num_1 != num_2)
print("Resultado da diferença:", resultado_diferenca)
print("\n")
