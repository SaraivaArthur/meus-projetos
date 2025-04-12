saldo = 1000.0

def mostrar_menu():
    print("\n=== Caixa Eletrônico ===")
    print("1 - Ver saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção:")
    
    if escolha == "1":
        print (f"\n💰 Saldo atual: R$ {saldo:.2f}")
    elif escolha == "2":
        valor = float(input("Digite o valor para sacar: R$"))
        if valor < saldo:
            saldo -= valor
            print (f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print ("❌ Saldo insuficiente.")
    elif escolha == "3":
        valor = float(input("Digite o valor para depositar: R$"))
        saldo += valor
        print (f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
    elif escolha == "4":
        print ("👋 Saindo... Obrigado por usar o caixa eletrônico!")
        break
    else: 
          print("⚠️ Opção inválida. Tente novamente.")
        
