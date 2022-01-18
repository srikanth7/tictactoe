theBoard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '}

turn = 'x'
isRunning = True
winner = None

def winpos(board,value):
    pos = None
    l = list(board.values())
    for i in l:
        if i=='x':
            l[l.index(i)] = 3
        elif i == 'o':
            l[l.index(i)] = 5
        else:
            l[l.index(i)] = 2
    
    if l[0]*l[1]*l[2]==value:
        if l[0]==2:
            return 1
        if l[1]==2:
            return 2
        if l[2]==2:
            return 3
    elif l[3]*l[4]*l[5]==value:
        if l[3]==2:
            return 4
        if l[4]==2:
            return 5
        if l[5]==2:
            return 6
    elif l[6]*l[7]*l[8]==value:
        if l[6]==2:
            return 7
        if l[7]==2:
            return 8
        if l[8]==2:
            return 9
    elif l[0]*l[4]*l[8]==value:
        if l[0]==2:
            return 1
        if l[4]==2:
            return 5
        if l[8]==2:
            return 9
    elif l[2]*l[4]*l[6]==value:
        if l[2]==2:
            return 3
        if l[4]==2:
            return 5
        if l[6]==2:
            return 6
    elif l[0]*l[3]*l[6]==value:
        if l[0]==2:
            return 1
        if l[3]==2:
            return 4
        if l[6]==2:
            return 7
    elif l[1]*l[4]*l[7]==value:
        if l[1]==2:
            return 2
        if l[4]==2:
            return 5
        if l[7]==2:
            return 8
    elif l[2]*l[5]*l[8]==value:
        if l[2]==2:
            return 3
        if l[5]==2:
            return 6
        if l[8]==2:
            return 9
    else:
        return 0

def makemove(board):
    pos = None
    if board['5'] == " " and winpos(board,50)==0 and winpos(board,18)==0:
        pos = 5
    elif board['1'] == " " and winpos(board,50)==0 and winpos(board,18)==0:
        pos = 1
    elif board['3'] == " " and winpos(board,50)==0 and winpos(board,18)==0:
        pos = 3
    elif board['7'] == " " and winpos(board,50)==0 and winpos(board,18)==0:
        pos = 7
    elif board['9'] == " " and winpos(board,50)==0 and winpos(board,18)==0:
        pos = 9
    elif winpos(board,50):
        pos = winpos(board,50)
    elif winpos(board,18):
        pos = winpos(board,18)
    return pos

def printBoard(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['7']+'|'+board['8']+'|'+board['9'])

def playerinput(board,turn):
    while True:
        inp = int(input("enter b/w the 1-9..."))
        if inp>=1 and inp<=9 and board[str(inp)] == ' ':
            board[str(inp)] = turn
            break
        else:
            print('Oops!!!')
            printBoard(theBoard)

def diag(board):
    if board['1'] == board['5'] == board['9'] != ' ':
        winner = board['5']
        return True
    if board['3'] == board['5'] == board['7'] != ' ':
        winner = board['5']
        return True

def horizantal(board):
    if board['1'] == board['2'] == board['3'] != ' ':
        winner = board['1']
        return True
    if board['4'] == board['5'] == board['6'] != ' ':
        winner = board['5']
        return True
    if board['7'] == board['8'] == board['9'] != ' ':
        winner = board['9']
        return True

def vertical(board):
    if board['1'] == board['4'] == board['7'] != ' ':
        winner = board['1']
        return True
    if board['2'] == board['5'] == board['8'] != ' ':
        winner = board['5']
        return True
    if board['3'] == board['6'] == board['9'] != ' ':
        winner = board['9']
        return True

def checkTie(board):
    if ' ' not in board.values():
        return True
    return False

def checkwin():
    if diag(theBoard) or horizantal(theBoard) or vertical(theBoard):
        if turn == "o":
            print("The "+ turn +" player won...")
        printBoard(theBoard)
        isRunning = False
        return False
    elif checkTie(theBoard):
        print("It's a Tie... XOXOXOX")
        printBoard(theBoard)
        isRunning = False
        return False
    return True

def computer(board):
    while turn == 'o':
        #position = random.randint(1, 9)
        position = makemove(board) 
        if board[str(position)] == ' ':
            board[str(position)] = 'o'
            print("After AI's Turn: ")
            switchPlayer()

def switchPlayer():
    global turn
    if turn == 'o':
        turn = 'x'
    else:
        turn = 'o'
    
while isRunning:
    printBoard(theBoard)
    playerinput(theBoard,turn)
    isRunning = checkwin()
    if isRunning:
        switchPlayer()
        printBoard(theBoard)
        computer(theBoard)
        isRunning = checkwin()
