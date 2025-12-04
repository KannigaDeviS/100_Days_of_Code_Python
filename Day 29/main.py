from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Hard level
    password_list = []
    password_list.extend([random.choice(letters) for num in range(random.randint(8,10))])
    password_list.extend([random.choice(symbols) for num in range(random.randint(2,4))])
    password_list.extend([random.choice(numbers) for num in range(random.randint(2,4))])

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website)== 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Hey! please don't leave any fields empty")
    else:
        is_okay=messagebox.askokcancel(title=website, message=f"The details entered are \n Email: {email} \n Password:{password}\n is it okay to save?" )
        if is_okay:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }
            try:
                data = read_data_from_json()
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def read_data_from_json():
    with open("data.json", "r") as f:
        data = json.load(f)
        return data

# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        data = read_data_from_json()
        website = website_input.get()
        search_data = data[f"{website}"]
    except KeyError:
        messagebox.showinfo(title="Not found", message=f"\n No password saved for the website {website}")
    except FileNotFoundError:
        print("No data in file")
    else:
        messagebox.showinfo(title=website,
                            message=f"\n Email: {search_data["email"]} \n Password:{search_data["password"]}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=220, height=220, padx=45, pady=45)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid( row=0, column=1)

# labels
website_label = Label(text = 'Website')
website_label.grid(row=1, column=0)
email_label = Label(text = 'Email/Username')
email_label.grid(row=2, column=0)
password_label = Label(text = 'Password')
password_label.grid(row=3, column=0)

# input
website_input = Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'aginnak@gmail.com')

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()