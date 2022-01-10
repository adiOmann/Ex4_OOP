"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI examples for python client to communicates with the server and "play the game!"
"""
import json
import random
from types import SimpleNamespace
import pygame
from pygame import *
from pygame import gfxdraw
from client import Client
from client_python import pokemons
from client_python.GraphAlgo import GraphAlgo
from client_python.pokemons import pokemon

WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666

# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

# init pygame
pygame.init()

# screen
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)

# caption
pygame.display.set_caption("Pokemon Game!")

# icon
icon = pygame.image.load('pikachu.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('background.jpg')
background = pygame.transform.scale2x(background)

demo_screen = screen.copy()
clock = pygame.time.Clock()
pygame.font.init()
client = Client()
client.start_connection(HOST, PORT)
pokeList = client.get_pokemons()
pokemons_obj = json.loads(pokeList, object_hook=lambda d: SimpleNamespace(**d))
print(pokeList)
graph_json = client.get_graph()
radius = 15

# font
FONT = pygame.font.SysFont('Arial', 15, bold=True)

# load the json string into SimpleNamespace Object
graph = json.loads(graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y


class button:
    def __init__(self, colorB, x, y, width, height, text=''):
        self.colorB = colorB
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        colorB = self.colorB
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(screen, colorB, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Ariel', 20)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

            return False


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")

# this command starts the server - the game is running now
client.start()


def redrawWindow():
    stopButton.draw(screen, (0, 0, 0))
    levelButton.draw(screen, (0, 0, 0))


data = json.loads(client.get_info())["GameServer"]
levelButton = button((128, 128, 128), 20, 20, 85, 40, 'LEVEL: ' + str(data["game_level"]))
stopButton = button((255, 0, 0), 980, 20, 85, 40, 'STOP GAME')


def load_pokemon(pok: str):
    J = json.loads(pok)
    ListPokemon = J['Pokemons']
    pokList = []
    for m in ListPokemon:
        try:
            poko = m['Pokemon']
            value = poko['value']
            type = poko['type']
            pos = poko['pos']
            pos = tuple(pos.split(','))
            P = pokemons.pokemon(value, type, pos)
            pokList.append(P)

        except Exception:
            x = random.uniform(35.19, 35.22)
            y = random.uniform(32.05, 32.22)
            pos = (x, y, 0.0)
            type = 0
            value = 0

    return pokList
i = 0
graphString = client.get_graph()
myGraph = GraphAlgo()
myGraph.load_from_string_json(graphString)
poke = client.get_pokemons()
listPok = load_pokemon(poke)

while client.is_running() == 'true':
    redrawWindow()
    pygame.display.update()
    pokeList = json.loads(client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokeList = [p.Pokemon for p in pokeList]
    for p in pokeList:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))
    agents = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))

    # check events
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stopButton.isOver(mouse.get_pos()):
                pygame.quit()
                exit(0)
        if event.type == pygame.MOUSEMOTION:
            if stopButton.isOver(pos):
                stopButton.colorB = (255, 255, 255)
            else:
                stopButton.colorB = (255, 0, 0)

    # refresh surface
    screen.fill(Color(0, 0, 0))
    screen.blit(background, (0, 0))
    stopButton.draw(screen)

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # It's just to get a nice antialiasing circle
        gfxdraw.filled_circle(screen, int(x), int(y), radius, Color(236, 247, 40))  # change the color of the node
        gfxdraw.aacircle(screen, int(x), int(y), radius, Color(0, 0, 0))  # change the color of the frame's node

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(0, 0, 0))  # change the color of node id
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(0, 0, 0), (src_x, src_y), (dest_x, dest_y))  # change the color of the edge

    # draw agents
    for agent in agents:
        iconAgent = pygame.image.load('agent.png')
        iconAgent = pygame.transform.scale(iconAgent, (30, 30))
        iconAgentX = agent.pos.x - 10
        iconAgentY = agent.pos.y - 10
        screen.blit(iconAgent, (iconAgentX, iconAgentY))

    # draw pokemon
    for p in pokeList:
        # represent pokemon
        iconPok = pygame.image.load('pokeball.png')
        iconPok = pygame.transform.scale(iconPok, (30, 30))
        iconPokX = p.pos.x - 10
        iconPokY = p.pos.y - 10
        screen.blit(iconPok, (iconPokX, iconPokY))

        # print value of each pokemon
        font_value = pygame.font.SysFont('Arial', 20, bold=True)
        valPok = font_value.render(str(pokemon.getValue(p)), True, (0, 0, 0))
        screen.blit(valPok, (iconPokX + 10, iconPokY - 30))

    # refresh rate
    timeButton = button((128, 128, 128), 20, 65, 85, 40, 'TIME: ' + str(int(pygame.time.get_ticks() / 1000)))
    timeButton.draw(screen, (0, 0, 0))
    clock.tick(60)

    # choose next edge
    for agent in agents:
        if agent.dest == -1 and len(listPok) > i:
            # n = myGraph.graph.all_in_edges_of_node(agent.src)  # return the all neighbors
            # n = list(n.keys())
            # # next_node = (agent.src - 1) % len(graph.Nodes)
            # next_node = random.choice(n)
            # return list of pokemons
            # we take the pos
            # while i<len(listPok):
            pokePos = listPok[i].getPos()  # Returns the position of one Pokemon at a time
            dest = myGraph.closest(float(pokePos[0]), float(pokePos[1]))  # Where we send the agent
            sp = myGraph.shortest_path(agent.src, dest)  # find the shortest way to the dest
            if (len(sp[1]) > 1):
                next_node = sp[1][1]
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            else:
                # next_node = sp[1][0]
                # client.choose_next_edge(
                #    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
                i = i + 1

    ttl = client.time_to_end()
    print(ttl, client.get_info())
    client.move()
    # display.update()
# game over:

