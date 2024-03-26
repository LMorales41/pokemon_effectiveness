from src.type_functions import *
from datascience import *
import numpy as np

def setup_tables():
    """Sets up all tables, add any necessary tables to this function and return at the end"""


    types_table = Table.read_table('data/types.csv')
    pokemon_types = Table.read_table('data/pokemon_types.csv')
    pkmn = Table.read_table('data/pokemon_species.csv')
    effective_chart = Table.read_table('data/type_efficacy.csv')
    moves = Table.read_table('data/moves.csv')
    learnable_moves = Table.read_table('data/pokemon_moves.csv')
    return types_table, pokemon_types, pkmn, effective_chart, moves, learnable_moves





def setup_pkmn_table(pkmn, pokemon_types):
    """Contains info of all pokemon, including their types(type1/type2), pokedex number(pokedex), and their names(species)"""

    # First exclude unnecessary columns and rows and add in guaranteed type1 column
    pkmn = pkmn.select('id', 'identifier')
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


    return pkmn_clean



def setup_effective_chart(effective_chart):
    """Columns are: attacking_type, defending_type, and the multiplier that comes when the attacking type attacks into the defending type"""

    #Clean up chart by renaming columns and then changing ids of types to strings with the names of thet types instead
    effective_chart = effective_chart.relabeled('damage_type_id', 'attacking_type').relabeled('target_type_id', 'defending_type').relabeled('damage_factor', 'multiplier')
    effective_chart = effective_chart.with_columns('attacking_type', id_into_string(effective_chart.column('attacking_type')), 'defending_type', id_into_string(effective_chart.column('defending_type')), 'multiplier', multiplier_conversion(effective_chart.column('multiplier')))

    return effective_chart



def setup_moves_table(moves):
    """Moves table contains all moves and their data"""
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

    return moves

def setup_learnable_moves_table(learnable_moves):
    """Learnable moves contains all the moves that a specific pokemon can learn"""
    #Big boy table BE CAREFUL (its yuge)
    # original columns are: pokemon_id,version_group_id,move_id,pokemon_move_method_id,level,order
    # We want to erase unwanted columns, and change things to be as readable as possible
    # We will leave this table in ids, as changing them would be far, far too time consuming
    learnable_moves = learnable_moves.drop('version_group_id', 'pokemon_move_method_id', 'level', 'order')
    learnable_moves = learnable_moves.where('pokemon_id', are.below_or_equal_to(898))

    return learnable_moves

