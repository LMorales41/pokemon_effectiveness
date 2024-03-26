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

def reformat_move(move):
    reformatted_move = move.replace(' ', '-').lower()
    return reformatted_move

def check_move_legality(move, moves_tbl):
    if (moves_tbl.where('move_name', are.equal_to(move)).num_rows >= 1):
        return True
    else:
        return False



    
def check_unique_move(moveset, move):
    for x in moveset:
        if x == move:
            return False
    
    return True

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

def convert_damage_type(moves_col):
    """I will change the spec/phys to represent the actual damage types"""
    conversions = {1 : 'status', 2 : 'physical', 3: 'special' }
    damage_type_converted = [conversions[num] for num in moves_col]
    return damage_type_converted

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
    return super_effective_against, neutral_against, resist_or_immune_to
        



def defensive_matchups(multiplier_table, pokemon_types):
    strong = []
    neutral = []
    weak = []
    types_table = Table().with_columns('attacking_type', [], 'defending_type', [], 'multiplier', [])


    #Grabs table with all types matching up into the defensive types given
    for defending_type in pokemon_types:
        storage_table = multiplier_table.where('defending_type', are.equal_to(defending_type))
        types_table.append(storage_table)
    
    #Generates arrays based on previous table created
    hit_super_effective_by = types_table.where('multiplier', are.equal_to(2)).column('attacking_type')
    resist_or_immune_to = types_table.where('multiplier', are.below_or_equal_to(0.5)).column('attacking_type')
    neutral = types_table.where('multiplier', are.equal_to(1)).column('attacking_type')

    #Sorting
    hit_super_effective_by = remove_and_sort(hit_super_effective_by)
    neutral = remove_and_sort(neutral)
    resist_or_immune_to = remove_and_sort(resist_or_immune_to)

    return hit_super_effective_by, neutral, resist_or_immune_to 

def print_effectivenesses(se, neutral, nve):
    print("Your moves are super effective against:", end=' ')
    for x in se:
        print(x, end='')
        if x != len(se) - 1:
            print(', ', end='')


    print("\nYour moves are neutral against: ", end='')
    for x in neutral:
        print(x, end='')
        if x != len(neutral) - 1:
            print(', ', end='')

    
    print("\nYour moves are resisted (or immuned by):", end='')
    for x in nve:
        print(x, end='')
        if x != len(nve) - 1:
            print(', ', end='')
    print("\n")


def stab_effectivenesses(effective_chart, types_to_test, purpose):
    super_effective, neutral, not_very_effective = type_matchups(effective_chart, types_to_test, purpose)
    print_effectivenesses(super_effective, neutral, not_very_effective)

def print_resistances(se, neutral, nve):
    print("You are vulnerable to super effective moves from:", end=' ')
    for x in se:
        print(x, end='')
        if x != len(se) - 1:
            print(', ', end='')


    print("\nYou are neutral into: ", end='')
    for x in neutral:
        print(x, end='')
        if x != len(neutral) - 1:
            print(', ', end='')

    
    print("\nYou resist or are immune to:", end='')
    for x in nve:
        print(x, end='')
        if x != len(nve) - 1:
            print(', ', end='')
    print("\n")

def resistances(effective_chart, types_to_test, purpose):
    super_effective, neutral, not_very_effective = type_matchups(effective_chart, types_to_test, purpose)
    print_resistances(super_effective, neutral, not_very_effective)

def get_move_types(moveset, move_tbl):
    """Gets array with moves, returns array with their types"""
    types_learned = []
    already_checked = set()
    for move in moveset:
        move_type = move_tbl.where('move_name', are.equal_to(move)).column('type')[0]
        if move_type not in already_checked:
            types_learned.append(move_type)
            already_checked.add(move_type)
    return types_learned
    






def get_maximum_coverage (types_learned, effectiveness_chart):
    #Should be string
    move_types = []
    #Should be int
    move_effective_against_ints = []
    for x in types_learned:
        effective_against = effectiveness_chart.where('attacking_type', are.equal_to(x)).where('multiplier', are.above_or_equal_to(1)).num_rows
        move_types.append(x)
        move_effective_against_ints.append(effective_against)
    print('move type len: ', len(move_types))
    print('move_effectiveness len: ', len(move_effective_against_ints))
    print(move_types)
    print(move_effective_against_ints)
    tuple_test = list(zip(move_types, move_effective_against_ints))
    tuple_test = sorted(tuple_test, key=lambda x: x[1], reverse=True)
    print(tuple_test)





        
