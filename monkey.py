from tkinter import *
import time

monkey_base = {'1': '(0_0)', '2': ' \\|/', '3': ' jj '}
monkey_left = {'1': '(0_0)', '2': ' \\|\\', '3': ' \\ \\'}
monkey_right = {'1': '(0_0)', '2': ' /|/', '3': ' //'}

all_monkeys = [monkey_base, monkey_left, monkey_right]
final = []
root = Tk()
frame = Frame(root)
frame.pack()
var = StringVar()
lbl = Label(root, textvariable = var)
lbl.pack()
i = 0

def draw_monkey():
    count = 0
    full_monkey = ''
    for part in all_monkeys[count].values():
        full_monkey += '\n' + part
        final.append(full_monkey)
    if count == 2:
        time.sleep(1)
        var.set(final)
        count = 0
    else:
        count += 1
    lbl['text'] = full_monkey
    lbl.pack()
    root.update_idletasks()


root.after(1000, draw_monkey())

root.mainloop()
