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

## Usage
To showcase the use case of the applictaion I will create a High Elf Sage character. 

When you run the application, you will be presented with a Race menu
![Race](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/f4ccbc54-be20-4e9e-b6ce-cc0bc474aef7)

If there are subrace options for the race the user will be presented with the subrace menu.
![subrace](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/575124aa-0826-47fd-b770-df9619dfd729)
Subrace options are available for the Dwarf, Elf, Halfling and Gnome races.

If the subrace allows the user to choose another language, the language menu will be provided.
![language1](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/1ef13ee3-dc47-4716-9ff8-24ea4f23221d)

The user will then be prompted to choose a class.
![class](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/801a7537-5ebf-4ed4-be79-7dd1093398e4)
Depending on the choice of class, more options might be asked to place the randomly generated stats in the correct attribute box.

![ranger choice](https://github.com/ChrisTheFish96/DnD_character_generator_w_PDF/assets/125367266/ba7f8f91-4eaf-4aa3-ab6e-870735bcc624)

This is true for Ranger as shown here as well as Fighter

## Credits
This project was created by Christopher Barnard (ChrisTheFish96)
