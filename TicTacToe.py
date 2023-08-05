def check(board,mark):
    if(board[0][0]==board[0][1]==board[0][2]!='' or board[1][0]==board[1][1]==board[1][2]!='' or board[2][0]==board[2][1]==board[2][2]!='' or board[0][0]==board[1][0]==board[2][0]!='' or board[0][1]==board[1][1]==board[2][1]!='' or board[0][2]==board[1][2]==board[2][2]!='' or board[0][0]==board[1][1]==board[2][2]!='' or board[0][2]==board[1][1]==board[2][0]!=''):
        print(mark,"Wins😁")
        exit()
    else:
        return
          
def printboard(board):
    print("\t",board[0][0],"\t|\t",board[0][1],"\t|\t",board[0][2],"\t")
    print("--------------------------------------------------")
    print("\t",board[1][0],"\t|\t",board[1][1],"\t|\t",board[1][2],"\t")
    print("--------------------------------------------------")
    print("\t",board[2][0],"\t|\t",board[2][1],"\t|\t",board[2][2],"\t")
    return

def addToBoard(board,mark):
    print("Enter the cell number to add ",mark," : ",end=' ')
    cell=int(input())
    row=int(cell/len(board))
    column=int(cell%len(board))
    if(board[row][column]==''):
        board[row][column]=mark
        printboard(board)
        check(board,mark)
    else:
        print("Already Filled😞")
        addToBoard(board,mark)

print("Welcome To Tic Tac Toe!")
print("Board: -")
print("\t0 \t|\t 1 \t|\t 2\t")
print("--------------------------------------------------")
print("\t3 \t|\t 4 \t|\t 5\t")
print("--------------------------------------------------")
print("\t6 \t|\t 7 \t|\t 8\t")
print("X goes first...")
board = [['','',''],['','',''],['','','']]
for i in range(9):
    if(i%2==0):
        addToBoard(board,'X')
    else:
        addToBoard(board,'O')
print("Tie😐")
