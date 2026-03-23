while True:
    from random import *
    a = input("rock, paper, scissors: ")
    b = choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {b}")
    if a == b:
        print("It's a tie!")
    elif (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper"):
        print("You win!")
    else:
        print("You lose!")
    from tkinter import *
    from tkinter import messagebox
    root = Tk()
    root.geometry("200x200")
    def msg():
        messagebox.showwarning("nice", "battle found")

    button = Button(root, text="scan for other battle", command=msg)
    button.place(x=40, y=80)
    button2 = Button(root, text="exit", command=root.destroy)
    root.mainloop() 