from tkinter import *
from tkinter import messagebox

FONT = ("Courier", 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
    column = 1,
    row = 0
    )

# Labels
website_label = Label(text = "Website:")
email_username_label = Label(text = "Email/Username:")
password_label = Label(text = "Password:")

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
website_text.focus()
email_username_text = Entry(width = 35)
email_username_text.insert(0, "mr.frantz.alexander@gmail.com")
password_text = Entry(width = 17)


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
    width = 30,
    command = save_entry
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