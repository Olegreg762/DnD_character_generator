import random
import streamlit as st


def set_name():
    char_name_input = input('What is your name?')
    return char_name_input


def roll_ability_scores():
    rolls = [[random.randint(1, 6) for i in range(4)] for i in range(6)]
    return [sum(sorted(r)[1:]) for r in rolls]



def class_set():
    class_choices = (
        'Artificer', 'Barbarian', 'Bard', 
        'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 
        'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'
        )
    class_pick = ('Choose a Class', class_choices)
    while class_pick not in (choice.casefold() for choice in class_choices):
        class_pick = input(f'Choose a Class {class_choices}').casefold()
    return class_pick.upper()



subclass_list = {
        'ARTIFICER': (
                    'Alchemist', 'Artillerist', 'Battle Smith', 'Armorer'
                    ),
        'BARBARIAN': (
                    'Berserker', 'Totem Warrior', 'Ancestral Guardian', 'Storm Herald', 
                    'Zealot', 'Beast', 'Wild Magic'
                    ),
        'BARD': (
                'Lore', 'Valor', 'Glamour', 'Swords', 'Whispers', 'Eloquence', 'Creation'
                ),
        'CLERIC': (
                'Knowledge', 'Life', 'light', 'Nature', 'Tempest', 'Trickery', 'War', 
                'Death', 'Arcana', 'Solidarity', 'Strength', 'Ambition', 'Zeal', 'Forge', 
                'Grave', 'Order', 'Peace', 'Twilight'
                ),
        'DRUID': (
                'Land', 'Moon', 'Dreams', 'Shepherd', 'Spores', 'Stars', 'Wildfire'
                ),

        'FIGHTER': (
                    'Champion', 'Battle Master', 'Eldritch Knight', 'Arcane Archer', 
                    'Cavalier', 'Samurai', 'Echo Knight', 'Psi Warrior', 'Rune Knight'
                    ),
        'MONK': (
                'Open Hand', 'Four Elements', 'Long Death', 'Sun Soul', 'Drunker Master', 
                'Kensei', 'Mercy', 'Astral Self'
                ),
        'PALADIN': (
                    'Devotion', 'Ancients', 'Vengeance', 'Oathbreaker', 'the Crown', 'Conquest', 
                    'Redemption', 'Glory', 'The Watchers'
                    ),
        'RANGER': (
                    'Hunter', 'Beast Master', 'Gloom Stalker', 'Horizon Walker', 'Monster Slayer', 
                    'Fey Wanderer', 'Swarmkeeper'
                    ),
        'ROGUE': (
                'Thief', 'Assassin', 'Arcane Trickster', 'Mastermind', 'Swashbuckler', 'Inquisitive', 
                'Scout', 'Phantom', 'Soulknife'
                ),
        'SORCERER': (
                    'Draconic Bloodline', 'Wild Magic', 'Storm Sorcery', 'Pyromancer', 'Divine Soul', 
                    'Shadow Magic', 'Aberrant Mind', 'Clockwork Soul'
                    ),
        'WARLOCK': (
                    'Archfey', 'Fiend', 'Great Old One', 'Undying', 'Celestial', 'Hexblade', 
                    'Fathomless', 'Genie'
                    ),
        'WIZARD': (
                'Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 
                'Necromancy', 'Transmutation', 'Bladesinging', 'War Magic', 'Chronurgy Magic', 
                'Graviturgy Magic', 'Order of Scribes'
                )
        }

def set_subclass(class_choice):
    subclass_list = {
        'ARTIFICER': (
                    'Alchemist', 'Artillerist', 'Battle Smith', 'Armorer'
                    ),
        'BARBARIAN': (
                    'Berserker', 'Totem Warrior', 'Ancestral Guardian', 'Storm Herald', 
                    'Zealot', 'Beast', 'Wild Magic'
                    ),
        'BARD': (
                'Lore', 'Valor', 'Glamour', 'Swords', 'Whispers', 'Eloquence', 'Creation'
                ),
        'CLERIC': (
                'Knowledge', 'Life', 'light', 'Nature', 'Tempest', 'Trickery', 'War', 
                'Death', 'Arcana', 'Solidarity', 'Strength', 'Ambition', 'Zeal', 'Forge', 
                'Grave', 'Order', 'Peace', 'Twilight'
                ),
        'DRUID': (
                'Land', 'Moon', 'Dreams', 'Shepherd', 'Spores', 'Stars', 'Wildfire'
                ),

        'FIGHTER': (
                    'Champion', 'Battle Master', 'Eldritch Knight', 'Arcane Archer', 
                    'Cavalier', 'Samurai', 'Echo Knight', 'Psi Warrior', 'Rune Knight'
                    ),
        'MONK': (
                'Open Hand', 'Four Elements', 'Long Death', 'Sun Soul', 'Drunker Master', 
                'Kensei', 'Mercy', 'Astral Self'
                ),
        'PALADIN': (
                    'Devotion', 'Ancients', 'Vengeance', 'Oathbreaker', 'the Crown', 'Conquest', 
                    'Redemption', 'Glory', 'The Watchers'
                    ),
        'RANGER': (
                    'Hunter', 'Beast Master', 'Gloom Stalker', 'Horizon Walker', 'Monster Slayer', 
                    'Fey Wanderer', 'Swarmkeeper'
                    ),
        'ROGUE': (
                'Thief', 'Assassin', 'Arcane Trickster', 'Mastermind', 'Swashbuckler', 'Inquisitive', 
                'Scout', 'Phantom', 'Soulknife'
                ),
        'SORCERER': (
                    'Draconic Bloodline', 'Wild Magic', 'Storm Sorcery', 'Pyromancer', 'Divine Soul', 
                    'Shadow Magic', 'Aberrant Mind', 'Clockwork Soul'
                    ),
        'WARLOCK': (
                    'Archfey', 'Fiend', 'Great Old One', 'Undying', 'Celestial', 'Hexblade', 
                    'Fathomless', 'Genie'
                    ),
        'WIZARD': (
                'Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 
                'Necromancy', 'Transmutation', 'Bladesinging', 'War Magic', 'Chronurgy Magic', 
                'Graviturgy Magic', 'Order of Scribes'
                )
        }

    subclass_prefix =  {
        'ARTIFICER': (''),
        'BARBARIAN': ('Path of '),
        'BARD': ('College of '),
        'CLERIC': ('Domain of '),
        'DRUID': ('Circle of '),
        'FIGHTER': (''),
        'MONK': ('Way of '),
        'PALADIN': ('Oath of '),
        'RANGER': (''),
        'ROGUE': (''),
        'SORCERER': (''),
        'WARLOCK': ('The '),
        'WIZARD': ('School of ')
        }
      
    subclass_pick = input(f'Choose a subclass {sorted(subclass_list[class_choice])}').casefold()
    while subclass_pick not in (choice.casefold() for choice in subclass_list[class_choice]):
        subclass_pick = input(f'Choose a subclass {sorted(subclass_list[class_choice])}').casefold()
    return subclass_prefix[class_choice].upper() + '' + subclass_pick.upper()


def set_ability_scores(class_choice,ability_rolls):
    ability_positions = {            
        'ARTIFICER': [5, 1, 3, 0, 2, 4],

        'BARBARIAN': [0, 2, 1, 5, 4, 3],

        'BARD': [4 , 1, 2, 3, 5, 0],

        'CLERIC': [3, 2, 1, 5, 0, 4],

        'DRUID': [4, 1, 2, 5, 0, 3],

        'FIGHTER': [1, 0, 2, 5, 4, 3],

        'MONK': [4, 0, 1, 5, 2, 3],

        'PALADIN': [3, 0, 1, 5, 4, 2],

        'RANGER': [3, 0, 1, 5, 2, 4],
        
        'ROGUE': [3, 0, 1, 2, 5, 4],
        
        'SORCERER': [5, 1, 2, 3, 4, 0],

        'WARLOCK': [5, 1, 2, 3, 4, 0],

        'WIZARD': [5, 1, 2, 0, 3, 4]
    }
    ability_names = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    ability_values = [ability_rolls[i] for i in ability_positions[class_choice]]
    abilities = dict(zip(ability_names, ability_values))

    for i in range(3):

        ability_choice = input(f'Choose an ability score you want to increase {ability_names}): ')
        while ability_choice.lower() not in ability_names:
            ability_choice = input(f'Invalid input. Choose an ability score you want to increase {ability_names}): ')

        abilities[ability_choice.lower()] += 1

    return abilities


def set_race():
    race_choices = (
        'Aarakocra', 'Aasimar', 'Air Genasi', 'Bugbear', 'Centaur', 
        'Changeling', 'Deep Gnome', 'Dragonborn', 'Drow', 'Duergar', 'Dwarf',
        'Earth Genasi', 'Eladrin', 'Fairy', 'Firbolg', 'Fire Genasi', 'Forest Gnome', 
        'Githyanki', 'Githzerai', 'Goblin', 'Goliath', 'Half-Elf', 'Half-Orc', 'Halfing', 
        'Harengon', 'High Elf', 'Hobogoblin', 'Human', 'Kenku', 'Kobold', 'Lizardfolk', 
        'Minotaur', 'Orc', 'Rock Gnome', 'Satyr', 'Sea Elf', 'Shifter', 'Tabaxi', 'Tiefling', 
        'Tortle', 'Triton', 'Water Genasi', 'Wood Elf', 'Yuan-Ti'
 )
    race_pick = input(f'Choose a Class {sorted(race_choices)}').casefold()
    while race_pick not in (choice.casefold() for choice in race_choices):
        race_pick = input(f'Choose a Class {race_choices}').casefold()
    return race_pick.upper()