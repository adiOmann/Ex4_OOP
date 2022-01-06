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

    def __init__(self,pokemon : pokemons ,is_l :bool , moves : int , grade : int, level:int ,max_user : int ,id :int, graph:DiGraph , agents: int)
        j = json.loads()

        self.pokemon = j['pokemons']
        self.is_l = j['is_l']
        self.moves = j['moves']
        self.grade = j['grade']
        self.level = j['level']
        self.max_user = j['max_user']
        self.id = j['id']
        self.graph_j = j['graph']
        self.graph = DiGraph()
        self.graph = GraphAlgo.load_from_json("../" + self.graph_j)
        self.agents = j['agents']



def get_pokemons(pokemons):
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


    # # choose next edge
    # for agent in agents:
    #     graphString = client.get_graph()
    #     myGraph = GraphAlgo()
    #     myGraph.load_from_string(graphString)
    #
    #     # if agent.dest == -1:
    #     #     next_node = (agent.src - 1) % len(graph.Nodes)
    #     #     client.choose_next_edge(
    #     #         '{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
    #     ttl = client.time_to_end()
    #     print(ttl, client.get_info())

    #client.move()
# game over:
