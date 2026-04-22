from datetime import datetime, timedelta, timezone

brasilia = timezone(timedelta(hours=-3))
data_atual = datetime.now(brasilia)

repetidor = "=" * 70


def data_compra(data):
    while data.weekday() in (5, 6):
        data += timedelta(days=1)
    return data


def opcoes_compra(meio_pagamento, pagamento, data_atual):
    if meio_pagamento == "0":
        mdr = pagamento * 0.01
        liquido = pagamento - mdr

        data_credito = data_compra(data_atual + timedelta(days=1))

        print(repetidor)
        print(f"Data da Compra:{data_atual.strftime('%d/%m/%y')}")
        print(f"Hora da Compra: {data_atual.strftime('%H:%M:%S')}")
        print("Meio de Pagamento: 0 – Cartão de débito")
        print(f"Valor da Compra:R$", pagamento)
        print(f"Valor do MDR:(taxa de transação): R$", mdr)
        print("Valor Liquído:", liquido)
        print(f"Data de Crédito: {data_credito.strftime('%d/%m/%y')}")


    elif meio_pagamento == "1":
        mdr = pagamento * 0.05
        liquido = pagamento - mdr
        data_credito = data_compra(data_atual + timedelta(days=1))

        print(repetidor)
        print(f"Data da Compra: {data_atual.strftime('%d/%m/%y')}")
        print(f"Hora da Compra: {data_atual.strftime('%H:%M:%S')}")
        print("Meio de Pagamento: 1 – Cartão de crédito à vista")
        print(f"Valor da Compra: R$", pagamento)
        print(f"Valor do MDR: R$", mdr)
        print("Valor Liquído: R$", liquido)





    elif meio_pagamento == "2":
        qts_parcelas = input("Digite a Quantidade de Parcelas (2 ou 3 Parcelas): ")
        mdr = pagamento * 0.05
        liquido = pagamento - mdr
        parcela = liquido / 2
        data_credito = data_compra(data_atual + timedelta(days=1))

        if qts_parcelas == "2":

            print(repetidor)
            print(f"Data da Compra: {data_atual.strftime('%d/%m/%y')}")
            print(f"Hora da Compra: {data_atual.strftime('%H:%M:%S')}")
            print("Meio de Pagamento: 1 – Cartão de crédito à vista")
            print(f"Valor da Compra: R$", pagamento)
            print(f"Valor do MDR: R$", mdr)
            print("Valor Liquído: R$", liquido)
            print()
            print(parcela,"1 / 2")
            print



        elif qts_parcelas == "3":

            print(repetidor)
            print(f"Data da Compra: {data_atual.strftime('%d/%m/%y')}")
            print(f"Hora da Compra: {data_atual.strftime('%H:%M:%S')}")
            print("Meio de Pagamento: 1 – Cartão de crédito à vista")
            print(f"Valor da Compra: R$", pagamento)
            print(f"Valor do MDR: R$", mdr)
            print("Valor Liquído: R$", liquido)


        else:
            print("Invalida")


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
    data_atual = datetime.now(brasilia)
    menu_inicial(data_atual)

    meio_pagamento = input("Digite o meio de pagamento: ")

    if meio_pagamento == "9":
        print("Sistema Encerrado")
        print(repetidor)
        break

    elif meio_pagamento in ("0", "1", "2"):
        pagamento = input("Digite o valor da compra R$ ")
        pagamento = int(pagamento)

        if pagamento > 0:
            opcoes_compra(meio_pagamento, pagamento, data_atual)

        else:
            print("Meio de Valor Invalido")



    else:
        print("Meio de Pagamento Invalido")



