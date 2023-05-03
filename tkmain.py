import customtkinter 
import configparser
import sys
import os
from tkindoorv import top
from tkoutdoorv import top2
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')

#for writing functions
def click1():
    root = customtkinter.CTkToplevel()
    top(root,main)

def click2():
    root = customtkinter.CTkToplevel()
    top2(root,main)

main = customtkinter.CTk()
main.title("GaMeR")
main.geometry("670x500")
main.resizable(False, False)

my_image = customtkinter.CTkImage(light_image=Image.open("png.png"),
                                  dark_image=Image.open("png.png"),
                                  size=(320, 490))
imglabel = customtkinter.CTkLabel(main,image=my_image,text="",corner_radius=10)
imglabel.grid(row=0,column=0,padx=10,pady=5)

frame1 = customtkinter.CTkFrame(main)
frame1.grid(row=0,column=1,sticky=customtkinter.NSEW,padx=5,pady=15)


head = customtkinter.CTkLabel(frame1,text='AUTOMATION OF AUTOCAD By GaMeR',font=('arial',15))
head.grid(row=0,column=0,padx=10,pady=20,sticky=customtkinter.N)

button1 = customtkinter.CTkButton(frame1,text="INDOOR PANEL",command=click1)
button1.grid(row=2,column=0,padx=10,pady=45,sticky=customtkinter.S)

button2 = customtkinter.CTkButton(frame1,text="OUTDOOR PANEL",command=click2)
button2.grid(row=4,column=0,padx=10,pady=45,sticky=customtkinter.S)

button2 = customtkinter.CTkButton(frame1,text="BOX PANEL")
button2.grid(row=5,column=0,padx=10,pady=45,sticky=customtkinter.S)

main.mainloop()