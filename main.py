from email.mime import image
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(4, 6))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Hey !", message="Please make sure you haven't left any empty.")
    else:
        try:
            with open("data.json", "r")as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w")as data_file:
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)
            
            with open("data.json", "w")as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="No data Found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="ERROR",message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Keeper")
window.config(padx=20, pady=20)

# img
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo)
canvas.grid(row=0, column=1)

# website

website_text = Label(text="Website:")
website_text.grid(row=1, column=2)

website_entry = Entry(width=23)
website_entry.grid(row=1, column=1,sticky="E")
website_entry.focus()  # let users start typing

#search
search_button = Button(text="Search", width=16,command=find_password)
search_button.grid(row=1, column=2)
# Email/Username

email_user_text = Label(text="Email/Username:")
email_user_text.grid(row=2, column=0)

email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "deathknight285@gmail.com")
# password
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, sticky="E")

# generate password button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
# Add button
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
