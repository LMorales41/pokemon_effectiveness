from datascience import *
import numpy as np

## 1 = normal 2 = fight 3 = fly 4 = poison
## 5 = ground 6 = rock 7 = bug 8 = ghost
## 9 = steel 10 = fire 11 = water 12 = grass
## 13 = electric 14 = psychic 15 = ice 16 = dragon
## 17 = dark 18 = fairy
def id_into_string(type_id):
    """I will change an int into a string based on what type it is in the database, using a map/dictionary"""
    types = {1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
                6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
                11 : 'water', 12 : 'grass', 13 : ' electric', 14 : 'psychic', 15 : 'ice',
                16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'}
    return types[type_id]

def id_into_string(type_ids):
    """I will change an int into a string based on what type it is in the database, using a map/dictionary"""
    types = {1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
                6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
                11 : 'water', 12 : 'grass', 13 : ' electric', 14 : 'psychic', 15 : 'ice',
                16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'}
    types_string = [types[num] for num in type_ids]
    return types_string
    


#lalala
def get_data_type(tbl):
    """This checks every column for what the data type in that column is """

    for label in tbl.labels:
        first_value = tbl.column(label)[0] 
        data_type = type(first_value)
        print(f"Data type of '{label}': {data_type}")



#Set up all tables properly (eliminate unnecessary columns)
types_table = Table.read_table('types.csv')
pokemon_types = Table.read_table('pokemon_types.csv')
pkmn = Table.read_table('pokemon_species.csv')
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
print(pkmn_clean)