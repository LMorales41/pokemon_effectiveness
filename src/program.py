from datascience import *
import numpy as np
def intro_loop(pkmn_tbl):
    while True:
        # Enter pokemon name
        selected_pokemon = input("Enter your selected Pokemon: ")
        lc_pkmn = selected_pokemon.lower()
        
        # Check if the user wants to continue
        if pkmn_tbl.where('species', are.equal_to(lc_pkmn)).num_rows >= 1:
            return lc_pkmn
            break
        else:
            print("That was not a valid pokemon, please try again! (Up to Gen 8 - Pokemon Sword and Shield, no forms!)")

def get_types(pkmn_clean, lc_pkmn ):
    pokemon_selected = pkmn_clean.where('species', are.equal_to(lc_pkmn))
    type_1 = pokemon_selected.column('type1')[0]
    type_2 = pokemon_selected.column('type2')[0]
    types_to_test = np.array([type_1, type_2])
    return types_to_test

