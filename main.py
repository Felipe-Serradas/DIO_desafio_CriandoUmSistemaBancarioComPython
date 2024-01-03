#Variáveis
saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

def menu():
    while True:
        opcao = input('''

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => ''')

        if opcao in 'dDsSeEqQ':
            return opcao.lower()
        else:
            print('Favor insira uma opção válida. Tente novamente!')
            print(opcao)
    
def depositar():
    global saldo, extrato
    deposito = float(input("Deposito: R$"))
    if deposito < 0:
        print('O valor de depósito deve ser maior que 0. tente novamente.')
        return
    extrato += f'R${saldo:.2f} +R${deposito:.2f} => R${saldo + deposito}\n'
    saldo += deposito

def sacar():
    global saldo, extrato, numero_saques, limite
    saque = float(input('Saque: R$'))
    if saque < 0:
        print('O valor de saque deve ser maior que 0. tente novamente.')
        return
    if numero_saques > 3:
        print('Limite de saques atingido. Tente novamente amanhã')
    elif saque > limite:
        print(f'Seu limite por saque é de R${limite:.2f}, você não pode sacar acima disso.')
    elif saque > saldo:
        print(f'Saldo insuficiente. Você possui R${saldo:.2f}')
    else:
        extrato += f'R${saldo:.2f} -R${saque:.2f} => R${saldo - saque}\n'
        saldo -= saque
        numero_saques += 1

def ver_extrato():
    global extrato
    print(extrato)

def main():
    while True:
        match menu():
            case 'd':
                depositar()
            case 's':
                sacar()
            case 'e':
                ver_extrato()
            case 'q':
                break

main()