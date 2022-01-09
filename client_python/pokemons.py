import json
import random

from client_python.DiGraph import Edge


class pokemon():

    def __init__(self, value, type, pos):
        self.value = value
        self.type = type
        self.pos = pos

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



