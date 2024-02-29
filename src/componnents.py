import tkinter as tk

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

    # I Expect this method to be used by a button 
    # to mutate the value in a class and to exit the window
    # it should be used by go_back()
    def on_button_click_and_close(self, button_value):
        self.choice = button_value
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

        def on_enter(e):
            button.config(cursor="hand2", bg=self.button_bg_color, fg='white')

       # Calculate available height for buttons
        available_height = self.screen_height // 2

        # Calculate button height based on available height
        button_height = available_height // 4


        opts = ["Search", "Edit", "Add", "Delete"]
        for i, name in enumerate(opts):
            button = tk.Button(button_frame, text=name,
                command=lambda i=i: self.on_button_click_and_close(i+1), width=20)
            button.bind("<Enter>", on_enter)
            button.config(bg=self.button_bg_color, fg='white')

            button.pack(pady=button_height // 8,
            padx=400, anchor="center", expand=True, fill="both")


        # Calculate available height for buttons
        available_height = self.screen_height // 2

        # Calculate button height based on available height
        button_height = available_height // 4

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

        def on_enter(e):
            button.config(cursor="hand2", bg=self.button_bg_color, fg='white')

        addon = self.choice / 10
        # Create buttons and add them to the frame in a grid layout
        for i, label in enumerate(buttons):
            button = tk.Button(button_frame, text=label,
                command=lambda i=i: self.on_button_click_and_close(i + 1 + addon),
                width=button_width, height=button_height)
            button.bind("<Enter>", on_enter)
            button.config(bg=self.button_bg_color, fg='white')


            button.grid(row=i // num_columns, column=i % num_columns,
                padx=40, pady=50)
    
        # Center the button grid in the frame
        for c in range(num_columns):
            button_frame.grid_columnconfigure(c, weight=1)
        for r in range(num_rows):
            button_frame.grid_rowconfigure(r, weight=1)
    
        self.root.update_idletasks()  # Update the GUI to reflect changes


    # I Expect this to be part of our OOP method
    # and I want it to create a frame where all the other 
    # stuff that is going to be updated going to be placed
    # WE MAY CHANGE THIS IDEA AND METHOD IT'S NOT CONCREATE
    def title_table_name(self, title):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
    
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        frame.configure(bg=self.bg_color)
    
        label = tk.Label(frame, text=title)  # Add label to the frame, not root window
        label.pack()
    
        return frame


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


