import math
from model import Coordinate, RouteController, Route
import numpy as np
import random as rn


class GeneticAlgorithm:
    def __init__(self, initital_route, pMutacion, N):
        if N % 2 == 1:
            N = N + 1
        self.N = N
        self.dictionary = {}
        self.rand = pMutacion
        self.Parejas = {}
        self.Individuos = {}
        self.better = None
        self.initial_route = initital_route
        for i in range(self.N):
            self.Individuos[i] = self.generateRandomRoute(initital_route)
        self.better = self.Individuos[0]

    def generateRandomRoute(self, initial_route):
        order = np.random.choice(range(1, len(initial_route)), len(initial_route) - 1, replace=False)
        new_route = [initial_route[0]]
        for i in range(0, len(order)):
            new_route.append(initial_route[order[i]])
        return new_route

    def getBestIndividuo(self):
        #better = self.Individuos[0]
        for i in range(0, len(self.Individuos)):
            if self.func(self.Individuos[i]) <= self.func(self.better):
                self.better = self.Individuos[i]
        return self.better
    def updateBetter(self,hijo_1,hijo_2):
        for i in (hijo_1,hijo_2):
            if self.func(i) <= self.func(self.better):
                self.better = i
    def func(self, individuo):
        route_distance = 0
        for indice in range(0, len(individuo)):
            start_coordinate = individuo[indice]
            if indice + 1 < len(individuo):
                goal_coordinate = individuo[indice + 1]
            else:
                goal_coordinate = individuo[0]
            route_distance += start_coordinate.distance(goal_coordinate, self.dictionary, True)
        return route_distance

    def couples(self):
        Aleatorio = rn.sample(range(self.N // 2, self.N), self.N // 2)
        self.Parejas = {}
        for i in range(self.N // 2):
            self.Parejas[i] = Aleatorio[i]
            self.Parejas[Aleatorio[i]] = i

    def mutate(self, i):
        if rn.random() <= self.rand:
            self.Individuos[i].reverse()
            aux = self.Individuos[i][0]
            self.Individuos[i][0] = self.Individuos[i][len(self.Individuos[i]) - 1]
            self.Individuos[i][(len(self.Individuos[i]) - 1)] = aux

    def check_is_in(self, coordinate, C):
        for i in range(len(C)):
            if coordinate.lat == C[i].lat and coordinate.long == C[i].long:
                return True
        return False

    def hijo(self, individuo, piece_replace):
        individuo_aux = []
        rn.shuffle(piece_replace)
        for i in range(len(individuo)):
            if not self.check_is_in(individuo[i], piece_replace):
                individuo_aux.append(individuo[i])
        return np.concatenate((individuo_aux, piece_replace))

    def cruce(self):
        self.couples()
        temp = 0
        for k, v in self.Parejas.items():
            if temp % 2 == 0:
                split = rn.randint(1, self.N //2)
                H1 = self.hijo(self.Individuos[k], self.Individuos[v][split::])
                H2 = self.hijo(self.Individuos[v], self.Individuos[k][split::])
                self.updateBetter(H1,H2)
                self.Individuos[k] = list(H1)
                self.Individuos[v] = list(H2)
                self.mutate(k)
                self.mutate(v)
            temp += 1

    def sel(self):
        self.couples()
        for k, v in self.Parejas.items():
            if self.func(self.Individuos[k]) <= self.func(self.Individuos[v]):
                self.Individuos[v] = self.Individuos[k]

    def generations(self, N=5):
        for i in range(N):
            self.sel()
            self.cruce()


