from FPS import Jogador
from armas import Lanca_Chamas, Revolver, Soco_Ingles
from golpes import Soco

def main():
    jogador1 = Jogador()
    jogador2 = Jogador()

    print(jogador1)
    print(jogador2)

    jogador1.armas.append(Soco_Ingles())
    jogador2.armas.append(Lanca_Chamas())

    jogador1.armas[0].agredir(jogador2)
    jogador2.armas[0].disparar(jogador1)

    jogador1.bater(jogador2, Soco())
    jogador2.bater(jogador1, arma=jogador2.armas[0])

    print(jogador1)
    print(jogador2)

if __name__ == "__main__":
    main()
