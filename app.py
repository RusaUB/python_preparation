import tkinter as tk
from tkinter import *

app = tk.Tk()
firstname = StringVar()
age = IntVar()

def enregistrer_en_texte():
  firstname_info = firstname.get()
  age_info = age.get()
  age_info = str(age_info)
  print(firstname_info, age_info)

  file = open("user.txt", "w")
  file.write(firstname_info)
  file.write(age_info)
  file.close()
  print(" User ", firstname_info, " has been registered successfully")


#input text
tk.Label(app, text="Nom et prenom").grid(row=0)
tk.Label(app, text="Age").grid(row=1)

input_1 = tk.Entry(app, textvariable = firstname, width = "30")
input_2 = tk.Entry(app, textvariable = age, width = "30")


input_1.grid(row=0, column=1)
input_2.grid(row=1, column=1)

#input radio 
v = tk.IntVar()
tk.Label(app, text="Sex", padx = 20).grid(row = 3)

tk.Radiobutton(app, text="Feminin",variable=v, value=1).grid(row = 3, column = 1)

tk.Radiobutton(app, text="Masculin", variable=v, value=2).grid(row = 3, column=2)


#continent
tk.Label(app, text = "Continent").grid(row = 6, column=0)
tk.Radiobutton(app, text = "Asie", variable = v,
                value = "Asie", indicator = 0,
                ).grid(row = 4, column=1)
tk.Radiobutton(app, text = "Afrique", variable = v,
                value = "Afrique", indicator = 0,
                ).grid(row = 5, column=1)
tk.Radiobutton(app, text = "Amérique", variable = v,
                value = "Amérique", indicator = 0,
                ).grid(row = 6, column=1)
tk.Radiobutton(app, text = "Europe", variable = v,
                value = "Europe", indicator = 0,
                ).grid(row = 7, column=1)


#Centre d'interet
tk.Label(app, text= "Centre d'interet").grid(row = 8, column=0)

tk.Checkbutton(app, text = "art").grid(column=1, row=8)

tk.Checkbutton(app, text = "science").grid(column=2, row=8)

tk.Checkbutton(app, text = "litterature").grid(column=3, row=8)

tk.Button(app, text = "Submit", command=enregistrer_en_texte).grid(row = 9, column=1)

app.mainloop()