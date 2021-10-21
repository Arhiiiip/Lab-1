import json
import re

file = open('pokemon_full.json')
pokemon_full = file.read()
file.close()

print('1. Общее количество символов:', len(pokemon_full))

pokemon_non_prep = re.sub('[\w]', '', pokemon_full)
print('2. Количество символов без знаков препинания:', len(pokemon_full) - len(pokemon_non_prep))

pokemon_full_mas = json.loads(pokemon_full)
max_ch = 0
name_t = ''
for char in pokemon_full_mas:
    max_ch = max(len(char['description']), max_ch)
    if len(char['description']) == max_ch:
        name_t = char['name']
print('3. Покемон с самым длинным описанием:', name_t)

col = 0
for skills in pokemon_full_mas:
    for skill in skills['abilities']:
        col = max(len(skill.split()), col)
print('4. Умение(я) с самым большим количеством слов: ')
for skills in pokemon_full_mas:
    for skill in skills['abilities']:
        if col == len(skill.split()):
            print(skill)