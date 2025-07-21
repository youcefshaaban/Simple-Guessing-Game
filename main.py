from tkinter import *
from tkinter import messagebox
import random

class Window:

    def __init__(self, master):


        self.master = master
        self.master.title("Simple Guessing Game")
        self.master.config(bg="#111")
        self.number = str(random.randint(1, 20))
        self.tries = 5
        self.user_guess = Entry()
        self.btn = Button(master, text="Submit", command=self.submiting)

        self.user_guess.config(bg="#111", fg="#00FF00", font=("Cascadia Code", 20))
        self.btn.config(bg="#111", fg="#00FF00", font=("Cascadia Code", 20))

        self.user_guess.pack(padx=20, pady=20)
        self.btn.pack(padx=20, pady=20)
        
    def submiting(self, event=None):
        if self.user_guess.get() == self.number:
            messagebox.showinfo("Congrats 🎉", "You Won!")
            exit(input("Press Enter to Exit..."))
        else:
            self.tries -= 1
            messagebox.showwarning("Be Careful 😲", f"Wrong, You Have {self.tries} Tries Left")
            self.user_guess.delete(0, END)

        if self.tries == 0:
            messagebox.showerror("Sorry 😥", "You Have Lost :(")
            exit()

if __name__ == "__main__":
    root = Tk()
    window = Window(root)
    root.mainloop()