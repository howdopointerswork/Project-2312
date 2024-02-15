from tkinter import *
from tkinter import ttk


#Temporary change


#Functions here
def hideMain():
	
	main.pack_forget()

#Function to hide/show page


def showMain():

	p1.pack_forget()
	p2.pack_forget()
	p3.pack_forget()
	p4.pack_forget()
	main.pack()



def changePage(self):


	hideMain()
	self.pack()







#For root
root = Tk()

root.title("Database GUI")
root.geometry("600x600")
root.resizable(0,0)





#Main page
main = Frame(root, height = 600, width = 600)
#Other pages
p1 = Frame(root, height = 600, width = 600)
p2 = Frame(root, height = 600, width = 600)
p3 = Frame(root, height = 600, width = 600)
p4 = Frame(root, height = 600, width = 600)





#Variables 
toChange = StringVar()  
p1Var = StringVar()
p2Var = StringVar()
p3Var = StringVar()
p4Var = StringVar()
curr = main




#Widgets 

	#For root


p1Btn = ttk.Button(main, text="Page 1", command= lambda: changePage(p1)).place(x = 250, y = 200)

p2Btn = ttk.Button(main, text="Page 2", command= lambda: changePage(p2)).place(x = 250, y = 300)

p3Btn = ttk.Button(main, text="Page 3", command= lambda: changePage(p3)).place(x = 250, y = 400)

p4Btn = ttk.Button(main, text="Page 4", command= lambda: changePage(p4)).place(x = 250, y = 500)

#Back button
backBtn = ttk.Button(root, text="Back", command=showMain).place(x = 50, y=500)



p1Lbl = ttk.Label(p1, textvariable=p1Var).place(x=250,y=300)
p1Var.set("Page 1")

p2Lbl = ttk.Label(p2, textvariable=p2Var).place(x=250,y=300)
p2Var.set("Page 2")

p3Lbl = ttk.Label(p3, textvariable=p3Var).place(x=250,y=300)
p3Var.set("Page 3")

p4Lbl = ttk.Label(p4, textvariable=p4Var).place(x=250,y=300)
p4Var.set("Page 4")

main.pack()
curr = main



#Additional actions


#Draw to Screen
root.mainloop()
