characterX = 1
characterY = 1

charaterPosition = "| A |"

board = [["|   |" for a in range (3)] for b in range(3)]
print(board)

board[characterX][characterY] = charaterPosition

while True:
    for i in board:
        print("_____ _____ _____")
        print(" ".join(i))
        print("_____ _____ _____")
    print("instructions:")
    print("Up: W")
    print("Down: S")
    print("Left: A")
    print("Right: D")

direction = input("Please enter one of the above options: ")
if direction == "W":
    board[characterX][characterY] = "|   |"
    characterX -= 1
    board[characterX][characterY] = "| A |"
elif direction == "S":
    board[characterX][characterY] = "|   |"
    characterX += 1
    board[characterX][characterY] = "| A |"
elif direction == "A":
    board[characterX][characterY] = "|   |"
    characterY -= 1
    board[characterX][characterY] = "| A |"
elif direction == "D":
    board[characterX][characterY] = "|   |"
    characterY += 1
    board[characterX][characterY] = "| A |"



