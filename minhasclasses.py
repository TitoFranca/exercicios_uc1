class Cao:
    def __init__(self, peso, raca):
        self.peso = peso
        self.raca = raca

    def __str__(self):
        return f"{self.raca} {self.peso}"
    
    def latir(self):
        print("au, au")


class Golden(Cao):
    def __init__(self, peso, cor_pelo):
        super().__init__(peso, "golden")
        self.cor_pelo = cor_pelo
    
    def latir(self):
        print("auf,auf auf")
    
    def sentar(self):
        print("Sentado!")

        
    