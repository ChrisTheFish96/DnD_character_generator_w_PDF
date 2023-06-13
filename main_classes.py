import random
import PyPDF4
from stat_calculations import (create_rolls, 
    barbarian_stats, 
    bard_stats, 
    cleric_stats, 
    druid_stats, 
    fighter_stats, 
    monk_stats, 
    paladin_stats, 
    ranger_stats, 
    rogue_stats, 
    sorcerer_stats, 
    warlock_stats, 
    wizard_stats
    )
from information import (languages, 
    race_list, 
    class_list, 
    dwarf_subraces, 
    elf_subraces, 
    halfling_subraces, 
    gnome_subraces, 
    backgrounds, 
    skills, 
    dwarf_traits, 
    background_skills, 
    class_skills, 
    barbarian_saving_throws, 
    bard_saving_throws, 
    cleric_saving_throws, 
    druid_saving_throws, 
    fighter_saving_throws, 
    monk_saving_throws, 
    paladin_saving_throws, 
    ranger_saving_throws, 
    rogue_saving_throws, 
    sorcerer_saving_throws, 
    warlock_saving_throws, 
    wizard_saving_throws, 
    dwarf_traits, 
    mountain_dwarf_traits, 
    hill_dwarf_traits, 
    duergar_traits, 
    human_traits, 
    elf_traits, 
    highelf_traits, 
    woodelf_traits, 
    darkelf_traits, 
    halfling_traits, 
    lightfoot_traits, 
    stout_traits, 
    dragonborn_traits, 
    gnome_traits, 
    forest_traits, 
    rock_traits, 
    half_elf_traits, 
    half_orc_traits, 
    tiefling_traits
    )
from class_info import (class_inp, 
    class_stat_choice, 
    class_stats, 
    background_stats
    )
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Bold and italics values for printing throughout.
b_s = "\033[1m"
b_e = "\033[0m"

i_s = "\033[3m"
i_e = "\033[0m"

# Race class, inclused method to determine attribute scores per race.
class Race:
    def __init__(self, name, ability_bonuses, traits):
        self.name = name
        self.ability_bonuses = ability_bonuses
        self.traits = traits

    def __str__(self):
        return self.name.capitalize()

    def calculate_attribute_scores(self, attribute_scores):
        for attribute, bonus in self.ability_bonuses.items():
            attribute_scores[attribute] += bonus
        return attribute_scores

# Race class, inclused method to determine attribute scores per subrace.
class Subrace:
    def __init__(self, name, parent_race, ability_bonuses, traits):
        self.name = name
        self.parent_race = parent_race
        self.ability_bonuses = ability_bonuses
        self.traits = traits
    def __str__(self):
        return self.name.capitalize()

    def calculate_attribute_scores(self, attribute_scores):
        for attribute, bonus in self.ability_bonuses.items():
            attribute_scores[attribute] += bonus
        return attribute_scores

# Class class.
class Class:
    def __init__(self, name, hit_dice, saving_throws):
        self.name = name
        self.hit_dice = hit_dice
        self.saving_throws = saving_throws

    def __str__(self):
        return self.name.capitalize()

# Function to determine language choice.
def lang_func ():
    for lang, description in languages.items():
        print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
    print()
    language_choice = input("What have you decided on? ").replace(" ", "").capitalize()
    print()
    return language_choice

# Function to calculate modifier scores.
def calculate_modifier(score):
    if score == 1:
        return '-5'
    elif 2 <= score <= 3:
        return '-4'
    elif 4 <= score <= 5:
        return '-3'
    elif 6 <= score <= 7:
        return '-2'
    elif 8 <= score <= 9:
        return '-1'
    elif 10 <= score <= 11:
        return '+0'
    elif 12 <= score <= 13:
        return '+1'
    elif 14 <= score <= 15:
        return '+2'
    elif 16 <= score <= 17:
        return '+3'
    elif 18 <= score <= 19:
        return '+4'
    elif 20 <= score <= 21:
        return '+5'
    elif 22 <= score <= 23:
       return '+6'
    elif 24 <= score <= 25:
        return '+7'
    elif 26 <= score <= 27:
        return '+8'
    elif 28 <= score <= 29:
        return '+9'
    elif score == 30:
        return '+10'

# Main character creation function.
def main():
    # Determine the base case for the race, subrace, class and speed.
    chosen_race = None
    chosen_subrace = None
    chosen_class = None
    speed = None
    # Create empty list to store traits.  
    trait_list = []
    # Create list with "Common" as only entry as it is common to all races.
    language_lst = ["Common"]
    # Create an empty dictionary to store the saving throws.
    chosen_class_saving_throws = {}

    # Create race objects.
    dwarf = Race("dwarf", {"Constitution": 2, "Wisdom": 1}, dwarf_traits)
    elf = Race("elf", {"Dexterity": 2, "Intelligence": 1}, elf_traits)
    halfling = Race("halfling", {"Dexterity":2}, halfling_traits)
    human = Race("human", {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1}, human_traits)
    dragonborn = Race("Dragonborn", {"Strength": 1, "Charisma": 1}, dragonborn_traits)
    gnome = Race("gnome", {"Intelligence": 2}, gnome_traits)
    half_elf = Race("half-elf", {"Charisma": 2}, half_elf_traits)
    half_orc = Race("half-orc", {"Strength": 2, "Constitution": 1}, half_orc_traits)
    tiefling = Race("tiefling", {"Intelligence": 1, "Charisma": 2}, tiefling_traits)
    
    # Create subrace objects.
    hill_dwarf = Subrace("hill", dwarf, {"Wisdom": 1}, hill_dwarf_traits)
    mountain_dwarf = Subrace("mountain", dwarf, {"Strength": 2}, mountain_dwarf_traits)
    duergar_dwarf = Subrace("duergar", dwarf, {"Constitution": 2}, duergar_traits)
    high_elf = Subrace("high", elf, {"Intelligence": 1}, highelf_traits)
    wood_elf = Subrace("wood", elf, {"Wisdom": 1}, woodelf_traits)
    dark_elf = Subrace("dark", elf, {"Charisma": 1}, darkelf_traits)
    lightfoot_halfling = Subrace("lightfoot", halfling, {"Charisma": 1}, lightfoot_traits)
    stout_halfling = Subrace("stout", halfling, {"Constitution": 1}, stout_traits)
    forest_gnome = Subrace("forest", gnome, {"Dexterity": 1}, forest_traits)
    rock_gnome = Subrace("rock", gnome, {"Constitution": 1}, rock_traits)

    # Create class objects.
    barbarian = Class("barbarian", "d12", barbarian_saving_throws)
    bard = Class("bard","d8", bard_saving_throws)
    cleric = Class("cleric","d8", cleric_saving_throws)
    druid = Class("druid","d8", druid_saving_throws)
    fighter = Class("fighter","d10", fighter_saving_throws)
    monk = Class("monk","d8", monk_saving_throws)
    paladin = Class("paladin","d10", paladin_saving_throws)
    ranger = Class("ranger","d10", ranger_saving_throws)
    rogue = Class("rogue","d8", rogue_saving_throws)
    sorcerer = Class("sorcerer","d6", sorcerer_saving_throws)
    warlock = Class("warlock","d8", warlock_saving_throws)
    wizard = Class("wizard", "d6", wizard_saving_throws)
    
    # Prompt user for race choice.
    # While loop used for error handling.
    print("Start out by choosing your race:")
    for race, description in race_list.items():
        print(f"{i_s}{b_s}{race:<11}{i_e}{b_e} -   {description}")
    print()
    while True:
        race_choice = input("What have you decided on? ").replace(" ", "").lower()
        print()
        if (race_choice == 'dwarf' or 
            race_choice == 'elf' or 
            race_choice == 'halfling' or 
            race_choice == 'human' or 
            race_choice == 'dragonborn' or 
            race_choice == 'gnome' or 
            race_choice == 'half-elf' or 
            race_choice == 'half-orc' or 
            race_choice == 'tiefling'):
            break  
        else:
            print("Please choose from the list provided.")
            print()
    
    # If statement used to create variables related to race and subrace.
    # Dwarf variables.
    if race_choice == "dwarf":
        # Prompt user for subrace choice.
        trait_list.append(dwarf_traits)
        print("There are different subraces of dwarf, which would you like to be?")  
        for sub, description in dwarf_subraces.items():
            print(f"{i_s}{b_s}{sub:<10}{i_e}{b_e} -   {description}")     
        # While loop used for error handling.
        while True:
            subrace_choice = input("What have you decided on? ").replace(" ", "").lower()
            print()
            if (subrace_choice == 'hill' or 
                subrace_choice == 'mountain' or 
                subrace_choice == 'duergar'):
                break  
            else:
                print("Please choose from the list provided.")
                print()
        speed = 25
        language_lst.append("Dwarvish")
        if subrace_choice == "hill":
            chosen_subrace = hill_dwarf
            trait_list.append(hill_dwarf_traits)
        elif subrace_choice == "mountain":
            chosen_subrace = mountain_dwarf
            trait_list.append(mountain_dwarf_traits)
        elif subrace_choice == "duergar":
            chosen_subrace = duergar_dwarf
            trait_list.append(duergar_traits)
        chosen_race = dwarf
    
    # Elf variables.
    elif race_choice == "elf":
        trait_list.append(elf_traits)
        print("There are different subraces of elf, which would you like to be?")  
        for sub, description in elf_subraces.items():
            print(f"{i_s}{b_s}{sub:<10}{i_e}{b_e} -   {description}")
        while True:
            subrace_choice = input("What have you decided on? ").replace(" ", "").lower()
            print()
            if (subrace_choice == 'high' or 
                subrace_choice == 'wood' or 
                subrace_choice == 'dark'):
                break
            else:
                print("Please choose from the list provided.")
                print()
        speed = 30
        language_lst.append("Elvish")
        if subrace_choice == "high":
            chosen_subrace = high_elf
            trait_list.append(highelf_traits)
            while True:
                print("You can choose another language besides Common and Elvish:")
                lang_choice = lang_func()
                if (lang_choice == 'Dwarvish' or 
                    lang_choice == 'Orcish' or
                    lang_choice == 'Draconic' or
                    lang_choice == 'Abyssal' or
                    lang_choice == 'Celestial' or
                    lang_choice == 'Infernal' or
                    lang_choice == 'Sylvan' or
                    lang_choice == 'Giant'):
                    language_lst.append(lang_choice)
                    break  
                elif (lang_choice == 'Common' or
                    lang_choice == 'Elvish'):
                    print("Your character already knows the language you chose.")
                    print()  
                else:
                    print("Please choose from the list provided.")
                    print()        
        elif subrace_choice == "wood":
            chosen_subrace = wood_elf
            trait_list.append(woodelf_traits)
            speed += 5
        elif subrace_choice == "dark":
            chosen_subrace = dark_elf
            trait_list.append(darkelf_traits)
        chosen_race = elf

    # Halfling variables.
    elif race_choice == "halfling":
        trait_list.append(halfling_traits)
        print("There are different subraces of halfling, which would you like to be?")  
        for sub, description in halfling_subraces.items():
            print(f"{i_s}{b_s}{sub:<10}{i_e}{b_e} -   {description}")
        while True:
            sub_choice = input("What have you decided on? ").replace(" ", "").lower()
            print()
            if (subrace_choice == 'lightfoot' or 
                subrace_choice == 'stout'):
                break
            else:
                print("Please choose from the list provided.")
                print()
        speed = 25
        language_lst.append("Halfling")
        if subrace_choice == "lightfoot":
            chosen_subrace = lightfoot_halfling
            trait_list.append(lightfoot_traits)
        elif subrace_choice == "stout":
            chosen_subrace = stout_halfling
            trait_list.append(stout_traits)
        chosen_race = halfling

    # Human variables.
    elif race_choice == "human":
        chosen_race = human
        trait_list.append(human_traits)
        print("You can choose another language besides Common:")
        lang_choice = lang_func()
        while True:
            print("You can choose another language besides Common and Elvish:")
            lang_choice = lang_func()
            if (lang_choice == 'Dwarvish' or 
                lang_choice == 'Elvish' or
                lang_choice == 'Orcish' or
                lang_choice == 'Draconic' or
                lang_choice == 'Abyssal' or
                lang_choice == 'Celestial' or
                lang_choice == 'Infernal' or
                lang_choice == 'Sylvan' or
                lang_choice == 'Giant'):
                language_lst.append(lang_choice)
                break  
            elif (lang_choice == 'Common'):
                print("Your character already knows the language you chose.")
                print()  
            else:
                print("Please choose from the list provided.")
                print()        
        speed = 30

    # Dragonborn variables.
    elif race_choice == "dragonborn":
        chosen_race = dragonborn
        trait_list.append(dragonborn_traits)
        language_lst.append("Draconic")
        speed = 30

    # Gnome variables.
    elif race_choice == "gnome":
        trait_list.append(gnome_traits)
        print("There are different subraces of gnome, which would you like to be?")  
        for sub, description in gnome_subraces.items():
            print(f"{i_s}{b_s}{sub:<10}{i_e}{b_e} -   {description}")     
        while True:
            subrace_choice = input("What have you decided on? ").replace(" ", "").lower()
            print()
            if (subrace_choice == 'forest' or 
                subrace_choice == 'rock'):
                break
            else:
                print("Please choose from the list provided.")
                print()
        speed = 25
        language_lst.append("Gnomish")
        if subrace_choice == "forest":
            chosen_subrace = forest_gnome
            trait_list.append(forest_traits)
            language_lst.append("Speak with Small Beasts")
        elif subrace_choice == "rock":
            chosen_subrace = rock_gnome
            trait_list.append(rock_traits)
        chosen_race = gnome

    # Half-elf variables.
    elif race_choice == "half-elf":
        chosen_race = half_elf
        trait_list.append(half_elf_traits)
        language_lst.append("Elvish")
        while True:
            print("You can choose another language besides Common and Elvish:")
            lang_choice = lang_func()
            if (lang_choice == 'Dwarvish' or
                lang_choice == 'Orcish' or
                lang_choice == 'Draconic' or
                lang_choice == 'Abyssal' or
                lang_choice == 'Celestial' or
                lang_choice == 'Infernal' or
                lang_choice == 'Sylvan' or
                lang_choice == 'Giant'):
                language_lst.append(lang_choice)
                break  
            elif (lang_choice == 'Common' or
                lang_choice == 'Elvish'):
                print("Your character already knows the language you chose.")
                print()  
            else:
                print("Please choose from the list provided.")
                print()        
        speed = 30

    # Half-orc variables.
    elif race_choice == "half-orc":
        chosen_race = half_orc
        trait_list.append(half_orc_traits)
        language_lst.append("Orcish")
        speed = 30

    # Tiefling variables.
    elif race_choice == "tiefling":
        chosen_race = tiefling
        trait_list.append(tiefling_traits)
        language_lst.append("Infernal")
        speed = 30
    
    # Determining the class choice using class_inp() from class_info.py.
    # Also use class specific stats() from stat_calculations.py.
    # Also save the saving throws specific to the class under a common variable for printing.
    class_choice = class_inp()
    # Initialize attribute_scores as an empty dictionary
    attribute_scores = {}
    if class_choice == "barbarian":
        attribute_scores, hit_points = barbarian_stats()
        chosen_class_saving_throws = barbarian_saving_throws
    elif class_choice == "bard":
        attribute_scores, hit_points = bard_stats()
        chosen_class_saving_throws = bard_saving_throws
    elif class_choice == "cleric":
        attribute_scores, hit_points = cleric_stats()
        chosen_class_saving_throws = cleric_saving_throws
    elif class_choice == "druid":
        attribute_scores, hit_points = druid_stats()
        chosen_class_saving_throws = druid_saving_throws
    elif class_choice == "fighter":
        attribute_scores, hit_points = fighter_stats()
        chosen_class_saving_throws = fighter_saving_throws
    elif class_choice == "monk":
        attribute_scores, hit_points = monk_stats()
        chosen_class_saving_throws = monk_saving_throws
    elif class_choice == "paladin":
        attribute_scores, hit_points = paladin_stats()
        chosen_class_saving_throws = paladin_saving_throws
    elif class_choice == "ranger":
        attribute_scores, hit_points = ranger_stats()
        chosen_class_saving_throws = ranger_saving_throws
    elif class_choice == "rogue":
        attribute_scores, hit_points = rogue_stats()
        chosen_class_saving_throws = rogue_saving_throws
    elif class_choice == "sorcerer":
        attribute_scores, hit_points = sorcerer_stats()
        chosen_class_saving_throws = sorcerer_saving_throws
    elif class_choice == "warlock":
        attribute_scores, hit_points = warlock_stats()
        chosen_class_saving_throws = warlock_saving_throws
    elif class_choice == "wizard":
        attribute_scores, hit_points = wizard_stats()
        chosen_class_saving_throws = wizard_saving_throws

    # Determine skills and background choice from class_stats function from class_info.py.
    skills, background_f = class_stats(class_choice)
    
    # Calculate attribute scores with race and class bonuses using class methods.
    chosen_race.calculate_attribute_scores(attribute_scores)
    if chosen_subrace is not None:
        chosen_subrace.calculate_attribute_scores(attribute_scores)
    
    # Capitalize background choice for printing.
    background_f_choice = background_f.capitalize()

    # Depending on the background chosen, you may be able to choose more languages.
    # If statements used to determine if the creator needs to be given the language menu.
    # While look for error handling in each if statement.
    if background_f_choice == "Acolyte":
        print("Based on your background choice you can choose two more languages:")
        for lang, description in languages.items():
            print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
        print()
        while True:
            lang1 = input("First choice: ").capitalize()
            if lang1 not in language_lst:       
                language_lst.append(lang1)
                break
            elif (lang1 != 'Dwarvish' or
                lang1 != 'Orcish' or
                lang1 != 'Draconic' or
                lang1 != 'Abyssal' or
                lang1 != 'Celestial' or
                lang1 != 'Infernal' or
                lang1 != 'Sylvan' or
                lang1 != 'Giant' or
                lang1 != 'Common' or
                lang1 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
        while True:
            lang2 = input("Second choice: ").capitalize()
            if lang2 not in language_lst:       
                language_lst.append(lang2)
                break
            elif (lang2 != 'Dwarvish' or
                lang2 != 'Orcish' or
                lang2 != 'Draconic' or
                lang2 != 'Abyssal' or
                lang2 != 'Celestial' or
                lang2 != 'Infernal' or
                lang2 != 'Sylvan' or
                lang2 != 'Giant' or
                lang2 != 'Common' or
                lang2 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
    elif background_f_choice == "Guild artisan":
        print("Based on your background choice you can choose one more language:")
        for lang, description in languages.items():
            print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
        print()
        while True:
            lang1 = input("Language choice: ").capitalize()
            if lang1 not in language_lst:       
                language_lst.append(lang1)
                break
            elif (lang1 != 'Dwarvish' or
                lang1 != 'Orcish' or
                lang1 != 'Draconic' or
                lang1 != 'Abyssal' or
                lang1 != 'Celestial' or
                lang1 != 'Infernal' or
                lang1 != 'Sylvan' or
                lang1 != 'Giant' or
                lang1 != 'Common' or
                lang1 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
    elif background_f_choice == "Hermit":
        print("Based on your background choice you can choose one more language:")
        for lang, description in languages.items():
            print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
        print()
        while True:
            lang1 = input("Language choice: ").capitalize()
            if lang1 not in language_lst:       
                language_lst.append(lang1)
                break
            elif (lang1 != 'Dwarvish' or
                lang1 != 'Orcish' or
                lang1 != 'Draconic' or
                lang1 != 'Abyssal' or
                lang1 != 'Celestial' or
                lang1 != 'Infernal' or
                lang1 != 'Sylvan' or
                lang1 != 'Giant' or
                lang1 != 'Common' or
                lang1 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
    elif background_f_choice == "Noble":
        print("Based on your background choice you can choose one more language:")
        for lang, description in languages.items():
            print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
        print()
        while True:
            lang1 = input("Language choice: ").capitalize()
            if lang1 not in language_lst:       
                language_lst.append(lang1)
                break
            elif (lang1 != 'Dwarvish' or
                lang1 != 'Orcish' or
                lang1 != 'Draconic' or
                lang1 != 'Abyssal' or
                lang1 != 'Celestial' or
                lang1 != 'Infernal' or
                lang1 != 'Sylvan' or
                lang1 != 'Giant' or
                lang1 != 'Common' or
                lang1 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
    elif background_f_choice == "Outlander":
        print("Based on your background choice you can choose one more language:")
        for lang, description in languages.items():
            print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
        print()
        while True:
            lang1 = input("Language choice: ").capitalize()
            if lang1 not in language_lst:       
                language_lst.append(lang1)
                break
            elif (lang1 != 'Dwarvish' or
                lang1 != 'Orcish' or
                lang1 != 'Draconic' or
                lang1 != 'Abyssal' or
                lang1 != 'Celestial' or
                lang1 != 'Infernal' or
                lang1 != 'Sylvan' or
                lang1 != 'Giant' or
                lang1 != 'Common' or
                lang1 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
    elif background_f_choice == "Sage":
        print("Based on your background choice you can choose two more languages:")
        for lang, description in languages.items():
            print(f"{i_s}{b_s}{lang:<11}{i_e}{b_e} -   {description}")
        print()
        while True:
            lang1 = input("First choice: ").capitalize()
            if lang1 not in language_lst:       
                language_lst.append(lang1)
                break
            elif (lang1 != 'Dwarvish' or
                lang1 != 'Orcish' or
                lang1 != 'Draconic' or
                lang1 != 'Abyssal' or
                lang1 != 'Celestial' or
                lang1 != 'Infernal' or
                lang1 != 'Sylvan' or
                lang1 != 'Giant' or
                lang1 != 'Common' or
                lang1 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
        while True:
            lang2 = input("Second choice: ").capitalize()
            if lang2 not in language_lst:       
                language_lst.append(lang2)
                break
            elif (lang2 != 'Dwarvish' or
                lang2 != 'Orcish' or
                lang2 != 'Draconic' or
                lang2 != 'Abyssal' or
                lang2 != 'Celestial' or
                lang2 != 'Infernal' or
                lang2 != 'Sylvan' or
                lang2 != 'Giant' or
                lang2 != 'Common' or
                lang2 != 'Elvish'):
                print("Please choose a language from the list..")
                print()
            else:
                print("Your character already knows that language.")
                print()
  
    # Calculate ability score modifiers using calculate_modifier function.
    modifiers = {}
    for ability, score in attribute_scores.items():
        modifiers[ability] = calculate_modifier(score)

    # Prompt user for player name.    
    player_name = input("Who will be using this character? ").capitalize()

    # Prompt user for character name.
    char_name = input("What is the characters name? ").capitalize()
    
    # Write data to a custom made PDF.
    # Open the existing PDF file.
    existing_pdf = "char_blank.pdf"
    output_pdf = "character_sheet.pdf"
    temp_pdf = "temp.pdf"

    # Register your own TTF font.
    font_path = "Simpsonfont.ttf"
    pdfmetrics.registerFont(TTFont('customFont', font_path))

    # Set the font and font size for the PDF content.
    pdf_canvas = canvas.Canvas(temp_pdf, pagesize=letter)
    # Write font size 20 information.
    pdf_canvas.setFont("customFont", 20)
    pdf_canvas.drawString(175 , 795, f"{player_name}")
    pdf_canvas.drawString(210 , 755, f"{char_name}")
    pdf_canvas.drawString(100 , 715, f"{class_choice}")
    pdf_canvas.drawString(375 , 795, f"{chosen_race}")
    pdf_canvas.drawString(410 , 755, f"{chosen_subrace}")
    pdf_canvas.drawString(450 , 715, f"{background_f_choice}")
    pdf_canvas.drawString(250 , 570, f"{hit_points}")
    pdf_canvas.drawString(245 , 500, f"{speed} ft")

    # Write font size 15 information.
    pdf_canvas.setFont("customFont", 13)
    skill_y = 615                                                               # Vertical position for the first item
    for skill, prof in skills.items():
        pdf_canvas.drawString(402, skill_y, f"{prof}")
        skill_y -= 20                                                           # Move to the next line
    attr_y = 619                                                               
    for ability, score in attribute_scores.items():
        pdf_canvas.drawString(43, attr_y, f"{score}")
        attr_y -= 31                                                            
    lang_y = 190
    for language in language_lst:
        pdf_canvas.drawString(30, lang_y, f"- {language}")
        lang_y -=20
    trait_y = 190
    for sublist in trait_list:
        for trait in sublist:
            pdf_canvas.drawString(370, trait_y, f"- {trait}")
            trait_y -= 20  

    # Write font size 10 information
    pdf_canvas.setFont("customFont", 10)
    mod_y = 622
    for ability, score in attribute_scores.items():
        modifier = modifiers[ability]
        pdf_canvas.drawString(126, mod_y, f"{modifier}")
        mod_y -= 30 

    saving_y = 380
    for saving, prof in chosen_class_saving_throws.items():
        pdf_canvas.drawString(56, saving_y, f"{prof}")
        saving_y -= 18  

   # Save the modifications to the temporary PDF file
    pdf_canvas.save()

    # Repair and write to PDF.
    existing_pdf_reader = PyPDF4.PdfFileReader(open(existing_pdf, "rb"))
    existing_page = existing_pdf_reader.getPage(0)
    modified_pdf_reader = PyPDF4.PdfFileReader(open(temp_pdf, "rb"))
    modified_page = modified_pdf_reader.getPage(0)
    existing_page.mergePage(modified_page)
    output_pdf_writer = PyPDF4.PdfFileWriter()
    output_pdf_writer.addPage(existing_page)
    # Save the merged PDF file
    with open(output_pdf, "wb") as output_file:
        output_pdf_writer.write(output_file)


if __name__ == "__main__":
    main()