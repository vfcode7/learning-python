print("Bem-vindo a calculadora")
print("Escolha a operação desejada:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite sua escolha (1/2/3/4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))   

if operacao == '1':
    print(num1 + num2)
elif operacao == '2':
    print(num1 - num2)
elif operacao == '3':
    print(num1 * num2)
elif operacao == '4':
    print(num1 / num2)
else:
    print("Opção inválida") 

    print("Deseja realizar outra operação? (s/n)")
    continuar = input().lower()
    if continuar == 's':
        exec(open("calculator.py").read())
    else:
        print("Obrigado por usar a calculadora!")
        
