
### ✅ 1) Verificar se três lados formam um triângulo


def verifica_triangulo():
    A = float(input("Lado A: "))
    B = float(input("Lado B: "))
    C = float(input("Lado C: "))
    if A < B + C and B < A + C and C < A + B:
        print("Forma um triângulo.")
    else:
        print("Não forma um triângulo.")


### ✅ 2) Verificação de código e senha


def verifica_login():
    codigo = int(input("Digite o código de usuário: "))
    if codigo != 1234:
        print("Usuário inválido!")
    else:
        senha = int(input("Digite a senha: "))
        if senha != 9999:
            print("Senha incorreta.")
        else:
            print("Acesso permitido.")

### ✅ 3) Maior entre três valores diferentes


def maior_de_tres():
    a = float(input("Valor A: "))
    b = float(input("Valor B: "))
    c = float(input("Valor C: "))
    maior = max(a, b, c)
    print(f"O maior valor é: {maior}")


### ✅ 4) Soma com regra de +8 ou -5


def soma_com_regra():
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    soma = n1 + n2
    if soma > 20:
        soma += 8
    else:
        soma -= 5
    print(f"Resultado: {soma}")

### ✅ 5) Múltiplo de 3

def multiplo_de_3():
    n = int(input("Digite um número: "))
    if n % 3 == 0:
        print("É múltiplo de 3.")
    else:
        print("Não é múltiplo de 3.")


### ✅ 6) Divisível por 3 e 7


def divisivel_por_3_e_7():
    n = int(input("Digite um número: "))
    if n % 3 == 0 and n % 7 == 0:
        print("É divisível por 3 e por 7.")
    else:
        print("Não é divisível por 3 e por 7.")


### ✅ 7) Divisível por 10, 5, 2 ou nenhum


def divisivel_por_10_5_2():
    n = int(input("Digite um número: "))
    if n % 10 == 0:
        print("Divisível por 10.")
    elif n % 5 == 0:
        print("Divisível por 5.")
    elif n % 2 == 0:
        print("Divisível por 2.")
    else:
        print("Não é divisível por 10, 5 ou 2.")


### ✅ 8) Verificar se dois números são iguais ou diferentes


def iguais_ou_diferentes():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    if a == b:
        print("Os números são iguais.")
    else:
        print("Os números são diferentes.")


### ✅ 9) Quadrado do menor e raiz do maior


import math

def quadrado_e_raiz():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    menor = min(a, b)
    maior = max(a, b)
    print(f"Quadrado do menor: {menor**2}")
    print(f"Raiz quadrada do maior: {math.sqrt(maior):.2f}")


### ✅ 10) Média e situação do aluno


def media_e_situacao():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    media = (n1 + n2 + n3) / 3
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Aprovado")
    elif 4 <= media < 7:
        print("Prova final")
        nota_final = 12 - media  # média final deve ser 6 (media + nota_final) / 2 = 6 → nota_final = 12 - media
        print(f"Nota necessária na prova final: {nota_final:.2f}")
    else:
        print("Reprovado")




### ✅ Executar todas as funções (se quiser testar uma por uma)


if __name__ == "__main__":
    verifica_triangulo()
    verifica_login()
    maior_de_tres()
    soma_com_regra()
    multiplo_de_3()
    divisivel_por_3_e_7()
    divisivel_por_10_5_2()
    iguais_ou_diferentes()
    quadrado_e_raiz()
    media_e_situacao()
