
def conversao():
    print("Conversor de Metros para decimentros, centimetros e milimetros")
    metros = float(input("Insira a medida em metros: "))
    if metros != 0:
        decimentros = metros * 10
        centimetros = metros * 100
        milimetros = metros * 1000

        print(f"A medida em decimentros é: {decimentros}")
        print(f"A medida em centimetros é: {centimetros}")
        print(f"A medida em milímetros é: {milimetros}")

    else:
        print("Insira uma medida maior que zero!")

#conversao()

def somar_numeros():
    print("Somar quatro números inteiros:")
    lista_numero = []
    contador = 0
    while contador < 4:
        numero = int(input(f"Insira o {contador + 1} número inteiro: "))
        lista_numero.append(numero)
        contador = contador + 1
    print(f"A soma total é: {sum(lista_numero)}")

#somar_numeros()

def calcular_media():
    print("Média aritméticas de três notas:")
    lista_nota = []
    contador = 0
    while contador < 3:
        nota = float(input(f"Insira a {contador + 1} nota: "))
        lista_nota.append(nota)
        contador = contador + 1
    print(f"A média aritmética é: {(sum(lista_nota)/3):.2}")

#calcular_media()

def media_ponderada():
    print("Média ponderada de três notas:")
    lista_nota = []
    contador = 0
    while contador < 3:
        nota = float(input(f"Insira a {contador + 1} nota: "))
        lista_nota.append(nota)
        contador = contador + 1
        if len(lista_nota) == 3:
            peso1 = 3
            peso2 = 2
            peso3 = 5
            soma_peso = peso1 + peso2 + peso3
            soma_ponderada = lista_nota[0] * peso1 + lista_nota[1] * peso2 + lista_nota[2] * peso3
            media = soma_ponderada / soma_peso

            
    print(f"A média ponderada é: {(media):.2}")

#media_ponderada()