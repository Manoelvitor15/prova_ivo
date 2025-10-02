

def valor_ascendente():
    print("Valores de forma ascendente (menor para maior)")
    lista_num = []
    contagem = 0

    while contagem < 3:
        num = int(input(f"Insira o {contagem + 1} número: "))
        lista_num.append(num)
        contagem = contagem + 1
        lista_num.sort()
    print(lista_num)

#valor_ascendente()

def numero_divisivel():
    print("Verificador de divisibilidade por 10, 5 ou 2.")
    try:
        num = int(input("Insira um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

    lista_divisores = [10, 5, 2]
    if (num % lista_divisores[0] == 0) or \
       (num % lista_divisores[1] == 0) or \
       (num % lista_divisores[2] == 0):
        print(f"\nO número {num} é divisível por:")
        encontrou_divisor = False 
        for divisor in lista_divisores:
            if num % divisor == 0:
                print(f"- {divisor}")
                encontrou_divisor = True
        if encontrou_divisor:
            print(f"\nConclusão: O número {num} é divisível por 10, 5 ou 2.")

    else:
        print(f"\nConclusão: O número {num} não é divisível por 10, 5 ou 2.")
#numero_divisivel()

def linha_de_credito():
    print("--- Linha de Crédito para Funcionários Estatutários ---")
    try:
        salario = float(input("Insira o Salário Bruto (R$): "))
        prestacao = float(input("Insira o Valor da Prestação Desejada (R$): "))
        
    except ValueError:
        print("\nERRO: Entrada inválida. Por favor, insira apenas números.")
        return
    limite_maximo = salario * 0.30
    if prestacao <= limite_maximo:
        print("Empréstimo CONCEDIDO!")
        print(f"O limite máximo de prestação para seu salário é de R$ {limite_maximo:.2f}.")
        print(f"A prestação de R$ {prestacao:.2f} está DENTRO do limite.")
    else:
        print("Empréstimo NEGADO!")
        print(f"O limite máximo de prestação para seu salário é de R$ {limite_maximo:.2f}.")
        print(f"A prestação de R$ {prestacao:.2f} ULTRAPASSA o limite.")
#linha_de_credito()

def intervalo():
    print("Verificar se ele é igual a 5, a 200, a 400, se está no intervalo entre 500 e 1000,")
    try:
        num = int(input("Insira um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
    
    if (num == 5) or \
       (num == 200) or \
       (num == 400):
        print("Número correto.")
    elif num >= 500 and num <= 1000:
        print(f"{num} está dentro do intervalo entre 500 - 1000.")

    else:
        print("Número está fora do escopo atual.")

#intervalo()

        

    