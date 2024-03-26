from src.type_functions import *
from src.program import *
from datascience import *
import numpy as np


#Set up all tables properly (eliminate unnecessary columns)
types_table = Table.read_table('data/types.csv')
pokemon_types = Table.read_table('data/pokemon_types.csv')
pkmn = Table.read_table('data/pokemon_species.csv')
effective_chart = Table.read_table('data/type_efficacy.csv')
pkmn = pkmn.select('id', 'identifier')
moves = Table.read_table('data/moves.csv')


#First type should be guaranteed for every pokemon
forms_excluded_array = pokemon_types.where('pokemon_id', are.below_or_equal_to(898))
slot1_array = forms_excluded_array.where('slot', 1).column('type_id')


#Second type is not available for every pokemon, we need to fill in monotypes with a "none" on their secondary type
slot2_table = forms_excluded_array.where('slot', 2)
empty_table = Table(['pokemon_id', 'type_id', 'slot'])
dex = range(1,899)
for id in dex:
    if id not in slot2_table.column('pokemon_id'):
        row = {'pokemon_id': id, 'type_id' : 0, 'slot': 2}
        empty_table = empty_table.with_row([id, 0, 2])


#Add the rows to columns to the pkmn table, now we have all types accounted for
slot2_table = slot2_table.append(empty_table).sort('pokemon_id')
slot2_array = slot2_table.where('slot', 2).column('type_id')
pkmn = pkmn.with_column('type1', slot1_array)
pkmn = pkmn.with_column('type2', slot2_array)

#Turn types from digits to strings (more descriptive), change column names
#End product is more readable table
pkmn_clean = pkmn.with_columns('type1', id_into_string(pkmn.column('type1')), 'type2', id_into_string(pkmn.column('type2')))
pkmn_clean = pkmn_clean.relabeled('id', 'pokedex').relabeled('identifier', 'species')
effective_chart = effective_chart.relabeled('damage_type_id', 'attacking_type').relabeled('target_type_id', 'defending_type').relabeled('damage_factor', 'multiplier')
effective_chart = effective_chart.with_columns('attacking_type', id_into_string(effective_chart.column('attacking_type')), 'defending_type', id_into_string(effective_chart.column('defending_type')), 'multiplier', multiplier_conversion(effective_chart.column('multiplier')))

#Begin cleaning up moves table, remove columns and change column name as well as row values
#Remove moves that have no clear damage value (dragons rage, sonicboom, etc.)
moves = moves.relabeled('identifier', 'move_name').relabeled('damage_class_id', 'phys_spec').relabeled('id', 'move_id')
moves = moves.where('phys_spec', are.above_or_equal_to(2)) #only attacking moves left
moves = moves.drop('generation_id', 'effect_chance','pp', 'priority', 'target_id','contest_type_id', 'contest_effect_id', 'super_contest_effect_id')
moves = moves.with_column('phys_spec', convert_damage_type(moves.column('phys_spec')))
moves = moves.where('power', are.above_or_equal_to(1))
moves = moves.relabeled('type_id', 'type')
moves = moves.where('type', are.below_or_equal_to(18))
moves = moves.with_column('type', id_into_string(moves.column('type')))


"""END OF SORTING DATA"""

# I like squirtles


"""BEGINNING OF PROGRAM"""
#User selects pokemon, then we grab its matchups

#lc_pkmn = intro_loop(pkmn_clean, effective_chart)
#lc_pkmn_types = get_types(pkmn_clean, lc_pkmn)
#stab_effectivenesses(effective_chart, lc_pkmn_types, 'offense')
#resistances(effective_chart, lc_pkmn_types, 'defensive')

#User gives a moveset, this checks its general coverage
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

print(moveset)
print(moveset_types)

stab_effectivenesses(effective_chart, moveset_types, 'offense')
#print(moves)
    