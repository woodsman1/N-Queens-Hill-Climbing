import hillClimb
import utility


def randomRestartHillClimbing(n, board):
  h = utility.get_heuristic_cost(n, board)
  print("h(Initial) =", h)
  new_h = 0
  cnt = 0
  restart_cnt = 0

  while(cnt < 20):
    flag, new_h, col, row = hillClimb.get_next_move(h, board, True)

    if(flag == False):
      # utility.print_board(board)
      restart_cnt+=1
      board = utility.generate_board(n)
      new_h = utility.get_heuristic_cost(n, board)
      # print("Faliure : Reached local maximum")
    elif new_h==0:
      board[col] = row
      utility.print_board(board)
      print("h(final) =", new_h)
      print("number of restart = ", restart_cnt)
      print("number of steps = ", cnt)
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
  print("Faliure : Moves Limit Exceeded")

  return board, new_h



if __name__ == "__main__":
  n = 8
  board = utility.generate_board(n)

  print("Initial = ", )
  utility.print_board(board)

  print("\nFinal")
  board, h = randomRestartHillClimbing(n, board)
  