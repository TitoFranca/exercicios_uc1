listaNomes = [ ]
listaFamilias = [ ]
qtdNomes = 3
qtdFamilias = 2

for familia in range(qtdFamilias):
    for nome in range(qtdNomes):
        nome = input( "Informe um nome de sua familia " )
        listaNomes.append( nome )

listaFamilias.append( listaNomes )
listaNomes = [ ]

for item in listaFamilias: 
    print( item )
    print()
