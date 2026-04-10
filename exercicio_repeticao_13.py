class Candidato:
    def __init__(self, nome, nota_portugues, nota_matematica, nota_conhcimento_gerais):

        self.nome = nome
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica
        self.nota_conhecimento_gerais = nota_conhecimento_gerais
        self.media = 0.0
        self.situacao = "REPROVADO"

    def __str__(self):
       return f"{nome}"
    

#programa principal
candidatos = []
continua = 0
while continua == 0:
    nome = input("Informe o nome do candidato: ")
    nota_portugues = float(input("Informe a nota de português: "))
    nota_matematica = float(input("Informe a nota de matemática: "))
    nota_conhecimento_gerais = float(input("Informe a nota de conhecimentos gerais: "))

    #Inserindo no dicionário o candidato
    candidato = Candidato(nome, nota_portugues, nota_matematica, nota_conhecimento_gerais)
    candidatos.append(candidato)

    continua = int(input("\nDeseja cadastrar novo candidato? (0 - Sim / Qualquer outro número - Não)"))
       #print()#

# for candidato in candidatos:
#     print(candidato)

#calcular a media dos candidatos e verificar se foi aprovado
for candidato in candidatos:
    media = (candidato.nota_portugues + candidato.nota_matematica + candidato.nota_conhecimento_gerais)/3
    candidato.media = media

    if candidato.nota_portugues <2.0 or candidato.nota_matematica <2.0 or candidato.nota_conhecimento_gerais <2.0:
        candidato_tem_nota_abaixo_2 = True
    else:
        candidato_tem_nota_abaixo_2 = False
    
    if candidato.media > 4.0 and candidato_tem_nota_abaixo_2 == False:
        candidato.situacao = "Aprovado"

for candidato in candidatos:
    print(f"Candidato: {candidato.nome} obteve média igual a {candidato.media} e está {candidato.situacao}")
        