from stat_calculations import create_rolls, barbarian_stats, bard_stats, cleric_stats,druid_stats,fighter_stats,monk_stats,paladin_stats,ranger_stats,rogue_stats,warlock_stats,wizard_stats
from information import class_list, class_skills, backgrounds, background_skills, skills
b_s = "\033[1m"
b_e = "\033[0m"

i_s = "\033[3m"
i_e = "\033[0m"
global stat_dict
global skills
global skill_string
global background_f
global class_skills_list

def two_skills():
    print("Choose two skills from below to be proficient in:")
    skill_string = class_stat_choice(class_choice)
    print(skill_string)
    while True:
        skill1 = input("First skill: ").capitalize()
        if skill1 in skill_string:
            skills[skill1] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()
    while True:
        skill2 = input("Second skill: ").capitalize()
        if skill2 in skill_string:
            skills[skill2] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()       
    return skills, background_f

def three_skills():
    print("Choose three skills from below to be proficient in:")
    skill_string = class_stat_choice(class_choice)
    print(skill_string)
    while True:
        skill1 = input("First skill: ").capitalize()
        if skill1 in skill_string:
            skills[skill1] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()
    while True:
        skill2 = input("Second skill: ").capitalize()
        if skill2 in skill_string:
            skills[skill2] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print() 
    while True:
        skill3 = input("Third skill: ").capitalize()
        if skill3 in skill_string:
            skills[skill3] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()
    return skills, background_f
    
def four_skills():
    print("Choose three skills from below to be proficient in:")
    skill_string = class_stat_choice(class_choice)
    print(skill_string)
    while True:
        skill1 = input("First skill: ").capitalize()
        if skill1 in skill_string:
            skills[skill1] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()
    while True:
        skill2 = input("Second skill: ").capitalize()
        if skill2 in skill_string:
            skills[skill2] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print() 
    while True:
        skill3 = input("Third skill: ").capitalize()
        if skill3 in skill_string:
            skills[skill3] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()
    while True:
        skill4 = input("Fourth skill: ").capitalize()
        if skill4 in skill_string:
            skills[skill4] = "X"
            break
        else:
            print("Please choose a skill from the list above.")
            print()
    return skills, background_f

def background_stats():
    global skills
    global backgr_choice
    print("Choose a background:")  
    for backgr, description in backgrounds.items():
        print(f"{i_s}{b_s}{backgr:<10}{i_e}{b_e} -   {description}")     
    while True:
        backgr_choice = input("What have you decided on? ").lower()
        print()
        if (backgr_choice == 'acolyte' or
            backgr_choice == 'charlatan' or
            backgr_choice == 'criminal' or
            backgr_choice == 'entertainer' or
            backgr_choice == 'folk hero' or
            backgr_choice == 'guild artisan' or
            backgr_choice == 'hermit' or
            backgr_choice == 'noble' or
            backgr_choice == 'outlander' or
            backgr_choice == 'sage' or
            backgr_choice == 'sailor' or
            backgr_choice == 'soldier' or
            backgr_choice == 'urchin'):
            break
        else:
            print("Please choose from the list provided.")
            print()

    if backgr_choice in background_skills:
        background_skill_list = background_skills[backgr_choice]
    else:
        background_skills_list = []

    if backgr_choice in background_skills:
        chosen_background = background_skills[backgr_choice]
        for skill in chosen_background:
            skills[skill] = "X"  # Change proficiency to "X" for selected skills
    
        return skills, backgr_choice

def class_inp():
    global class_choice
    print("What class do you want to make your character?")
    for cls, description in class_list.items():
        print(f"{i_s}{b_s}{cls:<11}{i_e}{b_e} -   {description}")
    while True:
        class_choice = input('What have you decided on? ').replace(" ", "").lower()
        if (class_choice == 'barbarian' or
            class_choice == 'bard' or
            class_choice == 'cleric' or
            class_choice == 'druid' or
            class_choice == 'fighter' or
            class_choice == 'monk' or
            class_choice == 'paladin' or
            class_choice == 'ranger' or
            class_choice == 'rogue' or
            class_choice == 'sorcerer' or
            class_choice == 'wizard' or
            class_choice == 'warlock'):
            break
        else:
            print("Please choose from the list provided.")
            print()
    return class_choice

def class_stat_choice(class_choice):
    global backgr_choice
    background_skill_list = background_skills[backgr_choice]  # Get the skills already covered by the background
    class_skills_list = class_skills[class_choice] # Get the skills associated with the chosen class
    leftover_list = []
    for skill in background_skill_list:
        if skill in class_skills_list:
            class_skills_list.remove(skill)
    skill_string = ", ".join(class_skills_list)
    for skill in skill_string:
        skill = skill.capitalize()
    return skill_string

def class_stats(class_choice): 
    global skills
    global skill_string
    global background_f
    if class_choice == 'barbarian':
        chosen_class = 'barbarian'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'bard':
        chosen_class = 'bard'
        background_stats()
        background_f = backgr_choice
        skills, background_f = three_skills()
        return skills, background_f

    elif class_choice == 'cleric':
        chosen_class = 'cleric'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'druid':
        chosen_class = 'druid'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'fighter':
        chosen_class = 'fighter'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'monk':
        chosen_class = 'monk'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f
        
    elif class_choice == 'paladin':
        chosen_class = 'paladin'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'ranger':
        chosen_class = 'ranger'
        background_stats()
        background_f = backgr_choice
        skills, background_f = three_skills()
        return skills, background_f

    elif class_choice == 'rogue':
        chosen_class = 'rogue'
        background_stats()
        background_f = backgr_choice
        skills, background_f = four_skills()
        return skills, background_f

    elif class_choice == 'sorcerer':
        chosen_class = 'sorcerer'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'warlock':
        chosen_class = 'warlock'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

    elif class_choice == 'wizard':
        chosen_class = 'wizard'
        background_stats()
        background_f = backgr_choice
        skills, background_f = two_skills()
        return skills, background_f

