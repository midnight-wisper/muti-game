import random
import os
import time
import colorama

# ----------- TO-DO ----------- #
# 1. ADD BINARY SEARCH TO ROBOT
# 2. MAKE RPS SMARTER
# 3. MAKE DICE ROLLING GAME MORE ADVANCED AND STYLED
# 4. OVERALL IMPROVMENT OF STYLE FOR ALL GAMES AND CMDS
# ----------------------------------------------------------


def color(string, color_name, style=''):
    return color_name + style + string + colorama.Style.RESET_ALL


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(color('we have multiple games for u to play. pick one! do "help" to see them all', colorama.Fore.MAGENTA))
name = input(
    color("some games use a name. please enter your name: ", colorama.Fore.BLUE))

while True:
    clear()
    print(color('----------- Menu ----------- ',
          colorama.Fore.BLACK, colorama.Style.BRIGHT))
    user_command = input(color("enter a cmd (q to quit): ",
                         colorama.Fore.MAGENTA, colorama.Style.BRIGHT)).lower()
    # ----------- HELP: ----------- #
    if user_command == 'help':

        print(
            f'hello {name}, here are a list of commands and games you can use')
        print('---------- GAMES/COMMANDS ----------')
        print('"q" | exits the program\n')
        print('"RPS" | starts rock paper scissors\n')
        print('"num guess" | starts number guessing game (remix)\n')
        print('"roll dice" | rolls a dice\n')
        print('"random game" | suggests a game you should start')
        print("------------------------------------")
    # ----------- QUIT: ----------- #
    elif user_command == 'q':
        print(f'exiting... thank you for playing {name}')
        break
    # ----------- RPS: ----------- #
    elif user_command == 'rps':
        print('clearing..')
        time.sleep(1)
        clear()
        print('LAUNCHED ROCK PAPER SCISSORS\n')
        print('welcome to rock paper scissors')
        start_questRPS = input('do you want to start (y/n): ').lower()
        if start_questRPS == "y":
            score_humanRPS = 0
            score_computerRPS = 0
            RPS_list = ["rock", "paper", "scissors"]
            print('compuer name: joe')

            while True:
                computer_handRPS = random.choice(RPS_list)
                hand_humanRPS = input(
                    color(f"pick a hand (out of 10): ", colorama.Fore.CYAN))

                if hand_humanRPS == 'paper' and computer_handRPS == 'rock':
                    print(color(f'{name} (you) has won', colorama.Fore.GREEN))
                    score_humanRPS += 1
                    print(color
                          (f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif computer_handRPS == 'paper' and hand_humanRPS == 'rock':
                    print(color(f'joe (computer) has won', colorama.Fore.RED))
                    score_computerRPS += 1
                    print(color(
                        f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif computer_handRPS == 'rock' and hand_humanRPS == 'scissors':
                    print(color(f'joe (computer) has won', colorama.Fore.RED))
                    score_computerRPS += 1
                    print(color(
                        f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif hand_humanRPS == 'rock' and computer_handRPS == 'scissors':
                    print(color(f'{name} (you) has won', colorama.Fore.GREEN))
                    score_humanRPS += 1
                    print(color(
                        f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won",
                              colorama.Fore.GREEN, colorama.Style))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif computer_handRPS == 'rock' and computer_handRPS == 'scissors':
                    print(color(f'joe (computer) has won', colorama.Fore.RED))
                    score_computerRPS += 1
                    print(color(
                        f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))

                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif hand_humanRPS == 'scissors' and computer_handRPS == 'paper':
                    print(color(f'{name} (you) has won', colorama.Fore.GREEN))
                    score_humanRPS += 1
                    print(color(
                        f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif computer_handRPS == 'scissors' and hand_humanRPS == 'paper':
                    print(color(f'{name} (you) has won', colorama.Fore.GREEN))
                    score_humanRPS += 1
                    print(color(
                        f'score is now: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif hand_humanRPS == 'rock' and computer_handRPS == 'rock':
                    print(f'TIE GAME. no one won')
                    print(color(
                        f'score is still: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif hand_humanRPS == 'paper' and computer_handRPS == 'paper':
                    print(f'TIE GAME. no one won')
                    print(color(
                        f'score is still: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                elif hand_humanRPS == 'scissors' and computer_handRPS == 'scissors':
                    print(f'TIE GAME. no one won')
                    print(color(
                        f'score is still: human: {score_humanRPS} VS computer: {score_computerRPS}', colorama.Fore.BLACK))
                    if score_computerRPS == 10:
                        print(color('GAME OVER! computer won', colorama.Fore.RED))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break
                    elif score_humanRPS == 10:
                        print(color("GAME OVER! human won", colorama.Fore.GREEN))
                        time.sleep(1)
                        print(color(f'Returning to Menu...',
                              colorama.Fore.GREEN, colorama.Style.DIM))
                        time.sleep(3)
                        clear()
                        break

                else:
                    print(
                        color('please enter a valid hand. (rock, paper or scissors)', colorama.Fore.RED))

        elif start_questRPS == "n":
            print("come back when your ready")
            continue
    # ----------- NUMBER GUESS: ----------- #
    elif user_command == 'num guess':

        lost = False
        while True:
            print('"help" to see list of modes')
            num_guessMODE = input(color
                                  ('pick a mode (q to return to menu): ', colorama.Fore.CYAN)).lower()

            if num_guessMODE == 'help':
                print('---------- MODES ----------')
                print('num guess: normal number guessing game. no modifiers')
                print(
                    'difficulty: difficulty mode has 3 diffculites (easy, medium, hard) you see them as u peak each difficulty')
                print('robot/robot difficulty: you play against a robot to see who guesses the numbers first. u can either do "robot diffculity" or normal "robot" "robot diffculity" is robot but with diffculites')
                print('------------------------------------')
            elif num_guessMODE == 'q':
                print(color('returning to menu...', colorama.Fore.RED))
                time.sleep(2)
                clear()
                break

            elif num_guessMODE == 'num guess':

                random_num = random.randint(1, 100)
                print(color("welcome to number guessing game!", colorama.Fore.GREEN))
                guesses = 0

                while True:
                    guess = int(
                        input(color("enter a guess (1, 100): ", colorama.Fore.BLUE)))

                    if guess > 100 or guess < 1:
                        print("INVALID. guess a number between 1 - 100")

                    elif guess > random_num:
                        print(color("to high! try again", colorama.Fore.RED))
                        guesses += 1

                    elif guess < random_num:
                        print(color("to low! try again", colorama.Fore.RED))
                        guesses += 1

                    else:
                        print(f"you got it with {guesses} wrong tries")
                        break

            elif num_guessMODE == 'q':
                break

            elif num_guessMODE == 'difficulty':
                difficulty = 'easy'
                difficulty_score = 0
                if difficulty == 'easy':
                    print(color('number guessing game (easy)',
                          colorama.Fore.GREEN, colorama.Style.BRIGHT))
                    print(
                        color('guess a number between 1 - 100. you have 10 guesses', colorama.Fore.GREEN))
                    random_numEASY = random.randint(1, 100)

                    for easy in range(1, 15):
                        guess = int(
                            input(color("enter a guess (1, 100): ", colorama.Fore.BLUE)))

                        if guess > random_numEASY:
                            print(color("to high! try again", colorama.Fore.RED))
                            if easy == 14:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numEASY}')
                                break

                        elif guess < random_numEASY:
                            print(color("to low! try again", colorama.Fore.RED))
                            if easy == 14:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numEASY}')
                                break

                        else:
                            print(color('you got it! good job\n',
                                  colorama.Fore.GREEN))
                            print(color('proceeding to next difficulty...\n',
                                  colorama.Fore.LIGHTGREEN_EX))
                            difficulty_score += 1
                            break

                    print(color('number guessing game (medium)',
                          colorama.Fore.YELLOW, colorama.Style.BRIGHT))
                    print(
                        color('guess a number between 1 - 300. you have 10 guesses', colorama.Fore.YELLOW))
                    random_numMED = random.randint(1, 300)

                    for medium in range(10):
                        guess = int(
                            input(color("enter a guess (1, 300): ", colorama.Fore.BLUE)))

                        if guess > random_numMED:
                            print(color("to high! try again", colorama.Fore.RED))
                            if medium == 9:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numMED}')
                                break

                        elif guess < random_numMED:
                            print(color("to low! try again", colorama.Fore.RED))
                            if medium == 9:
                                print(
                                    'aww your all out of tries!')
                                print(
                                    color(f'it was {random_numMED}', colorama.Fore.BLACK))
                                break

                        else:
                            print(color('you got it! good job\n',
                                  colorama.Fore.GREEN))
                            print(color('proceeding to next difficulty...\n',
                                  colorama.Fore.LIGHTGREEN_EX))
                            difficulty_score += 1
                            break

                    print(color('number guessing game (hard)',
                          colorama.Fore.RED, colorama.Style.BRIGHT))
                    print(
                        color('guess a number between 1 - 300. you have 10 guesses', colorama.Fore.RED))
                    random_numHARD = random.randint(1, 500)

                    for hard in range(5):
                        guess = int(
                            input(color("enter a guess (1, 500): ", colorama.Fore.BLUE)))

                        if guess > random_numHARD:
                            print(color("to high! try again", colorama.Fore.RED))
                            if hard == 4:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numHARD}')
                                break

                        elif guess < random_numHARD:
                            print(color("to low! try again", colorama.Fore.RED))
                            if hard == 4:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numHARD}')
                                break

                        else:
                            print('you got it! good job\n')
                            difficulty_score += 1
                            break

                    print('GAME OVER!\n')

                    print(color('---------- RESULTS ----------', colorama.Fore.GREEN))
                    print(
                        color(f'loses: you got {difficulty_score}/3', colorama.Fore.BLUE, colorama.Style.BRIGHT))
                    print(
                        color('------------------------------------', colorama.Fore.GREEN))
                    input(color('type any key to contiune: ',
                          colorama.Fore.BLACK, colorama.Style.BRIGHT))
                    time.sleep(0.25)
                    clear()

            elif num_guessMODE == 'robot':
                random_numRO = random.randint(1, 100)
                robot_listGUESSES = range(1, 100)
                print(color("welcome to number guessing game!", colorama.Fore.GREEN))
                guessesRO = 0
                guesses_robot = 0

                while True:
                    robot_guess = random.choice(robot_listGUESSES)
                    guessRO = int(
                        input(color("enter a guess (1, 100): ", colorama.Fore.BLUE)))

                    if guessRO > 100 or guessRO < 1:
                        print("INVALID. guess a number between 1 - 100")
                        if not robot_guess == random_numRO:
                            guesses_robot += 1

                    elif guessRO > random_numRO:
                        print(color("to high! try again", colorama.Fore.RED))
                        print(
                            color(f'ROBOTS GUESS: {robot_guess}', colorama.Fore.CYAN))
                        guessesRO += 1
                        if not robot_guess == random_numRO:
                            guesses_robot += 1

                    elif guessRO < random_numRO:
                        print(color("to low! try again", colorama.Fore.RED))
                        print(
                            color(f'ROBOTS GUESS: {robot_guess}', colorama.Fore.CYAN))
                        guessesRO += 1
                        if not robot_guess == random_numRO:
                            guesses_robot += 1

                    elif robot_guess == random_numRO:
                        print(color(
                            f'joe (computer) has won with {robot_guess} wrong tries', colorama.Fore.RED, colorama.Style.BRIGHT))
                        print(
                            color(f'number was {random_numRO}', colorama.Fore.CYAN, colorama.Style.DIM))
                        break

                    elif guessRO == random_numRO:
                        print(color(f"{name} (you) has won with {guessesRO} wrong tries",
                              colorama.Fore.GREEN, colorama.Style.BRIGHT))
                        break

            elif num_guessMODE == 'robot difficulty':
                robot_guesses = 0
                difficulty = 'easy'
                difficulty_score = 0
                difficulty_scoreRO = 0
                if difficulty == 'easy':
                    print(color('number guessing game (easy)',
                          colorama.Fore.GREEN, colorama.Style.BRIGHT))
                    print(
                        color('guess a number between 1 - 100. you have 10 guesses', colorama.Fore.GREEN))
                    random_numEASY = random.randint(1, 100)

                    for easy in range(1, 15):
                        robot_guess = random.choice(range(1, 100))
                        guess = int(
                            input(color("enter a guess (1, 100): ", colorama.Fore.BLUE)))

                        if guess > random_numEASY:
                            print(color("to high! try again", colorama.Fore.RED))
                            print(
                                color(f'robots guess: {robot_guess}', colorama.Fore.RED))

                            if easy == 14:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numEASY}')
                                print('robot has also lost')

                        elif guess < random_numEASY:
                            print(color("to low! try again", colorama.Fore.RED))
                            print(
                                color(f'robots guess: {robot_guess}', colorama.Fore.RED))

                            if easy == 14:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numEASY}')
                                print('joe (robot) has also lost')
                                break

                        elif guess == random_numEASY:
                            print(color('you got it! good job\n',
                                  colorama.Fore.GREEN))
                            print(color('proceeding to next difficulty...\n',
                                  colorama.Fore.LIGHTGREEN_EX))
                            difficulty_score += 1
                            break

                        elif robot_guess == random_numEASY:
                            print('JOE (ROBOT HAS WON)')
                            print('proceeding to text difficulty \n',
                                  colorama.Fore.LIGHTGREEN_EX)
                            difficulty_scoreRO += 1
                            break

                    print(color('number guessing game (medium)',
                          colorama.Fore.YELLOW, colorama.Style.BRIGHT))
                    print(
                        color('guess a number between 1 - 300. you have 10 guesses', colorama.Fore.YELLOW))
                    random_numMED = random.randint(1, 300)

                    for medium in range(10):
                        robot_guessMED = random.choice(range(1, 300))
                        guess = int(
                            input(color("enter a guess (1, 300): ", colorama.Fore.BLUE)))

                        if guess > random_numMED:
                            print(color("to high! try again", colorama.Fore.RED))
                            print(
                                color(f'robots guess: {robot_guessMED}', colorama.Fore.RED))

                            if medium == 9:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numMED}')
                                print('joe (robot) has also lost')
                                break

                        elif guess < random_numMED:
                            print(color("to low! try again", colorama.Fore.RED))
                            print(
                                color(f'robots guess: {robot_guessMED}', colorama.Fore.RED))

                            if medium == 9:
                                print(
                                    'aww your all out of tries!')
                                print(
                                    color(f'it was {random_numMED}', colorama.Fore.BLACK))
                                print('joe (robot) has also lost')
                                break

                        elif guess == random_numMED:
                            print(color('you got it! good job\n',
                                  colorama.Fore.GREEN))
                            print(color('proceeding to next difficulty...\n',
                                  colorama.Fore.LIGHTGREEN_EX))
                            difficulty_score += 1
                            break

                        elif robot_guessMED == random_numMED:
                            print('JOE (ROBOT HAS WON)')
                            print('proceeding to text difficulty \n',
                                  colorama.Fore.LIGHTGREEN_EX)
                            difficulty_scoreRO += 1
                            break
                    print(color('number guessing game (hard)',
                          colorama.Fore.RED, colorama.Style.BRIGHT))
                    print(
                        color('guess a number between 1 - 500. you have 5 guesses', colorama.Fore.RED))
                    random_numHARD = random.randint(1, 500)

                    for hard in range(5):
                        robot_guessHARD = random.choice(range(1, 500))
                        guess = int(
                            input(color("enter a guess (1, 500): ", colorama.Fore.BLUE)))

                        if guess > random_numHARD:
                            print(color("to high! try again", colorama.Fore.RED))
                            print(
                                color(f'robots guess: {robot_guessHARD}', colorama.Fore.RED))

                            if hard == 4:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numHARD}')
                                print('joe (robot) has also lost')
                                break

                        elif guess < random_numHARD:
                            print(color("to low! try again", colorama.Fore.RED))
                            print(
                                color(f'robots guess: {robot_guessHARD}', colorama.Fore.RED))

                            if hard == 4:
                                print(
                                    'aww your all out of tries!')
                                print(f'it was {random_numHARD}')
                                print('joe (robot) has also lost')
                                break

                        elif guess == random_numHARD:
                            print('you got it! good job\n')
                            difficulty_score += 1
                            break

                        elif robot_guessHARD == random_numHARD:
                            print('JOE (ROBOT HAS WON)')
                            print('proceeding to text difficulty \n',
                                  colorama.Fore.LIGHTGREEN_EX)
                            difficulty_scoreRO += 1

                    print('GAME OVER!\n')

                    print(color('---------- RESULTS ----------', colorama.Fore.GREEN))
                    print(
                        color(f'loses: you got {difficulty_score}/3', colorama.Fore.BLUE, colorama.Style.BRIGHT))
                    print(color(
                        f'robot loses: joe has got {difficulty_scoreRO}/3', colorama.Fore.BLUE, colorama.Style.BRIGHT))

                    print(
                        color('------------------------------------', colorama.Fore.GREEN))
                    input(color('type any key to contiune: ',
                          colorama.Fore.BLACK, colorama.Style.BRIGHT))
                    time.sleep(0.25)
                    clear()
    # ----------- ROLL DICE: ----------- #
    elif user_command == 'roll dice':
        print(color('rolling dice...',
              colorama.Fore.GREEN, colorama.Style.BRIGHT))

        dice = ['1', '2', '3',
                '4', '5', '6']

        dice_result = random.choice(dice)

        print(color(f'result: dice landed on ', colorama.Fore.GREEN) +
              color(f'{dice_result}', colorama.Fore.GREEN, colorama.Style.BRIGHT))
    # ----------- RANDOM GAME: ----------- #
    elif user_command == 'random game':
        games = ['number guess', 'rock paper scissors']
        random_game = random.choice(games)
        print(color(f'joe: you should try {random_game}',
              colorama.Fore.BLUE, colorama.Style.BRIGHT))
        RM_quit = input('enter to go to menu: ')
    # ----------- error: ----------- #
    else:
        print(color('please use a valid command ("help" to see commands)',
              colorama.Fore.RED, colorama.Style.BRIGHT))
        for number in range(1, 4):
            print(color(f'returnning in {number}',
                  colorama.Fore.BLACK, colorama.Style.DIM))
            time.sleep(1)
