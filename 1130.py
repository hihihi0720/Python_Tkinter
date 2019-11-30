import tkinter as tk
import random
class Grid:
    def __init__(self,n):
        self.size=n
        self.cells=self.generate_empty_grid()
        self.compressed=False
        self.merge=False
        self.moved=False
        self.current_score=0
        
        
    def generate_empty_grid(self):
        cells=[]
        for i in range(self.size):
            cells.append([])
            for j in range(self.size):
                cells[i].append(0)
        return cells

    def retrieve_empty_cell(self):
        empty_cells=[]
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j]==0:
                    empty_cells.append((i,j))
        return empty_cells
    
    def random_cell(self):
        cell=random.choice(self.retrieve_empty_cell())
        i=cell[0]
        j=cell[0]
        self.cells[i][j]=2

    def left_compress(self):
        self.compressed=False
        new_empty_cells=self.generate_empty_grid()
        
        for i in range(self.size):
            count=0
            for j in range(self.size):
                if self.cells[i][j]!=0:
                    new_empty_cells[i][count]=self.cells[i][j]
                    if j!=count:
                        self.compressed=True
                        count=count+1
        self.cells=new_empty_cells
class GamePanel:
    def paint(self):
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                if self.grid.cells[i][j]==0:
                    self.cell_labels[i][j].config(
                            text='',
                            bg=GamePanel.EMPTY_CELL_COLOR)
                else:
                    if self.grid.cells[i][j]>16:
                        self.cell_labels[i][j].config(
                                text=str(self.grid.cells[i][j]),
                                bg=GamePanel.CELL_BACKGROUND_COLOR_DICT.get('beyond'),
                                fg=GamePanel.CELL_COLOR_DICT.get('beyond'))
                    else:
                        self.cell_labels[i][j].config(
                                text=str(self.grid.cells[i][j]),
                                bg=GamePanel.CELL_BACKGROUND_COLOR_DICT.get(str(self.grid.cells[i][j])),
                                fg=GamePanel.CELL_COLOR_DICT.get(str(self.grid.cells[i][j])))
    
    
    
    
    
    
    BACKGROUND_COLOR="#2852b2"
    EMPTY_CELL_COLOR="#235a45"
    
    
    CELL_BACKGROUND_COLOR_DICT={
        '0':"#72527a",
        '2':"#408b7a",
        '4':"#ba8b7a",
        '8':"#ba7435",
        '16':"#3ea04f",
        '32':"#be58ae",
        '64':"#49586a",
        '128':"#f9f97e",
        'beyond':"#000000"
        }
    CELL_COLOR_DICT={
        '0':"#553333",
        '2':"#553333",
        '4':"#553333",
        '8':"#553333",
        '16':"#553333",
        '32':"#553333",
        '64':"#553333",
        '128':"#553333",
        'beyond':"#ffffff"
        }
    FONT=("Verdana",24,'bold')
    UP_KEYS=('w','W','Up')
    LEFT_KEYS=('a','A','Left')
    DOWN_KEYS=('s','S','Down')
    RIGHT_KEYS=('d','D','Right')
    
    
    def __init__(self,grid):
            self.grid=grid
            self.window=tk.Tk()
            self.window.title("2048")
            self.window.geometry('800x800')
            self.background=tk.Frame(self.window,bg=GamePanel.BACKGROUND_COLOR)
            self.cell_labels=[]
            
            
            
            for i in range(self.grid.size):
                self.cell_labels.append([])
                for j in range(self.grid.size):
                    label=tk.Label(self.background,text='0',bg=GamePanel.EMPTY_CELL_COLOR,font=GamePanel.FONT,width=4,height=2)
                    label.grid(row=i,column=j,padx=5,pady=5)
                    self.cell_labels[i].append(label)
            self.background.grid()
class Game:
    def __init__(self,grid,panel):
        self.grid=grid
        self.panel=panel
        self.start_cell_num=2
        for i in range(self.start_cell_num):
            self.grid.random_cell()
            
        self.panel.paint()
        self.panel.window.bind('<Key>',self.key_handler)
        self.panel.window.mainloop()            
        
    def key_handler(self,event):
        key_value=event.keysym
        print('{}{}key is pressed'.format(key_value,key_value))
        if key_value in GamePanel.UP_KEYS:
            self.up()
        elif key_value in GamePanel.DOWN_KEYS:
            self.down()
        elif key_value in GamePanel.LEFT_KEYS:
            self.left()
        elif key_value in GamePanel.RIGHT_KEYS:
            self.right()
        else:
            pass
        
    def up(self):
        pass
    def down(self):
        pass
    def right(self):
        pass
    def left(self):
        pass
            
           
grid=Grid(5)
panel=GamePanel(grid)
Gamepanel=Game(grid,panel)
         
