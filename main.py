def printBoard(xState, oState):
    p = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        p[i] = 'X' if xState[i] else ('O' if oState[i] else i)
        
    print(f"{p[0]} | {p[1]} | {p[2]}")
    print("—————————")
    print(f"{p[3]} | {p[4]} | {p[5]}")
    print("—————————")
    print(f"{p[6]} | {p[7]} | {p[8]}")
    print("\n")

def winner(xState, oState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(xState[win[0]] + xState[win[1]] + xState[win[2]] == 3):
            print("X won")
            return 1
        if(oState[win[0]] + oState[win[1]] + oState[win[2]] == 3):
            print("O won")
            return 0
    return -1

def game():
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1

    while True:
        printBoard(xState, oState)

        if turn == 1:
            value = int(input("Player1(X)'s turn, enter your place: "))
            print("\n")

            if value in range(0,9):
                if xState[value] or oState[value] == 1:
                    print("Invalid move\n")
                    continue
                else:
                    xState[value] = 1
            else:
                print("Invalid number\n")
                continue
        else:
            value = int(input("Player2(O)'s turn, enter your place: "))
            print("\n")
            
            if value in range(0,9):
                if xState[value] or oState[value] == 1:
                    print("Invalid move\n")
                    continue
                else:
                    oState[value] = 1
            else:
                print("Invalid number\n")
                continue

        won = winner(xState, oState)
        if(won != -1):
            break
        
        turn = 1 - turn

print("Welcome to this 2 player tic-tac-toe!\n")
game()
