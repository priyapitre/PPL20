from tkinter import *
from tkinter.colorchooser import askcolor

class myPaint() :

    DEFAULT_PEN_SIZE = 6.0
    DEFAULT_COLOR = 'black'
    def __init__(self) :
        self.master = Tk()
        self.brush_button = Button(self.master, text = 'Brush', command = self.brush)
        self.pen_button = Button(self.master, text = 'Pen', command = self.pen)
        self.eraser_button = Button(self.master, text = 'Eraser', command = self.eraser)
        self.color_button = Button(self.master, text = 'Color', command = self.choose_color)
        self.size_button = Scale(self.master, from_=1, to=10, orient = HORIZONTAL)

        self.c = Canvas(self.master, bg = 'white', width = 800, height= 600)
        self.c.grid(row = 1, columnspan = 5)
        self.brush_button.grid(row = 0, column = 0)
        self.pen_button.grid(row = 0, column = 1)
        self.eraser_button.grid(row = 0, column = 2)
        self.color_button.grid(row = 0, column = 3)
        self.size_button.grid(row = 0,column = 4)

        self.initialize()
        self.master.mainloop()

    #This function initializes the blank paint application window.
    def initialize(self) :
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
        self.old_x = None
        self.old_y = None
        self.line_width = self.size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button

    #This function takes care of proceedings when a button is clicked.
    def activate_button(self, selected_button, eraser_mode = False) :
        self.active_button.config(relief = RAISED)
        selected_button.config(relief = SUNKEN)
        self.active_button = selected_button
        self.eraser_on = eraser_mode

    #This function is called when brush button is clicked.
    def brush(self) :
        self.activate_button(self.brush_button)

    #This function is called when pen button is clicked.
    def pen(self) :
        self.activate_button(self.pen_button)

    #This function is called when eraser button is clicked.
    def eraser(self) :
        self.activate_button(self.eraser_button,eraser_mode = True)

    #This function helps the user to choose color.
    def choose_color(self) :
        self.eraser_on = False
        self.color = askcolor(color = self.color)[1]

    #This function deals with the execution when operations are performed in paint space.
    def paint(self,event) :
        self.line_width = self.size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y :
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,width=self.line_width,
                               fill=paint_color,capstyle=ROUND,smooth=TRUE,splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    #This function will reset everything back to initialized window.
    def reset(self,event) :
        self.old_x = None
        self.old_y = None


if __name__ == "__main__" :
    myPaint()
