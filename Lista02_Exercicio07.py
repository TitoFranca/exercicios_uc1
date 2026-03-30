valor_das_vendas = float(input( "Valor das Vendas "))
if valor_das_vendas > 20000.00:
    valor_comissao =  0.2
else: valor_comissao =  0.075
valor_recebimento = valor_das_vendas * valor_comissao


print(f" Valor a ser recebido R$ {valor_recebimento}")
    