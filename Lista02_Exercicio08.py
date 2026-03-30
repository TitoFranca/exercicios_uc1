soma_positivos = 0
quantidade_negativos = 0
lista_numeros = []
for i in range (5):
    numero_inteiro = int(input("Informe um número:"))
    lista_numeros.append(numero_inteiro)

print(lista_numeros)

qtd_elemento_lista = len(lista_numeros)
for i in range (qtd_elemento_lista):
    numero_inteiro = lista_numeros[i]
    
    if numero_inteiro >=0:
        soma_positivos = soma_positivos + numero_inteiro
    else:
        quantidade_negativos = quantidade_negativos +1 

print("A soma dos valores positivos é {0}".format(soma_positivos) )
print(f"A quantidade de valores negativos é {quantidade_negativos}")
                        