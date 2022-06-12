from tkinter import *
import random

root = Tk()
root.title("Make my day - app")
root.geometry("400x400")


def myclick():
    list_words = ["Come on, stay cool!", "You are the best!", "You are chicken!", "Don`t be sad!", "Learn every day!",
                  "!?!?!?"]
    myLabel = Label(root, text=random.choice(list_words))
    e.delete(0, "end")
    myLabel.pack(pady=5)


e = Entry(root, width=250, highlightcolor="blue", font=("Utf-8", 16))
e.pack(pady=10)
myButton = Button(root, text="Enter the question:", command=myclick)
myButton.pack(pady=10)

root.mainloop()
