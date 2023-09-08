import random
import string
import json

import pyperclip

from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters

    digits = string.digits

    symbols = string.punctuation

    if len(letters_quantity.get()) == 0:
        letters_count = 8
    
    else:
        letters_count = int(letters_quantity.get())
        
    if len(symbols_quantity.get()) == 0:
        symbols_count = 8
    
    else:
        symbols_count = int(symbols_quantity.get())
    
    if len(digits_quantity.get()) == 0:
        digit_count = 8
    
    else:
        digit_count = int(digits_quantity.get())
    
    # Choosing the number of letters
    letter_list = [letters[random.randint(0, len(letters) - 1)] for letter in range(0, letters_count)]

    symbol_list = [symbols[random.randint(0, len(symbols) - 1)] for symbol in range(0, symbols_count)]
        
    digit_list = [digits[random.randint(0, len(digits) - 1)] for digit in range(0, digit_count)]

    password_list = letter_list + symbol_list + digit_list
    
    random.shuffle(password_list)

    true_secret_word = "".join(password_list)
    
    password_text.insert(0, true_secret_word)
    
    pyperclip.copy(true_secret_word)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website_entry = website_text.get()
    email_username_entry = email_username_text.get()
    password_entry = password_text.get()
    new_data = {
        website_entry: {
            "email": email_username_entry,
            "password": password_entry
    }}
    
    if len(website_entry) == 0:
        messagebox.showwarning(title = "Warning", message = "The website text field is empty.")
        
    elif len(password_entry) == 0:
        messagebox.showerror(title = "Error", message = "The password text field is empty.")
    
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading in old data
                data = json.load(data_file)
                
        
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving updated data to file
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
                
            with open("data.json", mode = "w") as data_file:
                json.dump(data, data_file, indent = 4)
        
        finally:    
            website_text.delete(0, END)
            password_text.delete(0, END)
            
# ---------------------------- SEARCH ENTRY ------------------------------- #
def search_entry():
    website_name_entry = website_text.get().title()
    
    if len(website_name_entry) == 0:
        messagebox.showerror(title = "Error", message = "The website name field is empty")
    
    else:
        try:
            with open("data.json", mode = "r") as data_file:
                contents = json.load(data_file)
            
        except FileNotFoundError:
            messagebox.showwarning(title = "Warning", message= "Create & save a password first.")
        
        else:
            try:
                website_password_contents = contents[website_name_entry]
            
            except KeyError:
                messagebox.showerror(title = "Error", message = f"No details for {website_name_entry} were found.")
            
            else:
                email = website_password_contents['email']
                password = website_password_contents['password']
                messagebox.showinfo(
                    title = "Info", 
                    message = f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(
    padx = 50,
    pady = 50
    )

canvas = Canvas(
    width = 200, 
    height = 200    
    )

lock_image = PhotoImage(file = "logo.png")

canvas.create_image(
    100,
    100,
    image = lock_image
    )
canvas.grid(
    column = 0,
    row = 0,
    columnspan = 2
    )

# Labels
website_label = Label(text = "Website:")
email_username_label = Label(text = "Email/Username:")
password_label = Label(text = "Password:")
letters_quantity_label = Label(text = "Number of Letters:")
digits_quantity_label = Label(text = "Number of Digits:")
symbols_quantity_label = Label(text = "Number of Symbols:")

website_label.grid(
    column = 0,
    row = 1
    )

email_username_label.grid(
    column = 0,
    row = 3
    )

letters_quantity_label.grid(
    column = 0, 
    row = 4
    )
digits_quantity_label.grid(
    column = 0, 
    row = 5
    )
symbols_quantity_label.grid(
    column = 0, 
    row = 6
    )

password_label.grid(
    column = 0,
    row = 8
    )

# Entries
website_text = Entry(width = 35)
website_text.focus()
email_username_text = Entry(width = 35)
email_username_text.insert(
    0, 
    "mr.anderson@gmail.com"
    )
letters_quantity = Entry(width = 35)
symbols_quantity = Entry(width = 35)
digits_quantity = Entry(width = 35)
password_text = Entry(width = 35)

# Entry Positions
website_text.grid(
    column = 1,
    row = 1,
    columnspan = 2
    )

email_username_text.grid(
    column = 1,
    row = 3,
    columnspan = 2
    )
 
letters_quantity.grid(
    column = 1,
    row = 4
    )

symbols_quantity.grid(
    column = 1, 
    row = 5
    )

digits_quantity.grid(
    column = 1, 
    row = 6
    )

password_text.grid(
    column = 1,
    row = 8,
    )

# Buttons
search_button = Button(
    text = "Search",
    width = 30,
    command = search_entry
    )

generate_password_button = Button(
    text = "Generate Password",
    width = 30,
    command = generate_password
    )

add_password = Button(
    text = "Add Password",
    width = 30,
    command = save_entry
    )

# Button Positions
search_button.grid(
    column = 1,
    row = 2,
    columnspan = 2
    )

generate_password_button.grid(
    column = 1,
    row = 7,
    columnspan = 2
    )

add_password.grid(
    column = 1,
    row = 9,
    columnspan = 2
    )

window.mainloop()