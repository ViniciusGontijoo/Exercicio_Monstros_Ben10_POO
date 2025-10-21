class Monstro:
    def __init__(self, vida, ataque):
        self.__vida = vida
        self.__ataque = ataque

    def get_vida(self):
        return self.__vida
    def get_ataque(self):
        return self.__ataque
    
    def set_vida(self, vida):
        self.__vida = vida


class QuatroBracos(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque)
    
class Chama(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque)

class Diamante(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque)
        
class BalaDeCanhao(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque)
        
class UltraT(Monstro):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque)

class Duelo:
    def __init__(self, monstro1, monstro2):
        self.monstro1 = monstro1
        self.monstro2 = monstro2
        
    def monstro_ganhador(self):
        dicionario_monstros = {
            1: "Quatro Braços",
            2: "Chama",
            3: "Diamante",
            4: "Bala de Canhão",
            5: "Ultra T"
        }

        numero_monstro1 = self.monstro1
        numero_monstro2 = self.monstro2

        if self.monstro1 == 1:
            self.monstro1 = QuatroBracos(100, 7)
        elif self.monstro1 == 2:
            self.monstro1 = Chama(100, 8)
        elif self.monstro1 == 3:
            self.monstro1 = Diamante(100, 8)
        elif self.monstro1 == 4:
            self.monstro1 = BalaDeCanhao(100, 9)
        else:
            self.monstro1 = UltraT(100, 9)


        if self.monstro2 == 1:
            self.monstro2 = QuatroBracos(100, 7)
        elif self.monstro2 == 2:
            self.monstro2 = Chama(100, 8)
        elif self.monstro2 == 3:
            self.monstro2 = Diamante(100, 8)
        elif self.monstro2 == 4:
            self.monstro2 = BalaDeCanhao(100, 9)
        else:
            self.monstro2 = UltraT(100, 9)

        vida_monstro1 = 100
        vida_monstro2 = 100

        while vida_monstro1 > 0 and vida_monstro2 > 0:
            vida_monstro2 -= self.monstro1.get_ataque()
            print(f"\nAtaque do {dicionario_monstros[numero_monstro1]} é:  {self.monstro1.get_ataque()}")
            print(f"A vida do {dicionario_monstros[numero_monstro2]} é {vida_monstro2}")

            if vida_monstro2 <= 0:
                break
            
            vida_monstro1 -= (self.monstro2.get_ataque())
            print(f"\nAtaque do {dicionario_monstros[numero_monstro2]} é:  {self.monstro2.get_ataque()}")
            print(f"A vida do {dicionario_monstros[numero_monstro1]} é {vida_monstro1}")

        if vida_monstro1 > vida_monstro2:
            print(f"\nO {dicionario_monstros[numero_monstro1]} é o vencedor!")
        else:
            print(f"\nO {dicionario_monstros[numero_monstro2]} é o vencedor!")