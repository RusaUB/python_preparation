from tkinter import *
def click_me():
    print(i.get())
 
   
root =Tk()
i=IntVar()
c = Checkbutton(root, text = "art", variable=i).grid(column=1, row=1)

c1 = Checkbutton(root, text = "science").grid(column=2, row=1)

c2 = Checkbutton(root, text = "litterature").grid(column=3, row=1)

