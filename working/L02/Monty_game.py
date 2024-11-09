# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:36:39 2024

@author: ISAFA
"""

import numpy as np
import matplotlib.pyplot as plt

num_games = 10000
win_count_cons = 0
win_count_swit = 0
win_count_new = 0
doors = np.arange(3)

for i in range(num_games):
    
    car = np.random.choice(doors) #one of the door has a car behind
    first_choice = np.random.choice(doors) #first choice of the player
    
    monty_door = np.random.choice(np.delete(doors, [first_choice, car])) #Monty proposes a new door (obv without the car)
    switcher_choice = np.random.choice(np.delete(doors, [first_choice, monty_door])) #switcher changes door
    newcomer_choice = np.random.choice(np.delete(doors, monty_door))
    
    if first_choice == car:
        win_count_cons += 1
        
    if switcher_choice == car:
        win_count_swit += 1   
        
    if newcomer_choice == car:
        win_count_new += 1 
    
print(win_count_cons) 
print(win_count_swit)
print(win_count_new)

prob_cons = win_count_cons/num_games
prob_swit = win_count_swit/num_games
prob_new = win_count_new/num_games

fig, ax = plt.subplots()

people = ['conserver', 'switcher', 'newcomer']
counts = [prob_cons, prob_swit, prob_new]
#bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue','tab:orange']

ax.bar(people, counts, color= bar_colors)

ax.set_ylabel('Monty game probability')
ax.set_title('Probability')

plt.show()

  
#%% 
prize = ['goat', 'goat', 'car']

doors = np.random.choice(prize, 3, replace = False)
print('The prizes behind each door are: ')
print(doors)
print('   1\t  2\t  3\n')

first_choice = np.random.randint(0, 3)
print('The contestant chooses the door: ' + str(first_choice+1))

winning_door = np.where(doors=='car')[0][0]

while(True):
    open_door = np.random.randint(0, 3)
    if (open_door != winning_door and open_door != first_choice): break
print('The game host opens the door: ' + str(open_door+1))

conservator_door = first_choice

while(True): 
    switcher_door = np.random.randint(0, 3)
    if (switcher_door != first_choice and switcher_door != open_door): break
    
while(True):
    newcomer_door = np.random.randint(0, 3)
    if (newcomer_door != open_door): break
        
print('The conservator keeps his door: ' + str(conservator_door+1))
print('The switcher chooses the other door: ' + str(switcher_door+1))
print('The newcomer chooses a door: ' + str(newcomer_door+1) + '\n')

print('And the winner is...')

if(conservator_door == winning_door):
    print('\tconservator WINS!')
    print('\tswitcher loses...')
else:
    print('\tconservator loses...')
    print('\tswitcher WINS!')
if(newcomer_door == winning_door):
    print('\tnewcomer WINS!')
else:
    print('\tnewcomer loses...')
    
#%% SOLUZIONE PROF
import numpy as np
from tqdm.notebook import tqdm
import pylab as plt
plt.rcParams['figure.figsize'] = [8, 8]
def threedoors(which):

    labels = np.arange(3) # Labels of the three doors
    doors = np.zeros(3,dtype=int) # Content of three doors
    doors[np.random.choice(labels)] = 1 # One of them contains the prize, don't know which one
    choice = np.random.choice(labels) # I pick one door
    notchosen = np.delete(labels,choice) # These are the remaining doors 

    while True:
        opened = np.random.choice(notchosen) #One door is opened
        if doors[opened]==0: # But it's never the winning door
            other = int(np.delete(labels,[opened,choice])) # This is the other door left
            break
       
    if which == 'switch': # Do you switch? If yes, return content of the other door 
        return doors[other]

    elif which == 'keep': # If not, return content of the one you picked initially
        return doors[choice]
 
    elif which == 'external': # A third guy picks randomly between the two remaining doors
        picked = np.random.choice([choice,other])
        return doors[picked]
    
N  = int(1e5) # Do this many times
probs = {}

for which in tqdm(['switch','keep','external']):
    events = [threedoors(which) for i in tqdm(range(N))]
    probs[which] = np.sum(events)/ N
    
    # A simple bar chart
plt.bar([0,1,2], [probs[k] for k in probs.keys()], color='green');
plt.xticks([0,1,2], probs.keys());

for y in [1/3,1/2,2/3]:
    plt.axhline(y, ls='dotted',c='black')