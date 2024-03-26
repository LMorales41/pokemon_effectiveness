from src.type_functions import *
from datascience import *



def learnable_moves_for_selected(movepool_tbl, moves ,pokedex):
    """I want to return an array of a selected pokemon's movepool, from there we can work with the data"""
    pokemon_moves_precleanup = movepool_tbl.where('pokemon_id', are.equal_to(pokedex)).column('move_id')
    pokemon_moves_clean = []
    for x in pokemon_moves_precleanup:
        if (moves.where('move_id', are.equal_to(x)).num_rows != 0):
            pokemon_moves_clean.append(x)
    return learnable_moves_string(moves, pokemon_moves_clean)

def print_learnable_moves(move_tbl, selected_mon_movepool):
    for x in selected_mon_movepool:
        print( move_tbl.where('move_id', are.equal_to(x)).column('move_name')[0])

def learnable_moves_string(move_tbl, moveset_int):
        move_names = []
        for x in moveset_int:
            move_names.append(move_tbl.where('move_id', are.equal_to(x)).column('move_name')[0])
        return move_names


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
        preset_moves = reformat_move(preset_moves)
        if check_move_legality(preset_moves, move_tbl) == False:
            print("Please enter a legal move.")
            continue
        if preset_moves not in set_moves:
            set_moves.append(preset_moves)
        if len(set_moves) >= move_count:
            return set_moves


def generate_moveset(move_tbl, learnable_moves_tbl, effective_chart):
    set_moves = get_preset_moves(move_tbl)
    moveset_all_types = get_move_types(set_moves, move_tbl)
    moveset_all_types = remove_and_sort(moveset_all_types)

    #Once preset is out the way, fill in the rest with moves with high coverage
    for x in set_moves:
        immunities = get_immunities(x, effective_chart)
        resistances = get_resistances(x, effective_chart)
    max_moves = 4
    count = max_moves - len(set_moves)
    append_these = get_most_cov_type(immunities, resistances, count, effective_chart)
    for x in append_these:
        set_moves.append(x)
    print(set_moves)


        

    