import hillClimb
import randomRestart
import simulatedAnealing
import utility
import time


if __name__ == "__main__":
  t_test = 15
  t = t_test
  n = 16

  t_time1 = 0
  t_time2 = 0
  t_time3 = 0

  success1 = 0
  success2 = 0
  success3 = 0

  steps1 = 0
  steps2 = 0
  steps3 = 0

  while t:
    # print(t)
    board = utility.generate_board(n)
    board1 = board.copy()
    board2 = board.copy()
    board3 = board.copy()

    ## hillClimbing
    begin = time.time()
    time.sleep(0.1)
    
    flag, cnt, *_ =hillClimb.hillClimbing(n, board1, True)

    end = time.time()

    if flag:
      success1+=1
      steps1 += cnt

    t_time1 += (end-begin-0.1)*1000

    
    ## Random Restart
    begin = time.time()
    time.sleep(0.1)

    flag, cnt, *_ = randomRestart.randomRestartHillClimbing(n, board2, True)  

    end = time.time()

    if flag:
      success2 +=1
      steps2 += cnt

    t_time2 += (end-begin-0.1)* 1000


    ## Simulated Annealing
    begin = time.time()
    time.sleep(0.1)

    flag, cnt, *_ = simulatedAnealing.annealing(n, board)

    end = time.time()

    if flag:
      success3+=1
      steps3 += cnt

    t_time3 += (end-begin-0.1)* 1000

    t-=1

  # print Result

  print("Results")

  print(f"total tests = {t_test}")
  print(f"value of n = {n}")

  print("*********** Hill Climbing With sideways moves ***********")

  print(f'Total Success = {success1}')
  print(f'Total Faliure = {t_test-success1}')
  print(f'Avreage Steps of Success = {steps1/t_test}')
  print(f'Average Time Taken = {t_time1/t_test} ms')
  print()

  print("******************* Random Restart  ********************")

  print(f'Total Success = {success2}')
  print(f'Total Faliure = {t_test-success2}')
  print(f'Avreage Steps of Success = {steps2/t_test}')
  print(f'Average Time Taken = {t_time2/t_test} ms')
  print()

  print("*****************  Simulated Annealing  *****************")

  print(f'Total Success = {success3}')
  print(f'Total Faliure = {t_test-success3}')
  print(f'Avreage Steps of Success = {steps3/t_test}')
  print(f'Average Time Taken = {t_time3/t_test} ms')
  print()

  print("************************** end **************************")