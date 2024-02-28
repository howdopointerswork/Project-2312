import tkinter as tk

class ScreenManager:
    def __init__(self, root):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.choice = 0
        self.show_times = 1
        self.bg_color="#141A20"
        self.button_bg_color="#223C5B"
        self.back_bg="#DF1E34"


    def on_button_click_and_close(self, button_value):
        self.choice = button_value
        self.root.quit()




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

    def display_selected_option(self):
        selected_option = self.selected_option.get()
        print(f"Selected Option: {selected_option}")
    def add_more(self, button_value):
        print("I am working")
        self.choice = button_value
        self.show_times = self.show_times + 1
        print("I added")
        self.root.quit()
    def dropdown_column_selector(self, options, frame, return_this):
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])  # Set the default selected option

        def on_enter(e):
            dropdown_menu.config(cursor="hand2", bg=self.button_bg_color, fg='white')

        # Create the dropdown menu
        dropdown_menu = tk.OptionMenu(frame, self.selected_option, *options)
        dropdown_menu.pack(pady=10)

        # Button to display the selected option
        display_button = tk.Button(frame, text="add more", command=lambda: self.add_more(return_this))
        display_button.pack(pady=10)

        # Calculate available height for buttons
        available_height = self.screen_height // 2

        # Calculate button height based on available height
        button_height = available_height // 4

        self.root.update_idletasks()  # Update the GUI to reflect changes



    def go_back(self, return_this):
        # Create the "back" button and add it to the frame
        button = tk.Button(self.root, text="Back", command=lambda: self.on_button_click_and_close(return_this))
        button.config(bg=self.back_bg)
        button.place(relx=0.02, rely=0.95)  # Place the button at 2% from the left and 95% from the top of the window
        
        self.root.update_idletasks()  # Update the GUI to reflect changes


