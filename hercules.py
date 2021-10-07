import random

Hercules = {
    'Level': 1,
    'Name': 'Hercules',
    'Health': 100,
    'Attack_Power': 5,
    'Attacks': ['punch', 'stab', 'slice'],
    'Dodge': 3
}
Lion = {
    'Name': 'The Nemean Lion',
    'Health': 100,
    'Attack_Power': 5,
    'Attacks': ['bite', 'claw', 'pounce'],
    'Dodge': 5
}
Hydra = {
    'Name': 'The Nine Headed Lernaean Hydra',
    'Health': 250,
    'Attack_Power': 10,
    'Attacks': ['bite', 'claw', 'multi attack'],
    'Dodge': 10
}
Cerberus = {
    'Name': 'Cerberus',
    'Health': 350,
    'Attack_Power': 15,
    'Attacks': ['Bite', 'Swipe', 'Chew'],
    'Dodge': 10
}




def tell_story():
    print()
    print()
    print()
    print('|               💪 You are Hercules, the greatest of the Greek Heroes! 💪                 |')
    print('|        You have been tasked by King Eurystheus to slay the vicious Nemean Lion, 🦁      |')
    print('|         Defeat the impossible nine-headed Lernaean Hydra, 🐍🐍🐍🐍🐍🐍🐍🐍🐍            |')
    print('|             and Capture the guard dog of the underworld—Cerberus!! 🐺                   |')
    print()
    print()
    print()

def tell_end():
    print()
    print()
    print('| After a long and hard fought jouney you finally  |')
    print('| accomplished the mission you set out to do. King |')
    print('| Eurystheus is satisfied with your work, and has  |')
    print('|   named you the Dopest Demi God of all time.     |')    
    print()
    print()


def travel():
    print('Where would you like to go? Toward the Lions Cave to the East? Toward the Hydras Lair to the West? Or the Entrance of the Underworld?')
    print()
    user_input = input('Select East, West, or Underworld: ').lower()
    if user_input == 'east':
        print()
        print('Good choice, the Lion will be much easier for your first adventure.')
        print()
        encounter(Lion)
    elif user_input == 'west':
        print()
        print('Alright, I hope you are prepared!')
        print()
        encounter(Hydra)
    elif user_input == 'underworld':
        print()
        print('Good luck, you poor brave soul.')
        print()
        encounter(Cerberus)
    else:
        print()
        print('That wasnt an option, lets try again.')
        print()
        travel()            

def encounter(monster):
    name = monster['Name']
    print()
    print()
    print(f'After some time traveling, camping to stay healthy, and expertly tracking your prey, you encounter {name}!')
    print()
    print('Its time to fight, get ready!')
    while Hercules['Health'] > 0 or monster['Health'] > 0:
        print()
        user_input = input('Choose your Attack: Punch - Stab - Slice  ').lower()
        attack(user_input, monster)
        if monster['Health'] <= 0:
            print()
            print(f'{name} has been defeated! Prepare for your next adventure!')
            level_up()
            print()
            print(f'You have Leveled Up! You feel.. slightly stronger')
            print()
            heal()
            continue_onward()
            break
        print(f'{name} prepares his attack!')
        monster_attack(monster)
        if Hercules['Health'] <= 0:
            print(f'On No! You failed to defeat {name}!')
            print()
            print()
            print('You scramble back to your camp and nurse your wounds, preparing for the next battle!')
            heal()
            continue_onward()
          


def attack(string, monster):
    user_attack = string
    name = monster['Name']
    monster_dodge = random.randrange(0, monster['Dodge'])
    user_hit = random.randrange(0, Hercules['Attack_Power'])
    if user_hit >= monster_dodge:
        if user_attack in Hercules['Attacks']:
            print(f'You try and {user_attack} {name}!')
            print()  
            if user_attack == 'stab':
                dmg = Hercules['Attack_Power'] * user_hit + 10
            elif user_attack == 'slice':
                dmg = Hercules['Attack_Power'] * user_hit + 5
            elif user_attack == 'punch':
                dmg = Hercules['Attack_Power'] * 2 + user_hit        
            print(f'Nice! you did {dmg} damage to {name} with your {user_attack}!')
            print()
            new_hp = int(monster['Health']) - int(dmg)
            monster['Health'] = new_hp
            print(f'{name} has {new_hp} Health Left!')
            print()
        elif user_attack not in Hercules['Attacks']:
            print()
            print(f'It looks like {user_attack} is not an option! You miss this round!')  
            print()  
    else:
        print(f'You try and {user_attack} {name}!')
        print()
        print(f'{name} dodged your {user_attack}!')
        print()

def monster_attack(monster):
    name = monster['Name']
    monster_hit = random.randrange(0, monster['Attack_Power'])
    user_dodge = random.randrange(0, Hercules['Dodge'])
    if monster_hit > user_dodge:
        monster_attacks = monster['Attacks'][random.randrange(0, len(monster['Attacks']))]
        dmg = monster['Attack_Power'] * 5
        print()
        print(f'Oh no! {name} hit you with a {monster_attacks} for {dmg}')
        print()
        new_hp = int(Hercules['Health']) - int(dmg)
        Hercules['Health'] = new_hp
        if Hercules['Health'] > 0:
            print(f'Be Careful! You only have {new_hp} left!')
            print()
        elif Hercules['Health'] <= 0:
            print(f'This attack has knocked you to the floor with {new_hp} health left!')   
            print()
    else:
        print()
        print('Nice! You expertly doged out of the way!')  
        print()  


def heal():
    if Hercules['Level'] == 1:
        Hercules['Health'] = 100
    elif Hercules['Level'] == 2:
        Hercules['Health'] = 200
    elif Hercules['Level'] == 3:
        Hercules['Health'] = 300        


def level_up():
    new_attack_power = Hercules['Attack_Power'] + 5
    new_dodge = Hercules['Dodge'] + 2
    new_hp = Hercules['Health'] + 20
    Hercules['Health'] = new_hp
    Hercules['Dodge'] = new_dodge
    Hercules['Attack_Power'] = new_attack_power
    Hercules['Level'] += 1


def continue_onward():
    if Cerberus['Health'] <= 0 and Lion['Health'] <= 0 and Hydra['Health'] <= 0:
        tell_end()
    elif Lion['Health'] > 0 and Hydra['Health'] > 0 and Cerberus['Health'] > 0:
        travel()    
    elif Lion['Health'] <= 0 and Hydra['Health'] <= 0:
        print('Now that you have defeated the Lion and the Hydra, its time to go to the underworld!')
        print()
        encounter(Cerberus)
    elif Lion['Health'] <= 0 and Hydra['Health'] > 0 and Cerberus['Health'] > 0:
        print('Now that you have defeated that pesky Lion, where would you like to go next?')
        print()
        user_input = input('West, or toward the Underworld?: ').lower()
        if user_input == 'west':
            encounter(Hydra)
        elif  user_input == 'underworld':
             encounter(Cerberus)
    elif Hydra['Health'] <=0 and Lion['Health'] > 0 and Cerberus['Health'] > 0:
        print('Wow, did not expect you to take out that Hydra first. Where would you like to go next?')
        print()
        user_input = input('East, or toward the Underworld?: ').lower()
        if user_input == 'east':
            encounter(Lion)
        elif user_input == 'underworld':
            encounter(Cerberus)    
    elif Cerberus['Health'] <= 0 and Lion['Health'] > 0 and Hydra['Health'] > 0:
        print('You are truly a Demi God. The monsters to the East and West will be cake! Where too next?')
        print()
        user_input = input('East or West?: ').lower()
        if user_input == 'east':
            encounter(Lion)
        elif user_input == 'west':
            encounter(Hydra)
    elif Lion['Health'] <= 0 and Cerberus['Health'] <= 0:
        print('You took out the Lion, and Cerberus.. the only one that remains is the Hydra!')
        print()
        encounter(Hydra)        
                  


def run_game():
    tell_story()
    travel()


run_game()       