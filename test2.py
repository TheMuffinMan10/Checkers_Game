
import tkinter
#from PIL import ImageTk, Image

class Board:
    virBoard = []
    Turn = 1

    def __init__(self):
        rows = 8
        cols = 8
        for i in range(rows):        # Step 2: Loop through the rows
            rows = [None] * cols         # Step 3: Create a list (row) with `cols` number of zeros
            self.virBoard.append(rows) 
    
class Square:
    isTaken = False

    def __init__(self):
        self.isTaken = False

class Piece:
    row = column = 0
    colour = ""
    #toTake = False

    def __init__(self, Row, Column, Colour):
        self.column=Column
        self.row=Row
        self.colour = Colour

    def promote():
        pass

    @classmethod
    def show_black_right(self, man):
        try:
            self = man
            x: tkinter.Button
            G: Piece
            G = map.virBoard[man.row -1][man.column + 1]
            if(G is None):     #next square on the right is not taken
                board[man.row -1][man.column +1]["background"] = "green"
                x = board[self.row -1][self.column +1]
                x.config(command=lambda h= self.row -1, k= self.column +1
                         :self.transfer(h, k, False))

            elif(G.colour == "W"):     #next square on the right is black pawn
                try:
                    if(map.virBoard[man.row -2][man.column + 2] is None):     #final check to take a piece
                        #take the piece()
                        board[man.row -2][man.column + 2]["background"] = "green"
                        x = board[self.row - 2][self.column +2]
                        x.config(command=lambda f = self.row - 2, k = self.column + 2
                                    :self.transfer(f, k, True))
                        #self.take(self.row - 1, self.column + 1)
                            
                except IndexError:
                    #carry on to the left
                    #try catch statement for promotion!!!
                    self.show_black_left(self)

        except IndexError: #if this is hit, then we are at the edge of the board
            self.show_black_left(self)

        self.show_black_left(self)

    def show_black_left(self, man):
        #carry on to the left
        self = man
        s: tkinter.Button
        try:
            if(map.virBoard[self.row - 1][self.column + (- 1)] is None):     #next square on the left is taken
                board[self.row -1][self.column -1]["background"] = "green"
                s = board[self.row -1][self.column -1]
                s.config(command=lambda h= self.row -1, k= self.column -1
                         :self.transfer(h, k, False))

            elif(map.virBoard[self.row -1][self.column - 1].colour == "W"):         #next square on the left is black
                try:
                    if(map.virBoard[self.row - 2][self.column - 2] is None):         #final check to take a piece
                    #take the piece
                        board[self.row -2][self.column - 2]["background"] = "green"
                        s = board[self.row - 2][self.column -2]
                        s.config(command=lambda f = self.row - 2, k = self.column -2
                                    :self.transfer(f, k, True))
                        #self.take(self.row - 1, self.column - 1)
                except IndexError:
                    print("Edge-ish of board")
        except IndexError: #right fails, then check left to show both
            self.promote()
                
    def show_white_right(self, man):
        try:   #try to go right
            self = man
            s: tkinter.Button
            G: Piece
            #x: tkinter.Button
            G = map.virBoard[self.row +1][self.column + 1]
            if(G is None):     #next square on the right is not taken
                board[self.row +1][self.column +1]["background"] = "green"
                s = board[self.row +1][self.column +1]
                s.config(command=lambda h = self.row +1, k = self.column +1
                        :self.transfer(h, k, False))

            elif(G.colour == "B"):     #next square on the right is black pawn
                try:    #try to take a piece
                    if(map.virBoard[self.row +2][self.column + 2] is None):     #final check to take a piece
                        #take the piece()
                        board[self.row +2][self.column + 2]["background"] = "green"
                        s = board[self.row +2][self.column + 2]
                        s.config(command=lambda f = self.row +2, k = self.column +2
                                    :self.transfer(f, k, True))
                        
                except IndexError: 
                    #carry on to the left because right is closed
                    #try catch statement for promotion!!!
                    self.show_white_left(self)
                    '''if(map.virBoard[self.row + 1][self.column - 1] is None):     #next square on the left is taken
                        board[self.row +1][self.column -1]["background"] = "green"

                    elif(map.virBoard[self.row +1][self.column - 1].colour == "B"):         #next square on the left is black
                        if(map.virBoard[self.row +2][self.column - 2] is None):         #final check to take a piece
                        #take the piece
                            board[self.row +2][self.column - 2]["background"] = "green"'''

        except IndexError: #if this is hit, then we are at the edge of the board
            self.show_white_left(self)
            '''if(map.virBoard[self.row + 1][self.column - 1] is None):     #next square on the left is taken
                board[self.row +1][self.column -1]["background"] = "green"

            elif(map.virBoard[self.row +1][self.column - 1].colour == "W"):         #next square on the right is black
                if(map.virBoard[self.row +2][self.column - 2] is None):         #final check to take a piece
                #take the piece
                    map.virBoard[self.row +2][self.column - 2]["background"] = "green"'''

        self.show_white_left(self)

    def show_white_left(self, man):
        self = man
        s: tkinter.Button
        try:
            #carry on to the left
            if(map.virBoard[self.row + 1][self.column - 1] is None):     #next square on the left is taken
                board[self.row +1][self.column -1]["background"] = "green"
                s = board[self.row +1][self.column -1]
                s.config(command=lambda f = self.row +1, k = self.column -1
                        :self.transfer(f, k, False))

            elif(map.virBoard[self.row +1][self.column - 1].colour == "B"):         #next square on the left is black
                try:
                    if(map.virBoard[self.row +2][self.column - 2] is None):         #final check to take a piece
                    #take the piece
                        board[self.row +2][self.column - 2]["background"] = "green"
                        s = board[self.row +2][self.column -2]
                        s.config(command=lambda f = self.row +2, k = self.column -2
                                    :self.transfer(f, k, True))
                        #self.take(self.row + 1, self.column - 1)

                except IndexError:
                    print("edge-ish of board")

        except IndexError:
            #promotion
            print("promote to king")
            self.promote()

    def transfer(self, n_row, n_column, taking: bool):
        #self = man
        x: tkinter.Button
        n_x: tkinter.Button
        #alter virtual board
        x=board[self.row][self.column]
        x.config(text="", command=lambda: clean_squares)
        map.virBoard[self.row][self.column] = None
        
        #alter piece obj
        map.virBoard[n_row][n_column] = Piece(n_row, n_column, self.colour)
        
        #alter physical board
        n_x=board[n_row][n_column]
        n_x.config(font=("Consolas", 10, "bold"), text="O", command=lambda 
                                        m=map.virBoard[n_row][n_column] : move(m))
        
        #display the right pawn colour
        if(self.colour == "W"):
            n_x.config(foreground="white")
            if(taking):
                self.take(n_row, n_column, "W")
        else:
            n_x.config(foreground="red")
            if(taking):
                self.take(n_row, n_column, "B")

        clean_squares()
        
        if(map.Turn == 0):
            lblMove.config(text="White To Move", background="white", foreground="black")
            map.Turn = 1
        else: 
            lblMove.config(text="Black To Move", background="black", foreground="white")
            map.Turn = 0

        self = None

    def take(self, n_row, n_column, colour):
        new_position: tkinter.Button
        taken_position: tkinter.Button
        if(colour == "W"):
            if(n_column > self.column):  #moved right if true
                map.virBoard[self.row + 1][self.column + 1] = None
                taken_position = board[self.row + 1][self.column+1]
                taken_position.config(text="")
                map.virBoard[n_row][n_column] = Piece(n_row, n_column, "W")
                new_position = board[n_row][n_column]
                new_position.config(font=("Consolas", 10, "bold"), text="O", foreground="White")
            else:  #taking to the left
                map.virBoard[self.row+1][self.column - 1] = None
                map.virBoard[n_row][n_column] = Piece(n_row, n_column, "W")
                taken_position = board[self.row + 1][self.column-1]
                taken_position.config(text="")
                new_position = board[n_row][n_column]
                new_position.config(font=("Consolas", 10, "bold"), text="O", foreground="White")
        else:
            if(n_column > self.column):  #moved right if true
                map.virBoard[self.row - 1][self.column + 1] = None
                #board[n_row - 1][n_column - 1]["text"] = ""
                taken_position = board[self.row - 1][self.column+1]
                taken_position.config(text="")
                new_position = board[n_row][n_column]
                new_position.config(font=("Consolas", 10, "bold"), text="O", foreground="red")
            else: #taking on the left
                map.virBoard[self.row - 1][self.column - 1] = None
                #board[n_row - 1][n_column - 1]["text"] = ""
                taken_position = board[self.row - 1][self.column-1]
                taken_position.config(text="")
                new_position = board[n_row][n_column]
                new_position.config(font=("Consolas", 10, "bold"), text="O", foreground="red")

    #@staticmethod
    def move(self):
        if(self.colour == "B" and map.Turn==0):  #black's move 
            #lblMove.config(text="White To Move", background="white", foreground="black") 
            print("Turn")
            self.show_black_right(self)

        #white to move
        elif(self.colour == "W" and map.Turn==1):  #white's move
            self.show_white_right(self)
            
class King(Piece):
    def move():
        pass

def is_winner():     #bool: true if game is over
    pass

def is_king():          #bool: true if pawn is promoted
    pass

def clean_squares():
    g: tkinter.Button
    for i in range(8):
        for j in range(8):
            g = board[i][j]
            if(board[i][j]["background"] == "green"):
                g.config(background="black", command=lambda row=i, column=j: move(map.virBoard[row][column]))

def move(pawn: Piece):             #void: makes a move 
    if(not(pawn is None)):
        print("there")
        clean_squares()
        pawn.move()

window = tkinter.Tk()
window.geometry("650x650")
window.title("Cams")

mainFrame = tkinter.Frame(window, width=300, height=300,background= "black")

board = []
rows = 8
cols = 8

for i in range(rows):        # Step 2: Loop through the rows
    row = [0] * cols         # Step 3: Create a list (row) with `cols` number of zeros
    board.append(row) 

def board_set_up():

    global lblMove
    lblMove = tkinter.Label(mainFrame, text="White to move", background = "white")
    lblMove.grid(columnspan = 9, sticky="we")

    global map #= Board()
    map = Board()
    map.Turn =1
    for i in range(rows):        # Step 2: Loop through the rows
        for j in range(rows): 
            map.virBoard[i][j] is None#= Piece(8,8,"")

    colourFlag = False
    #img = ImageTk.PhotoImage(Image.open("white-pawn.jpg"))

    for row in range(8):
        colourFlag= not(colourFlag)
        for col in range(8):
            square = board[row][col]

            if(colourFlag):      #to colour in the blocks
                square = tkinter.Button(mainFrame, width="8", height="3", background="white")
                #board.append(square)
                colourFlag = False
            else:
                r=row
                c=col
                square = tkinter.Button(mainFrame, width="8", height="3", background="black")
                                       # command=lambda 
                                        #m=map.virBoard[r][c] : move(m))
                #m=map.virBoard[r][c]
                colourFlag  = True

            if((row < 3 or row > 4) and (colourFlag)):    #to fill in the letters (pieces) on right shade
                square.configure(font=("Consolas", 10, "bold"), 
                                                text="O")
                                                
                if(row < 3):
                    square.configure(foreground="white")
                    map.virBoard[row][col] =  Piece(row, col, "W")
                    m=map.virBoard[row][col]           
                    square.configure(command=lambda 
                                        m=map.virBoard[r][c] : move(m))
                else:
                    square.configure(foreground="red")
                    map.virBoard[row][col] =  Piece(row, col, "B")
                    square.configure(command=lambda 
                                        m=map.virBoard[r][c] : move(m))

            if(row == 4):
               print("")
            board[row][col] = square
            square.grid(row=row+1, column=col +1)
        
reset = tkinter.Button(mainFrame, text="Restart Game", background = "grey", command=board_set_up)
reset.grid(row=11,columnspan=9, sticky="we")

mainFrame.grid()
board_set_up()





window.mainloop()