#!/usr/bin/python
#coding: utf-8

import numpy as np
import cv2
import math
import sys



if __name__=="__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = "test1.jpg"
    # read a image from a file
    img = cv2.imread(file_path)
    img_dst = cv2.imread(file_path)
    
    height, width = img.shape[0:2]

    p_l = []
    p_r = []
    p_u = []
    p_d = []

    p1_height = p3_height = height / 2
    p1_width = p3_width = width / 6
    p2_height = height / 12
    print p1_height
    print p1_width

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
    '''
    for i in range(3):
        print p_l[i], p_r[i], p_u[i], p_d[i]
        img_dst[p_u[i]:p_d[i], p_l[i]:p_r[i]] = (255, 255, 255)
    '''
    color_list = []
    color_sel = []
    step = min(width / 20, 3)
    print "height =", height, "width =", width
    print "step =", step, "sample =", (width / step) * (height / step) 
    
    for i in range(3):
        for j in range(p_u[i], p_d[i], step):
            for k in range(p_l[i], p_r[i], step):
                tmp = (img[j, k][0], img[j, k][1], img[j, k][2])
                color_list.append(tmp)

    count_sel = max(width/500+1,1)
    print "count_sel =", count_sel
    for item in color_list:
        if  (item not in color_sel) and color_list.count(item) > count_sel:
            for i in range(-5,5):
                for j in range(-5,5):
                    for k in range(-5,5):
                        tmp = (item[0]+i, item[1]+j, item[2]+k)
                        if tmp not in color_sel:
                            color_sel.append(tmp)
    print "selected color number =", len(color_sel)


    fill_color = (255, 255, 255)
    for i in range(height):
        #print i
        for j in range(width):
            tmp = (img[i, j][0], img[i, j][1], img[i, j][2])
            if tmp in color_sel:
                img_dst[i][j] = fill_color 
        
    print "ok"
    #sorted(d_color.items(), key=lamada item:item[1])
    #sorted(d_color.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

    
    cv2.imshow('src', img)
    cv2.imshow('dst', img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                     
