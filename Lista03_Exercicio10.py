""""
nome da praia
a sua distancia do centro da cidade
o numero médio de veranistas da última temporada
tipo de acesso à praia (0 - acesso não asfaltado; 1 - acesso asfaltado)
"barra da tijuca": [20.0,10000.0,]

"""
praias = {} # dicionário é chaves
continua = 0 # O zeroserve para iniciar o comando

while continua == 0: #o zero servepara iniciar o comando. Para iniciar deverá ser o mesmo que foi atribuido a variável.
    # receber informações da praia#
    nome_praia = input ("Informe o nome da praia: ")
    distancia_centro = float(input("Informe a distância da praia ao centro da cidade: "))
    media_veranistas = float(input("Informe número de veranistas que vão à praia: "))
    tipo_acesso = float(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado; 1- acesso asfaltado): "))

     #criar dicionário  
    praias[nome_praia] = [distancia_centro, media_veranistas,tipo_acesso] #Chave nome_praia

    continua = int(input("Deseja cadastrar nova praia? (0 - Sim / 1 - Não)"))
print(praias)


