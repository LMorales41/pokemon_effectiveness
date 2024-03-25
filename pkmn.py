from datascience import *
import numpy as np
## 1 = normal 2 = fight 3 = fly 4 = poison
## 5 = ground 6 = rock 7 = bug 8 = ghost
## 9 = steel 10 = fire 11 = water 12 = grass
## 13 = electric 14 = psychic 15 = ice 16 = dragon
## 17 = dark 18 = fairy

def get_data_type(tbl):
    ### This checks every column for what the data type in that column is ###

    for label in tbl.labels:
        first_value = tbl.column(label)[0]
        data_type = type(first_value)
        print(f"Data type of '{label}': {data_type}")


types_table = Table.read_table('types.csv')
pokemon_types = Table.read_table('pokemon_types.csv')
pkmn = Table.read_table('pokemon_species.csv')
pkmn = pkmn.select('id', 'identifier')

forms_excluded_array = pokemon_types.where('pokemon_id', are.below_or_equal_to(898))
slot1_array = forms_excluded_array.where('slot', 1).column('type_id')
slot2_table = forms_excluded_array.where('slot', 2)
dex = range(1,899)
for id in dex:
    if id not in slot2_table.column('pokemon_id'):
        #filled_table = filled_table.with_row([id, 0, 2])
        print(id)
        slot2_table.append([id, 0, 2])
        
slot2_table.sort('pokemon_id')

pkmn = pkmn.with_column('type1', slot1_array)
#pkmn = pkmn.with_column('type2', [])
print(slot2_table)
#print(forms_excluded_array)