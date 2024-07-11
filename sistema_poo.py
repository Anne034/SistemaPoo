class Cliente:
    def __init__(self, endereco):
      self.endereco = endereco
      self.contas =[]

    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.appnd(conta)

class Usuario(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.saques = 0
        self.limite_saques = 3

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
        elif valor > self.limite:
            print('O limite de saque é de R$500!')
        elif self.saques >= self.limite_saques:
            print('Limite de saques diários atingido!')
        else:
            self.saldo -= valor
            self.saques += 1
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print('Saque realizado com sucesso!')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'Depósito de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}')
        else:
            print("Valor inválido. Digite um valor válido para depositar.")

    def exibir_extrato(self):
        print("EXTRATO: ")
        print(self.extrato)
        print(f"Saldo: R$ {self.saldo:.2f}")

class Banco:
    def __init__(self):
        self.agencia = "0001"
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input('Informe seu CPF: ')
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print('Este CPF já está em uso!')
            return

        nome = input('Informe seu nome completo: ')
        data_nascimento = input('Informe data de nascimento (dd-mm-aaaa): ')
        endereco = input('Informe endereço (logradouro, numero - bairro - cidade/sigla estado): ')

        self.usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
        print('!!!!USUARIO CRIADO!!!')

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta(self):
        cpf = input('Informe seu CPF: ')
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            conta = Conta(self.agencia, numero_conta, usuario)
            self.contas.append(conta)
            print("Conta criada com sucesso!")
        else:
            print('Usuário não encontrado! Crie um usuário')

    def listar_contas(self):
        for conta in self.contas:
            print('=' * 100)
            print(f'''\
Agência: {conta.agencia}
Nº Conta: {conta.numero_conta}
Titular: {conta.usuario.nome}
''')

def main():
    banco = Banco()
    menu = """
__________________________________________________
Olá!!! Bem vindo ao banco! Selecione alguma opção:
==================================================
[1] Sacar
[2] Depositar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Sair
"""

    while True:
        opcao = input(menu)

        if opcao == "1":
            numero_conta = int(input('Informe o número da conta: '))
            if numero_conta > 0 and numero_conta <= len(banco.contas):
                valor_saque = float(input('Informe o valor que deseja sacar: '))
                conta = banco.contas[numero_conta - 1]
                conta.sacar(valor_saque)
            else:
                print("Conta não encontrada!Crie uma conta!")

        elif opcao == "2":
            numero_conta = int(input('Informe o número da conta: '))
            if numero_conta > 0 and numero_conta <= len(banco.contas):
                valor_deposito = float(input('Informe o valor que deseja depositar: '))
                conta = banco.contas[numero_conta - 1]
                conta.depositar(valor_deposito)
            else:
                print("Conta não encontrada!Crie uma conta!")

        elif opcao == "3":
            numero_conta = int(input('Informe o número da conta: '))
            if numero_conta > 0 and numero_conta <= len(banco.contas):
                conta = banco.contas[numero_conta - 1]
                conta.exibir_extrato()
            else:
                print("Conta não encontrada!Crie uma conta!")

        elif opcao == "4":
            banco.criar_usuario()

        elif opcao == "5":
            banco.criar_conta()

        elif opcao == "6":
            banco.listar_contas()

        elif opcao == "7":
            print("Saindo! Agradecemos a preferência :)")
            break

if __name__ == "__main__":
    main()
