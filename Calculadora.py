import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Erro: Divisão por zero"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x) if x >= 0 else "Erro: Raiz quadrada de número negativo"

def get_user_input(message):
    return float(input(message))

def calculator():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        '5': power,
        '6': square_root
    }

    print("Selecione a operação:")
    for key, value in operations.items():
        print(f"{key}. {value.__name__.capitalize()}")

    choice = input("Digite a opção (1/2/3/4/5/6): ")

    if choice in operations:
        num1 = get_user_input("Digite o primeiro número: ")

        if choice != '6':
            num2 = get_user_input("Digite o segundo número: ")

        result = operations[choice](num1, num2) if choice != '6' else operations[choice](num1)
        print(f"Resultado: {result}")
    else:
        print("Opção inválida")

if __name__ == "__main__":
    calculator()
