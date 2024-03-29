#1. clear the screen
#2. make UI frame  
#3. have a loop where you create and than pack or grid 
import tkinter as tk
from src import bookingdb as db

# I Expect this Class to contain information that is need for the main loop
# all methods that create a new window should create a frame for it's content
# this class should than be used in a main loop to create an object to interact with
# to get values, call OOP and prosidural method etc
class ScreenManager:
    # I Expect here to be a UI looks related varibles and 
    # methods that are going to be used by OOP methods
    def __init__(self, root):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.choice = 0
        self.show_times = 1
        self.bg_color="#141A20"
        self.button_bg_color="#223C5B"
        self.back_bg="#DF1E34"

#        self.row = 2 #for spacing. Will be fixed at end
#        self.execute = 0 #separate choice for execute function in bookingdb.py
        self.drop_col_val = [] #to hold StringVars for each OptionMenu
        self.drop_col_con_val = [] #to hold StringVars for each OptionMenu
        self.ent_oper_val = [] #to hold the conditions/values for each OptionMenu
        self.ent_val = [] #to hold the conditions/values for each OptionMenu
        self.ent_set = [] #setting values for edit
        self.display_vals = []
        #self.command_count = 0 
        #self.condition_count = 0
        self.current = None

        self.row =1
        self.options = []
        self.operators = ['=', '>', '<', '>=', '<=', "!="]
        self.leftFrame = tk.Frame(self.root)
        self.rightFrame = tk.Frame(self.root)

 

    # I Expect this method to be used by a button 
    # to mutate the value in a class and to exit the window
    # it should be used by go_back()
    def on_button_click_and_close(self, button_value):
        self.choice = button_value

        #call execute

        # WHYYYYY
#        if(len(self.command) > 0):
#            db.execute(self.execute, self.current, self.command[0].get(), self.condition[0])
#
        self.root.quit()

       


    # I Expect this method to display options centered 
    # on the screen and Expect it to return a value that will 
    # represent the choice of action to do, like Edit, Delete etc
    def main_screen(self):
       # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")
        button_frame.configure(bg=self.bg_color)


       # Calculate available height for buttons
        available_height = self.screen_height // 2

        # Calculate button height based on available height
        button_height = available_height // 4


        opts = ["Search", "Edit", "Add", "Delete"]
        for i, name in enumerate(opts):
            button = tk.Button(button_frame, text=name,
                command=lambda i=i: self.on_button_click_and_close(i+1), width=20)

            button.pack(pady=button_height // 8,
            padx=400, anchor="center", expand=True, fill="both")


        self.root.update_idletasks()  # Update the GUI to reflect changes


    # I Expect this method to get the databaces tables and display them in the 
    # grid by 3 that will change the size depending on the ammount of inputs
    # This should return a value that is equal to a number of a current choice and
    # the bumber of previous choice written as "current_num.previous.num"
    # it is implemented this way to avoid problems with main loop
    def grid_table_chooser(self, buttons):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")
        button_frame.configure(bg=self.bg_color)
    
        # Calculate number of rows and columns for the grid
        num_buttons = len(buttons)
        num_columns = min(num_buttons, 3)
        num_rows = (num_buttons + num_columns - 1) // num_columns
    
        # Calculate button size similar to create_buttons method
        button_height = self.screen_height - 1000 // (2 * num_rows)
        button_width = self.screen_width - 1000 // (2 * num_columns)

        addon = self.choice / 10
        # Create buttons and add them to the frame in a grid layout
        for i, label in enumerate(buttons):
            button = tk.Button(button_frame, text=label,
                command=lambda i=i: self.on_button_click_and_close(i + 1 + addon),
                width=button_width, height=button_height)

            button.grid(row=i // num_columns, column=i % num_columns,
                padx=40, pady=50)
    
        # ASK GPT
        # Center the button grid in the frame
        for c in range(num_columns):
            button_frame.grid_columnconfigure(c, weight=1)
        for r in range(num_rows):
            button_frame.grid_rowconfigure(r, weight=1)
    
        self.root.update_idletasks()  # Update the GUI to reflect changes




    # I Expect this to be used to display a button that is always going to be 
    # in the left down corner and it should mutate the choice value
    # the new choice value will be read by main loop to determine what to display
    # because of this trick the illusion of "going back" is created 
    def go_back(self, return_this):
        # Create the "back" button and add it to the frame
        button = tk.Button(self.root, text="Back", command=lambda: self.on_button_click_and_close(return_this))
        button.config(bg=self.back_bg)
        button.place(relx=0.02, rely=0.95)  # Place the button at 2% from the left and 95% from the top of the window
        

        self.root.update_idletasks()  # Update the GUI to reflect changes


    # I Expect this to be used as a confirm button to be used to execute SQL
    # commands when data is inserted into the input fields 
    # For everything except Search, it should return you to the main screen
    # For Search, it will take you to a new page   
    def confirm(self, values_input, return_this):
        #change command so it calls a method that executes the command, then calls on_button_click_and_close
        if (return_this > 0):
            button = tk.Button(self.root, text="Confirm", command=lambda: self.confirm_exec(values_input, return_this))
            button.place(relx=0.45, rely=0.80)
        else: 
            pass

    def confirm_exec(self, values_input, return_this):
        for i in values_input:
            self.get_values(i)
        self.on_button_click_and_close(return_this)
        
    def clear_all_data(self):
        self.drop_col_val = [] #to hold StringVars for each OptionMenu
        self.drop_col_con_val = [] #to hold StringVars for each OptionMenu
        self.ent_oper_val = [] #to hold the conditions/values for each OptionMenu
        self.ent_val = [] #to hold the conditions/values for each OptionMenu
        self.ent_set = []
        self.row = 1


    def title_table_name(self, title):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
    
        frame = tk.Frame(self.root)
        frame.grid(sticky="ew")
        frame.configure(bg=self.bg_color)
    
        label = tk.Label(frame, text=title)  # Add label to the frame, not root window
        label.grid(column=0, row=0, columnspan=2, sticky="nsew")
    
        return frame

    def create_left_frame(self, mother_frame):
        frame = tk.Frame(mother_frame)
        frame.configure(bg=self.bg_color)

        self.leftFrame = frame
        self.leftFrame.grid(row = 1, column = 0, sticky="nsew",  padx=100, pady=5)

    def create_right_frame(self, mother_frame):
        frame = tk.Frame(mother_frame)
        frame.configure(bg=self.bg_color)

        self.rightFrame = frame
        self.rightFrame.grid(row = 1, column = 1,  sticky="nsew", padx=100, pady=5)


    def create_dropdown_column(self, frame):
   
        drop_choise= tk.StringVar()
        drop_choise.set(self.options[0])

        dropdown = tk.OptionMenu(frame, drop_choise, *self.options)  
        dropdown.grid(row=self.row,column=1)

        if(str(self.choice).endswith('2')):
            set_sign = tk.Label(frame, text='=')
            set_sign.grid(row=self.row, column=2, padx=10)
            input_val = tk.Entry(frame, width=15)
            input_val.grid(row=self.row,column=3, padx=10) 

            self.ent_set.append(input_val)



        #dropdown.grid(row=1, column=2)
        #self.command.insert(self.count,default)
        self.drop_col_val.append(drop_choise)
        self.row += self.row



    def create_entry_condition(self, frame):
        

        if not(str(self.choice).endswith('3')):
            oper_choise = tk.StringVar()
            oper_choise.set(self.operators[0])

            sign_menu = tk.OptionMenu(frame, oper_choise, *self.operators)
            sign_menu.grid(row=self.row, column=2, padx=10)

            
            self.ent_oper_val.append(oper_choise)


 
        drop_choise = tk.StringVar()
        drop_choise.set(self.options[0])


        dropdown_col = tk.OptionMenu(frame, drop_choise, *self.options)  
        dropdown_col.grid(row=self.row, column=1, padx=10)        

        input_val = tk.Entry(frame, width=15)
        input_val.grid(row=self.row, column=3, padx=10) 
   
        
        self.ent_val.append(input_val)

        self.drop_col_con_val.append(drop_choise)

        self.row += self.row



    def add_element(self, frame, element):
        add_el = tk.Button(frame, text="+", command=lambda: element(frame) )
        add_el.grid(columnspan=3)



    def get_values(self, values_input):
        values = []
        for var in values_input:
            values.append(var.get())

        print(values)





    def display_results(self, frame, columns_to_display, fields):

        i = 3
        j = 0 
        temp = 0

        print(fields)

        for column in columns_to_display:
            show_column = tk.Label(frame, text=column.get())
            show_column.grid(row=i, column=j, pady=20, padx=10)
            j+=1

        


        j = 0
        i+=len(columns_to_display)


        for value in fields:
            if(j == len(columns_to_display)):
                j = 0
                i+=len(columns_to_display)


            show_field = tk.Label(frame, text=value)
            show_field.grid(row=i, column=j)
                

                
            j+=1






        
  








