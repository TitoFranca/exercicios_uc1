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

     #Inserindo no dicionário as informações do dicionário
    praias[nome_praia] = [distancia_centro, media_veranistas,tipo_acesso] #Chave nome_praia

    continua = int(input("Deseja cadastrar nova praia? (0 - Sim / Qualquer outro número - Não)"))
""" print(praias) """


#processamento
numero_praias_15km = 0
numero_veranistas_praia_nao_asfaltada = 0
quantidade_numero_de_praias_acesso_nao_asfaltado = 0
praias_acesso_asfaltado_menos_10000_veranistas = {}

nomes_praia = praias.keys()
for nome in nomes_praia:
    elemento = praias.get(nome)
    print(elemento)

    distancia_centro = elemento [0]
    numero_veranistas = elemento [1]
    tipo_acesso = elemento [2]

    if distancia_centro > 15:
        numero_praias_15km = numero_praias_15km +1

    if tipo_acesso == 0:
        numero_veranistas_praia_nao_asfaltada = numero_veranistas_praia_nao_asfaltada + numero_veranistas
        quantidade_numero_de_praias_acesso_nao_asfaltado = quantidade_numero_de_praias_acesso_nao_asfaltado +1

    if tipo_acesso == 1 and numero_veranistas <1000:
        praias_acesso_asfaltado_menos_10000_veranistas [nome] = distancia_centro

media_veranistas = numero_veranistas_praia_nao_asfaltada / quantidade_numero_de_praias_acesso_nao_asfaltado

print(f" Número de praias mais de 15 km do centro: {numero_praias_15km}")
print(f" Média de veraistas de praias com acesso não asfaltado: {media_veranistas}")    
print(f" Praia com acesso asfaltado e com menos de 1000 veranistas: {praias_acesso_asfaltado_menos_10000_veranistas}")
    