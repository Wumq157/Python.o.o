class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo: ", round(self.saldo,2))

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

def exibirMenu():
    print("\n Menu:")
    print("1.Exibir Detalhes da conta.")
    print("2.Realizar deposito.")
    print("3.Realizar saque.")
    print("0.Sair do programa.")
    opcoes = int(input("Qual opção você deseja?"))
    return opcoes


#aqui estou criando uma instancia do objeto ContaBancaria
#com o nome conta_do_usuario
numero_conta = input("Digite o numero da conta: ")
titular_conta = input("Digite o titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: ").replace(",","."))


conta_do_usuario = ContaBancaria(numero_conta, titular_conta, saldo_inicial)

opcao = None

while opcao != 0:
    opcao = exibirMenu()

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado").replace(",","."))
        conta_do_usuario.depositar(valor_deposito)
    elif opcao == 3:
        valor_saque = float(input("Digite o valor a ser sacado").replace(",","."))
        conta_do_usuario.sacar
    else:
        print(f"A opção {opcao} não é valida.")

#Usando os metodos do objeto ContaBancaria


#conta_do_usuario.depositar(valor_deposito)
#conta_do_usuario.sacar(valor_saque)def exibirMenu():
#conta_do_usuario.exibir_detalhes()
