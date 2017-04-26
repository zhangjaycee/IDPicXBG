#!/usr/bin/python
#coding: utf-8

import numpy as np
import cv2
import math
import sys


def color_near(color1, color2):
    for i in range(3):
        if abs(int(color1[i]) - int(color2[i])) > 45:
            return False
    return True
    

if __name__=="__main__":
    ##### 1. read a image from a file
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = "test1.jpg"

    img = cv2.imread(file_path)
    img_dst = cv2.imread(file_path)
    height, width = img.shape[0:2]
    print "height =", height, "width =", width
    
    ##### 2. set a background color to be used
    fill_color = (255, 255, 255)

    ##### 3. sample current background color
    # init
    p_l = []
    p_r = []
    p_u = []
    p_d = []

    p1_height = p3_height = height / 2
    p1_width = p3_width = width / 8
    p2_height = height / 12

    #p_x[0]
    p_l.append(0)
    p_r.append(p1_width)
    p_u.append(0)
    p_d.append(p1_height)
    #p_x[1]
    p_l.append(0)
    p_r.append(width)
    p_u.append(0)
    p_d.append(p2_height)
    #p_x[2]
    p_l.append(width - p3_width)
    p_r.append(width)
    p_u.append(0)
    p_d.append(p3_height)

    # choose a sample step 
    step = max(width / 20, 3)
    print "step =", step, "sample =", (width / step) * (height / step) 
    
    # store sampled background candidte colors to a dict
    color_dict ={}
    for i in range(3):
        for j in range(p_u[i], p_d[i], step):
            for k in range(p_l[i], p_r[i], step):
                tmp = (img[j, k][0], img[j, k][1], img[j, k][2])
                if tmp in color_dict:
                    color_dict[tmp] += 1
                else: 
                    color_dict[tmp] = 1

    # threshold of choosing backfround colors from candidate colors dict
    count_sel = min(height/20 + width/20 + 2, 5)
    print "count_sel =", count_sel

    ##### 4. change any pixel near a current background color to the new color
    for i in range(height):
        for j in range(width):
            tmp = (img[i, j][0], img[i, j][1], img[i, j][2])
            for item in color_dict:
                if color_dict[item] > count_sel and color_near(tmp, item):
                    img_dst[i][j] = fill_color 
        

    print "Done!~"
    
    ##### 5. write dst_img to file, making sure the output file size is over 40K
    if height * width < 100000:
        r = 100000 / height / width
        img_dst=cv2.resize(img_dst, None, fx=r, fy=r, interpolation=cv2.INTER_CUBIC)
    dst_path = "dst.jpg"
    cv2.imwrite(dst_path, img_dst)
    
    cv2.imshow('src', img)
    cv2.imshow('dst', img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                     
