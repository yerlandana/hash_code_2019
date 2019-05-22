#%%
import pandas as pd
from collections import Counter

filename_example = 'a_example.txt'
filename_b = 'b_lovely_landscapes.txt'
filename_c = 'c_memorable_moments.txt'
filename_d = 'd_pet_pictures.txt'
filename_e = 'e_shiny_selfies.txt'

photos = []
type_photos = []

with open(filename_example, 'r') as file:
    p_num = file.readline()

with open(filename_example, 'r') as file:
    for photo in range(int(p_num) + 1):
        line = file.readline()
        type_photos.append(line[:1])

type_photos = type_photos[1:]

h_num = 0
v_num = 0

for c in type_photos:
    if(c == 'H'):
        h_num = h_num + 1
    if(c == 'V'):
        v_num = v_num + 1

v_num = int(v_num / 2)
slides = v_num + h_num

hashtags_v = {}
hashtags_h = {}

hashtags_v_num = {}
hashtags_h_num = {}
print(slides)

with open(filename_example, 'r') as file:
    for photo in range(int(p_num) + 1):
        line = file.readline()
        if(line[0] == 'V'):
            hashtags_v[photo] = line[4:]
        if(line[0] == 'H'):
            hashtags_h[photo] = line[4:]

with open(filename_example, 'r') as file:
    for photo in range(int(p_num) + 1):
        line = file.readline()
        if(line[0] == 'V'):
            hashtags_v_num[photo] = int(line[2:4])
        if(line[0] == 'H'):
            hashtags_h_num[photo] = int(line[2:4])

max_h_index = max(hashtags_h_num, key=hashtags_h_num.get) + 1
max_h = max(hashtags_h_num.values())

    
a = Counter(hashtags_h).keys()
b = Counter(hashtags_v).keys()        

print(slides)
print(max_h_index - 2)
next_h_index = list(a)[1] - 1
next_v1_index = list(b)[0] - 1
next_v2_index = list(b)[1] - 1
print(next_h_index)
print(str(next_v1_index) + ' ' + str(next_v2_index))

out_file = open('e_out.txt', 'w')
out_file.write(str(slides) + '\n')
out_file.write(str(max_h_index - 2) + '\n')
out_file.write(str(next_h_index) + '\n')
out_file.write(str(next_v1_index) + ' ' + str(next_v2_index))
out_file.close()