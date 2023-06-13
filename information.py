race_list = {
    'Dwarf': 'Resilient and skilled craftsmen known for their endurance and ability to withstand poisons and diseases.',
    'Elf': 'Graceful and long-lived beings with a deep connection to nature and a penchant for magic.',
    'Halfling': 'Small and nimble individuals with a lucky streak and a talent for avoiding danger.',
    'Human': 'Versatile and adaptable individuals with no innate racial abilities but capable of excelling in any class or profession.',
    'Dragonborn': 'Draconic humanoids with breath weapons and scales reminiscent of different dragon types.',
    'Gnome': 'Curious and inventive tricksters with a natural affinity for illusions and an affinity for tinkering.',
    'Half-Elf': 'Born of human and elven parentage, they combine the best qualities of both races, being adaptable, charismatic, and versatile.',
    'Half-Orc': 'Strong and imposing hybrids of human and orc descent, known for their physical prowess and endurance.',
    'Tiefling': 'Descendants of fiendish creatures, Tieflings possess demonic or devilish traits and are often skilled in dark magic.',
    }

class_list = {
    'Barbarian': 'Fierce warriors who tap into their primal instincts, gaining extraordinary strength, durability, and the ability to fly into a rage.',
    'Bard': 'Versatile performers and spellcasters who use their musical talents to inspire allies, cast spells, and manipulate emotions.',
    'Cleric': 'Devout agents of deities, blessed with divine magic, and skilled in healing, protection, and channeling the power of their gods.',
    'Druid': 'Guardians of nature, with the ability to shapeshift into animals, command elemental forces, and possess a deep connection to the natural world.',
    'Fighter': 'Masters of martial combat, proficient in a wide array of weapons and armor, and skilled in both offense and defense.',
    'Monk': 'Disciplined warriors who harness their inner energy, enabling them to perform extraordinary physical feats and wield unarmed strikes with deadly precision.',
    'Paladin': 'Holy knights, devoted to righteousness and justice, wielding divine magic to smite enemies, heal allies, and protect the weak.',
    'Ranger': 'Skilled hunters and trackers, adept at surviving in the wilderness, wielding a combination of martial prowess and nature-based magic.',
    'Rogue': 'Sneaky and agile individuals, specializing in stealth, deception, and precision strikes, often skilled in disarming traps and picking locks.',
    'Sorcerer': 'Innately magical individuals with a natural gift for spellcasting, drawing power from their bloodline or inherent connection to arcane forces.',
    'Warlock': 'Pact-bound spellcasters who form supernatural pacts with powerful beings, gaining access to eldritch magic and unique abilities.',
    'Wizard': 'Scholars of arcane knowledge who wield extensive spellcasting abilities, specializing in the study and manipulation of magic.',
    }

dwarf_subraces = {
    'Hill': 'Hill dwarves are known for their endurance and are even hardier than other dwarves. They have a deep connection to the land and are skilled in the arts of healing.',
    'Mountain': 'Mountain dwarves are strong and tough. They excel in combat and are skilled in working with various weapons and armor.',
    'Duergar': 'Duergar, or gray dwarves, are a subterranean subrace of dwarves. They have a natural affinity for darkness, can become invisible in certain conditions, and possess innate psionic abilities.',
}

dragonborn_colours = {
    'Black': 'Acid-based breath weapons.',
    'Blue': 'Lightning-based breath weapons.',
    'Brass': 'Fire-based breath weapons.',
    'Bronze': 'Lightning-based breath weapons.',
    'Copper': 'Acid-based breath weapons.',
    'Gold': 'Fire-based breath weapons.',
    'Green': 'Poison-based breath weapons.',
    'Red': 'Fire-based breath weapons.',
    'Silver': 'Cold-based breath weapons.',
    'White': 'Cold-based breath weapons.',
}


elf_subraces = {
    'High': 'Noble and magical elves with a keen intellect and proficiency in magic.',
    'Wood': 'Spirited and agile elves with a deep connection to nature and superior speed.',
    'Dark': '(Drow) Mysterious and cunning elves who dwell in the depths of the Underdark and excel in stealth and magic.',
}

halfling_subraces = {
    'Lightfoot': 'Friendly and social halflings known for their luck, stealth, and ability to blend in with other races.',
    'Stout': 'Sturdy and resilient halflings with a natural resistance to poison and a knack for enduring physical hardships.',
}

gnome_subraces = {
    'Forest': 'Gnomes with a deep affinity for nature and illusion magic, known for their stealth and ability to communicate with small animals.',
    'Rock': 'Gnomes with a talent for invention and engineering, known for their tinkering skills and ability to create small mechanical devices.',
}

tiefling_heritages = {
    'Asmodeus': 'Known for their affinity for manipulation and charm.',
    'Baalzebul': 'Known for their cunning and affinity for magic.',
    'Dispater': 'Known for their stealth and manipulative nature.',
    'Fierna': 'Known for their seductive charm and affinity for fire magic.',
    'Glasya': 'Known for their cunning and ability to manipulate shadows.',
    'Levistus': 'Known for their resilience and affinity for ice magic.',
    'Mammon': 'Known for their greed and affinity for wealth and treasure.',
    'Mephistopheles': 'Known for their cunning and affinity for fire magic.',
    'Zariel': 'Known for their martial prowess and affinity for weapons and combat.',
}

backgrounds = {
    'Acolyte': 'You have spent your life in the service of a temple, learning religious rituals and traditions.',
    'Charlatan': 'You are a skilled deceiver, tricking others with your artful lies and disguises.',
    'Criminal': 'You have a history of breaking the law, working in underground networks and illicit activities.',
    'Entertainer': 'You are a performer, captivating audiences with your artistic talents and showmanship.',
    'Folk Hero': 'You are a commoner who rose up to become a local hero, fighting for justice and protecting the people.',
    'Guild Artisan': 'You are a skilled craftsman or artisan, belonging to a guild and practicing a specific trade.',
    'Hermit': 'You have chosen a life of seclusion and solitude, seeking knowledge or enlightenment in isolation.',
    'Noble': 'You were born into a noble family, enjoying a life of privilege and influence.',
    'Outlander': 'You come from a distant land, living off the land and having a deep connection with nature.',
    'Sage': 'You are a scholar and researcher, possessing vast knowledge and expertise in various academic fields.',
    'Sailor': 'You have a background in sailing and maritime activities, navigating the seas and exploring new horizons.',
    'Soldier': 'You have served in an organized military force, honing your combat skills and discipline.',
    'Urchin': 'You grew up in the streets, surviving through your wit and resourcefulness in urban environments.',
}

skills = {
    "Acrobatics": "O",
    "Animal handling": "O",
    "Arcana": "O",
    "Athletics": "O",
    "Deception": "O",
    "History": "O",
    "Insight": "O",
    "Intimidation": "O",
    "Investigation": "O",
    "Medicine": "O",
    "Nature": "O",
    "Perception": "O",
    "Performance": "O",
    "Persuasion": "O",
    "Religion": "O",
    "Sleight of hand": "O",
    "Stealth": "O",
    "Survival": "O"
}

dwarf_traits = [
    "Dwarven Resilience",
    "Stonecunning",
    "Tool Proficiency",
    "Dwarven Combat Training",
    "Darkvision"
]
background_skills = {
    'acolyte': ["Insight", "Religion"],
    'charlatan': ["Deception", "Sleight of Hand"],
    'criminal': ["Deception", "Stealth"],
    'entertainer': ["Acrobatics", "Performance"],
    'folk hero': ["Animal handling", "Survival"],
    'guild artisan': ["Insight", "Persuasion"],
    'hermit': ["Medicine", "Religion"],
    'noble': ["History", "Persuasion"],
    'outlander': ["Athletics", "Survival"],
    'sage': ["Arcana", "History"],
    'sailor': ["Athletics", "Perception"],
    'soldier': ["Athletics", "Intimidation"],
    'urchin': ["Sleight of hand", "Stealth"],
}
class_skills = {
    "barbarian": ["Animal handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    "bard": ["Acrobatics", "Animal handling", "Arcana", "Athletics", "Deception", "History", "Insight",
             "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion",
             "Religion", "Sleight of hand", "Stealth", "Survival"],
    "cleric": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
    "druid": ["Arcana", "Animal handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
    "fighter": ["Acrobatics", "Animal handling", "Athletics", "History", "Insight", "Intimidation", "Perception",
                "Survival"],
    "monk": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
    "paladin": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
    "ranger": ["Animal handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth",
               "Survival"],
    "rogue": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception",
              "Performance", "Persuasion", "Sleight of hand", "Stealth"],
    "sorcerer": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
    "warlock": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    "wizard": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
}

languages = {
    "Common": "The most widely spoken language in most D&D campaign settings.",
    "Elvish": "A family of languages spoken by various elven races.",
    "Dwarvish": "The language spoken by dwarves, known for its robust sound.",
    "Orcish": "The language spoken by orcs, known for its harsh sounds and aggression.",
    "Draconic": "The language of dragons and dragon-like creatures, with a mystique and power.",
    "Abyssal": "The language spoken by creatures associated with the chaotic evil Abyss.",
    "Celestial": "The language of celestial beings, often considered a language of goodness and purity.",
    "Infernal": "The language spoken by creatures associated with the lawful evil Nine Hells.",
    "Sylvan": "The language of fey creatures, closely tied to nature and with a melodic quality.",
    "Giant": "The language spoken by giantkin races, with deep, rumbling tones."
}

barbarian_saving_throws = {
    "Strength":"X",
    "Dexterity":"O",
    "Intelligence":"O",
    "Wisdom":"O",
    "Charisma":"O",
    "Constitution":"X",
}
bard_saving_throws = {
    "Strength":"O",
    "Dexterity":"X",
    "Intelligence":"O",
    "Wisdom":"O",
    "Charisma":"X",
    "Constitution":"O",
}

cleric_saving_throws = {
    "Strength":"O",
    "Dexterity":"O",
    "Intelligence":"O",
    "Wisdom":"X",
    "Charisma":"X",
    "Constitution":"O",
}
druid_saving_throws = {
    "Strength":"O",
    "Dexterity":"O",
    "Intelligence":"X",
    "Wisdom":"X",
    "Charisma":"O",
    "Constitution":"O",
}
fighter_saving_throws = {
    "Strength":"X",
    "Dexterity":"O",
    "Intelligence":"O",
    "Wisdom":"O",
    "Charisma":"O",
    "Constitution":"X",
}
monk_saving_throws = {
    "Strength":"X",
    "Dexterity":"X",
    "Intelligence":"O",
    "Wisdom":"O",
    "Charisma":"O",
    "Constitution":"O",
}
paladin_saving_throws = {
    "Strength":"O",
    "Dexterity":"O",
    "Intelligence":"O",
    "Wisdom":"X",
    "Charisma":"X",
    "Constitution":"O",
}
ranger_saving_throws = {
    "Strength":"X",
    "Dexterity":"X",
    "Intelligence":"O",
    "Wisdom":"O",
    "Charisma":"O",
    "Constitution":"O",
}
rogue_saving_throws = {
    "Strength":"O",
    "Dexterity":"X",
    "Intelligence":"X",
    "Wisdom":"O",
    "Charisma":"O",
    "Constitution":"O",
}
sorcerer_saving_throws = {
    "Strength":"O",
    "Dexterity":"O",
    "Intelligence":"O",
    "Wisdom":"O",
    "Charisma":"X",
    "Constitution":"X",
}
warlock_saving_throws = {
    "Strength":"O",
    "Dexterity":"O",
    "Intelligence":"O",
    "Wisdom":"X",
    "Charisma":"X",
    "Constitution":"O",
}
wizard_saving_throws = {
    "Strength":"O",
    "Dexterity":"O",
    "Intelligence":"X",
    "Wisdom":"X",
    "Charisma":"O",
    "Constitution":"O",
}

dwarf_traits = [
    "Darkvision",
    "Dwarven Resilience",
    "Dwarven Combat Training",
    "Tool Proficiency",
    "Stonecunning",
]

mountain_dwarf_traits = [
    "Dwarven armor training"
]
hill_dwarf_traits = [
    "Dwarven toughness"
]
duergar_traits = [
    "Cantrip"
]
human_traits = [
    "Feat of your choice",
    "Skill of you choice"
]

elf_traits = [
    "Fey Ancestry",
    "Keen Senses",
    "Trance",
    "Darkvision"
]
highelf_traits = [
    "Elf weapon training",
    "Cantrip",
    "Extra language"
]
woodelf_traits = [
    "Elf weapon training",
    "Fleet of foot",
    "Mask of the wild"
]
darkelf_traits = [
    "Superior Darkvision",
    "Sunlight sensitivity",
    "Drow magic",
    "Drow weapon training"
]

halfling_traits = [
    "Lucky",
    "Brave",
    "Halfling Nimbleness"
]
lightfoot_traits = [
    "Naturally Stealthy",
]
stout_traits = [
    "Stout Resilience",
]

dragonborn_traits = [
    "Draconic Ancestry",
    "Breath Weapon",
    "Damage Resistance",
]

gnome_traits = [
    "Gnome Cunning",
    "Darkvision",
]

forest_traits = [
    "Natural Illusionist",
    "Speak with Small Beasts",
]

rock_traits = [
    "Artificer's Lore",
    "Tinker",
    "Tinker Device"
]

half_elf_traits = [
    "Darkvision",
    "Fey Ancestry",
    "Skill Versatility"
]

half_orc_traits = [
    "Darkvision",
    "Menacing",
    "Relentless Endurance",
    "Savage Attacks",
]

tiefling_traits = [
    "Darkvision",
    "Hellish Resistance",
    "Infernal Legacy"
]
