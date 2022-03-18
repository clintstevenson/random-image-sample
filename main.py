from PIL import Image
import numpy as np   
import random
import math
import itertools
from itertools import permutations
  
# Opening the image and converting 
# it to RGB color mode
photo_name = "captain_america"
img = Image.open(r"C:\\temp\\" + str(photo_name) + ".jpg").convert('RGB')
  
# Extracting the image data &
# creating an numpy array out of it
img_arr_orig = np.array(img)
img_arr = np.array(img)
percent_sample = .05

width, height = img.size
total_size = width * height
sample_size = total_size - math.floor(total_size * (1 - percent_sample))
if False:
    x_range = range(1, width)
    y_range = range(1, height)
    permut = itertools.permutations(x_range, len(y_range))

    sampled_list = []
    sampled_colors = []
    while len(sampled_list) < sample_size:
        n_x = random.randint(0, width - 1)
        n_y = random.randint(0, height - 1)
        sampled_location = str(n_y) + "," + str(n_x)
        pixel_color = img_arr_orig[n_y, n_x]

        if False: # Turn on for a biased result
            if n_y < height / 2 and n_x > width / 2:        
                if sampled_location not in sampled_list:
                    sampled_list.append(sampled_location)            
                    sampled_colors.append(pixel_color)
            else:
                if random.uniform(0,1) > .9 and sampled_location not in sampled_list:
                    sampled_list.append(sampled_location)            
                    sampled_colors.append(pixel_color)
        else:
            if sampled_location not in sampled_list:
                sampled_list.append(sampled_location)            
                sampled_colors.append(pixel_color)

    for i in range(0, len(sampled_list)):
        sampled_list[i] = sampled_list[i].split(",")

    img_arr[0 : height - 1, 0 : width - 1] = (0,0,0)

    for j in range(0, len(sampled_list) - 1):
        # Turning the pixel values of the 400x400 pixels to black 
        # print(str(i -1) + " " + str(random_x[i -1]))

        img_arr[int(sampled_list[j][0]), int(sampled_list[j][1])] = sampled_colors[j]

img_arr[0 : height - 1, 0 : width - 1] = (0,0,0)
img_arr[100 : 340, 0 : 240] = img_arr_orig[100 : 340, 0 : 240]
img = Image.fromarray(img_arr)
print(sample_size)
img.save('C:\\temp\\' + str(round(percent_sample * 100, 0)) + '-percent-sampled_picture_' + str(photo_name) + '.jpg')
# Displaying the image
img.show()
