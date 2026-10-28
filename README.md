# Simulador de Meio de Pagamento

Projeto acadêmico da UNICSUL que simula uma compra paga por cartão de débito ou crédito. O programa recebe o valor da compra e apresenta o desconto da taxa MDR, o valor líquido e as datas previstas para crédito.

## Formas de pagamento

| Opção | Meio de pagamento | MDR | Prazo de crédito previsto |
|---|---|---:|---|
| `0` | Cartão de débito | 1% | 1 dia após a compra |
| `1` | Cartão de crédito à vista | 5% | 30 dias após a compra |
| `2` | Cartão de crédito parcelado | 5% | Parcelas previstas a cada 30 dias |
| `9` | Encerrar o sistema | — | — |

As datas calculadas para crédito são ajustadas por `data_compra()`: se caírem em sábado ou domingo, avançam para o próximo dia útil (segunda-feira). Feriados não são considerados.

## Fluxo do programa

1. Define o fuso horário fixo de Brasília como UTC−3.
2. Mostra um menu com a data atual e as formas de pagamento disponíveis.
3. Lê a opção escolhida. A opção `9` encerra o programa.
4. Para as opções `0`, `1` e `2`, solicita o valor da compra. O programa aceita vírgula ou ponto como separador decimal.
5. Se o valor for positivo, calcula e exibe os dados da transação. Valores não positivos e opções inválidas recebem uma mensagem de erro.
6. No pagamento parcelado, solicita 2 ou 3 parcelas; outras quantidades são rejeitadas.

## Cálculos

- **MDR:** valor da compra multiplicado pela taxa da modalidade.
- **Valor líquido:** valor da compra menos MDR.
- **Débito:** crédito do líquido no dia seguinte à compra.
- **Crédito à vista:** crédito do líquido após 30 dias.
- **Crédito parcelado:** MDR é descontado do total e o líquido é dividido em 2 ou 3 partes. A divisão é feita em centavos inteiros; eventual diferença de arredondamento é alocada à primeira parcela.

No parcelamento, as datas são calculadas a partir da data da compra: primeira parcela em 30 dias, segunda em 60 dias e, quando houver três parcelas, terceira em 90 dias. Cada data é ajustada para o próximo dia útil se cair no fim de semana.

## Estrutura do código

- `data_compra(data)`: avança uma data de sábado ou domingo até um dia útil.
- `opcoes_compra(meio_pagamento, pagamento, data_atual)`: aplica a taxa, calcula líquido e datas e imprime o resumo da compra.
- `menu_inicial(data_hora)`: apresenta o título e as opções.
- Laço principal: atualiza a data e hora, lê as entradas, valida a opção e inicia cada simulação.

## Como executar

Salve o código em um arquivo, por exemplo `simulador_pagamento.py`, e execute com Python 3:

```bash
python simulador_pagamento.py
```

Não há dependências externas; o código usa apenas o módulo `datetime` da biblioteca padrão.

## Observações e limitações

- O código não captura entradas inválidas para o valor da compra. Texto não numérico pode gerar um erro ao converter para `float`.
- Valores financeiros são calculados com `float`, que pode introduzir pequenas diferenças de precisão em operações monetárias. Para uso financeiro real, prefira `Decimal`.
- O calendário considera apenas fins de semana; feriados e regras de liquidação da operadora não são considerados.
- No parcelamento, o programa exibe as parcelas calculadas a partir do valor líquido, ou seja, após a dedução do MDR.
- A data do crédito parcelado segue intervalos fixos de 30, 60 e 90 dias corridos, não meses de calendário.
