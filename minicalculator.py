from tkinter import *

#This function returns a Frame
def iCalc(source, side):
    "Returns a Frame object yet packed and expanded, to shorten the code"
    # the bd is the border of the frame
    storeObj = Frame(source, borderwidth=10, bd=1, bg="gray")
    # the pack methos is needed to diplay the object
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

# This class inherit from Frame
class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")


        #  THE DISPLAY
        display = StringVar()
        # relief can be FLAT or RIDGE or RAISED or SUNKEN GROOVE
        entry = Entry(self, relief=FLAT, textvariable=display, justify='right', bd=15, bg='orange')
        entry.pack(side=TOP)
        # I added an action to calculate the operation when Return (Enter) is hit
        entry.focus()
        # You can hit enter to get the result instead of clicking =
        self.master.bind("<Return>", lambda e, s=self, storeObj=display: s.calc(storeObj))
        # YOu can click del button on the keyboard to cancel
        self.master.bind("<Delete>", lambda e, s=self, storeObj=display: storeObj.set(""))
        self.master.bind("<BackSpace>", lambda e, s=self, storeObj=display: storeObj.set(""))



    def calc(self, display):
        try:
        	# Sets the display to the evaluation of the string in the display itself, i.e. calculate the result
            display.set(eval(display.get()))
        except:
        	# if something goes wrong with the result
            display.set("ERROR")


if __name__ == '__main__':
    App().mainloop()