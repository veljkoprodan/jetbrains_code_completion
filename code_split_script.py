import os
import numpy as np
import random
import json

codes = []

for filename in os.listdir('./files/'):
    with open('./files/' + filename, 'r') as file:
        
        code = ""
        
        for line in file:
            if (line.strip() and
                not line.startswith('# In[') and 
                not line.startswith('#!/usr/bin/env') and 
                not line.startswith('# coding: utf-8') and
                not 'Created by' in line and
                line.strip() != "//" and
                line.strip() != "#"
               ):
                
                code += line
                
        codes.append(code)
        
middle_lens = [random.choice([1,2,3]) for _ in range(len(codes))]
dataset = []
padding = 1

for code, middle_len in zip(codes, middle_lens):    
    lines = code.splitlines()
    if i == 23:
        idx = 1
    else:
        idx = random.choice(range(padding, len(lines) - middle_len - padding))
    
    
    data = {}
    data['prefix'] = '\n'.join(lines[:idx])
    data['middle'] = '\n'.join(lines[idx:idx + middle_len])
    data['suffix'] = '\n'.join(lines[idx + middle_len:])
    
    dataset.append(data)
    
with open('dataset_512.json', 'w') as file:
    json.dump(dataset, file)
