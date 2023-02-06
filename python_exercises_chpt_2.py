# Keep in mind that I'm only writing the answers of the questions that require coding.

'''
Write a function named announce_pitch that takes in the name of a player and a pitch (e.g 'Kershaw', 'slider') and returns a
string of the form 'Kershaw with the slider'.
'''
def announce_pitch(pitcher_name, pitch):
    return f'{pitcher_name} with the {pitch}'

print(announce_pitch('Urías', '4 seam fastball'))

'''
Write a funcion is_travisd that takes in a player name and returns a bool indicating whether the player's name is 'Travis d'Arnaud'
regardless of case or wether the user included the '.
'''
# My answer
def is_travisd(name):
    if name == "Travis d'Arnaud" or name == "Travis dArnaud":
        return True
    else:
        return False
#Book Answer
def is_travisd(player):
    return player.replace("'", '').lower() == 'travis darnaud'

is_travisd('babe ruth')
is_travisd("Travis d'Arnaud")
is_travisd("TRAVIS DARNAUD")

'''
Write a function 'commentary' that takes in a batting average (without the decimal, 333, 280) and returns the string '333 is a good average'
if the number is >= 300 ir '275 is not that good' otherwise.
'''
def commentary(avg):
    if avg >= 300:
        return f'{avg} is a good average'
    else:
        return f'{avg} is not that good'

'''
Write a function 'commentary_plus' that works like commentary but can also hanle averages passed on decimal form. Note, it should be able
to handle non-decimal avgs too.
'''
def commentary_plus(avg):
    if avg < 1:
        avg = int(avg * 1000)
    if avg >= 300:
        return f'{avg} is a good average'
    else:
        return f'{avg} is not that good'

'''
From the given list, print the list without 'mookie betts' in 3 different ways. Use at least one list-comprehension
'''
dodgers_roster = ['clayton kershaw', 'cody bellinger', 'mookie betts']

print(dodgers_roster[0:2])
print(dodgers_roster[:-1])
print([player for player in dodgers_roster if player != 'mookie betts'])

'''
With the following dict:

1. Change the 'starter' to Joe Kelly
2. Write a funcion 'toggle_throws' that takes a dict like pitcher_info, turns 'throws_right' to the opposite of whatever it is
and returns the updated settings dictionary.
'''
pitcher_info = {'starter': 'Kershaw', 'throws_right': False}

pitcher_info['starter'] = 'Joe Kelly'
def toggle_throws(pitcher):
    pitcher['throws_right'] = not pitcher['throws_right']
    return pitcher

toggle_throws(pitcher_info)

'''
Assuming we have the same dict, go through each line and say wether it'll work without an error:

1. pitcher_info['era'] -> undefined
2. pitcher_info['starter'] -> no error
3. pitcher_info['age'] = 32 -> no error
'''

