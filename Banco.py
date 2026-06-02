# ==================================================
# SISTEMA BANCÁRIO
# Autor: Seu Nome
# Objetivo:
# Demonstrar o uso de TADs, encapsulamento,
# composição de objetos e subprogramas em Python.
# ==================================================


# ==================================================
# SUBPROGRAMAS DE VALIDAÇÃO
# Funções reutilizáveis responsáveis por verificar
# se os dados informados seguem as regras do sistema.
# ==================================================

def validar_nome(nome):
    # Verifica se o nome possui pelo menos 5 caracteres
    return nome is not None and len(nome.strip()) >= 5


def validar_cpf(cpf):
    # Remove caracteres não numéricos e verifica
    # se existem exatamente 11 dígitos
    if cpf is None:
        return False

    cpf = ''.join(filter(str.isdigit, cpf))
    return len(cpf) == 11


def validar_telefone(telefone):
    # Telefone é opcional.
    # Quando informado deve possuir 10 ou 11 dígitos.
    if telefone == "" or telefone is None:
        return True

    telefone = ''.join(filter(str.isdigit, telefone))
    return len(telefone) in [10, 11]


def validar_email(email):
    # E-mail é opcional.
    # Quando informado deve conter "@"
    if email == "" or email is None:
        return True

    return '@' in email


# ==================================================
# TAD CLIENTE
# Representa uma pessoa que pode possuir uma ou mais
# contas bancárias.
# ==================================================

class Cliente:

    # Construtor da classe Cliente
    def __init__(self, nome, cpf, telefone="", email=""):

        self.__nome = nome if validar_nome(nome) else None

        if validar_cpf(cpf):
            self.__cpf = ''.join(filter(str.isdigit, cpf))
        else:
            self.__cpf = None

        self.__telefone = telefone if validar_telefone(telefone) else None
        self.__email = email if validar_email(email) else None

    # Retorna o nome do cliente
    def get_nome(self):
        return self.__nome

    # Retorna o CPF do cliente
    def get_cpf(self):
        return self.__cpf

    # Retorna o telefone do cliente
    def get_telefone(self):
        return self.__telefone

    # Retorna o e-mail do cliente
    def get_email(self):
        return self.__email

    # Atualiza o telefone caso seja válido
    def alterar_telefone(self, telefone):
        if validar_telefone(telefone):
            self.__telefone = telefone

    # Atualiza o e-mail caso seja válido
    def alterar_email(self, email):
        if validar_email(email):
            self.__email = email


# ==================================================
# TAD CONTA BANCÁRIA
# Representa uma conta pertencente a um cliente e
# associada a um banco.
# ==================================================

class ContaBancaria:

    # Construtor da conta bancária
    def __init__(self, numero, titular, banco, saldo_inicial):

        self.__numero = numero if numero > 0 else 0
        self.__titular = titular
        self.__banco = banco
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0

    # Realiza depósito caso o valor seja positivo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    # Realiza saque caso exista saldo suficiente
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    # Retorna o saldo atual da conta
    def consultar_saldo(self):
        return self.__saldo

    # Retorna o número da conta
    def get_numero(self):
        return self.__numero

    # Retorna o titular da conta
    def get_titular(self):
        return self.__titular

    # Retorna o banco associado
    def get_banco(self):
        return self.__banco

    # Verifica se a conta está ativa
    def esta_ativa(self):
        return self.__saldo > 0


# ==================================================
# TAD BANCO
# Responsável por armazenar e administrar as contas
# bancárias cadastradas.
# ==================================================

class Banco:

    # Construtor da classe Banco
    def __init__(self, nome, codigo):

        self.__nome = nome if len(nome) >= 3 else None
        self.__codigo = codigo if codigo > 0 else 0
        self.__contas = []

    # Adiciona uma conta ao banco
    def adicionar_conta(self, conta):

        if self.buscar_conta(conta.get_numero()) is not None:
            return False

        self.__contas.append(conta)
        return True

    # Remove uma conta pelo número
    def remover_conta(self, numero):

        conta = self.buscar_conta(numero)

        if conta:
            self.__contas.remove(conta)
            return True

        return False

    # Procura uma conta pelo número
    def buscar_conta(self, numero):

        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta

        return None

    # Retorna a quantidade de contas cadastradas
    def quantidade_contas(self):
        return len(self.__contas)

    # Retorna todas as contas cadastradas
    def listar_contas(self):
        return self.__contas

    # Retorna o nome do banco
    def get_nome(self):
        return self.__nome

    # Retorna o código do banco
    def get_codigo(self):
        return self.__codigo


# ==================================================
# PROGRAMA PRINCIPAL
# Criação dos objetos e execução do cenário pedido
# na atividade.
# ==================================================

# Criação do banco
banco = Banco("Banco LNPG", 1001)

# Criação dos clientes
cliente1 = Cliente("Joao Silva", "12345678901",
                   "82999999999", "joao@email.com")

cliente2 = Cliente("Maria Souza", "11122233344",
                   "82988888888", "maria@email.com")

cliente3 = Cliente("Pedro Santos", "55566677788",
                   "82977777777", "pedro@email.com")

# Criação das contas
conta1 = ContaBancaria(101, cliente1, banco, 1000)
conta2 = ContaBancaria(102, cliente2, banco, 500)
conta3 = ContaBancaria(103, cliente3, banco, 200)
conta4 = ContaBancaria(104, cliente1, banco, 1500)

# Cadastro das contas no banco
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)
banco.adicionar_conta(conta4)

# Operações bancárias
conta1.depositar(500)
conta2.depositar(300)

conta1.sacar(200)
conta3.sacar(50)


# ==================================================
# RELATÓRIO FINAL
# Exibe todas as informações solicitadas na atividade
# ==================================================

print("\n===== RELATÓRIO DO BANCO =====")

print(f"Banco: {banco.get_nome()}")
print(f"Código: {banco.get_codigo()}")
print(f"Quantidade de contas: {banco.quantidade_contas()}")

saldo_total = 0

for conta in banco.listar_contas():

    cliente = conta.get_titular()

    print("\n----------------------")
    print(f"Titular: {cliente.get_nome()}")
    print(f"CPF: {cliente.get_cpf()}")
    print(f"Telefone: {cliente.get_telefone()}")
    print(f"E-mail: {cliente.get_email()}")
    print(f"Conta: {conta.get_numero()}")
    print(f"Saldo: R$ {conta.consultar_saldo():.2f}")

    saldo_total += conta.consultar_saldo()

print("\n======================")
print(f"Saldo total do banco: R$ {saldo_total:.2f}")
