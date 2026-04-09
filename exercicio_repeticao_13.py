class Candidato:
    def __init__(self, nome, nota_portugues, nota_matematica, nota_conhcimento_gerais):

        self.nome = nome
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica
        self.nota_conhcimento_gerais = nota_conhcimento_gerais
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
    print()

for candidato in candidatos:
    print(candidato)

