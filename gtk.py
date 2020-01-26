from tkinter import *
import random


root = Tk()


monkey = {'1':'(0_0)', '2' : ' \|/', '3': ' | |'}







class App:

    def __init__(self, root_in):

        frame = Frame(root_in)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button = Button(
            frame, text="Join", fg="red", command=frame.quit
        )

        self.labelText = StringVar(frame)
        self.labelText.set('hello')
        self.label = Label(root_in, text='frame')
        text = Text(root_in)
        i = 0
        change_arm = {1: ' /|\\', 2: ' \|\\'}
        change_leg = {1: '/\\', 2: '<>'}

        value = random.randint(1, 2)
        anti_half_monkey = []
        while i < 3:
            for values in monkey.values():
                anti_half_monkey.append(values)
                i = i + 1
            monkey['2'] = change_arm[value]
            for value in monkey.values():
                print(value)
                text.insert(INSERT, value)
                text.insert(END, "\n")
                text.pack()

        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")


app = App(root)

root.mainloop()
root.destroy() # optional; see description below