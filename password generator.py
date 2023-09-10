import random
from tkinter import *

# Define the character sets for the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{[]}<>/?|\"':;"

# Function to generate a random password
def generate_password():
  length = int(entry_length.get())
  password = "".join(random.sample(characters, length))
  label_password.config(text=password)

# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry("500x500")

# Create the length entry box
label_length = Label(window, text="Password length:")
entry_length = Entry(window)

# Create the generate button
button_generate = Button(window, text="Generate Password", command=generate_password)

# Create the password label
label_password = Label(window, text="")

# Pack the widgets
label_length.pack()
entry_length.pack()
button_generate.pack()
label_password.pack()

# Start the main loop
window.mainloop()
