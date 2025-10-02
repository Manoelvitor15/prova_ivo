# 1) Algoritmo que imprime os valores de A, B e C em ordem crescente (do menor para o maior).
def ordem_crescente():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    
    valores = [A, B, C]
    valores.sort()
    
    print("Valores em ordem crescente:", valores)

# 2) Algoritmo que verifica se um número é divisível por 10, 5 ou 2.
def divisivel_por():
    num = int(input("Digite um número: "))
    
    if num % 10 == 0:
        print(f"{num} é divisível por 10")
    elif num % 5 == 0:
        print(f"{num} é divisível por 5")
    elif num % 2 == 0:
        print(f"{num} é divisível por 2")
    else:
        print(f"{num} não é divisível por 10, 5 ou 2")

# 3) Algoritmo que verifica se o empréstimo pode ser concedido, baseado no salário e valor da prestação.
def emprestimo():
    salario = float(input("Digite o salário bruto: "))
    prestacao = float(input("Digite o valor da prestação: "))
    
    if prestacao <= 0.30 * salario:
        print("Empréstimo pode ser concedido.")
    else:
        print("Empréstimo não pode ser concedido.")

# 4) Algoritmo que verifica se o número é igual a 5, 200, 400, entre 500 e 1000 ou fora desses casos.
def verificar_numero():
    numero = int(input("Digite um número: "))
    
    if numero == 5:
        print("O número é igual a 5.")
    elif numero == 200:
        print("O número é igual a 200.")
    elif numero == 400:
        print("O número é igual a 400.")
    elif 500 <= numero <= 1000:
        print("O número está no intervalo entre 500 e 1000.")
    else:
        print("O número está fora dos escopos anteriores.")

# 5) Algoritmo que informa o mês de renovação do emplacamento com base no último número da placa.
def renovacao_placa():
    placa = input("Digite a placa do carro (último número): ")
    ultimo_numero = int(placa[-1])
    
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    print(f"O mês de renovação do emplacamento é: {meses[ultimo_numero - 1]}")

# 6) Algoritmo que calcula a dosagem de medicamento com base na idade e peso do paciente.
def dosagem_medicamento():
    idade = int(input("Digite a idade do paciente: "))
    peso = float(input("Digite o peso do paciente (em kg): "))
    
    if idade >= 12:
        if peso >= 60:
            dosagem = 1000
        else:
            dosagem = 875
    else:
        if peso <= 10:
            dosagem = 250
        elif peso <= 20:
            dosagem = 375
        elif peso <= 30:
            dosagem = 500
        elif peso <= 40:
            dosagem = 625
        elif peso <= 50:
            dosagem = 750
        else:
            dosagem = 875
    
    gotas = (dosagem / 500) * 20
    print(f"O paciente deve tomar {gotas:.0f} gotas por dose.")

# 7) Algoritmo que calcula o custo de pulverização e aplica descontos.
def custo_pulverizacao():
    nome = input("Digite o nome do fazendeiro: ")
    tipo = int(input("Digite o tipo de pulverização (1 a 4): "))
    area = float(input("Digite a área a ser pulverizada (em acres): "))
    
    if tipo == 1:
        preco_por_acre = 5
    elif tipo == 2:
        preco_por_acre = 10
    elif tipo == 3:
        preco_por_acre = 15
    elif tipo == 4:
        preco_por_acre = 25
    else:
        print("Tipo de pulverização inválido.")
        return
    
    custo_total = preco_por_acre * area
    
    if area > 300:
        custo_total *= 0.95  # Desconto de 5% para área maior que 300 acres
    
    if custo_total > 1750:
        custo_total -= (custo_total - 1750) * 0.10  # Desconto de 10% no valor que ultrapassar R$ 1750
    
    print(f"Fazendeiro: {nome}")
    print(f"Valor a ser pago: R$ {custo_total:.2f}")

# 8) Algoritmo que apresenta um menu com as opções e realiza as operações.
def menu_troco():
    print("Menu:")
    print("1 – Ler valores (vf e vt)")
    print("2 – Obter troco")
    print("3 – Mostrar cédulas do troco")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        vf = int(input("Digite o valor fornecido: "))
        vt = int(input("Digite o valor total da conta: "))
        print(f"Valores lidos: vf = {vf}, vt = {vt}")
    elif opcao == 2:
        vf = int(input("Digite o valor fornecido: "))
        vt = int(input("Digite o valor total da conta: "))
        troco = vf - vt
        print(f"O troco a ser devolvido é: R$ {troco}")
    elif opcao == 3:
        troco = int(input("Digite o valor do troco: "))
        notas = [100, 50, 20, 10, 5, 2, 1]
        for nota in notas:
            qtd = troco // nota
            if qtd > 0:
                print(f"{qtd} cédula(s) de R$ {nota}")
            troco %= nota
    else:
        print("Opção inválida.")

# 9) Algoritmo que verifica se a letra é uma vogal ou não.
def verificar_vogal():
    letra = input("Digite uma letra: ").lower()
    
    if letra in 'aeiou':
        print(f"{letra.upper()} é uma vogal.")
    else:
        print(f"{letra.upper()} não é uma vogal.")

# Chamar as funções para testar
if __name__ == "__main__":
    ordem_crescente()
    divisivel_por()
    emprestimo()
    verificar_numero()
    renovacao_placa()
    dosagem_medicamento()
    custo_pulverizacao()
    menu_troco()
    verificar_vogal()
