## 1 = normal 2 = fight 3 = fly 4 = poison
## 5 = ground 6 = rock 7 = bug 8 = ghost
## 9 = steel 10 = fire 11 = water 12 = grass
## 13 = electric 14 = psychic 15 = ice 16 = dragon
## 17 = dark 18 = fairy
from datascience import *
PKMN_TYPES = [
    'normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 
    'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 
    'dark', 'fairy'
]

def remove_and_sort(arr):
    arr = sorted(set(arr))
    return arr


def id_into_string(type_id):
    """I will change an int into a string based on what type it is in the database, using a map/dictionary"""
    types = {1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
                6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
                11 : 'water', 12 : 'grass', 13 : ' electric', 14 : 'psychic', 15 : 'ice',
                16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'}
    return types[type_id]



def id_into_string(type_ids):
    """Convert type IDs into strings based on a map"""
    types = {
        1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
        6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
        11 : 'water', 12 : 'grass', 13 : 'electric', 14 : 'psychic', 15 : 'ice',
        16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'
    }
    types_string = [types[num] for num in type_ids]
    return types_string

def multiplier_conversion(multipliers):
    """I will change an int into a float based on what type it is in the database, using a map/dictionary"""
    conversions = {100 : 1.0, 200 : 2.0, 50 : 0.5, 0 : 0.0}
    multipliers_converted = [conversions[num] for num in multipliers]
    return multipliers_converted


def remove_none(my_array):
    filtered_array = [item for item in my_array if 'none' not in item]
    return filtered_array

def type_matchups(multiplier_table, pokemon_types, purpose):
    remove_none(pokemon_types)
    if (purpose == 'offense'):
        return offensive_matchups(multiplier_table, pokemon_types)
    else:
        return defensive_matchups(multiplier_table, pokemon_types)
    
def offensive_matchups(multiplier_table, pokemon_types):
    strong = []
    neutral = []
    weak = []
    types_table = Table().with_columns('attacking_type', [], 'defending_type', [], 'multiplier', [])
    print(pokemon_types)

    #Grabs table with one/two types and all defending types
    for attacking_type in pokemon_types:
        storage_table = multiplier_table.where('attacking_type', are.equal_to(attacking_type))
        types_table.append(storage_table)
    
    #Generates arrays based on previous table created
    super_effective_against = types_table.where('multiplier', are.equal_to(2)).column('defending_type')
    resist_or_immune_to = types_table.where('multiplier', are.below_or_equal_to(0.5)).column('defending_type')
    neutral_against = types_table.where('multiplier', are.equal_to(1)).column('defending_type')

    #Can split resistances/immunities with these two lines
    #not_very_effective_against = types_table.where('multiplier', are.equal_to(0.5)).column('defending_type')
    #cannot_hit = resist_or_immune_to = types_table.where('multiplier', are.equal_to(0)).column('defending_type')
    #return super_effective_against, neutral_against, not_very_effective_against, cannot_hit
    super_effective_against = remove_and_sort(super_effective_against)
    neutral_against = remove_and_sort(neutral_against)
    resist_or_immune_to = remove_and_sort(resist_or_immune_to)
    return super_effective_against, neutral_against, resist_or_immune_to, 
        



def defensive_matchups(multiplier_table, pokemon_types):
    ...

def print_effectivenesses(se, neutral, nve):
    print("Your moves are super effective against:", end=' ')
    for x in se:
        print(x, end='')
        if x != len(se) - 1:
            print(', ', end='')


    print("\nYour moves are neutral against: ", end='')
    for x in neutral:
        print(x, end='')
        if x != len(se) - 1:
            print(', ', end='')

    
    print("\nYour moves are resisted (or immuned by):", end='')
    for x in nve:
        print(x, end='')
        if x != len(se) - 1:
            print(', ', end='')


def stab_effectivenesses(effective_chart, types_to_test, purpose):
    super_effective, neutral, not_very_effective = type_matchups(effective_chart, types_to_test, purpose)
    print_effectivenesses(super_effective, neutral, not_very_effective)