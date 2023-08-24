from tkinter import *

FONT = ("Courier", 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
    column = 1,
    row = 0
)

# Labels
website_label = Label(text = "Website:")
email_username_label = Label(text = "Email/Username:")
password_label = Label(text = "Password:")

# Label Positions
website_label.grid(
    column = 0,
    row = 1
)

email_username_label.grid(
    column = 0,
    row = 2
)

password_label.grid(
    column = 0,
    row = 3
)

# Entries
website_text = Entry(width = 35)
email_username_text = Entry(width = 35)
password_text = Entry(width = 17)

# Text Field Positions
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

password_text.grid(
    column = 1,
    row = 3,
)

# Buttons
generate_password_button = Button(text = "Generate Password")

add_password = Button(
    text = "Add",
    width = 30
)

# Button Positions
generate_password_button.grid(
    column = 2,
    row = 3
)

add_password.grid(
    column = 1,
    row = 4,
    columnspan = 2
)

window.mainloop()