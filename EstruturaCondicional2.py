

### 1) Verifica se um número é divisível por 3:


def divisivel_por_3():
    numero = int(input("Digite um número inteiro: "))
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3.")
    else:
        print(f"{numero} não é divisível por 3.")

### 2) Verifica se o dia é útil, fim de semana ou inválido:

def dia_util_fim_de_semana():
    dia = int(input("Digite o número referente ao dia da semana (1 a 7): "))
    if dia == 1 or dia == 7:
        print("Fim de semana.")
    elif 2 <= dia <= 6:
        print("Dia útil.")
    else:
        print("Dia inválido.")


### 3) Informa as cédulas necessárias para um valor informado:


def cédulas_necessarias():
    valor = int(input("Digite o valor desejado: "))
    cedulas = [100, 50, 10, 5, 1]
    
    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R${cedula}.")
            valor %= cedula


### 4) Valida CPF:


def valida_cpf():
    cpf = input("Digite o CPF (somente números): ")
    
    if len(cpf) != 11:
        print("CPF inválido. Deve conter 11 dígitos.")
        return
    
    # Passo 1
    soma1 = sum([int(cpf[i]) * (10 - i) for i in range(9)])
    digito1 = 11 - (soma1 % 11)
    if digito1 >= 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        print(f"{cpf} não é válido! O 1º dígito deveria ser {digito1}.")
        return

    # Passo 2
    soma2 = sum([int(cpf[i]) * (11 - i) for i in range(10)])
    digito2 = 11 - (soma2 % 11)
    if digito2 >= 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        print(f"{cpf} não é válido! O 2º dígito deveria ser {digito2}.")
        return
    
    print(f"{cpf} é um CPF válido!")


### 5) Identifica quantos dias há em um mês, considerando o ano:


import calendar

def dias_no_mes():
    mes = int(input("Digite o número do mês (1-12): "))
    ano = int(input("Digite o ano: "))
    
    if mes < 1 or mes > 12:
        print("Mês inválido!")
    else:
        dias = calendar.monthrange(ano, mes)[1]
        print(f"O mês {mes}/{ano} tem {dias} dias.")


### 6) Identifica se um mês é de alta ou baixa temporada:


def temporada():
    mes = int(input("Digite o número do mês (1-12): "))
    
    if mes in [12, 1, 2, 6, 7]:
        print("Alta temporada.")
    elif 3 <= mes <= 5 or 8 <= mes <= 11:
        print("Baixa temporada.")
    else:
        print("Mês inválido.")

### 7) Identifica se o dia da semana é de semana, fim de semana ou inválido:


def dia_da_semana():
    dia = int(input("Digite o número do dia da semana (1 a 7): "))
    
    if dia == 1 or dia == 7:
        print("Fim de semana.")
    elif 2 <= dia <= 6:
        print("Dia de semana.")
    else:
        print("Dia inválido.")


### 8) Calcula o valor a ser pago por um plano de saúde:


def plano_de_saude():
    idade = int(input("Digite a idade do conveniado: "))
    valor_base = 100
    
    if idade < 10:
        valor_adicional = 80
    elif 10 <= idade <= 30:
        valor_adicional = 50
    elif 40 <= idade <= 60:
        valor_adicional = 95
    else:
        valor_adicional = 130
    
    valor_total = valor_base + valor_adicional
    print(f"O valor a ser pago pelo plano de saúde é R${valor_total}.")

### 9) Calcula o valor da multa de anuidade de uma associação:


def anuidade_com_juros():
    valor_inicial = float(input("Digite o valor da anuidade (R$): "))
    meses_atraso = int(input("Digite o número de meses de atraso: "))
    
    valor_final = valor_inicial
    
    for mes in range(1, meses_atraso + 1):
        valor_final *= 1.05  # Juros de 5% por mês
    
    print(f"O valor final da anuidade com juros é R${valor_final:.2f}.")



divisivel_por_3()
dia_util_fim_de_semana()
cédulas_necessarias()
valida_cpf()
dias_no_mes()
temporada()
dia_da_semana()
plano_de_saude()
anuidade_com_juros()
