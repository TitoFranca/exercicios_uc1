valor_da_compra = float(input(" Valor da Sua Compra "))
if valor_da_compra > 5000.00:
    desconto = 0.2
else:
    desconto = 0.15
valor_final = valor_da_compra * desconto
print(f" O Seu desconto foi de R$ {valor_final}")
valor_a_pagar = valor_da_compra - valor_final
print(f" O Valor a pagar é de R$ {valor_a_pagar} ")