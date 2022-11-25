# Import required libraries
import random as rm

# Function to check who won the game


def won():
	if (player == ai):
		print("\nAI Won\n")
	else:
		print("\nYou Won\n")


# Driver Code
i = rm.randint(1, 2)  # AI chooses 'X' or 'O'

# Decide who will start the game ('X' starts the game)
if (i == 1):
	ai = 1
	human = 2
	player = ai
	opponent = human

else:
	ai = 2
	human = 1
	player = human
	opponent = ai

print("\nX = 1 , O = 2")
print("\nAI -", ai)
print("Human -", human)

# Blank - 0, X - 1, O - 2
board = [1, 0, 2, 2, 2, 0, 1, 0, 1]

# All possible moves
move_table = [
	[[1, 1, 2, 2, 2, 0, 1, 0, 1],
            [1, 0, 2, 2, 2, 1, 1, 0, 1],
            [1, 0, 2, 2, 2, 0, 1, 1, 1]],
	[[1, 1, 2, 2, 2, 2, 1, 0, 1],
            [1, 1, 2, 2, 2, 0, 1, 2, 1]],
	[[1, 2, 2, 2, 2, 1, 1, 0, 1],
            [1, 0, 2, 2, 2, 1, 1, 2, 1]],
	[[1, 1, 2, 2, 2, 1, 1, 2, 1]],
	[[1, 2, 2, 2, 2, 1, 1, 1, 1]],
]

print("\nBoard is :", board)
print("\n-------------------------------------------------")

# Game starts
j = 0
for i in range(2):
	# AI's Turn
	if (player == ai):
		print("\nAI's Turn")

		print("\nThe Possible Moves are :")
		for move in range(len(move_table[j])):
			print("Move {} = {} " .format(move, move_table[j][move]))

		k = rm.randint(0, len(move_table[j])-1)
		print("\nAI's Move is: Move", k)
		board = move_table[j][k]
		print("\nBoard is :", board)
		print("\n-------------------------------------------------")

    # Human's Turn
	else:
		print("\nYour Turn")

		print("\nThe Possible Moves are :")
		for move in range(len(move_table[j])):
			print("Move {} = {} " .format(move, move_table[j][move]))

		T = 1
		while (T > 0):
			k = int(input("\nEnter the number of move you want to play: "))
			print("\nYour Move is: Move", k)

			if (k > len(move_table[j])-1):
				print("\nWrong Move. Play Again!!")
			else:
				board = move_table[j][k]
				print("\nBoard is :", board)
				print("\n-------------------------------------------------")
				break

	# Check if anyone won or a tie
	if (k == 2):  # X won
		won()
		break

	elif (board == move_table[1][0]):
		won()  # O won

	elif (board == move_table[1][1]):
		board = move_table[3][0]
		print("\nFinal Board is :", board)
		print("\n-------------------------------------------------")

		print("\nIt is a Tie\n")

	elif (board == move_table[2][0]):  # X won
		player, opponent = opponent, player
		board = move_table[4][0]
		print("\nFinal Board is :", board)
		print("\n-------------------------------------------------")
		won()

	elif (board == move_table[2][1]):
		board = move_table[3][0]
		print("\nFinal Board is :", board)
		print("\n-------------------------------------------------")

		print("\nIt is a Tie\n")

	elif (k == 0):
		j = 1

	elif (k == 1):
		j = 2

	# Decide whose turn is it now
	player, opponent = opponent, player
