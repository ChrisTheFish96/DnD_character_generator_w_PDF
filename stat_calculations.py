import random

b_s = "\033[1m"
b_e = "\033[0m"

i_s = "\033[3m"
i_e = "\033[0m"
global stats_dict
global stats_keys
global highest
global second_highest
global second_value
global third_value
global sum_num

stats = []

# Function to create the attribute lists from randomly generated numbers (simulating d20 rolls)
def create_rolls():
    # Define global varaibles
    global stats_dict
    global stats_keys
    global sum_num

    # Create a list with 4 randomly generated values between 1 and 6
    # From the list, find the highest value and add it to the stats list
    # Continue this until the stats list has 6 numbers, one for each attribute
    for _ in range(6):
        four_rolls = []  # Reset the four_rolls list for each iteration
        # max_sum = []
        for _ in range(4):
            random_number = random.randint(1, 6)
            four_rolls.append(random_number)
        
        four_rolls.sort()
        sum_num = four_rolls[-1] + four_rolls[-2] + four_rolls[-3]
        stats.append(sum_num)
        #print(four_rolls)
        #max_in_four = max(four_rolls)
        #stats.append(max_in_four)
    # Create an empty dictionary and create a list of keys for it.
    stats_dict = {}
    stats_keys = ["Strength", "Dexterity", "Intelligence", "Wisdom","Charisma", "Constitution"]

# Functions to generate attribute dictionary, assigning the generated 'rolls' to attributes per class   
# Barbarian attributes 
def barbarian_stats():
    # Define global variables
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    # Creates random numbers as explained above.
    create_rolls()
    
    # Find the highest and second-highest values
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    # Initialize second_value with a default value to avoid NameError when the if conditions are not met
    second_value = 0
    
    # Check if highest and second_highest are the same
    # If they are, the second stat value uses the second higest number
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
    # Highest and second highest number gets removed to ensure no values are repeated
    stats.remove(highest)
    stats.remove(second_highest)
    # Assign stat values to keys in the dictionary
    for key in stats_keys:
        if key == "Strength":
            stats_dict[key] = highest
        elif key == "Constitution":
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    
    hit_points = 12 + int(stats_dict['Constitution'])
    # Return the full dictionary with the correctly assigned stats
    return stats_dict, hit_points

# Bard attributes, works the same as barbarian_stats()
def bard_stats():
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()

    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
    stats.remove(highest)
    stats.remove(second_highest)

    for key in stats_keys:
        if key == 'Charisma':
            stats_dict[key] = highest
        elif key == 'Dexterity':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 8 + int(stats_dict['Constitution'])
    return stats_dict, hit_points

# Cleric attributes
def cleric_stats():
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global third_highest
    global constitution_value
    global stats
    global second_value
    global third_value

    create_rolls()
    
    # Find the three highest values
    highest = max(stats)
    second_highest = sorted(stats)[-2]
    third_highest = sorted(stats)[-3]

    # Initialize second_value and third_value with a default value to avoid NameError when the if conditions are not met
    second_value = 0
    third_value = 0

    # Check if the highest, second highest and third highest numbers are the same
    # If they are that number is saved under third and second number
    # Also checks if only the highest and second number is the same
    # Lastly checks if the second and third highest values are the same if different than highest
    if highest == second_highest == third_highest:
        second_value = second_highest
        third_value = third_highest
    elif highest == second_highest:
        second_value = second_highest
        third_value = third_highest
    else:
        second_value = third_highest
        third_value = second_highest
        
    # Remove the highest, second highest and third highest values from the list to ensure no values are repeated    
    stats.remove(highest)
    stats.remove(second_highest)
    stats.remove(third_highest)
    
    # Assign attribute values to keys in the dictionary
    for key in stats_keys:
        if key == 'Wisdom':
            stats_dict[key] = highest
        elif key == 'Constitution':
            stats_dict[key] = second_highest
        elif key == 'Strength':
            stats_dict[key] = third_highest
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 8 + int(stats_dict['Constitution'])
    # Return complete dictionary of attributes and values
    return stats_dict, hit_points

# Druid attributes, works the same as barbarian_stats()
def druid_stats():

    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
    
    stats.remove(highest)
    stats.remove(second_highest)
    
    for key in stats_keys:
        if key == 'Wisdom':
            stats_dict[key] = highest
        elif key == 'Constitution':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 8 + int(stats_dict['Constitution'])
    return stats_dict, hit_points

# Fighter attributes
def fighter_stats():
    # Define global variables
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global third_highest
    global constitution_value
    global stats
    
    # Create randomly generated list of numbers
    create_rolls()
    
    # Find the three highest value
    highest = max(stats)  
     
    # Determine if the character is a melee or finesse build
    choice = input(f"Do you want to focus on {i_s}{b_s}melee{i_e}{b_e} weapons or {i_s}{b_s}finesse?{i_e}{b_e} ")
    
    # If the build is melee, set strength to the highest value and make dexterity a random value ourt of the list
    # Then remove both values assigned to strength and dexterity
    if choice == 'melee':
        stats_dict['Strength'] = highest
        stats_dict['Dexterity'] = random.choice(stats)
        stats.remove(stats_dict['Strength'])
        stats.remove(stats_dict['Dexterity'])
        
    # If the build is finesse, set dexterity to the highest value and make strength a random value ourt of the list
    # Then remove both values assigned to strength and dexterity
    elif choice == 'finesse':
        stats_dict['Dexterity']= highest  
        stats_dict['Strength'] = random.choice(stats)
        stats.remove(stats_dict['Dexterity'])
        stats.remove(stats_dict['Strength'])
    else:
        return "Input a correct choice"
    
    # Assign attribute values to keys other than strength and dexterity in the dictionary
    for key in stats_keys:
        if key not in ['Strength', 'Dexterity']:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 10 + int(stats_dict['Constitution']) 
    # Return complete dictionary of attributes and values
    return stats_dict, hit_points

# Monk attributes, works the same as barbarian_stats()   
def monk_stats():
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)

    for key in stats_keys:
        if key == 'Dexterity':
            stats_dict[key] = highest
        elif key == 'Wisdom':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 8 + int(stats_dict['Constitution'])        
    return stats_dict, hit_points

# Paladin attributes, works the same as barbarian_stats()   
def paladin_stats():
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)
    
    for key in stats_keys:
        if key == 'Strength':
            stats_dict[key] = highest
        elif key == 'Charisma':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 10 + int(stats_dict['Constitution'])
    return stats_dict, hit_points

# Ranger attributes
def ranger_stats():
    # Define global variables
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    # Creates random numbers as explained above.
    create_rolls()
    
    # Find the highest and second-highest values
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    # Initialize second_value with a default value to avoid NameError when the if conditions are not met
    second_value = 0
    
    # Check if highest and second_highest are the same
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)
    
    # Assign values to keys in the dictionary
    # Determine if the character is a duel-weapon or archery build
    choice = input(f"Do you want to focus on {i_s}{b_s}duel-weapon{i_e}{b_e} fighting or {i_s}{b_s}archery{i_e}{b_e}?")
    
    # If it is a duel-weapon build, strength must be the highest stat
    # Second highest must be wisdom
    # The rest of the attributes have randomly assigned values from the list
    # The dictionary is returned
    if choice == "duel-weapon":
        for key in stats_keys:
            if key == 'Strength':
                stats_dict[key] = highest
            elif key == 'Wisdom':
                stats_dict[key] = second_value
            else:
                random_value = random.choice(stats)
                stats_dict[key] = random_value
                stats.remove(random_value)
        hit_points = 10 + int(stats_dict['Constitution'])
        return stats_dict, hit_points
    
    # If it is an archery build, dexterity must be the highest stat
    # Second highest must be wisdom
    # The rest of the attributes have randomly assigned values from the list
    # The dictionary is returned
    elif choice=="archery":
        for key in stats_keys:
            if key == 'Dexterity':
                stats_dict[key] = highest
            elif key == 'Wisdom':
                stats_dict[key] = second_value
            else:
                random_value = random.choice(stats)
                stats_dict[key] = random_value
                stats.remove(random_value)
        hit_points = 10 + int(stats_dict['Constitution'])        
        return stats_dict, hit_points
    else:
        print("Choose a valid style.")
    
# Rogue attributes, works the same as barbarian_stats()  
def rogue_stats():
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)
    
    for key in stats_keys:
        if key == 'Dexterity':
            stats_dict[key] = highest
        elif key == 'Intelligence':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 8 + int(stats_dict['Constitution'])        
    return stats_dict, hit_points

# Sorcerer attributes, works the same as barbarian_stats()
def sorcerer_stats():
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)
    
    for key in stats_keys:
        if key == 'Charisma':
            stats_dict[key] = highest
        elif key == 'Constitution':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 6 + int(stats_dict['Constitution']) 
    print(stats_dict)       
    return stats_dict, hit_points

# Warlock attributes, works the same as barbarian_stats()
def warlock_stats():
    global stats
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global second_value
    
    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]

    second_value = 0
    
    if highest == second_highest:
        second_value = second_highest
    else:
        second_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)
    
    for key in stats_keys:
        if key == 'Charisma':
            stats_dict[key] = highest
        elif key == 'Constitution':
            stats_dict[key] = second_value
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 8 + int(stats_dict['Constitution'])        
    return stats_dict, hit_points

# Wizard attributes, works the same as cleric_stats()
def wizard_stats():
    global stats_dict
    global stats_keys
    global highest
    global second_highest
    global third_highest
    global constitution_value
    global stats
    global second_value
    global third_value

    create_rolls()
    
    highest = max(stats)
    second_highest = sorted(stats)[-2]
    third_highest = sorted(stats)[-3]

    second_value = 0
    third_value = 0

    if highest == second_highest == third_highest:
        second_value = second_highest
        third_value = third_highest
    elif highest == second_highest:
        second_value = second_highest
        third_value = third_highest
    else:
        second_value = third_highest
        third_value = second_highest
        
    stats.remove(highest)
    stats.remove(second_highest)
    stats.remove(third_highest)
    
    for key in stats_keys:
        if key == 'Intelligence':
            stats_dict[key] = highest
        elif key == 'Constitution':
            stats_dict[key] = second_highest
        elif key == 'Charisma':
            stats_dict[key] = third_highest
        else:
            random_value = random.choice(stats)
            stats_dict[key] = random_value
            stats.remove(random_value)
    hit_points = 6 + int(stats_dict['Constitution'])
    return stats_dict, hit_points