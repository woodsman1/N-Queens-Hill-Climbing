import random
import utility
import time

def get_next_move(h, board, flag=False):
  """
  moving each queen up and down in their column
  and calculating the h value for each move and then random move
  from the list of all minimum moves and
  return ture if we get the min move else false with
  h value of min move and cordinates of that move 
  """

  next_moves_h = {}
  n = len(board)

  for col in range(0, n):
    for row in range(n):
      if board[col] == row: continue # skipping the original state

      ## for every possible move get_heuristic value and store that move
      ## with value in the dictionary with its h value
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


  ####### without sideways move 
  if flag and min_h == h: return False, h, -1, -1  


  # select any random moves from the list of min heuristic moves
  if len(min_h_moves) > 0:
    x = random.randint(0, len(min_h_moves)-1)
    return True, min_h, min_h_moves[x][0], min_h_moves[x][1]
  else: 
    return False, min_h, -1, -1



def hillClimbing(n , board, test = False):
  """
  Implementation of hillClimbing algorithum
  """
  
  h = utility.get_heuristic_cost(n, board)
  
  if not test:
    print("h(Initial) =", h)
  
  new_h = 0
  cnt = 0


  ## loop till the limit or till the goal state is achieved
  while(cnt < 1000):
    ## get optimal next moves 
    flag, new_h, col, row = get_next_move(h, board)


    if(flag == False):    ## No optimal moves obtained
      if not test:
        print("\nFinal = ")
        utility.print_board(board)
        print("h(final) =", h)
        print("number of moves = ", cnt)
        print("Faliure : Reached local maximum")
      return False, cnt, board, h
    elif new_h==0:       ## Reached the goal state
      board[col] = row
      if not test:
        print("\nFinal = ")
        utility.print_board(board)
        print("h(final) =", new_h)
        print("number of moves = ", cnt)
        print("Success : Reached Goal Sate")
      return True, cnt, board, h
    else:               ## Optimal move in obtained
      board[col] = row

    h = new_h

    ### printing board after every move

    # print()
    # utility.print_board(board)
    # print("h =",new_h)
    # print()

    cnt+=1
  
  ## reached the limit of moves but goal state no achieved
  if not test:
    print("\nFinal = ")
    utility.print_board(board)
    print(cnt)
    print("Faliure : Sideways Move or Local Maximum")

  return False, cnt, board, new_h



if __name__ == "__main__":

  begin = time.time()
  time.sleep(0.3)

  n = 8
  board = utility.generate_board(n)

  print("Initial = ", )
  utility.print_board(board)

  # print("\nFinal")
  _ , cnt, board, h = hillClimbing(n, board)


  end = time.time()

  print(f"Total runtime = {(end-begin-0.3)*1000} ms")

  print()
  
