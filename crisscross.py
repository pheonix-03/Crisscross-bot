import numpy as np
import random
a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
human = 'O'
ai = 'X'

a = np.array(a)
def checkWinner(ar):
    #rows
    if(ar[0]==ar[1] and ar[1]==ar[2]):
        if(ar[0]=='O'):
            return -1
        elif(ar[0]=='X'):
            return 1
    if(ar[3]==ar[4] and ar[4]==ar[5]):
        if(ar[3]=='O'):
            return -1
        elif(ar[3]=='X'):
            return 1
    if(ar[6]==ar[7] and ar[7]==a[8]):
        if(ar[6]=='O'):
            return -1
        elif(ar[6]=='X'):
            return 1
    #columns
    if(ar[0]==ar[3] and ar[3]==ar[6]):
        if(ar[0]=='O'):
            return -1
        elif(ar[0]=='X'):
            return 1
    if(ar[1]==ar[4] and ar[4]==a[7]):
        if(ar[1]=='O'):
            return -1
        elif(ar[1]=='X'):
            return 1
    if(ar[2]==ar[5] and ar[5]==ar[8]):
        if(ar[2]=='O'):
            return -1
        elif(ar[2]=='X'):
            return 1
    #diagonals
    if(ar[0]==ar[4] and ar[4]==ar[8]):
        if(ar[0]=='O'):
            return -1
        elif(ar[0]=='X'):
            return 1
    if(a[2]==ar[4] and ar[4]==ar[6]):
        if(ar[2]=='O'):
            return -1
        elif(ar[2]=='X'):
            return 1
    c=0
    for i in range(9):
        if(ar[i]!= ' '):
            c=c+1
            #print(c)
    if(c==9):
        return 0

    
def display(board):
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
    print("-----------")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("-----------")
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+" ")
    #print("-----------")
def valid_move(ax,px):
    if ax[px] == ' ':
        return True
    else:
        return False
def best_moves(arx):
    best_score = -10000000000000000000
    best_move  = None
    for i in range(9):
        if(arx[i]==' '):
            arx[i] = ai
            score =  min_max(arx,False)
            arx[i] = ' '
            if(score>best_score):
                best_score = score
                best_move = i 
    #print(best_move)
    return best_move


def min_max(ard,isMaximizing):
    result = checkWinner(ard)
    if(result != None):
        return result
    if(isMaximizing):
        best_score = -1000000000000000000000000000
        for i in range(9):
            if ard[i]==' ':
                ard[i]=ai
                score = min_max(ard,False)
                ard[i]=' '
                best_score = max(best_score,score)
        return best_score
    else:
        best_score = 1000000000000000000000000000
        for i in range(9):
            if ard[i]==' ':
                ard[i]=human
                score = min_max(ard,True)
                ard[i]=' '
                best_score = min(best_score,score)
        return best_score



def enter(axy):
    f=0
    x=0
    #ch = int(input("Who wants to go first??\nYou or the ai\n0 for u and 1 for ai"))1

    while(f==0):
        if x%2 ==0:
            move = int(input("Enter position : "))
            move =move-1
            if valid_move(a,move) == True:
                a[move] = human
                display(axy)
            else:
                print("Error re enter the position :")
                continue
        else:
            m=best_moves(axy)
            if valid_move(axy,m) == True:
                axy[m] = ai
                display(axy)

            else:
                print("Error re enter the position :")
                continue
        x=x+1
        if(x==9):
            f=1
        if(checkWinner(axy)== 1):
            print("The ai won !")
            f=1
        if checkWinner(axy) ==-1:
            print("Human Won that was not Expected of u")
            f=1
        if checkWinner(axy) ==0:
            print("You really played well Congratulations")
            f=1

display(a)
enter(a)
