listaFamilias = []
qtdNomes = 3
qtdFamilias = 2

for familia in range(qtdFamilias):
    listaNomes = [] # Criamos/limpamos a lista no início de cada família
    print(f"--- Família {familia + 1} ---")
    
    for nome in range(qtdNomes):
        nome_input = input("Informe um nome de sua família: ")
        listaNomes.append(nome_input)
    
    # IMPORTANTE: Salva a lista de nomes atual dentro da lista de famílias
    listaFamilias.append(listaNomes)

# Exibição dos resultados
print("\nEstrutura final:")
for item in listaFamilias: 
    print(item)