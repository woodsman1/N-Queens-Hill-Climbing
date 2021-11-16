import random
import utility

def get_next_move(h, board):

  next_moves_h = {}
  n = len(board)

  for col in range(0, n):
    for row in range(n):
      if board[col] == row: continue

      temp_board = board.copy()
      temp_board[col] = row
      next_moves_h[(col, row)] = utility.get_heuristic_cost(n, temp_board)

  min_h_moves = []
  min_h = h

  # finding min heuristic value from the list of all possible moves
  for value in next_moves_h.values():
    if value < min_h:
      min_h = value

  # make a list of the moves with min heuristic values
  for cordinates, value in next_moves_h.items():
    if value == min_h:
      min_h_moves.append(cordinates)


  ####### without sideways move (strict condition)
  # if(min_h == h): return False, h, -1, -1  


  # select any random moves from the list of min heuristic moves
  if len(min_h_moves) > 0:
    x = random.randint(0, len(min_h_moves)-1)
    return True, min_h, min_h_moves[x][0], min_h_moves[x][1]
  else: 
    return False, min_h, -1, -1



def hillClimbing(n , board):
  h = utility.get_heuristic_cost(n, board)
  new_h = 0
  cnt = 0

  while(cnt < 20):
    flag, new_h, col, row = get_next_move(h, board)

    if(flag == False):
      utility.print_board(board)
      print("h(final) =", h)
      print("number of moves = ", cnt)
      print("Faliure : Reached local maximum")
      return board, h
    elif new_h==0:
      board[col] = row
      utility.print_board(board)
      print("h(final) =", new_h)
      print("number of moves = ", cnt)
      print("Success : Reached Goal Sate")
      return board, h
    else:
      board[col] = row

    h = new_h

    ### printing board after every move
    # print()
    # utility.print_board(board)
    # print("h =",new_h)
    # print()

    cnt+=1
  
  
  utility.print_board(board)
  print(cnt)
  print("Faliure : Sideways Move or Local Maximum")

  return board, new_h



if __name__ == "__main__":
  n = 8
  board = utility.generate_board(n)

  print("Initial = ", )
  utility.print_board(board)

  print("\nFinal")
  board, h = hillClimbing(n, board)
  
