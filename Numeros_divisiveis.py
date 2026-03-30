resultado1 = ""
resultado2 = ""
resultado3 = ""
resultado4 = ""

numero_01 = float(input("Informe Número 1 "))
numero_02 = float(input("Informe Número 2 "))
numero_03 = float(input("Informe Número 3 "))
numero_04 = float(input("Informe Número 4 "))

if numero_01 % 2 == 0 and  numero_01 % 3 == 0:
    resultado1 = f"O número {numero_01} é divisível por 2 ou 3"
    print(f"O número {numero_01} é divisível por 2 ou 3")
else:   
    resultado1 = f"O número {numero_01} é indivisível por 2 ou 3"
    print(f"O número {numero_01} é indivisível por 2 ou 3")

if numero_02 % 2 == 0 and  numero_02 % 3 == 0:
    resultado2 = f"O número {numero_02} é divisível por 2 ou 3"
    print(f"O número {numero_02} é divisível por 2 ou 3")
else:   
    resultado2 = f"O número {numero_02} é indivisível por 2 ou 3"
    print(f"O número {numero_02} é indivisível por 2 ou 3")

if numero_03 % 2 == 0 and  numero_03 % 3 == 0:
    resultado3 = f"O número {numero_03} é divisível por 2 ou 3"
    print(f"O número {numero_03} é divisível por 2 ou 3")
else:   
    resultado3 = f"O número {numero_03} é indivisível por 2 ou 3"
    print(f"O número {numero_03} é indivisível por 2 ou 3")

if  numero_04 % 2 == 0 and  numero_04 % 3 == 0:
    resultado4 = f"O número {numero_04} é divisível por 2 ou 3"
    print(f"O número {numero_04} é divisível por 2 ou 3")
else:    
    resultado4 = f"O número {numero_04} é indivisível por 2 ou 3"
    print(f"O número {numero_04} é indivisível por 2 ou 3")

print("-------------------------")
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
