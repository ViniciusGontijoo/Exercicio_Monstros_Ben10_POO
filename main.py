print("\n1 - Quatro Braços")
print("2 - Chama")
print("3 - Diamante")
print("4 - Bala de Canhão")
print("5 - Ultra T")

monstro1 = int(input("\nDigite o número do Monstro 1 (1 a 5): "))

if (monstro1 < 1 or monstro1 > 5):
    while monstro1 < 1 or monstro1 > 5:
        print("ERRO: Número inválido. O número deve ser entre 1 e 5")
        monstro1 = int(input("\nDigite novamente o número do Monstro 1 (1 a 5): "))

monstro2 = int(input("\nDigite o número do Monstro 2 (1 a 5): "))

if (monstro2 < 1 or monstro2 > 5):
    while monstro2 < 1 or monstro2 > 5:
        print("ERRO: Número inválido. O número deve ser entre 1 e 5")
        monstro2 = int(input("\nDigite novamente o número do Monstro 2 (1 a 5): "))

if monstro1 == monstro2:
    print(monstro1)
    print(monstro2)
    print("\nERRO: O monstro 1 deve ser diferente do monstro 2.")
    print("Os monstros não podem ser iguais. Por favor, escolha dois monstros diferentes e tente novamente.")
else:
    from Exercicio_Monstros_Ben10_POO.monstro import Duelo

    duelo_monstros = Duelo(monstro1, monstro2)
    duelo_monstros.monstro_ganhador()