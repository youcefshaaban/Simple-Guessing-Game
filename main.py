# Importing Modules
from tkinter import *
from tkinter import messagebox
import random

# Functions
def submiting(event=None):
    global tries
    if user_guess.get() == number:
        messagebox.showinfo("Congrats 🎉", "You Won!")
        exit(input("Press Enter to Exit..."))
    else:
        tries -= 1
        messagebox.showwarning("Be Careful 😲", f"Wrong, You Have {tries} Tries Left")
        user_guess.delete(0, END)
    
    if tries == 0:
        messagebox.showerror("Sorry 😥", "You Have Lost :(")
        exit()

# Defining Variables
number = str(random.randint(1, 20)) # Number Variable
tries = 5 # Tries Variable
root = Tk() # Main Variable
warning = Label(root, text="Enter Number Only") # Warning Label
user_guess = Entry() # Input Variable
submit = Button(root, text="Submit", command=submiting)

# PLacing Elements
user_guess.pack(padx=20, pady=20)
warning.pack(padx=20, pady=20)
submit.pack(padx=20, pady=20)

# Customizing Main Variable
root.config(bg="#111")
root.title("Simple Guess Game")

# Customizing Elements
user_guess.config(bg="#111", fg="#00FF00", font=("Cascadia Code", 20))
warning.config(bg="#111", fg="#00FF00", font=("Cascadia Code", 20))
submit.config(bg="#111", fg="#00FF00", font=("Cascadia Code", 20))

# Binding The Enter Key To Submit
root.bind("<Return>", submiting)

# Mainloop
root.mainloop()