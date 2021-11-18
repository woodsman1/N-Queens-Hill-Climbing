import hillClimb
import utility
import time

def randomRestartHillClimbing(n, board):
  """
  Implemeting RandomRestart
  """

  h = utility.get_heuristic_cost(n, board)
  print("h(Initial) =", h)
  new_h = 0
  cnt = 0
  restart_cnt = 0

  while(cnt < 40):
    ## True because we dont want to move sideways instead we want to Restart again.
    flag, new_h, col, row = hillClimb.get_next_move(h, board, True)  

    if(flag == False):
      ## Random Restart by creating new random Board
      restart_cnt+=1
      board = utility.generate_board(n)
      new_h = utility.get_heuristic_cost(n, board)

    elif new_h==0:
      ## Goal State (heuristic value = 0)
      board[col] = row
      print("\nFinal = ")
      utility.print_board(board)
      print("h(final) =", new_h)
      print("number of restart = ", restart_cnt)
      print("number of steps = ", cnt)
      print("Success : Reached Goal Sate")
      return board, h
    else:
      board[col] = row

    h = new_h

    ## printing board after every move
    # print()
    # utility.print_board(board)
    # print("h =",new_h)
    # print()

    cnt+=1
  
  print("\nFinal = ")
  utility.print_board(board)
  new_h = utility.get_heuristic_cost(n, board)
  print("h(final) =", new_h)

  print("number of steps = ", cnt)
  print("Faliure : Moves Limit Exceeded")

  return board, new_h



if __name__ == "__main__":
  begin = time.time()
  time.sleep(0.3)

  n = 8
  board = utility.generate_board(n)

  print("Initial = ", )
  utility.print_board(board)

  board, h = randomRestartHillClimbing(n, board)


  end = time.time()

  print(f"Total runtime = {(end-begin-0.3)*1000} ms")

  print()
  