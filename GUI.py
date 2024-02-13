from tkinter import *
from tkinter import ttk



#Functions here
def changeText():

  toChange.set("Button Pressed")




#For root
root = Tk()

root.title("Database GUI")
root.geometry("600x600")
root.resizable(0,0)
root['bg'] = "white"



#Main page
main = Frame(root, height = 600, width = 600)

main.pack()


#Variables 
toChange = StringVar()  



#Widgets 
TestLabel = ttk.Label(main, text = "This Will Change", textvariable = toChange).place(x = 250, y = 100)
TestButton = ttk.Button(main, text="Do Something", command=changeText).place(x = 250, y = 200)


#Additional actions
toChange.set("Button Not Pressed")

#Draw to Screen
root.mainloop()