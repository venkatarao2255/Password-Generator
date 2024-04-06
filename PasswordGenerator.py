import random
import string
from tkinter import Tk, Label, Entry, IntVar, StringVar, OptionMenu, Button, Checkbutton

def generate_password():
    """Generates a random password based on user selections."""
    length = password_length.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    char_set = ""
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_lowercase:
        char_set += string.ascii_lowercase
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation

    if not char_set:
        password_entry.delete(0, 'end')
        password_entry.insert(0, "Please select at least one character type.")
        return

    password = ''.join(random.sample(char_set, length))
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)


root = Tk()
root.title("Password Generator")
root.geometry("400x300")  


password_length_label = Label(root, text="Password Length:")
password_length_label.grid(row=0, column=0, padx=10, pady=10)  
password_length = IntVar(root, value=12)  
password_length_entry = Entry(root, textvariable=password_length, width=5)
password_length_entry.grid(row=0, column=1, padx=10, pady=10)


uppercase_var = IntVar(root)
lowercase_var = IntVar(root)
numbers_var = IntVar(root)
symbols_var = IntVar(root)

uppercase_checkbox = Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=10) 
lowercase_checkbox = Checkbutton(root, text="Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.grid(row=2, column=0, padx=10, pady=10)
numbers_checkbox = Checkbutton(root, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=3, column=0, padx=10, pady=10) 
symbols_checkbox = Checkbutton(root, text="Symbols", variable=symbols_var)
symbols_checkbox.grid(row=4, column=0, padx=10, pady=10)  

password_entry = Entry(root, width=30)
password_entry.grid(row=5, columnspan=2, padx=10, pady=10)  


generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=6, column=0, padx=10, pady=10)  
close_button = Button(root, text="Close", command=root.destroy)  
close_button.grid(row=6, column=1, padx=10, pady=10)  


root.mainloop()
