from turtle import *
import turtle as t
from table import CaroTable
 
class PlayGame:
    def __init__(self, turtle = t, player1 = "player1", player2 = 'player2', 
    player1_score = 0, player2_score = 0, total_matchs = 0, x_o_size = 8):
        self.table = CaroTable()
        self.turtle = turtle
        self.player1 = player1
        self.player1_score = player1_score
        self.player2 = player2
        self.player2_score = player2_score
        self.total_matchs = total_matchs
        self.x_o_size = x_o_size
        self.turtle.hideturtle()
        
    def play(self):
        self.turtle.onscreenclick(self.draw_o)
    
    def draw_o(self, x, y):
        pen_size = 3
        self.turtle.pensize(pen_size)
        x,y = self.position(x,y)
        row, column = self.get_cell_position(x,y)      
        if(self.table.table_cells[row][column] == '_'):
            self.table.goto_cord( x, y - (self.table.cell_width + self.table.line_size)/2 + pen_size,self.turtle)
            self.turtle.circle(self.x_o_size)
            self.table.table_cells[row][column] = 'o'
            if(self.is_end_game(row, column)):
                print("O win")
                self.show_massages("O")
            self.turtle.onscreenclick(self.draw_x)
        
       
    def draw_x(self, x, y):
        pen_size = 3
        self.turtle.pensize(pen_size)
        x,y = self.position(x,y)
        row, column = self.get_cell_position(x,y)
        if(self.table.table_cells[row][column] == '_'):
            self.table.goto_cord(x + self.x_o_size, y + self.x_o_size,self.turtle)
            self.turtle.goto(x - self.x_o_size, y - self.x_o_size)
            self.table.goto_cord(x, y + self.x_o_size,self.turtle)
            self.turtle.goto(x + self.x_o_size, y - self.x_o_size) 
            self.table.table_cells[row][column] = 'x'
            if(self.is_end_game(row, column)):
                print("X win")
                self.show_massages("X")
            self.turtle.onscreenclick(self.draw_o)
        
        
    def position(self, x, y):
        cell_width = self.table.cell_width + self.table.line_size
       
        if x > 0 and y > 0:
            x = int(x/cell_width) * cell_width + cell_width/2
            y = int(y/cell_width) * cell_width + cell_width/2
        if x > 0 and y < 0:
            x = int(x/cell_width) * cell_width + cell_width/2 
            y = int(y/cell_width) * cell_width + cell_width/2 - cell_width
        if x < 0 and y < 0:
            x = int(x/cell_width) * cell_width + cell_width/2 - cell_width
            y = int(y/cell_width) * cell_width + cell_width/2 - cell_width
        if x < 0 and y > 0:
            x = int(x/cell_width) * cell_width + cell_width/2 - cell_width
            y = int(y/cell_width) * cell_width + cell_width/2 
        return x,y
 
    def get_cell_position(self,x,y):
        x,y = self.offset_cord(x,y)
        column = int(x/(self.table.cell_width + self.table.line_size))
        row = int(y/(self.table.cell_width + self.table.line_size))
        return row, column
 
    def offset_cord(self,x, y):
        x = self.table.width/2 + x
        y = self.table.height/2  -y 
        return x,y
 
    def reverse_offset_cord(self, x, y):
        x = x - self.table.width/2 
        y = self.table.height/2 - y
        return x,y
 
    def score(self, row, col):
        table = self.table.table_cells
        
    def is_end_game(self, row, col):
        if self.is_end_horizontal(row, col) or self.is_end_vertical(row, col) or self.is_end_primary(row, col) or self.is_end_sub(row, col):
            return True
        return False

    def is_end_horizontal(self, row, col):
        table_cells = self.table.table_cells
        current_turn = table_cells[row][col]
        table_width = len(table_cells)
        left_count, right_count = 0,0
        for i in range(col-1, -1, -1):
            if table_cells[row][i] == current_turn:
                left_count += 1
            else:
                break
        for i in range(col+1, table_width):
            if table_cells[row][i] == current_turn:
                right_count += 1
            else:
                break
        if left_count + right_count + 1 >= 5:
            return True
        return False

    def is_end_vertical(self, row, col):
        table_cells = self.table.table_cells
        current_turn = table_cells[row][col]
        table_height = len(table_cells[0])
        top_count, bottom_count = 0,0
        for i in range(row-1, -1, -1):
            if table_cells[i][col] == current_turn:
                top_count += 1
            else:
                break
        for i in range(row+1, table_height):
            if table_cells[i][col] == current_turn:
                bottom_count += 1
            else:
                break
        if top_count + bottom_count + 1 >= 5:
            return True
        return False
    
    def is_end_primary(self, row, col):
        table_cells = self.table.table_cells
        current_turn = table_cells[row][col]
        table_width = len(table_cells)
        table_height = len(table_cells[0])
        top_count, bottom_count = 0,0
        for i in range(0,row+1):
            if row-i < 0 or col-i < 0: break
            if table_cells[row-i][col-i] ==  current_turn:
                top_count += 1
        for i in range(1, table_width - row + 1):
            if row+i >= table_width or col+i >= table_height: break
            if table_cells[row+i][col+i] ==  current_turn:
                bottom_count += 1
        if top_count + bottom_count >= 5:
            return True
        return False
    
    def is_end_sub(self, row, col):
        table_cells = self.table.table_cells
        current_turn = table_cells[row][col]
        table_width = len(table_cells)
        table_height  = len(table_cells[0])
        top_count, bottom_count = 0,0
        for i in range(0,row+1):
            if row-i < 0 or col+i >= table_width: break
            if table_cells[row-i][col+i] ==  current_turn:
                top_count += 1
        for i in range(1, table_width - row + 1):
            if row+i >= table_height or col-i < 0: break
            if table_cells[row+i][col-i] ==  current_turn:
                bottom_count += 1
        if top_count + bottom_count >= 5:
            return True
        return False
    def end_game(self, player):
        self.show_massages(player)
        if self.is_continue:
            self.new_game()
        else: 
            self.exit_game()
    
    def show_massages(self,player):
        self.turtle.fillcolor("white")
        self.table.goto_cord(-150, 50, self.turtle)
        self.rectangle(300,100)
       
        self.table.goto_cord(-20,30,self.turtle)
        self.turtle.color("black")
        self.turtle.write(f"{player} Win!", font=("Verdana", 13, "normal"))
        
    def rectangle(self, width, height):
        self.turtle.begin_fill()
        for i in range(4):
            if i% 2 == 0:
                self.turtle.forward(width)
                self.turtle.right(90)
            else:
                self.turtle.forward(height)
                self.turtle.right(90)
        self.turtle.end_fill()
        


 
game = PlayGame()
game.play()
game.turtle.mainloop()