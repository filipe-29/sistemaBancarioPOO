class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = {}

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado no banco {self.nome}.")

    def abrir_conta(self, cliente):
        if cliente not in self.clientes:
            print("Cliente não cadastrado no banco.")
            return None
        conta = ContaBancaria(cliente)
        self.contas[cliente.cpf] = conta
        print(f"Conta aberta para o cliente {cliente.nome}.")
        return conta

    def buscar_conta(self, cpf):
        return self.contas.get(cpf)

# Exemplo de uso:

# Criando um banco
meu_banco = Banco("Meu Banco")

# Cadastrando clientes
cliente1 = Cliente("João", "123.456.789-00")
cliente2 = Cliente("Maria", "987.654.321-00")
meu_banco.cadastrar_cliente(cliente1)
meu_banco.cadastrar_cliente(cliente2)

# Abrindo contas para os clientes
conta1 = meu_banco.abrir_conta(cliente1)
conta2 = meu_banco.abrir_conta(cliente2)

# Realizando operações nas contas
conta1.depositar(1000)
conta2.depositar(500)
conta1.sacar(200)
conta2.sacar(700)
conta1.consultar_saldo()
conta2.consultar_saldo()
