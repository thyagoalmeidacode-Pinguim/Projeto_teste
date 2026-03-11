# Entrada de dados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Escolha da operação
print("\nEscolha a operação:")
print("+  -> Soma")
print("-  -> Subtração")
print("*  -> Multiplicação")
print("/  -> Divisão")
operacao = input("Digite a operação desejada: ")

# Cálculo sem if nem dicionário
resultado = (operacao == "+" and numero1 + numero2) \
          or (operacao == "-" and numero1 - numero2) \
          or (operacao == "*" and numero1 * numero2) \
          or (operacao == "/" and numero1 / numero2)

# Exibição do resultado
print("Resultado:", resultado)