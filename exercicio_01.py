salario_bruto = float(input("Informe o salário:\n"))
desconto = salario_bruto*0.4
salario_liquido = salario_bruto - desconto
print(f"Salário Líquido: {salario_liquido:2f}")