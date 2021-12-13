import sys

boardvalue = ["1", "2", "3",
              "4", "5", "6",
              "7", "8", "9", ]


def board(boardvalue):
    k = 0
    for i in range(1, 6):
        j = i + k
        if i % 2 != 0:
            print(boardvalue[j - 1], " |", boardvalue[j], "|", boardvalue[j + 1])
            k += 1
        else:
            print("---", "---", "---")


def game():
    while True:
        Player1 = input("Select your choice 'X' or 'O' \n")
        if Player1 == "O" or Player1 == "X":
            if Player1 == "O":
                Player2 = "X"
            else:
                Player2 = "O"
            break
        else:
            print('please enter appropriate value\n')
    print("Player 1 = %s" % Player1)
    print("Player 2 = %s " % Player2)
    currentplayer = Player1
    count = 1

    while True:
        try:
            uturn = int(input("Enter the board value where you want to place your %s \n" % currentplayer))
            move = uturn - 1
            print(move)
            if uturn in range(1, 10):
                if "1" <= boardvalue[move] <= "9":
                    boardvalue[move] = currentplayer

                    if 9 > count > 4:
                        win(currentplayer)
                    elif count == 9:
                        print("it is a tie!!!!")
                        repeat()
                    board(boardvalue)
                    if currentplayer == Player1:
                        currentplayer = Player2
                        count += 1
                    else:
                        currentplayer = Player1
                        count += 1

                else:
                    print("Please enter appropriate place to enter")
            else:
                print("Please number from 0-9")
        except ValueError:
            print("Please enter number not string")


def repeat():
    ans = input("Would you like to play again \n1. Yes \n 2. No")
    if ans == "Yes":
        k = 0
        for i in range(0, 9):
            boardvalue[i] = str(i + 1)
        board(boardvalue)
        game()
    else:
        quit()


def win(currentPlayer):
    if boardvalue[0] == boardvalue[1] == boardvalue[2] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[3] == boardvalue[4] == boardvalue[5] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[6] == boardvalue[7] == boardvalue[8] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[0] == boardvalue[3] == boardvalue[6] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[0] == boardvalue[4] == boardvalue[8] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[1] == boardvalue[4] == boardvalue[7] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[2] == boardvalue[5] == boardvalue[8] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()
    elif boardvalue[2] == boardvalue[4] == boardvalue[6] == currentPlayer:
        print("Player %s won \n" % currentPlayer)
        repeat()


board(boardvalue)
game()
