import math
import random
import utility
import time


def make_annealing_move(n, board, h, temprature):
  """
  make a random move 
  if result in optimal move accept it
  else analyse the risk based on that take decision
  return new board with accepted move 
  """
  temp_board = list(board)
  found = False
 
  while not found:
    temp_board = list(board)

    ## Select any random move
    new_row = random.randint(0,n-1)
    new_col = random.randint(0,n-1)
    temp_board[new_col] = new_row
    new_h = utility.get_heuristic_cost(n, temp_board)

    ## if optimal then accept it
    if new_h < h:
      found = True
    else:
      ## else measure the risk. If risky reject it else accept it
      delta_e = h - new_h
      accept_prob = min(1,math.exp(delta_e/temprature))
      found = random.random() <= accept_prob
   
  return temp_board


def annealing(n, board):
  """
  get the accepted move and then cools the temrature value
  till the goal state is obtained
  """
  temprature = n**2
  cooling_rate = 0.95
  h = utility.get_heuristic_cost(n, board)
  steps = 0
   
  while h > 0:
    board = make_annealing_move(n, board,h, temprature)
    h = utility.get_heuristic_cost(n, board)

    #Make sure temprature doesn't get impossibly low
    n_temp = max(temprature * cooling_rate,0.01)
    temprature = n_temp

    # print()
    # utility.print_board(board)

    steps+=1
    if steps >= 10000:
      break
  
  return steps, board



if __name__ == "__main__":

  begin = time.time()
  time.sleep(0.3)

  n = 8
  board = utility.generate_board(n)

  print("Initial = ", )
  utility.print_board(board)

  print("\nFinal = ")
  steps, board = annealing(n, board)
  
  
  utility.print_board(board)
  h = utility.get_heuristic_cost(n, board)

  print("h (final) =", h)
  print("step count = ", steps)

  if h != 0:
    print("Faliure : Moves Limit Exceeded")
  else:
    print("Success : Reached Goal Sate")

  end = time.time()

  print(f"Total runtime = {(end-begin-0.3)*1000} ms")

  print()