import random
import string

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
    
    if len(website_entry) == 0:
        messagebox.showwarning("Warning", "The website text field is empty.")
        
    elif len(password_entry) == 0:
        messagebox.showerror("Error", "The password text field is empty.")
    
    else:
        is_okay = messagebox.askokcancel(
            title = website_entry, 
            message = f"These are the details entered: \nEmail: {email_username_entry} \nPassword: {password_entry} \nIs it okay to save?"
            )
        
        if is_okay:
            with open("data.txt", "a") as data:
                data.write(f"\n{website_entry}, {email_username_entry}, {password_entry}")
                
        website_text.delete(0, END)
        password_text.delete(0, END)

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
    row = 2
    )

letters_quantity_label.grid(
    column = 0, 
    row = 3
    )
digits_quantity_label.grid(
    column = 0, 
    row = 4
    )
symbols_quantity_label.grid(
    column = 0, 
    row = 5
    )

password_label.grid(
    column = 0,
    row = 7
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

website_text.grid(
    column = 1,
    row = 1,
    columnspan = 2
    )

email_username_text.grid(
    column = 1,
    row = 2,
    columnspan = 2
    )
 
letters_quantity.grid(
    column = 1,
    row = 3
    )

symbols_quantity.grid(
    column = 1, 
    row = 4
    )

digits_quantity.grid(
    column = 1, 
    row = 5
    )

password_text.grid(
    column = 1,
    row = 7,
    )

# Buttons
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
generate_password_button.grid(
    column = 1,
    row = 6,
    columnspan = 2
    )

add_password.grid(
    column = 1,
    row = 8,
    columnspan = 2
    )

window.mainloop()