import json
import random
import time

file = open('pokemon_full.json')
pokemon_full = file.read()
file.close()

pokemon_full_list = json.loads(pokemon_full)
fighters = random.sample(pokemon_full_list, 2)
names = []
tots = []
skills = []
for char in fighters:
    names.append(char['name'])
    skills.append(char['stats'])
for skill in skills:
    tots.append(skill['total'])

print(names[0], 'VS', names[1])
time.sleep(1)
print('...1...')
time.sleep(0.5)
print('...2...')
time.sleep(0.5)
print('...3...')
time.sleep(0.5)
print('FIGHT')
time.sleep(1)
if tots[0] > tots[1]:
    print('WINNER:', names[0], '!!!')
elif tots[0] < tots[1]:
    print('WINNER:', names[1], '!!!')
else:
    print('Draw(((')
