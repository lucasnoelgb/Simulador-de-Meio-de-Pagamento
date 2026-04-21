from datetime import datetime, timedelta

repetidor = "=" * 70


def data_compra(data):
    while data.weekday() in (5, 6):
        data += timedelta(days=1)
    return data


def opcoes_compra(pagamento, data_atual):
    if pagamento == "0":
        print("debito")

    elif pagamento == "1":
        print("Cartão de Crédito")

    elif pagamento == "2":
        print("Cartão de Crédito Parcelado")


def menu_inicial(data_hora):
    print(repetidor)
    print(f"UNICSUL - Simulador de Meio de Pagamento – versão 2026  {data_hora.strftime('%d/%m/%Y')}")
    print()
    print("Meios de Pagamentos disponiveis")
    print("0 – Cartão de Débito")
    print("1 – Cartão de Crédito à Vista")
    print("2 – Cartão de Crédito Parcelado")
    print("9 – Sair")
    print()


while True:
    data_atual = datetime.now()
    menu_inicial(data_atual)

    pagamento = input("Digite o meio de pagamento: ")
    print(repetidor)

    if pagamento == "9":
        print("Sistema Encerrado")
        break

    elif pagamento in ("0", "1", "2"):
        opcoes_compra(pagamento, data_atual)


    else:
        print("Meio de Pagamento Invalido")




