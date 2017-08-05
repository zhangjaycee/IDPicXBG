#!/usr/bin/python
#coding: utf-8

import numpy as np
import cv2
import math
import sys
import PIL
from PIL import Image, ImageTk


class CvImage:
    def __init__(self, path):
        self.load_img(path)
        print "loaded, inited ok..."

    def load_img(self, file_path):
        self.img = cv2.imread(file_path)
        self.img_dst = cv2.imread(file_path)
        self.height, self.width = self.img.shape[0:2]
        print "height =", self.height, "width =", self.width

    def refresh_tk_imgs(self, width):
        height = width * self.height / self.width 
        self.img_tk = self.cv2tk(self.img, width, height)
        self.img_dst_tk = self.cv2tk(self.img_dst, width, height)
    def cv2tk(self, img, width, height):
        img=cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        img_cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_cv_rgb)
        img_pil_tk = ImageTk.PhotoImage(img_pil)
        return img_pil_tk

    def set_bgcolor(self, b, g, r):
        self.fill_color = (r, g, b)

    def sample_bgcolor(self):
        # init
        p_l = []
        p_r = []
        p_u = []
        p_d = []
        p1_height = p3_height = self.height / 2
        p1_width = p3_width = self.width / 8
        p2_height = self.height / 12
        #p_x[0]
        p_l.append(0)
        p_r.append(p1_width)
        p_u.append(0)
        p_d.append(p1_height)
        #p_x[1]
        p_l.append(0)
        p_r.append(self.width)
        p_u.append(0)
        p_d.append(p2_height)
        #p_x[2]
        p_l.append(self.width - p3_width)
        p_r.append(self.width)
        p_u.append(0)
        p_d.append(p3_height)
        # choose a sample step 
        step = max(self.width / 20, 3)
        print "step =", step, "sample =", (self.width / step) * (self.height / step) 
        # store sampled background candidte colors to a dict
        self.color_dict ={}
        for i in range(3):
            for j in range(p_u[i], p_d[i], step):
                for k in range(p_l[i], p_r[i], step):
                    tmp = (self.img[j, k][0], self.img[j, k][1], self.img[j, k][2])
                    if tmp in self.color_dict:
                        self.color_dict[tmp] += 1
                    else: 
                        self.color_dict[tmp] = 1
        # threshold of choosing backfround colors from candidate colors dict
        self.count_sel = min(self.height/20 + self.width/20 + 2, 5)
        print "count_sel =", self.count_sel

    def color_near(self, color1, color2):
        for i in range(3):
            if abs(int(color1[i]) - int(color2[i])) > 45:
                return False
        return True

    def change_color(self):
        for i in range(self.height):
            for j in range(self.width):
                tmp = (self.img[i, j][0], self.img[i, j][1], self.img[i, j][2])
                for item in self.color_dict:
                    if self.color_dict[item] > self.count_sel and self.color_near(tmp, item):
                        self.img_dst[i][j] = self.fill_color 
        print "Done!~"

    def cut(self):
        if self.height * self.width < 100000:
            r = 100000 / self.height / self.width
            self.img_dst=cv2.resize(self.img_dst, None, fx=r, fy=r, interpolation=cv2.INTER_CUBIC)
        
    
    def write2file(self, path):
        cv2.imwrite(path, self.img_dst)

    def show_img(self):
        cv2.imshow('src', self.img)
        cv2.imshow('dst', self.img_dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
def main():
    ##### 1. init
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = "test1.jpg"
    img_proc = CvImage(file_path)

    ##### 2. set a background color to be used
    img_proc.set_bgcolor()

    ##### 3. sample current background color
    img_proc.sample_bgcolor()

    ##### 4. change any pixel near a current background color to the new color
    img_proc.change_color()        

    ##### 5. write dst_img to file, making sure the output file size is over 40K
    img_proc.cut()
    img_proc.write2file("dst_test.jpg")
    
    #### 6. show
    img_proc.show_img()
                     
if __name__=="__main__":
    main()
