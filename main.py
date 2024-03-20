
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

    display_results = []
    
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
            screen_manager.clear_arrays()
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
        # I Expect this part to use OOP method to update it's contence
        # and than be terminated by "canfirm" method that is goint to be prosidual
        confirm_temp =0
        if (etc.ends_with(screen_manager.choice, 1)):
            screen_manager.clear_arrays()
            title_frame = screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            title_frame.pack(side="top", pady=65)
            mother_frame = tk.Frame(root)
            mother_frame.pack()

            # <><><><><><><><><><><><>
            #screen_manager.execute = 1
            #            screen_manager.conditions()
            options_temp = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            options_temp.append('*')
            screen_manager.options = options_temp


            screen_manager.create_left_frame(mother_frame)
            screen_manager.add_element(screen_manager.leftFrame, screen_manager.create_dropdown_column)
            screen_manager.create_dropdown_column(screen_manager.leftFrame)

            screen_manager.create_right_frame(mother_frame)
            screen_manager.add_element(screen_manager.rightFrame, screen_manager.create_entry_condition)
            screen_manager.create_entry_condition(screen_manager.rightFrame)

            screen_manager.current = tables[int(screen_manager.choice)-1]
            screen_manager.go_back(1)
            arr = [screen_manager.drop_col_val, screen_manager.drop_col_con_val, screen_manager.ent_oper_val, screen_manager.ent_val]
            screen_manager.confirm(arr, 11)


            #if(screen_manager.confirm == True):

                #db.execute(screen_manager.choice, tables[int(screen_manager.choice)-1])

            root.update()

            # I used a temp choice to store current choice for future go_back()
            # have it before mainloop() because otherwise it would be assigned to new choice 
            confirm_temp = screen_manager.choice



            print("temp choice:", confirm_temp)
 
            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (screen_manager.choice == 11):
            display_results = db.db_search(screen_manager.current, screen_manager.drop_col_val, screen_manager.drop_col_con_val, screen_manager.ent_oper_val, screen_manager.ent_val)
            screen_manager.clear_arrays()
            screen_manager.clear_all_data()
            title_frame = screen_manager.title_table_name('Results') 
            title_frame.pack(side="top", pady=65)
            screen_manager.go_back(confirm_temp)            
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
            print("New Choice that we store for go back:", confirm_temp)
#<><><><><><><><><><><><><><><> Edit option <><><><><><><><><><><><><><><>
        if (screen_manager.choice == 2):
            db.db_edit(screen_manager.current, screen_manager.drop_col_val, screen_manager.ent_set, screen_manager.drop_col_con_val, screen_manager.ent_oper_val, screen_manager.ent_val)
            screen_manager.clear_arrays()
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)

        if (etc.ends_with(screen_manager.choice, 2)):
            title_frame = screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            title_frame.pack(side="top", pady=65)
            mother_frame = tk.Frame(root)
            mother_frame.pack()


            options_temp = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            #options_temp.append('*')
            screen_manager.options = options_temp


            screen_manager.create_left_frame(mother_frame)
            screen_manager.add_element(screen_manager.leftFrame, screen_manager.create_dropdown_column)
            screen_manager.create_dropdown_column(screen_manager.leftFrame)

            screen_manager.create_right_frame(mother_frame)
            screen_manager.add_element(screen_manager.rightFrame, screen_manager.create_entry_condition)
            screen_manager.create_entry_condition(screen_manager.rightFrame)

            screen_manager.current = tables[int(screen_manager.choice)-1]
            screen_manager.go_back(1)
            arr = [screen_manager.drop_col_val, screen_manager.ent_set, screen_manager.drop_col_con_val, screen_manager.ent_oper_val, screen_manager.ent_val]
            screen_manager.confirm(arr, 2)


            
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)

#<><><><><><><><><><><><><><><> Add option <><><><><><><><><><><><><><><>
        
        

        if (screen_manager.choice == 3):
            db.db_add(screen_manager.drop_col_con_val, screen_manager.ent_val, screen_manager.current)
            screen_manager.clear_arrays()
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (etc.ends_with(screen_manager.choice, 3)):
            title_frame = screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            title_frame.pack(side="top", pady=65)

            mother_frame = tk.Frame(root)
            mother_frame.pack()
            
            options_temp = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            #options_temp.append('*')
            screen_manager.options = options_temp

            screen_manager.create_right_frame(mother_frame)
            screen_manager.add_element(screen_manager.rightFrame, screen_manager.create_entry_condition)
            screen_manager.create_entry_condition(screen_manager.rightFrame)
 
            
            screen_manager.current = tables[int(screen_manager.choice)-1]
            screen_manager.go_back(3)
            arr = [screen_manager.drop_col_con_val, screen_manager.ent_val]
            screen_manager.confirm(arr, 3)
            
            #db.db_add(screen_manager.drop_col_con_val, screen_manager.ent_val, screen_manager.current)



                       
            



            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)

#<><><><><><><><><><><><><><><> Delete option <><><><><><><><><><><><><><><>
 
        if (screen_manager.choice == 4):
            db.db_delete(screen_manager.drop_col_con_val, screen_manager.ent_val, screen_manager.ent_oper_val, screen_manager.current)
            screen_manager.clear_arrays()

            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            db.db_delete(screen_manager.drop_col_con_val, screen_manager.ent_val, screen_manager.ent_oper_val, screen_manager.current)
            screen_manager.clear_arrays()
            root.update()


            root.mainloop()
            print("Choice:", screen_manager.choice)
        if (etc.ends_with(screen_manager.choice, 4)):
            title_frame = screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
            title_frame.pack(side="top", pady=65)

            mother_frame = tk.Frame(root)
            mother_frame.pack()
 
            screen_manager.go_back(4)
            #screen_manager.confirm(0)
            #screen_manager.conditions()
            options_temp = [item[0] for item in db.db_get_columns(tables[int(screen_manager.choice)-1])]
            #options_temp.append('*')
            screen_manager.options = options_temp


            screen_manager.create_right_frame(mother_frame)
            screen_manager.add_element(screen_manager.rightFrame, screen_manager.create_entry_condition)
            screen_manager.create_entry_condition(screen_manager.rightFrame)

            screen_manager.current = tables[int(screen_manager.choice)-1]
            screen_manager.go_back(1)
            arr = [screen_manager.drop_col_con_val, screen_manager.ent_oper_val, screen_manager.ent_val]
            screen_manager.confirm(arr, 4)
           

            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)


   

     

        #screen_manager.choice = 0

    db.db_end()

if __name__ == "__main__":
    main()




