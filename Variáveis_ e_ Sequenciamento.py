# 1) Algoritmo que pergunta um valor em metros e imprime o correspondente em decímetros, centímetros e milímetros.
def converter_metros():
    metros = float(input("Digite um valor em metros: "))
    decimetros = metros * 10
    centimetros = metros * 100
    milimetros = metros * 1000
    print(f"{metros} metros equivalem a {decimetros} decímetros, {centimetros} centímetros e {milimetros} milímetros.")

# 2) Algoritmo que recebe quatro números inteiros, calcula e mostra a soma.
def soma_numeros():
    soma = sum([int(input(f"Digite o {i+1}º número: ")) for i in range(4)])
    print(f"A soma dos números é: {soma}")

# 3) Algoritmo que recebe três notas e calcula a média aritmética.
def media_aritmetica():
    notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(3)]
    media = sum(notas) / len(notas)
    print(f"A média aritmética é: {media}")

# 4) Algoritmo que recebe três notas e seus respectivos pesos, calcula a média ponderada.
def media_ponderada():
    notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(3)]
    pesos = [float(input(f"Digite o peso da {i+1}ª nota: ")) for i in range(3)]
    media = sum([notas[i] * pesos[i] for i in range(3)]) / sum(pesos)
    print(f"A média ponderada é: {media}")

# 5) Algoritmo que calcula várias operações sobre um número positivo.
def operacoes_numero():
    numero = float(input("Digite um número positivo: "))
    if numero > 0:
        print(f"O quadrado de {numero} é {numero**2}")
        print(f"O cubo de {numero} é {numero**3}")
        print(f"A raiz quadrada de {numero} é {numero**0.5}")
        print(f"A raiz cúbica de {numero} é {numero**(1/3)}")
    else:
        print("O número deve ser positivo e maior que zero.")

# 6) Algoritmo que converte segundos em horas, minutos e segundos.
def converter_segundos():
    segundos = int(input("Digite o número de segundos: "))
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    print(f"{segundos} segundos são {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")

# 7) Algoritmo que converte temperatura de Fahrenheit para Celsius.
def fahrenheit_para_celsius():
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"A temperatura em Celsius é: {celsius}°C")

# 9) Algoritmo que converte polegadas para milímetros.
def polegadas_para_milimetros():
    polegadas = float(input("Digite o valor em polegadas: "))
    milimetros = polegadas * 25.4
    print(f"{polegadas} polegadas são {milimetros} milímetros.")

# 10) Algoritmo que calcula a conta de uma lanchonete.
def conta_lanchonete():
    hamburguer = 3.00
    cheeseburger = 2.50
    fritas = 2.50
    refrigerante = 1.00
    
    qtd_hamburguer = int(input("Quantos hambúrgueres você consumiu? "))
    qtd_cheeseburger = int(input("Quantos cheeseburgers você consumiu? "))
    qtd_fritas = int(input("Quantas porções de fritas você consumiu? "))
    qtd_refrigerante = int(input("Quantos refrigerantes você consumiu? "))
    
    total = (qtd_hamburguer * hamburguer) + (qtd_cheeseburger * cheeseburger) + (qtd_fritas * fritas) + (qtd_refrigerante * refrigerante)
    print(f"O total da sua conta é R$ {total:.2f}")

# 11) Algoritmo que calcula o salário de um vendedor com comissão.
def salario_vendedor():
    nome = input("Digite o nome do vendedor: ")
    carros_vendidos = int(input("Quantos carros o vendedor vendeu? "))
    total_vendas = float(input("Qual foi o valor total das vendas? "))
    
    salario_base = 500
    comissao_por_carro = 50
    comissao_por_venda = 0.05
    
    salario_total = salario_base + (carros_vendidos * comissao_por_carro) + (total_vendas * comissao_por_venda)
    print(f"O salário do vendedor {nome} é R$ {salario_total:.2f}")

# 12) Algoritmo que calcula a área e o perímetro de um retângulo.
def area_perimetro_retangulo():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    
    area = largura * altura
    perimetro = 2 * (largura + altura)
    
    print(f"A área do retângulo é: {area}")
    print(f"O perímetro do retângulo é: {perimetro}")

# 13) Algoritmo que calcula o percentual de votos.
def percentual_votos():
    total_eleitores = int(input("Digite o número total de eleitores: "))
    votos_brancos = int(input("Digite o número de votos brancos: "))
    votos_nulos = int(input("Digite o número de votos nulos: "))
    votos_validos = int(input("Digite o número de votos válidos: "))
    
    percentual_brancos = (votos_brancos / total_eleitores) * 100
    percentual_nulos = (votos_nulos / total_eleitores) * 100
    percentual_validos = (votos_validos / total_eleitores) * 100
    
    print(f"Votos brancos: {percentual_brancos:.2f}%")
    print(f"Votos nulos: {percentual_nulos:.2f}%")
    print(f"Votos válidos: {percentual_validos:.2f}%")

# 14) Algoritmo que calcula o novo salário após reajuste.
def reajuste_salarial():
    salario_atual = float(input("Digite o salário atual do funcionário: "))
    percentual_reajuste = float(input("Digite o percentual de reajuste: "))
    
    novo_salario = salario_atual * (1 + percentual_reajuste / 100)
    print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}")

# 15) Algoritmo que calcula o custo final de um carro.
def custo_carro():
    custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
    
    percentual_distribuidor = 0.28
    percentual_impostos = 0.45
    
    custo_final = custo_fabrica * (1 + percentual_distribuidor + percentual_impostos)
    print(f"O custo final ao consumidor é: R$ {custo_final:.2f}")

# Chamar todas as funções para testar
if __name__ == "__main__":
    # Exemplos de execução de cada função
    converter_metros()
    soma_numeros()
    media_aritmetica()
    media_ponderada()
    operacoes_numero()
    converter_segundos()
    fahrenheit_para_celsius()
    polegadas_para_milimetros()
    conta_lanchonete()
    salario_vendedor()
    area_perimetro_retangulo()
    percentual_votos()
    reajuste_salarial()
    custo_carro()
