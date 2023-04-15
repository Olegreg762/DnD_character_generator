import streamlit as st
import random

st.header('Welcome to my D&D character creater')

char_name = st.text_input('Enter your Name')

st.write('Your character name is ',char_name)

def roll_ability_scores():
        rolls = [[random.randint(1, 6) for i in range(4)] for i in range(6)]
        return [sum(sorted(r)[1:]) for r in rolls] 



if 'ability_rolls' not in st.session_state:
        st.session_state['ability_rolls'] = roll_ability_scores()


#if 'ability_rolls' not in st.session_state:
#    st.session_state.key = roll_ability_scores()

ability_rolls = st.session_state['ability_rolls'] = st.session_state['ability_rolls']

ability_col, class_col, ability_assign_col = st.columns(3)

with ability_col:
               
        st.write(ability_rolls)

with class_col:
        class_choices = (
            'Artificer', 'Barbarian', 'Bard', 
            'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 
            'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'
            )
        class_choice_box = st.selectbox('Choose a Class', class_choices)
        class_choice = class_choice_box.upper()
        
        st.write(class_choice)

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


        subclass_choice_box = st.selectbox('Choose Subclass', subclass_list[class_choice])

        subclass_choice = subclass_choice_box

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
        

        st.write(subclass_prefix[class_choice],subclass_choice)


with ability_assign_col:
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


        st.write('strength', abilities['strength'])
        st.write('dexterity', abilities['dexterity'])
        st.write('constitution', abilities['constitution'])
        st.write('intelligence', abilities['intelligence'])
        st.write('wisdom', abilities['wisdom'])
        st.write('charisma', abilities['charisma'])

