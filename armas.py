from golpes import Soco
from abc import ABC, ABCMeta, abstractmethod

class Arma(ABC):
    destruicao : float

    def __init__(self, d: float):
        self.destruicao = d

    def agredir(self, jogador):
        jogador.energia -= 5

    def __str__(self):
        return f"Arma com poder de destruição: {self.destruicao}"

class Faca(Arma):
    lamina : int

    def __init__(self):
        super().__init__(15)
        self.lamina = 10

    def agredir(self, jogador):
        if self.lamina > 0:
            jogador.energia -= self.destruicao
            self.lamina -= 1
        else:
            super().agredir(jogador)

class Soco_Ingles(Faca, Soco):
    def agredir(self, jogador):
        super().agredir(jogador)
        self.golpear(jogador)

class Disparavel(metaclass=ABCMeta):
    @abstractmethod
    def disparar(self, jogador):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma, Disparavel):
    cartucho : int

    def __init__(self):
        self.destruicao = 20
        self.cartuchos = 6

    def disparar(self, jogador):
        if self.cartuchos > 0:
            jogador.energia -= self.destruicao
            self.cartuchos -= 1

    def recarregar(self):
        self.cartuchos = 6

class Lanca_Chamas(Arma, Disparavel):
    gas: float

    def __init__(self):
        self.destruicao = 30
        self.gas = 100

    def disparar(self, jogador):
        if self.gas > 0:
            jogador.energia -= self.destruicao
            self.gas -= 5.5

    def recarregar(self):
        self.gas = 100