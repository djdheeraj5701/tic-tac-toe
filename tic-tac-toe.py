'''
minimax algo
inefficient for larger n as it is recursive approach
presumed to be O((n*n)!)
'''

def isWon(n,board,player):
    pos=[]
    marker='X'*(player==0)+'O'*(player==1)
    for i in range(n):
        for j in range(n):
            if board[i][j]==marker:
                pos.append((i,j))
    for p in range(len(pos)):
        i,j=pos[p]
        if (i,j+1) in pos[p+1:] and (i,j+2) in pos[p+1:]:  # row
            return True
        if (i+1,j) in pos[p+1:] and (i+2,j) in pos[p+1:]:  # col
            return True
        if (i+1,j+1) in pos[p+1:] and (i+2,j+2) in pos[p+1:]:  # diag1
            return True
        if (i+1,j-1) in pos[p+1:] and (i+2,j-2) in pos[p+1:]:  # diag2
            return True
    return False

def tictactoe(n,board,player,filled):
    me=1
    if me==0 and filled==0:
        return ((n//2,n//2),0)
    if isWon(n,board,player^1):
        # print((player+1)%2,n*n-filled+1)
        if player!=me:
            return 1  # n*n-filled+1
        return -1  # (n*n-filled+1)*-1
    if filled==n*n:
        # print("Draw")
        return 0

    positions=[]
    values =[]
    for i in range(n):
        for j in range(n):
            if board[i][j]=='-':
                positions.append((i,j))
                board[i][j]='X'*(player==0)+'O'*(player==1)
                t=tictactoe(n,board,player^1,filled+1)
                if type(t)==int:
                    values.append(t)
                else:
                    values.append(t[1])
                board[i][j] = '-'
    # print(positions)
    # print(values)
    # print()
    if player==me:
        i=values.index(max(values))
        return positions[i],values[i]
    i = values.index(min(values))
    return positions[i],values[i]

def getNewBoard(n):
    b=[]
    for i in range(n):
        x=[]
        for j in range(n):
            x.append("-")
        b.append(x)
    return b

def displayBoard(board):
    for k in board:
        print(*k)
    print()

n=3
filled=0
board=getNewBoard(n)
player=0
mark=['X','O']
while filled!=n*n:
    if player:
        p,v=tictactoe(n,board,player,filled)
    else:
        p=list(map(int,input("dj move: ").split()))
    board[p[0]][p[1]]=mark[player]
    player^=1
    filled+=1
    displayBoard(board)
    if isWon(n,board,player^1):
        break