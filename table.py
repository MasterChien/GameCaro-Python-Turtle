from turtle import *
import turtle as turtle
 
class CaroTable:
    def __init__(self, rows=0, columns=0, cell_width=24, line_size=1, 
    width=550, height=550,x_o_size = 5):
        self.turtle = turtle
        self.rows = rows
        self.columns = columns
        self.cell_width = cell_width
        self.line_size = line_size
        self.width = width
        self.height = height
        self.x_o_size = x_o_size
        self.table_cells = self.calcu_table_cells()
        self.draw_table()
 
    def setup(self):
        self.turtle.setup(self.width, self.height)
        self.turtle.hideturtle()
 
    def goto_cord(self, x, y, turtle):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
 
    def draw_vertical_lines(self):
        xcord = -self.width/2
        ycord = self.height/2
        t = self.turtle
        t.speed(0)
        self.goto_cord(xcord, ycord,self.turtle)
        while ycord > -self.round_up(self.height,2):
            if xcord == -self.width/2:
                xcord = self.width/2
                t.goto(xcord, ycord)
                ycord = ycord - self.cell_width - self.line_size
                t.goto(xcord, ycord)
            if xcord == self.width/2:
                xcord = -self.width/2
                t.goto(xcord, ycord)
                ycord = ycord - self.cell_width - self.line_size
                t.goto(xcord, ycord)
 
    def draw_horizon_lines(self):
        xcord = -self.width/2
        ycord = self.height/2
        t = self.turtle
        t.speed(0)
        self.goto_cord( xcord, ycord,self.turtle) 
        while xcord < self.round_up(self.width,2):
            if ycord == self.height/2:
                ycord = -self.height/2
                t.goto(xcord, ycord)
                xcord = xcord + self.cell_width + self.line_size
                t.goto(xcord, ycord)
            if ycord == -self.height/2:
                ycord = self.height/2
                t.goto(xcord, ycord)
                xcord = xcord + self.cell_width + self.line_size
                t.goto(xcord, ycord)
 
    def draw_table(self):
        self.setup()
        self.draw_vertical_lines()
        self.draw_horizon_lines()
 
    def calcu_table_cells(self):
        cols = self.width /(self.cell_width + self.line_size)
        rows = self.height /(self.cell_width + self.line_size)
 
        rows = self.round_up(rows,1)
        cols = self.round_up(cols,1)
 
        cells = [['_' for i in range(cols)] for j in range(rows)]
        return cells
 
    def round_up(self, x, by_x):
        if x/by_x > int(x/by_x): x = int(x/by_x) + 1
        else: x = int(x/by_x)
        return x
 
    def draw_x(self, x, y):
        self.turtle.hideturtle()
        self.goto_cord(x, y- self.x_o_size,self.turtle)
        self.turtle.circle(self.x_o_size)