# Inicializamos a variável para acumular o total arrecadado pela loja
faturamento_total = 0

# Estrutura de repetição para processar 10 clientes
for i in range(1, 3):
    print(f"\n--- Dados do Cliente {i} ---")
    
    nome = input("Digite o nome do cliente: ")
    valor_compra = float(input(f"Digite o valor da compra de {nome}: R$ "))
    
    # Lógica do desconto:
    # 20% (0.20) se >= 250, caso contrário 15% (0.15)
    if valor_compra >= 250:
        percentual = 20
        desconto = valor_compra * 0.20
    else:
        percentual = 15
        desconto = valor_compra * 0.15
        
    valor_a_pagar = valor_compra - desconto
    
    # Somamos o valor pago ao faturamento total da loja
    faturamento_total += valor_a_pagar
    
    # Exibição dos resultados individuais
    print(f"Cliente: {nome}")
    print(f"Valor Original: R$ {valor_compra:.2f}")
    print(f"Desconto aplicado ({percentual}%): R$ {desconto:.2f}")
    print(f"Valor Final a Pagar: R$ {valor_a_pagar:.2f}")

# Após o loop, exibimos o total arrecadado
print("\n" + "="*60)
print(f"FATURAMENTO TOTAL DA LOJA: R$ {faturamento_total:.2f}")
print("="*60)