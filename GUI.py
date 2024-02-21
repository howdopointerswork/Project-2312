from tkinter import *
from tkinter import ttk


#For future:

#Create Page class
#Make Main parent
#Make Pages children


#Each has their own layout
#And can use reset and change pages through member function



#Hide back button on main page



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
	resetP3()
	self.pack()


def resetP3():

	p3_Alter_Ipt_Var.set(p3_Alter_Ipt_Arr[0])
	p3_Add_Ipt_Var.set(p3_Add_Ipt_Arr[0])
	p3_drop.set(p3_drop_Arr[0])
	
	

def addCol():



	p3_addCol_Var.set("Successfully Added Column!")




	#resetP3()

	
	







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

#Label variables
############################################
#Labels/Text for Page 1
p1_Select_Lbl_Var = StringVar()
p1_From_Lbl_Var = StringVar()
p1_Where_Lbl_Var = StringVar()

p2_Select_Lbl_Var = StringVar()
p2_Set_Lbl_Var = StringVar()
p2_Where_Lbl_Var = StringVar()


p3_Alter_Lbl_Var = StringVar()
p3_Add_Lbl_Var = StringVar()
p3_Type_Lbl_Var = StringVar()


p4_Delete_Lbl_Var = StringVar()
p4_Delete_Lbl_Var2 = StringVar()



#Input variables
#############################################

#Used for Selection/Search page (Page 1) 
#To be used for first argument in SELECT query (column name)
p1_Select_Ipt_Var = StringVar()
#To be used for second argument in SELECT query (table name)
p1_From_Ipt_Var = StringVar()
#To add WHERE field and functionality
p1_Where_Ipt_Var1 = StringVar()
p1_Where_Ipt_Var2 = IntVar()


p2_Update_Ipt_Var = StringVar()
p2_Set_Ipt_Var = StringVar()
p2_Where_Ipt_Var1 = StringVar()
p2_Where_Ipt_Var2 = IntVar()

p3_Alter_Ipt_Var = StringVar()
p3_Alter_Ipt_Arr = ["Select Table", "Table1", "Table2", "Table3"]

p3_Add_Ipt_Var = StringVar()
p3_Add_Ipt_Arr = ["Select Column", "Column1", "Column2", "Column3", "Column4"]

p4_Delete_Ipt_Var = StringVar()
p4_Where_Ipt_Var = StringVar()
p4_Where_Ipt_Var2 = IntVar() # Can also be String, applies to all Condition Entries



#Misc variables
#############################################

p1_drop = StringVar()


p2_drop = StringVar()

p3_drop = StringVar()
p3_tbl_drop = StringVar()
p3_drop_Arr = ["Select Type", "Char", "Int", "Decimal", "Longtext", "Date", "Varchar", "Autonumber", "Shorttext", "Number"]


p4_drop = StringVar()

p3_addCol_Var = StringVar()




#For messages to the user









#Widgets 

	#For root


p1Btn = ttk.Button(main, text="Search", command= lambda: changePage(p1)).place(x = 250, y = 100)

p2Btn = ttk.Button(main, text="Edit", command= lambda: changePage(p2)).place(x = 250, y = 200)

p3Btn = ttk.Button(main, text="Add", command= lambda: changePage(p3)).place(x = 250, y = 300)

p4Btn = ttk.Button(main, text="Delete", command= lambda: changePage(p4)).place(x = 250, y = 400)

#Back button
#May change to be part of each page, so that it is present only upon clicking an initial button
#Rather than being obsolete on the main page
backBtn = ttk.Button(root, text="Back", command=showMain).place(x = 50, y=500)




#Page 1 layout
#The two labels and entries below will likely be shifted up in the future to make space for where conditions
p1_lbl1 = ttk.Label(p1, textvariable=p1_Select_Lbl_Var).place(x=150,y=100)
p1_Select_Lbl_Var.set("Select Column:")

#Going to only allow characters here
#Entry box for the SELECT clause
p1_ipt1 = ttk.Entry(p1, width=20, textvariable=p1_Select_Ipt_Var).place(x=300, y=100)


#Label for the entry box for FROM clause
p1_lbl2 = ttk.Label(p1, textvariable=p1_From_Lbl_Var).place(x=150, y=200)
p1_From_Lbl_Var.set("From Table:")
#Only characters here as well
#Entry box for the FROM clause

p1_ipt2 = ttk.Entry(p1, width=20, textvariable=p1_From_Ipt_Var).place(x=300, y=200)

#Label for conditions for searching
p1_lbl3 = ttk.Label(p1, textvariable=p1_Where_Lbl_Var).place(x=150, y=300)
p1_Where_Lbl_Var.set("Condition:")

#Entry box for the WHERE clause
p1_ipt3 = ttk.Entry(p1, width=20, textvariable=p1_Where_Ipt_Var1).place(x=300, y=300)
#May add BETWEEN and such
p1_drop = OptionMenu(p1, p1_drop, "=", ">", "<", ">=", "<=").place(x=375, y=350)
p1_ipt4 = ttk.Entry(p1, width=20, textvariable=p1_Where_Ipt_Var2).place(x=300, y=400)


#Button for conducting the actual search (SELECT query) with the given inputs
p1_btn1 = ttk.Button(p1, text="Search").place(x=225, y=500)







#Page 2 layout
p2_lbl1 = ttk.Label(p2, textvariable=p2_Select_Lbl_Var).place(x=150,y=100)
p2_Select_Lbl_Var.set("Table to Update:")

p2_ipt1 = ttk.Entry(p2, width=20, textvariable=p2_Update_Ipt_Var).place(x=300, y=100)

#To put a 'Separate by Comma' label below this
p2_lbl2 = ttk.Label(p2, textvariable=p2_Set_Lbl_Var).place(x=150, y=200)
p2_Set_Lbl_Var.set("Column(s) to Change:")

p2_ipt2 = ttk.Entry(p2, width=20, textvariable=p2_Set_Ipt_Var).place(x=300, y=200)

p2_lbl3 = ttk.Label(p2, width=20, textvariable=p2_Where_Ipt_Var1).place(x=300, y=300)
p2_Where_Lbl_Var.set("Condition:")


p2_ipt3 = ttk.Entry(p2, width=20, textvariable=p2_Where_Ipt_Var1).place(x=300, y=300) 
p2_dropdown = OptionMenu(p2, p2_drop, "=", ">", "<", ">=", "<=").place(x=375, y=350)

p2_ipt4 = ttk.Entry(p2, width=20, textvariable=p2_Where_Ipt_Var2).place(x=300, y=400)

p2_btn1 = ttk.Button(p2, text="Update").place(x=225, y=500)




#Page 3 layout
#p3_Lbl1 = ttk.Label(p3, textvariable=p3_Alter_Lbl_Var).place(x=150,y=100)
#p3_Alter_Lbl_Var.set("Select Table:")

p3_ipt1 = ttk.OptionMenu(p3, p3_Alter_Ipt_Var, *p3_Alter_Ipt_Arr).place(x=250, y=100)
#p3_drop.set("Select Table")



#p3_lbl2 = ttk.Label(p3, textvariable=p3_Add_Lbl_Var).place(x=150, y=200)
#p3_Add_Lbl_Var.set("Column to add:")

p3_ipt2 = ttk.OptionMenu(p3, p3_Add_Ipt_Var, *p3_Add_Ipt_Arr).place(x=250, y=200)

#p3_lbl3 = ttk.Label(p3, textvariable=p3_Type_Lbl_Var).place(x=150, y=300)
#p3_Type_Lbl_Var.set("Data Type:")
p3_dropdown = OptionMenu(p3, p3_drop, *p3_drop_Arr).place(x=250, y=300)
#Will add int specifications for types like char and int
p3_btn1 = ttk.Button(p3, text="Add Column", command=addCol).place(x=250, y=400)
p3_addCol = ttk.Label(p3, textvariable = p3_addCol_Var).place(x=225, y=500)






#Page 4 layout
p4_Lbl1 = ttk.Label(p4, textvariable=p4_Delete_Lbl_Var).place(x=150,y=100)
p4_Delete_Lbl_Var.set("Table to Delete From:")

p4_ipt1 = ttk.Entry(p4, width=20, textvariable=p4_Delete_Ipt_Var).place(x=300,y=100)

p4_Lbl2 = ttk.Label(p4, textvariable=p4_Delete_Lbl_Var2).place(x=150,y=200)
p4_Delete_Lbl_Var2.set("Condition:")

p4_ipt2 = ttk.Entry(p4, width=20, textvariable=p4_Where_Ipt_Var).place(x=300, y=200)


p4_dropdown = OptionMenu(p4, p4_drop, "=", ">", "<", ">=", "<=").place(x=375, y=250)

p4_ipt3 = ttk.Entry(p4, width=20, textvariable=p4_Where_Ipt_Var2).place(x=300, y=300)

p4_btn1 = ttk.Button(p4, text="Delete").place(x=225, y=300)





main.pack()




#Additional actions


#Draw to Screen
root.mainloop()

