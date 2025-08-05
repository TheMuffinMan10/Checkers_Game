
import tkinter
from PIL import ImageTk, Image

def new_game():
    pass


window = tkinter.Tk()
window.geometry("500x650")
window.title("Cams")

mainFrame = tkinter.Frame(window, width=300, height=300, background= "black")
mainFrame.grid_propagate(False)

lblMove  = tkinter.Label(mainFrame, text="White to move")
lblMove.grid(columnspan = 9, sticky="we")

rows = 8
cols = 8
board = []

for i in range(rows):        # Step 2: Loop through the rows
    row = [0] * cols         # Step 3: Create a list (row) with `cols` number of zeros
    board.append(row)        # Step 4: Append the row to the main array

#print(board)

colourFlag = True

for row in range(8):
    colourFlag= not(colourFlag)
    for col in range(8):
        if(colourFlag):
           board[row][col] = tkinter.Button(mainFrame, font=("Consolas", 50, "bold"), background="blue")
           colourFlag = False
        else:
            board[row][col] = tkinter.Button(mainFrame, background="brown")
            colourFlag  = True

        board[row][col].grid(row=row+1, column=col +1)

reset = tkinter.Button(mainFrame, text="Restart Game", command=new_game)
reset.grid(row=10,columnspan=9, sticky="we")

mainFrame.grid()
window.mainloop()
