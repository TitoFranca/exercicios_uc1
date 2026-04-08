
for i in range (1, 4):
    print("Dados por alunos");
    idade = int(input("Digite a idade "))
    altura = float(input("Digita a altura "))

idade_media = 0

if altura < 1.70:
    idade_media = idade_media + idade

print(f"A média de idade dos alunos abaixo de 1.70: {idade_media/3}")