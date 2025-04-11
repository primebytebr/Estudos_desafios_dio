print("Desafio 1 - Meu Banco Digital")
print("## Digite a opção desejada! ##")

def exibir_menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor deve ser positivo.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor <= 0:
        print("Operação falhou! O valor deve ser positivo.")
    elif valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! Valor excede o limite de R$ 500.00.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Limite de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 1
    limite = 750
    extrato = ""
    numero_saques = 4
    LIMITE_SAQUES = 5

    while True:
        opcao = input(exibir_menu()).lower()

        try:
            if opcao == "d":
                valor = float(input("Informe o valor do depósito: R$ "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: R$ "))
                saldo, extrato, numero_saques = sacar(
                    saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
                )

            elif opcao == "e":
                exibir_extrato(saldo, extrato)

            elif opcao == "q":
                print("Obrigado por utilizar nossos serviços. Seu Banco Agradece, Até logo!")
                break

            else:
                print("Operação inválida! Por favor, selecione uma opção válida.")

        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")

        print()  

if __name__ == "__main__":
    main()