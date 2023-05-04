# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:44:34 2023

@author: upon
"""

import os

from PIL import Image


bg_img = '../Data/bg.png'
data_1_img = '../Data/little_new_1.png'
data_2_img = '../Data/little_new_1.png'
data_3_img = '../Data/little_white.png'
data_4_img = '../Data/little_new_big_head.png'


Imgs = ['../Data/little_new_1.png',
        '../Data/little_new_1.png',
        '../Data/little_white.png',
        '../Data/little_new_big_head.png']

for i,path_id in enumerate(Imgs,start=1):
    path = os.path.join(os.getcwd(),path_id)
    img = Image.open(path)
    
    print("%d:%s" %(i,path_id))
    print ("Format:", img.format) # PNG
    print ("Image Size:",img.size) # (3500, 3500)
    print()
