from PIL import Image
import numpy as np
import os

#geting the image file name from the user
image = input("Enter the image file name (including the extension): ")

#setting thr treshold valure which the pixel value will be compared to

a = 25
b = 50
c = 75
d = 100
e = 125
f = 150
g = 175
h = 200
i = 225
j = 250


#geting thte image to python screipt and makin it to a blacka and whte image
main_path = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(main_path, image)).convert("L")


#rezing the image to counter the fact that the height of terminal charector is double of its widhth
w, h = img.size
img = img.resize((500, int(((h / w) * 500) // 2.4)))

#converting the image to an numpy array
img_arr = np.array(img)

#selecting the ASCII charectors to act as the pixels
chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '&']

# Print loop
for row in range(img_arr.shape[0]):
    for col in range(img_arr.shape[1]):
        v = img_arr[row, col]
        if   v < a: c_ = 0
        elif v < b: c_ = 1
        elif v < c: c_ = 2
        elif v < d: c_ = 3
        elif v < e: c_ = 4
        elif v < f: c_ = 5
        elif v < g: c_ = 6
        elif v < h: c_ = 7
        elif v < i: c_ = 8
        elif v < j: c_ = 9
        else:       c_ = 10
        print(chars[c_], end="")
    print()