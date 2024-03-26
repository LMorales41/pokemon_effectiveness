from src.type_functions import *
from src.program import *
from src.move_funcs import *
from src.setup_cleaning_funcs import *
from datascience import *
import numpy as np

"""DATA SETUP"""


#Set up all tables properly
types_table, pokemon_types, pkmn, effective_chart, moves, learnable_moves = setup_tables()


# Shortened code, placed ugly messy non-looksmaxxing code in setup_cleaning_funcs
# Cleaned up tables by changing names, adding/removing columns; overall made data more workable-with
pkmn_clean = setup_pkmn_table(pkmn, pokemon_types)
effective_chart = setup_effective_chart(effective_chart)
moves = setup_moves_table(moves)
learnable_moves = setup_learnable_moves_table(learnable_moves)


"""END OF SORTING DATA"""

# I like squirtles


"""BEGINNING OF PROGRAM"""
#User selects pokemon, then we grab:
    # The matchups its STAB (Same Type Attack Bonus) has
    # Its defensive matchups
    # Its moveset type matchup
    # Generated moveset for maximum coverage (theoretically)

#intro_loop(pkmn_clean, effective_chart, moves, learnable_moves)
moveset = learnable_moves_for_selected(learnable_moves, moves, 233)
moveset_types = get_move_types(moveset, moves)
get_maximum_coverage(moveset_types, effective_chart)


