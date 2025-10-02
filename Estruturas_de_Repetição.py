# 1) Leia 5 valores para uma variável A e mostre quantos são pares, ímpares, positivos e negativos.
def contar_pares_impares_positivos_negativos():
    pares = impares = positivos = negativos = 0
    
    for i in range(5):
        A = int(input(f"Digite o {i+1}º valor: "))
        
        if A % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if A > 0:
            positivos += 1
        elif A < 0:
            negativos += 1
    
    print(f"Pares: {pares}, Ímpares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# 2) Calcule e mostre a soma dos números pares entre 1 e 100, inclusive.
def soma_pares():
    soma = sum([i for i in range(1, 101) if i % 2 == 0])
    print(f"A soma dos números pares entre 1 e 100 é: {soma}")

# 3) Calcule e mostre a média dos números pares entre 1 e 100, inclusive.
def media_pares():
    pares = [i for i in range(1, 101) if i % 2 == 0]
    media = sum(pares) / len(pares)
    print(f"A média dos números pares entre 1 e 100 é: {media}")

# 4) Leia 2 valores: X e Y. Calcule e mostre a soma dos números ímpares entre X e Y.
def soma_impares_entre_X_e_Y():
    X = int(input("Digite o valor de X: "))
    Y = int(input("Digite o valor de Y: "))
    
    soma = sum([i for i in range(X, Y + 1) if i % 2 != 0])
    print(f"A soma dos números ímpares entre {X} e {Y} é: {soma}")

# 5) Apresente o quadrado de cada número par entre 1 e 1000.
def quadrado_pares():
    for i in range(1, 1001):
        if i % 2 == 0:
            print(f"O quadrado de {i} é {i**2}")

# 6) Apresente todos os números divisíveis por 5 maiores que 0 e menores ou iguais a 200.
def divisiveis_por_5():
    for i in range(1, 201):
        if i % 5 == 0:
            print(i)

# 7) Escreva um algoritmo que leia 10 valores quaisquer e mostre quantos estão dentro e fora do intervalo (10,20).
def dentro_fora_intervalo():
    dentro = fora = 0
    
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor: "))
        if 10 < valor < 20:
            dentro += 1
        else:
            fora += 1
    
    print(f"{dentro} valores estão dentro do intervalo (10,20) e {fora} valores estão fora.")

# 8) Escreva um algoritmo que leia um número e diga se ele é perfeito.
def numero_perfeito():
    numero = int(input("Digite um número: "))
    soma_divisores = sum([i for i in range(1, numero) if numero % i == 0])
    
    if soma_divisores == numero:
        print(f"{numero} é um número perfeito.")
    else:
        print(f"{numero} não é um número perfeito.")

# 9) Mostre os números entre 1000 e 2000 que, quando divididos por 11, dão resto igual a 5.
def numeros_divisiveis_por_11():
    for i in range(1000, 2001):
        if i % 11 == 5:
            print(i)

# 10) Leia uma quantidade de valores para X indeterminadamente (parar quando o valor digitado for igual a 0).
# Para cada valor lido, mostrar se ele é primo ou não.
def verificar_primos():
    while True:
        X = int(input("Digite um número (0 para parar): "))
        if X == 0:
            break
        
        if X < 2:
            print(f"{X} não é primo.")
        else:
            primo = True
            for i in range(2, int(X ** 0.5) + 1):
                if X % i == 0:
                    primo = False
                    break
            if primo:
                print(f"{X} é primo.")
            else:
                print(f"{X} não é primo.")

# 11) Gere e mostre os valores primos entre 1 e 1000. Mostre também a soma desses valores.
def primos_entre_1_e_1000():
    soma = 0
    for num in range(1, 1001):
        if num < 2:
            continue
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print(num)
            soma += num
    print(f"A soma dos números primos entre 1 e 1000 é: {soma}")

# Chamar as funções para testar
if __name__ == "__main__":
    contar_pares_impares_positivos_negativos()
    soma_pares()
    media_pares()
    soma_impares_entre_X_e_Y()
    quadrado_pares()
    divisiveis_por_5()
    dentro_fora_intervalo()
    numero_perfeito()
    numeros_divisiveis_por_11()
    verificar_primos()
    primos_entre_1_e_1000()
