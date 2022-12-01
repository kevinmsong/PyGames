import numpy as np
import sys

board = np.zeros((6, 7), dtype = "str")
print("WELCOME TO CONNECT FOUR")

def drop_piece(column, piece):  
  if column < 1 or column > 7:
    print("Make sure to pick a column between 1 and 7 that is not full\n")
    return
  
  if piece != "X" and piece != "O":
    print("Make sure to use either an \'X\' or an \'O\' as your piece\n")
    return

  this_column = board[:, column - 1]
  counter = 0

  for item in this_column:
    if item == "X" or item == "O":
      counter += 1
  
  if counter >= 6:
    print("Make sure to pick a column between 1 and 7 that is not full\n")
    return

  if this_column[-1] == "":
    this_column[-1] = piece
    print("Placed an " + piece + " in column " + str(column) + "\n")
  
  else:
    for i in range(len(this_column) - 1, -1, -1):
      if this_column[i] != "X" and this_column[i] != "O":
        this_column[i] = piece
        print("Placed an " + piece + " in column " + str(column) + "\n")
        break

  print(board)
  print("")

def run_game():
  while(True):
    column = int(input("Column for X: "))
    drop_piece(column, "X")
    column = int(input("Column for O: "))
    drop_piece(column, "O")

run_game()
