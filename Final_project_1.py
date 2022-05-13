from tkinter import *

class main:
    
    
    def __init__(self):
        """This is the main function it is in charge of setting up the GUI and call the minor functions"""
        self.x = 0
        self.window = Tk()
        self.window.title("Area Calculator")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        label1 = Label(self.window, text = "Please select your shape")
        options = ["Circle", "Rectangle", "Square", "Triangle"]
        self.clicked = StringVar()
        drop = OptionMenu(self.window, self.clicked, *options)
        label1.pack()
        drop.pack()
        frame_bottom = Frame(self.window)
        button_done = Button(frame_bottom, text ="done", command=self.window.destroy)
        button_done.pack()
        frame_bottom.pack(pady=15, side=BOTTOM)
        self.clicked.trace("w", self.shapelogic)
        self.window.mainloop()
        
    
    def shapelogic(self, a, b, c):
        """This function is called when the user changes the shape selection and it removes the previous shape
        frame as well as setting up the correct labels and entry boxes for whatever shape the user selected"""
        if self.x == 1:
            self.frame_shape.destroy()
        else:
            self.x += 1
        shape = "a"
        shape = self.clicked.get()
        if shape == "Circle":
            self.frame_shape = Frame(self.window)
            self.rlabel = Label(self.frame_shape, text="Please enter the radius' length")
            self.radius = Entry(self.frame_shape)
            self.rlabel.pack()
            self.radius.pack()
            self.button_calculate = Button(self.frame_shape, text ="calculate", command=self.ca)
            self.button_calculate.pack()
            self.frame_shape.pack()
        if shape == "Rectangle":
            self.frame_shape = Frame(self.window)
            self.s1label = Label(self.frame_shape, text="Please enter base's length")
            self.s2label = Label(self.frame_shape, text="Please enter height's length")
            self.s1 = Entry(self.frame_shape)
            self.s2 = Entry(self.frame_shape)
            self.button_calculate = Button(self.frame_shape, text ="calculate", command=self.ra)
            self.s1label.pack()
            self.s1.pack()
            self.s2label.pack()
            self.s2.pack()
            self.button_calculate.pack()
            self.frame_shape.pack()
        if shape == "Square":
            self.frame_shape = Frame(self.window)
            self.s1label = Label(self.frame_shape, text="Please enter the side's length")
            self.side = Entry(self.frame_shape)
            self.button_calculate = Button(self.frame_shape, text ="calculate", command=self.sa)
            self.s1label.pack()
            self.side.pack()
            self.button_calculate.pack()
            self.frame_shape.pack()
        if shape == "Triangle":
            self.frame_shape = Frame(self.window)
            self.s1label = Label(self.frame_shape, text="Please enter base's length")
            self.s2label = Label(self.frame_shape, text="Please enter height's length")
            self.s1 = Entry(self.frame_shape)
            self.s2 = Entry(self.frame_shape)
            self.button_calculate = Button(self.frame_shape, text ="calculate", command=self.ta)
            self.s1label.pack()
            self.s1.pack()
            self.s2label.pack()
            self.s2.pack()
            self.button_calculate.pack()
            self.frame_shape.pack()
            
            
            
            

    def ca(self):
        """This function is called when the calculate button is clicked for the Circle shape and is responsible for
        the error handeling and calculations associated with calculating the area of a Circle"""
        self.rad = self.radius.get()
        try:
            b = int(self.rad)
        except:
            self.elabel = Label(self.frame_shape, text="Your radius is not an integer")
            self.elabel.pack()
        else:
            if b <= 0:
                self.nlabel = Label(self.frame_shape, text="Your radius is negative")
                self.nlabel.pack()
            c = 3.141529 * b * b
            self.alabel = Label(self.frame_shape, text=f"Circle area = {c:.2f}")
            self.alabel.pack()
        self.frame_shape.pack()
    def ra(self):
        """This function is called when the calculate button is clicked for the Rectangle shape and is responsible for
        the error handeling and calculations associated with calculating the area of a Rectangle"""
        ras1 =self.s1.get()
        ras2 = self.s2.get()
        try:
            b = int(ras1)
            c = int(ras2)
        except:
            self.elabel = Label(self.frame_shape, text="One of your sides is not an integer")
            self.elabel.pack()
        else:
            if b <= 0 or c <= 0:
                self.nlabel = Label(self.frame_shape, text="One of your sides are negative")
                self.nlabel.pack()
            d = b * c
            self.alabel = Label(self.frame_shape, text=f"Rectangle area = {d:.2f}")
            self.alabel.pack()
        self.frame_shape.pack()
    def sa(self):
        """This function is called when the calculate button is clicked for the Square shape and is responsible for
        the error handeling and calculations associated with calculating the area of a Square"""
        b = self.side.get()
        try:
            b = int(b)
        except:
            self.elabel = Label(self.frame_shape, text="Your side is not an integer")
            self.elabel.pack()
        else:
            if b <= 0:
                self.nlabel = Label(self.frame_shape, text="Your side are negative")
                self.nlabel.pack()
            d = b * b
            self.alabel = Label(self.frame_shape, text=f"Square area = {d:.2f}")
            self.alabel.pack()
        self.frame_shape.pack()
    def ta(self):
        """This function is called when the calculate button is clicked for the Triangle shape and is responsible for
        the error handeling and calculations associated with calculating the area of a Triangle"""
        b = self.s1.get()
        c = self.s2.get()
        try:
            b = int(b)
            c = int(c)
        except:
            self.elabel = Label(self.frame_shape, text="One of your sides is not an integer")
            self.elabel.pack()
        else:
            if b <= 0 or c <= 0:
                self.nlabel = Label(self.frame_shape, text="One of your sides are negative")
                self.nlabel.pack()
            d = (b * c)/2
            self.alabel = Label(self.frame_shape, text=f"Triangle area = {d:.2f}")
            self.alabel.pack()
        self.frame_shape.pack()

if __name__ == "__main__":
    main()
    
    
    
    
    
    