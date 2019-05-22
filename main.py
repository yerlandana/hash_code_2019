#%%
import pandas as pd 

Dana = 'a_example.txt'
filename_small = 'b_lovely_landscapes.txt'
filename_medium = 'c_memorable_moments.txt'
filename_big = 'd_pet_pictures.txt'
df = pd.read_csv(Dana)

photos =[]
type_photos = []


df_header = str(df.iloc[[0], [0]])

with open(Dana, 'r') as file:
    p_num = file.readline()
with open(Dana, 'r') as file:
    for photo in range(int(p_num)+1):
        line = file.readline()
        

print(p_num)
#print(df_header)