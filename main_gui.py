#!/usr/bin/python
#coding: utf-8

import sys
import image
import Tkinter
import PIL

import tkFileDialog

class TkGUI:
    def __init__(self, root):
        root.title("IDPicXBG")
        self.button_sel = Tkinter.Button(root, text="select a image", command=self.load_image) 
        self.button_proc = Tkinter.Button(root, text="start processing", command=self.process_image) 
        self.button_sel.grid(row=0, column=0, padx=5, pady=5)
        self.button_proc.grid(row=0, column=1, padx=5, pady=5)

    def load_image(self):
        file_path = tkFileDialog.askopenfilename(filetypes=(('JPEG','*.jpg'), ('PNG', '*.png')))        
        self.img_proc = image.CvImage(file_path)
        self.img_proc.refresh_tk_imgs(256) #by default, width=256
        img1 = Tkinter.Label(image=self.img_proc.img_tk)
        #img1.pack(side="left", padx=10, pady=10)
        #img2 = Tkinter.Label(image=self.img_proc.img_dst_tk)
        #img2.pack(side="right", padx=10, pady=10)
        img1.grid(row=3, column=0)
        #img2.grid(row=3, column=1)

    def process_image(self):
        self.img_proc.set_bgcolor(255, 255, 255)
        self.img_proc.sample_bgcolor()
        self.img_proc.change_color()
        self.img_proc.write2file("dst_test.jpg")
        self.show_image()

    def show_image(self):
        self.img_proc.refresh_tk_imgs(256) #by default, width=256
        img1 = Tkinter.Label(image=self.img_proc.img_tk)
        #img1.pack(side="left", padx=10, pady=10)
        img2 = Tkinter.Label(image=self.img_proc.img_dst_tk)
        #img2.pack(side="right", padx=10, pady=10)
        img1.grid(row=3, column=0)
        img2.grid(row=3, column=1)

        
def main():
    ##### 1. init

    ##### 2. set a background color to be used ,for default, white (R, G, B)

    ##### 3. sample current background color

    ##### 4. change any pixel near a current background color to the new color

    ##### 5. write dst_img to file, making sure the output file size is over 40K
    #img_proc.cut()

    ##### 6. gui show
    root = Tkinter.Tk()
    window = TkGUI(root)
    root.mainloop()
                     
if __name__=="__main__":
    main()
