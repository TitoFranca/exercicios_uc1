ganhos = float(input("Ganhos no mês "))
if ganhos <= 400.00: 
    aliquota = 0
elif ganhos <= 1500.00:
    aliquota = 0.1
elif ganhos <= 2500.00:
    aliquota = 0.15
else:
    aliquota = 0.2
valor_desconto = ganhos * aliquota
print(f"O Valor que o leão comeu foi de {valor_desconto} reais")