from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3



con = sqlite3.connect("chinook.db")
cur = con.cursor()

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
	p3_addCol_Var.set("")
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

	
	
def p1SelectTable(self):

#Function for changing pages upon selecting a table
#Will take table as input and display it at top of page
#Upon clicking any table, it will change to the columns page
	p1.forget()
	p1a.pack()
	p1a_table.set(self)

	#loadMenu = cur.execute("SELECT * FROM " + p1a_table.get() + " WHERE 1=0")

	#p1a_list = [i[0] for i in loadMenu.fetchall()]

	#for row in loadMenu.fetchall():
	#	p1a_list.append(str(row))
	p1a_list = ['Select Table']

	if(p1a_table.get().lower() == 'customers'):
		p1a_list = p1a_cols_t1
	
	if(p1a_table.get().lower() == 'employees'):
		p1a_list = p1a_cols_t2

	if(p1a_table.get().lower() == 'albums'):
		p1a_list = p1a_cols_t3

	if(p1a_table.get().lower() == 'tracks'):
		p1a_list = p1a_cols_t4		


		
	#optionsList = tk.StringVar()
	#optionsList.set(p1a_list[0])

	p1a_col = ttk.OptionMenu(p1a, p1a_drop, *p1a_list).place(x=100, y=300)


def showP1():

	p1a.forget()
	p1.pack()

def showP1a():

	p1b.forget()
	p1a.pack()	


def search():

	p1a.forget()
	p1b.pack()
	x = 0
	y = 25
	data = cur.execute("SELECT " +p1a_drop.get()+ " FROM " + p1a_table.get()) 
	getData = data.fetchall()
	for row in getData:
		tk.Label(p1b, text=str(row)).place(x=x,y=y)
		x += 100
		
		if(x+75 >= 1000):
			x = 25
			y += 50

	#con.commit()
	#p1a_lbl2_var.set(data) 
	#for row in data:
	#	print(row)
	#p1a.forget()
	#p1b_lbl_var.set(data.fetchall())








#For root
root = tk.Tk()

root.title("Database GUI")
root.geometry("1000x1000")
#root.resizable(0,0)







#Main page
main = Frame(root, height = 600, width = 600)

#Other pages




#PAGE 1
##################################################


#Pages
#Main page for p1 (Tables)
p1 = Frame(root, height = 600, width = 600)
#Sub page for p1 (Columns)
p1a = Frame(root, height=600, width = 600)

p1b = Frame(root, height = 1000, width = 1000)

#Background colour


#Button on main
p1Btn = tk.Button(main, text="Search", font=("Arial",15), height=3, width=20, command= lambda: changePage(p1)).place(x=200, y=50)

#Back button to get to main
backBtn1 = tk.Button(p1, text="Back", command=showMain).place(x =25, y=550)

#Choose from table label
p1_lbl1 = tk.Label(p1, text="Choose a Table to Search From", font=("Arial",25)).place(x=125, y=100)


#Dummies
p1_tbl1_var = StringVar()
p1_tbl2_var = StringVar()
p1_tbl3_var = StringVar()
p1_tbl4_var = StringVar()

p1_tbl1 = tk.Button(p1, textvariable=p1_tbl1_var, font=("Arial", 15),height=3, width=20, command= lambda: p1SelectTable("Customers")).place(x=50, y=200)
p1_tbl1_var.set("Customers")

p1_tbl2 = tk.Button(p1, textvariable=p1_tbl2_var, font=("Arial", 15),height=3, width=20, command= lambda: p1SelectTable("Employees")).place(x=350, y=200)
p1_tbl2_var.set("Employees")

p1_tbl3 = tk.Button(p1, textvariable=p1_tbl3_var, font=("Arial", 15),height=3, width=20, command= lambda: p1SelectTable("Albums")).place(x=50, y=300)
p1_tbl3_var.set("Albums")

p1_tbl4 = tk.Button(p1, textvariable=p1_tbl4_var, font=("Arial", 15),height=3, width=20, command= lambda: p1SelectTable("Tracks")).place(x=350, y=300) 
p1_tbl4_var.set("Tracks")






##################################################
#Page 1 Sub Page

p1a_table = StringVar()

p1a_drop = StringVar()

p1a_cols_t1 = ['CustomerId', 'FirstName', 'LastName', 'Company', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email', 'SupportRepId']
p1a_cols_t2 = ['EmployeeId', 'LastName', 'FirstName', 'Title', 'ReportsTo', 'BirthDate', 'HireDate', 'Address']
p1a_cols_t3 = ['AlbumId', 'Title', 'ArtistId']
p1a_cols_t4 = ['TrackId', 'Name', 'AlbumId', 'MediaTypeId', 'GenreId', 'Composer', 'Milliseconds', 'Bytes', 'UnitPrice']

p1a_lbl1 = tk.Label(p1a, textvariable=p1a_table, font=("Arial",25)).place(x=250, y=100)


backBtn2 = tk.Button(p1a, text="Back", command=showP1).place(x =25, y=550) 




#p1a_col = ttk.OptionMenu(p1a, p1a_drop, *p1a_list).place(x=100, y=300)



p1a_confirm = tk.Button(p1a, text="Confirm", command=search).place(x=100, y=550)

#For column, we will put every name of column in an array
#And alter the option menu to use the respective array depending on the selected table
#For example, selecting table 1 will change the OptionMenu array to Table 1's columns

##################################################
#Page 1 Sub Page 2 

#p1b_lbl_var = StringVar()
#p1b_lbl = tk.Label(p1b, width=300, textvariable=p1b_lbl_var).place(x=100, y=200)
#p1b_lbl_var.set("Results")

backBtn3 = tk.Button(p1b, text="Back", command=showP1a).place(x =25, y=650) 




##################################################






#PAGE 2
##################################################
p2 = Frame(root, height = 600, width = 600)
p2['bg'] = "#d6d0d0"


p2_Select_Lbl_Var = StringVar()
p2_Set_Lbl_Var = StringVar()
p2_Where_Lbl_Var = StringVar()


p2_Update_Ipt_Var = StringVar()
p2_Set_Ipt_Var = StringVar()
p2_Where_Ipt_Var1 = StringVar()
p2_Where_Ipt_Var2 = IntVar()
p2_drop = StringVar()




p2Btn = tk.Button(main, text="Edit", font=("Arial",15), height=3, width=20, command= lambda: changePage(p2)).place(x = 200, y = 200)



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



##################################################











#PAGE 3
##################################################


p3 = Frame(root, height = 600, width = 600)
p3['bg'] = "#d6d0d0"

p3Btn = tk.Button(main, text="Add", font=("Arial", 15), height=3, width=20).place(x = 200, y = 350)

p3_Alter_Lbl_Var = StringVar()
p3_Add_Lbl_Var = StringVar()
p3_Type_Lbl_Var = StringVar()

p3_Alter_Ipt_Var = StringVar()
p3_Alter_Ipt_Arr = ["Select Table", "Table1", "Table2", "Table3"]

p3_Add_Ipt_Var = StringVar()
p3_Add_Ipt_Arr = ["Select Column", "Column1", "Column2", "Column3", "Column4"]


p3_drop = StringVar()
p3_tbl_drop = StringVar()
p3_drop_Arr = ["Select Type", "Char", "Int", "Decimal", "Longtext", "Date", "Varchar", "Autonumber", "Shorttext", "Number"]

p3_addCol_Var = StringVar()


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




##################################################










#PAGE 4
##################################################

p4 = Frame(root, height = 600, width = 600)

p4Btn = tk.Button(main, text="Delete", font=("Arial", 15), height=3, width=20, command= lambda: changePage(p4)).place(x = 200, y = 500)


p4_Delete_Lbl_Var = StringVar()
p4_Delete_Lbl_Var2 = StringVar()


p4_Delete_Ipt_Var = StringVar()
p4_Where_Ipt_Var = StringVar()
p4_Where_Ipt_Var2 = IntVar() # Can also be String, applies to all Condition Entries



p4_drop = StringVar()

p4_Lbl1 = ttk.Label(p4, textvariable=p4_Delete_Lbl_Var).place(x=150,y=100)
p4_Delete_Lbl_Var.set("Table to Delete From:")

p4_ipt1 = ttk.Entry(p4, width=20, textvariable=p4_Delete_Ipt_Var).place(x=300,y=100)

p4_Lbl2 = ttk.Label(p4, textvariable=p4_Delete_Lbl_Var2).place(x=150,y=200)
p4_Delete_Lbl_Var2.set("Condition:")

p4_ipt2 = ttk.Entry(p4, width=20, textvariable=p4_Where_Ipt_Var).place(x=300, y=200)


p4_dropdown = OptionMenu(p4, p4_drop, "=", ">", "<", ">=", "<=").place(x=375, y=250)

p4_ipt3 = ttk.Entry(p4, width=20, textvariable=p4_Where_Ipt_Var2).place(x=300, y=300)

p4_btn1 = ttk.Button(p4, text="Delete").place(x=225, y=300)



##################################################




























main.pack()




#Additional actions


#Draw to Screen
root.mainloop()

