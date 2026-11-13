print("\n------ Estoque Olliver ------")

product = input("Digite o nome do produto: ")

while True:
    try:
        stock = int(input("Digite a quantidade do produto: "))
        if stock < 0:
            print("A quantidade não pode ser negativa.")
            continue
        break
    except ValueError:
        print("Digite apenas números inteiros.")

while True:
    print("\n------ Menu do Estoque ------")
    print("(1) Adicionar produtos")
    print("(2) Retirar produtos")
    print("(3) Consultar estoque")
    print("(4) Sair do programa")

    option = input("\nDigite uma opção: ")

    if option in ("1", "2"):
        try:
            quantity = int(input("Digite a quantidade: "))
        except ValueError:
            print("\nDigite apenas números inteiros.")
            continue

        if quantity <= 0:
            print("\nA quantidade deve ser maior que zero.")
            continue

        if option == "1":
            stock += quantity
            print(f"\nEstoque atualizado de {product}: {stock}")
        else:
            if quantity <= stock:
                stock -= quantity
                print(f"\nEstoque atualizado de {product}: {stock}")
            else:
                print("\nEstoque insuficiente!")

    elif option == "3":
        print(f"\nEstoque atual de {product}: {stock}")

    elif option == "4":
        print("Saindo do estoque...")
        break
    else:
        print("Opção inválida, tente novamente!")