from typing import List
from armas import Arma, Disparavel
from golpes import Golpe

class Jogador:
    energia : float
    armas : List[Arma]

    def __init__(self):
        self.energia = 150
        self.armas : List[Arma] = []

    def disparar(self, disparavel : Disparavel, jogador):
        disparavel.disparar(jogador)

    def municiar(self, disparavel : Disparavel):
        disparavel.recarregar()

    def bater(self, jogador, golpe : Golpe=None, arma : Arma=None):
        if golpe == None and arma != None:
            arma.agredir(jogador)
        elif arma == None and golpe != None:
            golpe.golpear(jogador)


    def __str__(self):
        return f"Jogador com energia: {self.energia}"