from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from random import randint, choice, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    symbols_letter = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_letter = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + symbols_letter + numbers_letter

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website:{
        "email": email, "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ooops", message="one of the field is empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def search_website():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="oops", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=40, justify='left')
website_input.grid(row=1,column=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "gurbrar@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

add_button = Button(text="Add", width=25, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search Website",width=13, command=search_website)
search_button.grid(row=1, column=2)

window.mainloop()
