""" 
Exercício 21: Conversor de Temperatura
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida. 
"""
""" 
try:
    print("Exercício 21: Conversor de Temperatura")
    valor_celsius = float(input("Informe o valor em celsius: "))
    valor_fahrenheit = (valor_celsius * 9/5) + 32
    print(f' {valor_celsius} graus celsius =  {valor_fahrenheit} Fahrenheit')
    print("\n")
except TypeError as msg_error:
    print(f'Ocorreu o seguinte erro: {msg_error}')        
except ValueError:
    print("Grau celsius deve ser um valor numérico")
 """
 
 
""" Exercício 22: Verificador de Palíndromo
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize try-except para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada. """
# Observação: como defini no input que o valor digitado deve ser string a validação isinstance() não será necessária.

""" try:
    print("Exercício 22: Verificador de Palíndromo")
    frase = str(input("Informe uma frase: "))
    frase_formatada = frase.replace(" ", "").lower()
    if frase_formatada == frase_formatada [::-1]:
        print("É um palíndrono")
    else:
        print("Não é um palindrono")
except TypeError as e:
    print(f'Ocorreu o seguinte erro: {e}')
except ValueError as e:
    print(e)        
 """
 
""" Exercício 23: Calculadora Simples
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
Use try-except para lidar com divisões por zero e entradas não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
Imprima o resultado ou uma mensagem de erro apropriada. """

""" try:
    valor_1 = float(input("Informe o primeiro valor: "))
    valor_2 = float(input("Informe o segundo valor : "))
    operador = str(input("Informe a operação aritiméca (adição(+), subtração(-), divisão(/) ou multiplicação(*)): ")).strip()
    resultado = None
    if operador == "+":
        resultado = valor_1 + valor_2
    elif operador == "-":
        resultado = valor_1 - valor_2
    elif operador == "*":
        resultado = valor_1 * valor_2
    elif operador == "/":
        resultado = valor_1 / valor_2
    else:
        print(f'Operador {operador}  inválido. Informe uma operação aritiméca válida (adição(+), subtração(-), divisão(/) ou multiplicação(*))')
    print(resultado)
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Não é possível fazer divisão por zero") 
     """
     
""" Exercício 24: Classificador de Números
Escreva um programa que solicite ao usuário para digitar um número. 
Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar".    """
""" try: 
    numero = int(input("Informe um número inteiro: "))
    if numero == 0:
        classifica_numero = "é zero"
    elif numero < 0:
        classifica_numero = "é negativo"
    else:
        classifica_numero = "é positivo"
    resto = numero % 2
    if resto == 0:
        par_impar = "par"
    else:
        par_impar = "impar"
    print(f'O número {numero} é {classifica_numero} e é um número {par_impar}')
except ValueError:
    print("Informe um número inteiro válido.")
 """
     
""" Exercício 25: Conversão de Tipo com Validação
Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
O programa deve converter a string de entrada em uma lista de números inteiros. 
Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.     """
try:
    lista_numeros = input("Digite uma lista de números separados por vírgula: ")
    numeros_str = lista_numeros.split(",")
    numeros_int = []
    try:
        for num in numeros_str:
            numeros_int.append(int(num.strip()))
        print(f'Lista de inteiros: {numeros_int}')
    except ValueError:
        print("Os elementos digitados devem ser números inteiros.")
finally:
    print("Programa finalizado")