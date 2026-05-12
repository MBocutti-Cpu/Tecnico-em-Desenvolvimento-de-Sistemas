#CALCULADORA BÁSICA
print("=== Calculadora ===\n")

num1 = float(input("Digite o primeiro número:"))
operador = input("Digite o operador: (+, -, /, *)")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    if num2 == 0:
        print("não é possivel realizar")
    else:
        print(num1 / num2)
else:
    print("operador invalido")
    
