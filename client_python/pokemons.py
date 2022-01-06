import json
import random

from client_python.DiGraph import Edge


class pokemon:
    def _init_(self, edge: Edge, value, type, pos, listP: []):
        self.listP = listP
        self.edge = edge
        self.value = value
        self.type = type
        self.pos = pos

    def getEdge(self):
        return self.edge

    def setEdge(self, e):
        self.edge = e

    def getValue(self):
        return self.value

    def setValue(self, v):
        self.value = v

    def getType(self):
        return self.type

    def setType(self, t):
        self.type = t

    def getPos(self):
        return self.pos

    def setPos(self, p):
        self.pos = p

    def get_pokemons(feile_str: str):
        J = json.loads(feile_str)
        ListPokemon = J['pokemon']
        for n in ListPokemon:
            try:
                value = n['value']
                type = n['type']
                pos = n['pos']
                pos = tuple(pos.split(','))

            except Exception:
                x = random.uniform(35.19, 35.22)
                y = random.uniform(32.05, 32.22)
                pos = (x, y, 0.0)
                type = 0
                value = 0
        return ListPokemon