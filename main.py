
import tkinter as tk
from src import componnents as com
from src import bookingdb as db
from src import etc as etc

# I Expect this main function in contain a an infinite loop that will contain methods 
# from screen_manager object, I expect this methods to return values so that in the main function
# they would be used to determine what to do next
# some methods are prosidual and some are OOP, refer to "./UI_Technical_plan.png"
def main():
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.config(bg="#141A20")
    

    screen_manager = com.ScreenManager(root)

    tables = db.db_get_tables()


    
    # main loop
    # I Expect to screen_manager.choice to be updated by go_back() 
    # and than the value that go_back() will return will be than used to determine 
    # what if condition to display
    while screen_manager.choice != -1:
#<><><><><><><><><><><><><><><> Main screen <><><><><><><><><><><><><><><>
        if (screen_manager.choice == 0):
            screen_manager.main_screen()
            screen_manager.go_back(-1)
            screen_manager.show_times = 1
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
    
#<><><><><><><><><><><><><><><> Search option <><><><><><><><><><><><><><><>
        if (screen_manager.choice == 1):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
        # I Expect this part to use OOP method to update it's contence
        # and than be terminated by "canfirm" method that is goint to be prosidual
        confirm_temp =0
        if (etc.ends_with(screen_manager.choice, 1)):
            screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            screen_manager.go_back(1)
            screen_manager.confirm(11)
            columns = [item[0] for item in db.db_get_columns(tables[int(confirm_temp)-1])]
            columns.append('*')
            screen_manager.columns(columns)
            #screen_manager.conditions()
            #screen_manager.plus_condition()

           # screen_manager.add_dropdown(columns)
            #screen_manager.add_condition()

            root.update()

            # I used a temp choice to store current choice for future go_back()
            # have it before mainloop() because otherwise it would be assigned to new choice 
            confirm_temp = screen_manager.choice
            print("temp choice:", confirm_temp)
 
            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (screen_manager.choice == 11):
            screen_manager.title_table_name('Results') 
            screen_manager.go_back(confirm_temp)            
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
            print("New Choice that we store for go back:", confirm_temp)
#<><><><><><><><><><><><><><><> Edit option <><><><><><><><><><><><><><><>
        if (screen_manager.choice == 2):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (etc.ends_with(screen_manager.choice, 2)):
            screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            screen_manager.go_back(2)
            screen_manager.confirm(0)
            columns = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            columns.append('*')
           # screen_manager.columns_conditions(columns)

            
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)

#<><><><><><><><><><><><><><><> Add option <><><><><><><><><><><><><><><>
        if (screen_manager.choice == 3):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (etc.ends_with(screen_manager.choice, 3)):
            screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            screen_manager.go_back(3)
            screen_manager.confirm(0)
            columns = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            columns.append('*')
          #  screen_manager.columns_conditions(columns)


            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)

#<><><><><><><><><><><><><><><> Delete option <><><><><><><><><><><><><><><>
        if (screen_manager.choice == 4):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (etc.ends_with(screen_manager.choice, 4)):
            screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            screen_manager.go_back(4)
            screen_manager.confirm(0)
            columns = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            columns.append('*')
           # screen_manager.columns_conditions(columns)
           

            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)


   

     

        #screen_manager.choice = 0

    db.db_end()

if __name__ == "__main__":
    main()



