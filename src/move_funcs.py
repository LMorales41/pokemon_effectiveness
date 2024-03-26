from src.type_functions import *
from datascience import *



def learnable_moves_for_selected(movepool_tbl, moves ,pokedex):
    """I want to return an array of a selected pokemon's movepool, from there we can work with the data"""
    pokemon_moves_precleanup = movepool_tbl.where('pokemon_id', are.equal_to(pokedex)).column('move_id')
    pokemon_moves_clean = []
    for x in pokemon_moves_precleanup:
        if (moves.where('move_id', are.equal_to(x)).num_rows != 0):
            pokemon_moves_clean.append(x)
    return learnable_moves_string(moves, pokemon_moves_clean)

def print_learnable_moves(move_tbl, selected_mon_movepool):
    for x in selected_mon_movepool:
        print( move_tbl.where('move_id', are.equal_to(x)).column('move_name')[0])

def learnable_moves_string(move_tbl, moveset_int):
        move_names = []
        for x in moveset_int:
            move_names.append(move_tbl.where('move_id', are.equal_to(x)).column('move_name')[0])
        return move_names

def generate_moveset(pkmn_moveset, move_tbl):
    #print(move_tbl)
    split = input("Will this pokemon be a special attacker or physical attacker? (1 for special, 2 for physical): ")
    if (split == 'special'):
        ...
    else:
        ...
