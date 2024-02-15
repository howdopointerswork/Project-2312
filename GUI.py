from tkinter import *
from tkinter import ttk




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

#Labels/Text for Page 1
p1_Select_Lbl_Var = StringVar()
p1_From_Lbl_Var = StringVar()


p2Var = StringVar()
p3Var = StringVar()
p4Var = StringVar()


#Used for Selection/Search page (Page 1) 
#To be used for first argument in SELECT query (column name)
p1_Select_Ipt_Var = StringVar()
#To be used for second argument in SELECT query (table name)
p1_From_Ipt_Var = StringVar()
#To add WHERE field and functionality


#Widgets 

	#For root


p1Btn = ttk.Button(main, text="Page 1", command= lambda: changePage(p1)).place(x = 250, y = 200)

p2Btn = ttk.Button(main, text="Page 2", command= lambda: changePage(p2)).place(x = 250, y = 300)

p3Btn = ttk.Button(main, text="Page 3", command= lambda: changePage(p3)).place(x = 250, y = 400)

p4Btn = ttk.Button(main, text="Page 4", command= lambda: changePage(p4)).place(x = 250, y = 500)

#Back button
backBtn = ttk.Button(root, text="Back", command=showMain).place(x = 50, y=500)




#Page 1 layout
p1_lbl1 = ttk.Label(p1, textvariable=p1_Select_Lbl_Var).place(x=150,y=200)
p1_Select_Lbl_Var.set("Select Column:")

#Going to only allow characters here
p1_ipt1 = ttk.Entry(p1, width=20, textvariable=p1_Select_Ipt_Var).place(x=300, y=200)



p1_lbl2 = ttk.Label(p1, textvariable=p1_From_Lbl_Var).place(x=150, y=300)
p1_From_Lbl_Var.set("From Table:")

#Only characters here as well
p1_ipt2 = ttk.Entry(p1, width=20, textvariable=p1_From_Ipt_Var).place(x=300, y=300)



#Where condition text and field to be added here





#Page 2 layout
p2Lbl = ttk.Label(p2, textvariable=p2Var).place(x=250,y=300)
p2Var.set("Page 2")


#Page 3 layout
p3Lbl = ttk.Label(p3, textvariable=p3Var).place(x=250,y=300)
p3Var.set("Page 3")

#Page 4 layout
p4Lbl = ttk.Label(p4, textvariable=p4Var).place(x=250,y=300)
p4Var.set("Page 4")

main.pack()




#Additional actions


#Draw to Screen
root.mainloop()

