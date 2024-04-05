from tkinter import *

class MainGUI(Frame):
    
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setupGUI()

    # sets up the GUI
    def setupGUI(self):
        # the display
        self.display = Label(self, text = "", anchor = E, bg = "white", height = 1, fg = "black", font = ("TexGyreAdventor", 25))
        self.display.grid(row = 0, column = 0, columnspan = 2, sticky = E+W+N+S)

        # configure the rows and columns of the Frame to adjust to the window
        for row in range(3):
            Grid.rowconfigure(self, row, weight = 1)
        for col in range(4):
            Grid.columnconfigure(self, col, weight = 1)

        # box 1
        button = Button(self, bg = "white", text = "BOX 1", borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("1"))
        button.grid(row = 1, column = 0, sticky = N+S+E+W)
        
        # box 2
        button = Button(self, bg = "white", text = "BOX 2", borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("2"))
        button.grid(row = 1, column = 1, sticky = N+S+E+W)
        
        # box 3
        button = Button(self, bg = "white", text = "BOX 3", borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("3"))
        button.grid(row = 1, column = 2, sticky = N+S+E+W)
        
        # box 4
        button = Button(self, bg = "white", text = "BOX 4", borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("4"))
        button.grid(row = 1, column = 3, sticky = N+S+E+W)

        self.pack(fill = BOTH, expand = 1)

    # processes button presses
    def process(self, button):
        # let the user know which box they clicked
        if (button == "1"):
            self.display["text"] = "YOU CLICKED BOX 1"
        if (button == "2"):
            self.display["text"] = "YOU CLICKED BOX 2"
        if (button == "3"):
            self.display["text"] = "YOU CLICKED BOX 3"
        if (button =="4"):
            self.display["text"] = "YOU CLICKED BOX 4"

window = Tk()
p = MainGUI(window)
window.title("Box Selection")
window.mainloop
