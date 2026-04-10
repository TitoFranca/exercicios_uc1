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
lista_nomes_aprovados = []
for candidato in candidatos:
    #calcular média#
    media = (candidato.nota_portugues + candidato.nota_matematica + candidato.nota_conhecimento_gerais)/3
    candidato.media = media

    #verificar se o aluno tem nota abaixo de 2
    if candidato.nota_portugues <2.0 or candidato.nota_matematica <2.0 or candidato.nota_conhecimento_gerais <2.0:
        candidato_tem_nota_abaixo_2 = True
    else:
        candidato_tem_nota_abaixo_2 = False

    #definir a situação do aluno
    if candidato.media > 4.0 and candidato_tem_nota_abaixo_2 == False:
        candidato.situacao = "Aprovado"

for candidato in candidatos:
    print(f"Candidato: {candidato.nome} obteve média igual a {candidato.media} e está {candidato.situacao}")

# Variáveis para os novos requisitos
soma_portugues = 0
cont_item_c = 0
cont_item_d = 0

for candidato in candidatos:
    # --- Cálculo da Média e Situação (Seu código original) ---
    media = (candidato.nota_portugues + candidato.nota_matematica + candidato.nota_conhecimento_gerais) / 3
    candidato.media = media
    
    abaixo_minimo = candidato.nota_portugues < 2 or candidato.nota_matematica < 2 or candidato.nota_conhecimento_gerais < 2
    
    if candidato.media > 4.0 and not abaixo_minimo:
        candidato.situacao = "APROVADO"
    else:
        candidato.situacao = "REPROVADO"

    # --- ITEM B: Acumular nota de português para média posterior ---
    soma_portugues += candidato.nota_portugues

    # --- ITEM C: Média > 4.5 E Conhecimentos Gerais > 6.0 ---
    if candidato.media > 4.5 and candidato.nota_conhecimento_gerais > 6.0:
        cont_item_c += 1

    # --- ITEM D: Aprovado E Matemática > 5.0 ---
    if candidato.situacao == "APROVADO" and candidato.nota_matematica > 5.0:
        cont_item_d += 1

# --- Exibição dos Resultados ---

# a) Nomes dos aprovados
print("\n--- Candidatos Aprovados ---")
for c in candidatos:
    if c.situacao == "APROVADO":
        print(f"- {c.nome}")

# b) Média de Português (Soma total / quantidade de candidatos)
if len(candidatos) > 0:
    media_geral_port = soma_portugues / len(candidatos)
    print(f"\nb) Média da prova de Português: {media_geral_port:.2f}")

# c) Contador específico
print(f"c) Candidatos com Média > 4.5 e Conhecimentos Gerais > 6.0: {cont_item_c}")

# d) Contador específico
print(f"d) Candidatos aprovados com Matemática > 5.0: {cont_item_d}")