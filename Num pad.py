from tkinter import *

window = Tk()
window.title("number Pad")
window.geometry("250x300")

nums = [[9,8,7],[6,5,4],[3,2,1],["#",0,"@"]]

for i in range(4):
    window.columnconfigure(i, weight = 1, minsize = 100)
    window.rowconfigure(i, weight = 1, minsize = 100)
for i in range(4):
    for j in range(3):
        frame = Frame(master = window, relief = GROOVE, borderwidth = 1.5, bg = "blue")
        frame.grid(row=i, column = j, sticky="nsew")
        label = Label(master = frame, text = nums[i][j])
        label.pack(expand = True, fill = "both", padx = 5, pady = 5)
window.mainloop()
