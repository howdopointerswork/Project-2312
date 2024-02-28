
import tkinter as tk
from src import componnents as com
from src import bookingdb as db
from src import etc as etc

def main():
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.config(bg="#141A20")
    

    screen_manager = com.ScreenManager(root)

    tables = db.db_get_tables()
    # main loop
    while screen_manager.choice != -1:
        if (screen_manager.choice == 0):
            screen_manager.main_screen()
            screen_manager.go_back(-1)
            screen_manager.show_times = 1
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
     
        if (screen_manager.choice == 1):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)

            i = 0
            if (etc.has_decimal_part(screen_manager.choice)):
                table_choice = tables[int(screen_manager.choice)-1]
                frame = screen_manager.title_table_name(table_choice)
                # find a way to change stuff without without restarting stuff from stratch
                while i < screen_manager.show_times:
                    screen_manager.dropdown_column_selector(db.db_get_columns(table_choice), frame, 1) 
                    print(screen_manager.show_times)
                    print("this is I ?", (i,))
                    i += 1

                screen_manager.go_back(1)
                root.update()

                root.mainloop()
                print("Choice:", screen_manager.choice)
        if (screen_manager.choice == 2):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
            if (etc.has_decimal_part(screen_manager.choice)):
                screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
                screen_manager.go_back(2)
                root.update()

                root.mainloop()
                print("Choice:", screen_manager.choice)
        if (screen_manager.choice == 3):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
            if (etc.has_decimal_part(screen_manager.choice)):
                screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
                screen_manager.go_back(3)
                root.update()

                root.mainloop()
                print("Choice:", screen_manager.choice)
        if (screen_manager.choice == 4):
            screen_manager.grid_table_chooser(tables)
            screen_manager.go_back(0)
            root.update()

            root.mainloop()
            print("Choice:", screen_manager.choice)
            if (etc.has_decimal_part(screen_manager.choice)):
                screen_manager.title_table_name(tables[int(screen_manager.choice)-1])
                screen_manager.go_back(4)
                root.update()

                root.mainloop()
                print("Choice:", screen_manager.choice)



        #screen_manager.choice = 0

    db.db_end()

if __name__ == "__main__":
    main()

