# 1. have a in class self.frame going on
# 2. have a button that will use a self.frame 
#   and call a "create method" or use a lambda func instead
# 3. to have a "create method" that will 
#   do the seld.func_name or have the lambda for that instead

import tkinter as tk

class DropdownExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Dropdown Menu Example")

        # Initial options for the dropdown menu
        self.options = ["Option 1", "Option 2", "Option 3"]

        # Create a frame to hold the dropdowns and button
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)



    def create_dropdown(self):
        # Variable to store the selected option
        selected_option = tk.StringVar()
        selected_option.set(self.options[0])  # Set the default selected option

        # Create the dropdown menu
        dropdown_menu = tk.OptionMenu(self.frame, selected_option, *self.options)
        dropdown_menu.pack(pady=5)

    def add_more_button(self):
        add_more_button = tk.Button(self.frame, text="Add More", command=lambda: self.create_dropdown())
        add_more_button.pack(pady=10)

    def add_more_dropdown(self):
        # Add a new dropdown menu
        self.create_dropdown()

def main():
    root = tk.Tk()
    app = DropdownExample(root)
    app.add_more_button()
    app.create_dropdown()
    root.mainloop()

if __name__ == "__main__":
    main()

