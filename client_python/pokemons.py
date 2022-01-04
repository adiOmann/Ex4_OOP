import json
import random


class Pokemon:
    def __init__(self, listP: []):
        self.listP = listP

    def get_pokemons(feile_str : str):
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