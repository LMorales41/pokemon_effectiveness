from src.type_functions import *
from datascience import *
import numpy as np


def intro_loop(pkmn_tbl, effective_chart):
    while True:
        # Enter pokemon name
        selected_pokemon = input("Enter your selected Pokemon: ")
        lc_pkmn = selected_pokemon.lower()
        
        # Check if the user wants to continue
        if pkmn_tbl.where('species', are.equal_to(lc_pkmn)).num_rows >= 1:
            lc_pkmn_types = get_types(pkmn_tbl, lc_pkmn)
            #stab_effectivenesses(effective_chart, lc_pkmn_types, 'offense')
            resistances(effective_chart, lc_pkmn_types, 'defensive')
            break
        else:
            print("That was not a valid pokemon, please try again! (Up to Gen 8 - Pokemon Sword and Shield, no forms!)")

def get_moveset_info(moves):
    move_count = input("How many moves will your Pokemon have?\n")
    move_count = int(move_count)
    moveset = []
    while len(moveset) < move_count:
        my_move = input("Enter move: ")
        my_move = reformat_move(my_move)
        legality = check_move_legality(my_move, moves)
        uniq_move = check_unique_move(moveset, my_move)
        if (legality and uniq_move):
            moveset.append(my_move)
        else:
            print("Adding that move is not legal, please enter again. ")

    moveset_types = get_moveset_types(moveset, moves)
    return moveset, moveset_types 

def get_types(pkmn_clean, lc_pkmn ):
    pokemon_selected = pkmn_clean.where('species', are.equal_to(lc_pkmn))
    type_1 = pokemon_selected.column('type1')[0]
    type_2 = pokemon_selected.column('type2')[0]
    types_to_test = np.array([type_1, type_2])
    return types_to_test

