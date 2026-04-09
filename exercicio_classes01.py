import minhasclasses as mc

# Programa
meucao = mc.Cao(10,"poodle")
peso = meucao.peso
raca = meucao.raca
print(f"meu {raca} pesa {peso} kg")

meu_outro_cao = mc.Cao(12,"labador")
print(f"meu outro cão é um {meu_outro_cao.raca} e pesa {meu_outro_cao.peso } kg")
meu_outro_cao.latir()

print(meucao)
print(meu_outro_cao)

meu_golden = mc.Golden(15, "creme claro")
peso = meu_golden.peso
raca = meu_golden.raca
cor_pelo = meu_golden.cor_pelo
print(f"Meu golden pesa {peso} kg, com pelo {cor_pelo}")
meu_golden.latir()
meu_golden.sentar()

