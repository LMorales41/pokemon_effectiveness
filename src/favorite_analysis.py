import numpy as np
import matplotlib.pyplot as plt
from datascience import *

def random_pkmn(bool_arr):
    """Just needs a table that shows which pokemon have already been picked, will generate nonselected random"""
    generated = np.random.randint(0, 897) 
    while (bool_arr[generated] == True):
        generated = np.random.randint(0,897)
    return generated


def present_favorites(pkmn_tbl):
    """Shows 2 pokemon to choose from at a time, will return two arrays of chosen and unchosen pkmn"""
    #loop_size = list(range(449))
    loop_size = 50

    bool_arr = np.full(898, False, dtype=bool)
    selected_arr = []
    unselected_arr = []

    for i in range(loop_size):
        first_mon = random_pkmn(bool_arr)
        bool_arr[first_mon] = True  #flip this to true to avoid generating the same number again
        second_mon = random_pkmn(bool_arr)
        bool_arr[second_mon] = True

        pkmn_arr = pkmn_tbl.column('species')

        first_pkmn = pkmn_arr[first_mon]
        second_pkmn = pkmn_arr[second_mon]


        selection = input("Do you prefer " + first_pkmn + " or " + second_pkmn + " please enter 1 or 2! ")
        if (selection == '1'):
            selected_arr.append(first_mon)
            unselected_arr.append(second_mon)
        elif(selection == '2'):
            selected_arr.append(second_mon)
            unselected_arr.append(first_mon)
        
    return selected_arr, unselected_arr
    
def get_types(mon_list, pkmn_tbl):
    list_2d = []
    type_list = []
    for x in mon_list:
        type_list.append(pkmn_tbl.column('type1')[x])

        if pkmn_tbl.column('type2')[x] != 'none': #To account for monotypes
            type_list.append(pkmn_tbl.column('type2')[x])

        #list_2d.append(type_list)
        #type_list = []
    return type_list

def most_common_type(pokemon_types):
    type_counts = {}
    for type in pokemon_types:
        if type in type_counts:
            type_counts[type] += 1
        else:
            type_counts[type] = 1
    most_common_type = max(type_counts, key=type_counts.get)
    return most_common_type


def analyze_choices(pkmn_tbl):
    selected_mons, unselected_mons = present_favorites(pkmn_tbl)
    type_list_selected = get_types(selected_mons, pkmn_tbl)
    type_list_unselected = get_types(unselected_mons, pkmn_tbl)
    type_list_selected = sorted(type_list_selected)
    type_list_unselected = sorted(type_list_unselected)


    #print("Your selected types: ")
    #print(type_list_selected)
    #print("Your not selected types: ")
    #print(type_list_unselected)
    
    # Repeat Code for 2 seperate images
    type_counts1 = {}
    for type in type_list_selected:
        if type in type_counts1:
            type_counts1[type] += 1
        else:
            type_counts1[type] = 1

    types1 = list(type_counts1.keys())
    counts1 = list(type_counts1.values())

    plt.bar(types1, counts1, color='skyblue')
    plt.xlabel('Pokemon Type')
    plt.ylabel('Frequency')
    plt.title('Frequency of Pokemon Types')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.savefig('selectedplot.png')
            
    type_counts2 = {}
    for type in type_list_unselected:
        if type in type_counts2:
            type_counts2[type] += 1
        else:
            type_counts2[type] = 1

    # Extract types and counts
    types2 = list(type_counts2.keys())
    counts2 = list(type_counts2.values())

    plt.bar(types2, counts2, color='skyblue')
    plt.xlabel('Pokemon Type')
    plt.ylabel('Frequency')
    plt.title('Frequency of Pokemon Types')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.savefig('unselectedplot.png')

    # Display common types for visual view
    common_type = most_common_type(type_list_selected)
    print("Your most common favorite type is: " + common_type )
    common_type = most_common_type(type_list_unselected)
    print("Your most common least favorite type is: " + common_type )



def init_system(pkmn_tbl):
    analyze_choices(pkmn_tbl)




    
