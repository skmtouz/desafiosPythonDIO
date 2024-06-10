menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu).lower().strip()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            
            if valor > 0 and round(valor, 2) == valor:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação não foi concluída! O valor informado é inválido.")
        except ValueError:
            print("Operação não foi concluída! Valor digitado não é um número válido.")
        
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0 and round(valor, 2) == valor:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação não foi concluída! Valor digitado não é um número válido.")

    elif opcao == "e":
        print("\n====================== EXTRATO ======================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in extrato:
                print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")
    
    elif opcao == "q":
        print("Saindo do sistema. Obrigado por usar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
