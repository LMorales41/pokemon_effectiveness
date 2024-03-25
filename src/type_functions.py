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
    """Convert type IDs into strings based on a map"""
    types = {
        1 : 'normal', 2: 'fighting', 3 : 'flying', 4 : 'poison', 5 : 'ground',
        6 : 'rock', 7 : 'bug', 8 : 'ghost', 9 : 'steel', 10 : 'fire',
        11 : 'water', 12 : 'grass', 13 : 'electric', 14 : 'psychic', 15 : 'ice',
        16 : 'dragon', 17 : 'dark', 18: 'fairy', 0 : 'none'
    }
    types_string = [types[num] for num in type_ids]
    return types_string



def offense_effectiveness_multiplier(attacking_type, defending_type):
    """Calculate the effectiveness multiplier for a given attacking type against a defending type."""
    effectiveness_chart = {
        'normal': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                   'rock': 0.5, 'bug': 1, 'ghost': 0, 'steel': 0.5, 'fire': 1,
                   'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'fighting': {'normal': 2, 'fighting': 1, 'flying': 0.5, 'poison': 0.5, 'ground': 1,
                     'rock': 2, 'bug': 0.5, 'ghost': 0, 'steel': 2, 'fire': 1,
                     'water': 1, 'grass': 1, 'electric': 1, 'psychic': 0.5, 'ice': 2,
                     'dragon': 1, 'dark': 2, 'fairy': 0.5, 'none': 1},
        'flying': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 1, 'ground': 1,
                   'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                   'water': 1, 'grass': 2, 'electric': 0.5, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'poison': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 0.5, 'ground': 0.5,
                   'rock': 0.5, 'bug': 1, 'ghost': 0.5, 'steel': 0, 'fire': 1,
                   'water': 1, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 2, 'none': 1},
        'ground': {'normal': 1, 'fighting': 1, 'flying': 0, 'poison': 2, 'ground': 1,
                   'rock': 2, 'bug': 0.5, 'ghost': 1, 'steel': 2, 'fire': 2,
                   'water': 1, 'grass': 0.5, 'electric': 2, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'rock': {'normal': 1, 'fighting': 0.5, 'flying': 2, 'poison': 1, 'ground': 0.5,
                 'rock': 1, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 2,
                 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 2,
                 'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'bug': {'normal': 1, 'fighting': 0.5, 'flying': 0.5, 'poison': 1, 'ground': 1,
                'rock': 1, 'bug': 1, 'ghost': 0.5, 'steel': 0.5, 'fire': 0.5,
                'water': 1, 'grass': 2, 'electric': 1, 'psychic': 2, 'ice': 1,
                'dragon': 1, 'dark': 2, 'fairy': 0.5, 'none': 1},
        'ghost': {'normal': 0, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                  'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1,
                  'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                  'dragon': 1, 'dark': 0.5, 'fairy': 1, 'none': 1},
        'steel': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                  'rock': 2, 'bug': 1, 'ghost': 1, 'steel': 0.5,'fire': 0.5, 'water': 0.5, 
                  'grass': 1, 'electric': 0.5, 'psychic': 1,
                  'ice': 2, 'dragon': 1, 'dark': 1, 'fairy': 2, 'none': 1},
        'fire': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                 'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 2, 'fire': 0.5,
                 'water': 0.5, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 2,
                 'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'water': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 2,
                  'rock': 2, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 2,
                  'water': 0.5, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 1,
                  'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'grass': {'normal': 1, 'fighting': 1, 'flying': 0.5, 'poison': 0.5, 'ground': 2,
                  'rock': 2, 'bug': 0.5, 'ghost': 1, 'steel': 0.5, 'fire': 0.5,
                  'water': 2, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 2,
                  'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'electric': {'normal': 1, 'fighting': 1, 'flying': 2, 'poison': 1, 'ground': 0,
                     'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 1,
                     'water': 2, 'grass': 0.5, 'electric': 0.5, 'psychic': 1, 'ice': 1,
                     'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'psychic': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 2, 'ground': 1,
                    'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                    'water': 1, 'grass': 1, 'electric': 1, 'psychic': 0.5, 'ice': 1,
                    'dragon': 1, 'dark': 0, 'fairy': 1, 'none': 1},
        'ice': {'normal': 1, 'fighting': 1, 'flying': 2, 'poison': 1, 'ground': 2,
                'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5,
                'water': 0.5, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 0.5,
                'dragon': 2, 'dark': 1, 'fairy': 1, 'none': 1},
        'dragon': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                   'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                   'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                   'dragon': 2, 'dark': 1, 'fairy': 0, 'none': 1},
        'dark': {'normal': 1, 'fighting': 0.5, 'flying': 1, 'poison': 1, 'ground': 1,
                 'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1,
                 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 2, 'ice': 1,
                 'dragon': 1, 'dark': 0.5, 'fairy': 0.5, 'none': 1},
        'fairy': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 0.5, 'ground': 1,
                 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5,
                 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                 'dragon': 2, 'dark': 2, 'fairy': 1, 'none': 1},
        'none': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 1,
                 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                 'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1}
    }

    return effectiveness_chart[attacking_type][defending_type]



def defense_effectiveness_multiplier(defending_type, attacking_type):
    """Calculate the defensive effectiveness multiplier for a given defending type against an attacking type."""
    effectiveness_chart = {
        'normal': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 1, 'ground': 1,
                   'rock': 1, 'bug': 1, 'ghost': 0, 'steel': 1, 'fire': 1,
                   'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'fighting': {'normal': 1, 'fighting': 1, 'flying': 0.5, 'poison': 0.5, 'ground': 1,
                     'rock': 2, 'bug': 0.5, 'ghost': 0, 'steel': 1, 'fire': 1,
                     'water': 1, 'grass': 1, 'electric': 1, 'psychic': 2, 'ice': 1,
                     'dragon': 1, 'dark': 2, 'fairy': 2, 'none': 1},
        'flying': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 1, 'ground': 1,
                   'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                   'water': 1, 'grass': 0.5, 'electric': 2, 'psychic': 1, 'ice': 2,
                   'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'poison': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 0.5, 'ground': 0.5,
                   'rock': 0.5, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 1,
                   'water': 1, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 0.5, 'none': 1},
        'ground': {'normal': 1, 'fighting': 1, 'flying': 0, 'poison': 2, 'ground': 1,
                   'rock': 2, 'bug': 0.5, 'ghost': 1, 'steel': 2, 'fire': 2,
                   'water': 1, 'grass': 0.5, 'electric': 0, 'psychic': 1, 'ice': 1,
                   'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'rock': {'normal': 1, 'fighting': 0.5, 'flying': 2, 'poison': 1, 'ground': 1,
                 'rock': 1, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                 'water': 2, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 2,
                 'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'bug': {'normal': 1, 'fighting': 0.5, 'flying': 0.5, 'poison': 1, 'ground': 1,
                'rock': 2, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 2,
                'water': 1, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 1,
                'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'ghost': {'normal': 0, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                  'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1,
                  'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                  'dragon': 1, 'dark': 0.5, 'fairy': 1, 'none': 1},
        'steel': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                  'rock': 2, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5,
                  'water': 0.5, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 2,
                  'dragon': 1, 'dark': 1, 'fairy': 2, 'none': 1},
        'fire': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                 'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 2, 'fire': 0.5,
                 'water': 2, 'grass': 0.5, 'water': 2, 'grass': 2, 'electric': 1, 
                 'psychic': 1, 'ice': 2,'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'water': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 2,
                  'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 2,
                  'water': 0.5, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 1,
                  'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'grass': {'normal': 1, 'fighting': 1, 'flying': 2, 'poison': 2, 'ground': 0.5,
                  'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 1, 'fire': 2,
                  'water': 0.5, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 2,
                  'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'electric': {'normal': 1, 'fighting': 1, 'flying': 0.5, 'poison': 1, 'ground': 2,
                     'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                     'water': 1, 'grass': 1, 'electric': 0.5, 'psychic': 1, 'ice': 1,
                     'dragon': 0.5, 'dark': 1, 'fairy': 1, 'none': 1},
        'psychic': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 2, 'ground': 1,
                    'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 1,
                    'water': 1, 'grass': 1, 'electric': 1, 'psychic': 0.5, 'ice': 1,
                    'dragon': 1, 'dark': 2, 'fairy': 1, 'none': 1},
        'ice': {'normal': 1, 'fighting': 1, 'flying': 2, 'poison': 1, 'ground': 2,
                'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 2,
                'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 0.5,
                'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1},
        'dragon': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                   'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5,
                   'water': 0.5, 'grass': 0.5, 'electric': 0.5, 'psychic': 1, 'ice': 2,
                   'dragon': 2, 'dark': 1, 'fairy': 2, 'none': 1},
        'dark': {'normal': 1, 'fighting': 0.5, 'flying': 1, 'poison': 1, 'ground': 1,
                 'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1,
                 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 2, 'ice': 1,
                 'dragon': 1, 'dark': 0.5, 'fairy': 0.5, 'none': 1},
        'fairy': {'normal': 1, 'fighting': 0.5, 'flying': 1, 'poison': 2, 'ground': 1,
                  'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5,
                  'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                  'dragon': 0, 'dark': 2, 'fairy': 1, 'none': 1},
        'none': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1,
                 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 1,
                 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1,
                 'dragon': 1, 'dark': 1, 'fairy': 1, 'none': 1}
    }

    return effectiveness_chart[defending_type][attacking_type]