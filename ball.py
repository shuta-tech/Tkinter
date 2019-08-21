import sys
import tkinter

def pushed(self):
    self["text"] = "change"
#creat a main window
root = tkinter.Tk()
root.title(u"Shuta")
root.geometry("640x480")

#creat a button

    #print("clicked")

button = tkinter.Button(root, text = "BUTTON", command = lambda : pushed(button))
#button.grid()
button.pack()

#label
static1 = tkinter.Label(text = u'test')
#static1.pack()

root.mainloop()
