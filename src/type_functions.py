## 1 = normal 2 = fight 3 = fly 4 = poison
## 5 = ground 6 = rock 7 = bug 8 = ghost
## 9 = steel 10 = fire 11 = water 12 = grass
## 13 = electric 14 = psychic 15 = ice 16 = dragon
## 17 = dark 18 = fairy
from datascience import *

# Here for use whenever, all types in string form, their index order matches with the type_id assigned to them in data files
PKMN_TYPES = [
    'normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 
    'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 
    'dark', 'fairy'
]

"""Category 1 Functions: Conversions and simple general use functions; aka some of these can be slightly changed to be used in other projects"""

def remove_and_sort(arr):
    """Grabs an array with potentially multiple of same element and sorts + removes for unique elements in this array"""
    # Uses a set
    arr = sorted(set(arr))
    return arr


def reformat_move(move):
    """Grabs a (legal) move and replaces spaces with hyphens to be usable in table; changes to lowercase"""
    reformatted_move = move.replace(' ', '-').lower()
    return reformatted_move


def check_move_legality(move, moves_tbl):
    """If move exists in table, return True, if move does not exist, return False"""
    if (moves_tbl.where('move_name', are.equal_to(move)).num_rows >= 1):
        return True
    else:
        return False

    
def check_unique_move(moveset, move):
    """Iterates through moveset, if move shows up more than one time, returns false"""
    for x in moveset:
        if x == move:
            return False
    
    return True


def id_into_string(type_id):
    """Changes a singular type_id int into a string based on what type it is in the database, using a map/dictionary"""
    types = {1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
                6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
                11 : 'water', 12 : 'grass', 13 : ' electric', 14 : 'psychic', 15 : 'ice',
                16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'}
    return types[type_id]


def id_into_string(type_ids):
    """Converts multiple (an array of) type IDs into strings based on a map"""
    types = {
        1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
        6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
        11 : 'water', 12 : 'grass', 13 : 'electric', 14 : 'psychic', 15 : 'ice',
        16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'
    }
    types_string = [types[num] for num in type_ids]
    return types_string


def multiplier_conversion(multipliers):
    """Changes multiple ints (array of ints) into floats based on what type it is in the database, using a map/dictionary"""
    conversions = {100 : 1.0, 200 : 2.0, 50 : 0.5, 0 : 0.0}
    multipliers_converted = [conversions[num] for num in multipliers]
    return multipliers_converted


def convert_damage_type(moves_col):
    """Changes damage_id into spec/phys strings to represent the actual damage types; special included it is status moves that do not have effectivenesses, thus excluded for now"""
    conversions = {1 : 'status', 2 : 'physical', 3: 'special' }
    damage_type_converted = [conversions[num] for num in moves_col]
    return damage_type_converted


def remove_none(my_array):
    """When pokemon is monotype, none is present in type2 so it can fit inside the table. Thus we need to take it out using this function before it causes a mess"""
    # Array handed to us is always size 2 unless someone (me) does a stinky little oopsie
    filtered_array = [item for item in my_array if 'none' not in item]
    return filtered_array

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    #When not present
    return -1
    

"""END Category 1 Functions"""



"""Category 2 Functions: Specific use functions (Does not fit into above category); overall mostly custom functions that will only work in the scope of this project"""


def type_matchups(multiplier_table, pokemon_types, purpose):
    """Split into offense or defense so it can check proper column."""
    # ALWAYS REMOVE NONE or else ruh roh raggy
    remove_none(pokemon_types)
    if (purpose == 'offense'):
        return offensive_matchups(multiplier_table, pokemon_types)
    else:
        return defensive_matchups(multiplier_table, pokemon_types)
    

def offensive_matchups(multiplier_table, pokemon_types):
    # Same as defensive_matchups, with slight grammatical differences
    """type_matchups leads here, will return in same order as defensive_matchups. Creates second table to avoid extra commands requiring removing all other types"""
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
    #resist_or_immune_to = types_table.where('multiplier', are.below_or_equal_to(0.5)).column('defending_type')
    neutral_against = types_table.where('multiplier', are.equal_to(1)).column('defending_type')
    not_very_effective_against = types_table.where('multiplier', are.equal_to(0.5)).column('defending_type')
    cannot_hit = types_table.where('multiplier', are.equal_to(0)).column('defending_type')

    #Can split resistances/immunities 
    not_very_effective_against = remove_and_sort(not_very_effective_against)
    cannot_hit = remove_and_sort(cannot_hit)
    super_effective_against = remove_and_sort(super_effective_against)
    neutral_against = remove_and_sort(neutral_against)
    #resist_or_immune_to = remove_and_sort(resist_or_immune_to)
    #return super_effective_against, neutral_against, resist_or_immune_to
    return super_effective_against, neutral_against, not_very_effective_against, cannot_hit
        

def defensive_matchups(multiplier_table, pokemon_types):
    # Same as offensive_matchups, with a few grammatical differences
    """type_matchups leads here, will return in same order as offensive_matchups. Creates second table to avoid extra commands requiring removing all other types"""
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
    #resist_or_immune_to = types_table.where('multiplier', are.below_or_equal_to(0.5)).column('attacking_type')
    resist = types_table.where('multiplier', are.equal_to(0.5)).column('attacking_type')
    immune_to = types_table.where('multiplier', are.equal_to(0)).column('attacking_type')
    neutral = types_table.where('multiplier', are.equal_to(1)).column('attacking_type')

    #Sorting
    hit_super_effective_by = remove_and_sort(hit_super_effective_by)
    neutral = remove_and_sort(neutral)
    #resist_or_immune_to = remove_and_sort(resist_or_immune_to)
    resist = remove_and_sort(resist)
    immune_to = remove_and_sort(immune_to)

    #return hit_super_effective_by, neutral, resist_or_immune_to 
    return hit_super_effective_by, neutral, resist, immune_to


def combine_multipliers(se, neutral, nve, immune):
    multiplier = 1
    mult_0x = []
    mult_05x = []
    mult_1x = []
    mult_2x = []
    for types in PKMN_TYPES:
        if types in se:
            multiplier *= 2
        if types in neutral:
            multiplier *= 1
        if types in nve:
            multiplier *= 0.5
        if types in immune:
            multiplier *= 0
        if multiplier == 0:
            mult_0x.append(types)
        elif multiplier > 0 and multiplier < 1:
            mult_05x.append(types)
        elif multiplier > 1:
            mult_2x.append(types)
        else:
            mult_1x.append(types)
        multiplier = 1
    return mult_2x, mult_1x, mult_05x, mult_0x



def get_multiplier_value(a_type, d_type, effective_chart):
    """Returns multiplier value"""
    return effective_chart.where('attacking_type', are.equal_to(a_type)).where('defending_type', are.equal_to(d_type)).column('multiplier')[0]


def print_effectivenesses(se, neutral, nve, immune):
    """Prints out what your moves are effective/neutral/ineffective against"""
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

    
    print("\nYour moves are resisted by:", end='')
    for x in nve:
        print(x, end='')
        if x != len(nve) - 1:
            print(', ', end='')
    
    print("\nYour moves cannot hit:", end='')
    for x in immune:
        print(x, end='')
        if x != len(nve) - 1:
            print(', ', end='')
    print("\n")


def print_resistances(se, neutral, nve, immune):
    # Does not account for abilities like Water Absorb, Levitate, Dry Skin which change multipliers drastically depending on conditions
    # Can be further optimized, current output is not accounting for when 2 types multipliers cause something to turn neutral or super effective or immune
    """Prints what types your Pokemon is weak/neutral/resistant to"""
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

    
    print("\nYou resist:", end='')
    for x in nve:
        print(x, end='')
        if x != len(nve) - 1:
            print(', ', end='')


    print("\nYou are immune to:", end='')
    for x in immune:
        print(x, end='')
        if x != len(immune) - 1:
            print(', ', end='')
    print("\n")


def stab_effectivenesses(effective_chart, types_to_test, purpose):
    """Combines type_matchups, offensive_matchups, and print_effectivenesses functions into one clean callable line"""
    super_effective, neutral, not_very_effective, immune = type_matchups(effective_chart, types_to_test, purpose)
    super_effective, neutral, not_very_effective, immune = combine_multipliers(super_effective, neutral, not_very_effective, immune)
    print_effectivenesses(super_effective, neutral, not_very_effective, immune)
    return super_effective, neutral, not_very_effective, immune


def resistances(effective_chart, types_to_test, purpose):
    """Combines type_matchups, defensive_matchups, and print_resistances functions into one clean callable line"""
    super_effective, neutral, not_very_effective, immune = type_matchups(effective_chart, types_to_test, purpose)
    super_effective, neutral, not_very_effective, immune = combine_multipliers(super_effective, neutral, not_very_effective, immune)
    print_resistances(super_effective, neutral, not_very_effective, immune)
    return super_effective, neutral, not_very_effective, immune


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
  
    tuple_test = list(zip(move_types, move_effective_against_ints))
    tuple_test = sorted(tuple_test, key=lambda x: x[1], reverse=True)

    for type, covers_this_many_types in tuple_test:
        print(type, " can cover ", covers_this_many_types, " types")

def get_preset_moves(move_tbl):
    set_moves = []
    flag1 = True
    flag2 = True
    while flag1:
        #Get count of preset moves
        while flag2:
            try:
                move_count = input("How many preset moves will your Pokemon have?\n")
                move_count = int(move_count)
                if move_count > 4:
                    print("You cannot have more than 4 moves!")
                    continue
                flag2 = False
            except ValueError:
                print("That is not a valid integer, please try again.")
        #End
        
        preset_moves = input("Enter a move you want to have in the generated moveset: ")
        if check_move_legality(preset_moves, move_tbl) == False:
            print("Please enter a legal move.")
            continue
        if preset_moves not in set_moves:
            set_moves.append(preset_moves)
        if len(set_moves) >= move_count:
            return set_moves


def generate_moveset(move_types, move_tbl):
    set_moves = get_preset_moves(move_tbl)
    print (set_moves)
    

    



        
