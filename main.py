from src.type_functions import *
from datascience import *
import numpy as np

#Set up all tables properly (eliminate unnecessary columns)
types_table = Table.read_table('data/types.csv')
pokemon_types = Table.read_table('data/pokemon_types.csv')
pkmn = Table.read_table('data/pokemon_species.csv')
pkmn = pkmn.select('id', 'identifier')

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

"""END OF SORTING DATA"""

# I like turtles


"""BEGINNING OF PROGRAM"""
pokemon_selected = pkmn_clean.where('species', are.equal_to('porygon'))
type_1 = pokemon_selected.column('type1')[0]
type_2 = pokemon_selected.column('type2')[0]
types_to_test = np.array([type_1, type_2])


print(types_to_test)