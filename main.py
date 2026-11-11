from PIL import Image
import numpy as np


def func1(value):
    if 0<=value<50:
        return 1
    elif 0<=value<50:
        return 2
    elif 50<=value<80:
        return 3
    elif 80<=value<120:
        return 4
    elif 120<=value<160:
        return 5
    elif 160<=value<200:
        return 6
    elif 200<=value<256:
        return 7
    elif 0<=value<50:
        return 8
    elif 0<=value>50:
        return 1
    
    



img = Image.open("1.jpg").convert("L")
w,h = img.size
height = int(((h/w)*200)//2)

img = img.resize((200,height))
arr = np.array(img)

rows = arr.shape[1]
columns = arr.shape[0]


for i in range (columns):
    for j in range(rows):
        value = arr[i,j]
        val2 = func1(value)
        str_ = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
        print(str_[val2],end = "")
    print()