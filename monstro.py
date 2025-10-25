class Monstro:
    def __init__(self, vida, ataque):
        self.__vida = vida
        self.__ataque = ataque

    def get_vida(self):
        return self.__vida
    def get_ataque(self):
        return self.__ataque
    
    def set_vida(self, vida_atualizada):
        self.__vida = vida_atualizada



class QuatroBracos(Monstro):
    def __init__(self):
        super().__init__(100, 7)
    
class Chama(Monstro):
    def __init__(self):
        super().__init__(100, 8)

class Diamante(Monstro):
    def __init__(self):
        super().__init__(100, 8)
        
class BalaDeCanhao(Monstro):
    def __init__(self):
        super().__init__(100, 9)
        
class UltraT(Monstro):
    def __init__(self):
        super().__init__(100, 9)



class Duelo:
    def __init__(self, monstro1, monstro2):
        self.numero_do_monstro1 = monstro1
        self.numero_do_monstro2 = monstro2

        self.monstro1 = None
        self.monstro2 = None

        self.dicionario_monstros = {
            1: "Quatro Braços",
            2: "Chama",
            3: "Diamante",
            4: "Bala de Canhão",
            5: "Ultra T"
        }
        

    def preparar_duelo(self):
        if self.numero_do_monstro1 == 1:
            self.monstro1 = QuatroBracos()
        elif self.numero_do_monstro1 == 2:
            self.monstro1 = Chama()
        elif self.numero_do_monstro1 == 3:
            self.monstro1 = Diamante()
        elif self.numero_do_monstro1 == 4:
            self.monstro1 = BalaDeCanhao()
        else:
            self.monstro1 = UltraT()


        if self.numero_do_monstro2 == 1:
            self.monstro2 = QuatroBracos()
        elif self.numero_do_monstro2 == 2:
            self.monstro2 = Chama()
        elif self.numero_do_monstro2 == 3:
            self.monstro2 = Diamante()
        elif self.numero_do_monstro2 == 4:
            self.monstro2 = BalaDeCanhao()
        else:
            self.monstro2 = UltraT()


    def realizar_duelo(self):
        while self.monstro1.get_vida() > 0 and self.monstro2.get_vida() > 0:
            monstro1 = self.dicionario_monstros[self.numero_do_monstro1]
            monstro2 = self.dicionario_monstros[self.numero_do_monstro2]
            
            ataque_do_monstro1 = self.monstro1.get_ataque()
            vida_atualizada_do_monstro2 = self.monstro2.get_vida() - ataque_do_monstro1
            self.monstro2.set_vida(vida_atualizada_do_monstro2)

            print(f"\nAtaque do {monstro1} é:  {ataque_do_monstro1}")
            print(f"A vida do {monstro2} é {vida_atualizada_do_monstro2}")

            if vida_atualizada_do_monstro2 <= 0:
                break
            
            ataque_do_monstro2 = self.monstro2.get_ataque()
            vida_atualizada_do_monstro1 = self.monstro1.get_vida() - ataque_do_monstro2
            self.monstro1.set_vida(vida_atualizada_do_monstro1)

            print(f"\nAtaque do {monstro2} é:  {ataque_do_monstro2}")
            print(f"A vida do {monstro1} é {vida_atualizada_do_monstro1}")

        if vida_atualizada_do_monstro1 > vida_atualizada_do_monstro2:
            print(f"\nO {monstro1} é o vencedor!")
        else:
            print(f"\nO {monstro2} é o vencedor!")