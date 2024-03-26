from src.type_functions import *
from src.move_funcs import *
from datascience import *
import numpy as np

#Basic program loop
def intro_loop(pkmn_tbl, effective_chart, moves, learnable_moves):
    while True:
        # Enter pokemon name
        selected_pokemon = input("Enter your selected Pokemon: ")
        lc_pkmn = selected_pokemon.lower()
        
        # Complicatedness more like complicated MESS amirite xdddddddddddddddddddddd
        if pkmn_tbl.where('species', are.equal_to(lc_pkmn)).num_rows >= 1:
            lc_pkmn_pokedex = pkmn_tbl.where('species', are.equal_to(lc_pkmn)).column('pokedex')[0]
            lc_pkmn_types = get_types(pkmn_tbl, lc_pkmn)
            resistances(effective_chart, lc_pkmn_types, 'defensive')
            moveset_cont = input("Would you like to check the effectiveness of this Pokemon's moveset? (Y/N)")
            if (moveset_cont == 'y' or moveset_cont == 'Y'):
                #User gives the pokemon a moveset, this checks its general coverage
                moveset, moveset_types = get_moveset_info(moves)
                stab_effectivenesses(effective_chart, moveset_types, 'offense')
                print("Your total movepool coverages: ")
                moveset = learnable_moves_for_selected(learnable_moves, moves, lc_pkmn_pokedex)
                print(moveset)
                moveset_types = get_move_types(moveset, moves)
                get_maximum_coverage(moveset_types, effective_chart)
            #generate_cont = input("Would you like to generate a moveset for maximum coverage? (Y/N)")
            #if (generate_cont == 'y' or generate_cont == 'Y'):
                #pkmn_moveset_all = learnable_moves_for_selected(learnable_moves, moves, lc_pkmn_pokedex)
                #desired_moveset = generate_moveset(pkmn_moveset_all, moves)
            break
        else:
            print("That was not a valid pokemon, please try again! (Up to Gen 8 - Pokemon Sword and Shield, no forms!)")

def get_moveset_info(moves):
    flag = True
    while flag:
        try:
            move_count = input("How many moves will your Pokemon have?\n")
            move_count = int(move_count)
            if move_count > 4:
                print("You cannot have more than 4 moves!")
                continue
            flag = False
        except ValueError:
            print("That is not a valid integer, please try again.")

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

    moveset_types = get_move_types(moveset, moves)
    return moveset, moveset_types 

def get_types(pkmn_clean, lc_pkmn ):
    pokemon_selected = pkmn_clean.where('species', are.equal_to(lc_pkmn))
    type_1 = pokemon_selected.column('type1')[0]
    type_2 = pokemon_selected.column('type2')[0]
    types_to_test = np.array([type_1, type_2])
    return types_to_test

