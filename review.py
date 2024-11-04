import json
from termcolor import colored

with open('./json/dataset_reviewed.json', 'r') as file:
    dataset = json.load(file)
    
for i, data in enumerate(dataset, start=1):
    print(f'{i}/{len(dataset)}')
    print('=' * 100)
    
    print(data['prefix'])
    print('-' * 50)
    
    print(colored(data['middle'], 'green'))
    print('*' * 20)
    print(colored(data['middle_predicted'], 'yellow'))
    print('-' * 50)
    
    print(data['suffix'], '\n')
    
    print('~' * 50)
    print('Is the predicted code correct?\n(1 - completely incorrect, 5 - perfect)')
    data['review_label'] = input()

    print('Comment:')
    data['comment'] = input()
    print('~' * 40)
    
    print('\n')
    print('=' * 100)
    

with open('./json/dataset_reviewed.json', 'w') as file:
    json.dump(dataset, file)
