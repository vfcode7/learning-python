while True:
    print("\nBem-vindo a calculadora")
    print("Escolha a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    operacao = input("Digite sua escolha (1/2/3/4): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))   
    
    if operacao == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif operacao == '4':
        if num2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Opção inválida!")
    
    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
    if continuar != 's':
        print("Obrigado por usar a calculadora!")
        break
