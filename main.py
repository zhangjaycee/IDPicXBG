#!/usr/bin/python
#coding: utf-8

import sys
import process

def main():
    ##### 1. init
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = "test1.jpg"
    img_proc = process.Process(file_path)

    ##### 2. set a background color to be used
    img_proc.set_bgcolor()

    ##### 3. sample current background color
    img_proc.sample_bgcolor()

    ##### 4. change any pixel near a current background color to the new color
    img_proc.change_color()

    ##### 5. write dst_img to file, making sure the output file size is over 40K
    #img_proc.cut()
    img_proc.write2file("dst_test.jpg")

    ##### 6. show
    img_proc.show_img()
                     
if __name__=="__main__":
    main()
