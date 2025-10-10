import random
board = [1,2,3,4,5,6,7,8,9]
board=[1,2,3,4,5,6,7,8,9]
playing=True
while playing:
    print(f"{board[0]}  {board[1]}  {board[2]}\n {board[3]}  {board[4]}  {board[5]}\n{board[6]}  {board[7]}  {board[8]}")

    while True:
        computer = random.randint(1,9)
        player = input("Choose a spot (1-9) to place your X: ")
        turn = board.append("X",player-1)
        
        c_turn = board.append("O",computer-1)
        

        if player(1, "X") and player(2, "X") and player(3, "X"):
            print ("you won")
            
        elif player(4, "X") and player(5, "X") and player(6, "X"):
            print ("you won")

        elif player(7, "X") and player(8, "X") and player(9, "X"):
            print ("you won")

        elif player(1, "X") and player(5, "X") and player(9, "X"):
            print ("you won")

        elif player(7, "X") and player(5, "X") and player(3, "X"):
            print ("you won")
        elif player (1, "X") and player (4, "X") and player (7,"X"):
            print("You win!")
        elif player (2, "X") and player (5, "X") and player (8,"X"):
            print("You win!")
        elif player (3, "X") and player (6, "X") and player (9,"X"):
            print("You win!")

        elif computer (1, "O") and computer (2, "O") and computer (3,"O"):
            print("Computer wins!")

        elif computer (4, "O") and computer (5, "O") and computer (6,"O"):
            print("Computer wins!")

        elif computer (7, "O") and computer (8, "O") and computer (9,"O"):
            print("Computer wins!")
        elif computer(1, 'O') and computer(5, 'O') and computer(9, 'O'):
            print("Computer wins")

        elif computer(7, 'O') and computer(5, 'O') and computer(3, 'O'):
            print("Computer wins")

        elif computer(1, 'O') and computer(4, 'O') and computer(7, 'O'):
            print("computer wins")

        elif computer(2, 'O') and computer(5, 'O') and computer(8, 'O'):
            print("computer wins")

        elif computer(3, 'O') and computer(6, 'O') and computer(9, 'O'):
            print("computer wins")

        else:
            print("Tie")
