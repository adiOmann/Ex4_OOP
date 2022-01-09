######################their start######################33

########################getGraph-->############################

###########################build object init function#####################3

"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import random
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import pokemons
from client_python.DiGraph import DiGraph
from client_python.GraphAlgo import GraphAlgo


class myGame:

    def __init__(self, json_str: str):
        j = json.loads(json_str)['GameServer']

        self.pokemon = j['pokemons']
        self.is_l = j['is_l']
        self.moves = j['moves']
        self.grade = j['grade']
        self.level = j['level']
        self.max_user = j['max_user']
        self.id = j['id']
        self.graph_j = j['graph']
        self.graph = DiGraph()
        self.load_from_string_json("../" + self.graph_j)
        self.agents = j['agents']

    def load_from_string_json(self, guistr: str) -> bool:
        with open(guistr, 'r') as file:
            J = json.loads(guistr)
            ListNode = J['Nodes']
            ListEdge = J['Edges']
            g = DiGraph()
        for n in ListNode:
            try:
                pos = n['pos']
                pos = tuple(pos.split(','))
                pos = (x, y, 0.0)

            except Exception:
                x = random.uniform(35.19, 35.22)
                y = random.uniform(32.05, 32.22)
                pos = (x, y, 0.0)
            self.graph.add_node(n['id'], pos)

        for e in ListEdge:
            self.graph.add_edge(e['src'], e['dest'], e['w'])
        return True

    def load_pokemon(pokemons):
        J = json.loads(pokemons)
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
        return True

    def algo(self,):
        nodelist = DiGraph.NodeDict
        for n in nodelist:
            plus = 1
            src = n
            dest = plus
            plus = plus+1
            GraphAlgo.shortest_path(src, dest)



    # client.move()
# game over:
