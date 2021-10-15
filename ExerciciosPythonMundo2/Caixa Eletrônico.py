Conta:

cliente = 'João Tadeu'
agencia = '0001'
numero_conta = '1010-2'
saldo = 0


def depositar(self, valor):
    eu.saldo + = valor
    eu.extrato(valor)


def sacar(self, valor):
    se
    valor <= self.saldo:
    eu.saldo - = valor
    eu.extrato(- valor)


mais:
imprimir('Saldo insuficiente.')

menu


def(próprio):
    imprimir('-' * 30)
    imprimir(f
    'MENU DE OPERAÇÕES' )
    imprimir('-' * 30)
    imprimir('Opções:')
    imprimir('1 - Extrato')
    imprimir('2 - Depósito')
    imprimir('3 - Saque')
    imprimir('4 - Sair')
    opcao = input('Digite a opção desejada:')
    se
    opcao == '1':
    eu.extrato()

elif opcao == '2':
valor = float(input('Digite o valor a ser depositado:'))
eu.depositar(valor)
elif opcao == '4':
sair()


def extrato(self, ultimo=0):
    imprimir()
    imprimir('-' * 40)
    imprimir(f
    'EXTRATO' )
    imprimir('-' * 40)
    imprimir(f'CLIENTE - {self.cliente} ')
    imprimir(f'AGÊNCIA {self.agencia} CONTA {self.numero_conta} ')
    imprimir('-' * 40)
    imprimir('LANÇAMENTOS')
    se
    ultimo > 0:
    imprimir(f
    'DEPÓSITO ATM | CRÉDITO { ultimo : .2F } ' )
    imprimir('| |')
    imprimir('| |')
    imprimir('-' * 40)
    imprimir(f
    'SALDO: R $ { self . saldo : .2F } ' )
    imprimir('-' * 40)
    imprimir('FIM DO EXTRATO')
    imprimir('-' * 40)
    aperte = input('Aperte ENTER para retornar ao MENU \ n ou (X e ENTER) para sair:')
    se
    aperte == 'X'
    ou
    aperte == 'x':
    sair()


mais:
eu.menu()

pessoa = Conta()

enquanto
verdadeiro:
pessoa.menu()

# print (pessoa.cliente)
# print (pessoa.numero_conta)
# print (pessoa.saldo)
# pessoa.depositar (552)
# pessoa.depositar (1000)