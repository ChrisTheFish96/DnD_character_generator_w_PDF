# Character Generator for Dungeons & Dragons

## Description
A program that walks through the steps of the players handbook to create a character.
Provides short description of each attribute you can choose from.
Creates a first level character.
Does not add Armor, Armor Class, Treasure or Equipment as that is often things the DM might want to control.
The created PDF does however provide space for these things.

## Table of Contents
1. Installation
1. Usage
1. Credits

## Installation
The code can be copied into any code editor.
Comments are available in the code to explain what each section does.

The only imports needed is PyPDF4 and Random.

The pdf char_blank.pdf also need to be present in the same directory a she main code.py file.

## Usage
To showcase the use case of the applictaion I will create a High Elf Sage character. 

When you run the application, you will be presented with a Race menu:

![Race](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/f4ccbc54-be20-4e9e-b6ce-cc0bc474aef7)

If there are subrace options for the race the user will be presented with the subrace menu:

![subrace](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/575124aa-0826-47fd-b770-df9619dfd729)

Subrace options are available for the Dwarf, Elf, Halfling and Gnome races.

If the subrace allows the user to choose another language, the language menu will be provided:

![language1](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/1ef13ee3-dc47-4716-9ff8-24ea4f23221d)

The user will then be prompted to choose a class:

![class](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/801a7537-5ebf-4ed4-be79-7dd1093398e4)

Depending on the choice of class, more options might be asked to place the randomly generated stats in the correct attribute box.

![ranger choice](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/ba7f8f91-4eaf-4aa3-ab6e-870735bcc624)

This is true for Ranger as shown here as well as Fighter

The user is then prompted to choose a background:

![background](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/495fac34-7300-4a21-9a4f-f895c415a2fc)

Based on the class that the user chose, they will then be able to choose a certain amount of skills from a list determined by their chosen background:

![skills](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/990a63f3-710f-4d07-9d0f-5fc04c0e5bf3)

Based on the background choice, the user might be able to choose more languages:

![language2](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/6da96cf6-0329-4bf0-922d-256e825f28cf)

The last things needed from the user is to provide their names as well as a name for their character:

![names](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/5d130144-435d-404b-bbaf-5d9b10d7b1b2)

Two PDFs will then be generated, temp which contains the information that is mapped to the correct places on the blank form, (char_blank.pdf) as well as character_sheet.pdf, which is the filled in pdf.

The names, background choice, class choice and race choices will be printed in the top bar:

![main block](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/22128c0a-1266-457b-a591-002e21914fe7)

The attribute scores as well as the calculated modifiers will be printed from the lists generated in an easy to read format:

![attr and mods](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/f6695d75-013d-469d-bc9c-7a8e189c1ad6)

Hit points and speed will be calculated and printed out based on class and race choices.

![mid stats](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/bff77e09-844f-4cce-9d81-d7231a494a31)

Saving throw proficiencies and skill proficiencies, based on class and background choices are also printed from a list:

![sav throw](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/2b0df247-a604-4062-b3c6-2e3659f51fb9)

![skills_print](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/4b182491-7fe0-4254-9bda-a6c6ffa1c1d8)

An appended trait list combinging race and subrace traits are printed from a list, and languages are also printed from a list leaving enough space for filling out other equipment chosen later.

![traits](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/e1bb0557-fc77-40fe-a91d-b5c4f909ed3d)
![langs](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/079555c4-87a5-4bc0-973a-3a33d0c25e69)

## Credits
This project was created by Christopher Barnard (ChrisTheFish96)

