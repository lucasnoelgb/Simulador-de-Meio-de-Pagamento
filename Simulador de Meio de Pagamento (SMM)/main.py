def valor_compra():
    x = input("Digite o valor da compra")
    return (x)


def debito():
    tc = valor_compra()
    MDR = x * 0.01


def credito():
    valor_compra()


def credito_parcelado():
    valor_compra()


def menu():
    print("Meios de Pagamento")
    print("0 - Débito")
    print("1 - Crédito")
    print("2 - Crédito parcelado")
    print("9 - Sair")


while True:
    pagamento = input("Digite o meio de pagamento: ")

    if pagamento == 0:
        debito():

    elif pagamento == 1:
        credito():


    elif pagamento == 2:
        credito_parcelado():


    elif pagamento == 9:
        break


    else:
        print("Opção invalida")
        continue