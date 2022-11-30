# 09.07.2021 07:14 Completed
# Tic Tac Toe Game
# This is small program


def print_ttt_banner():
    print()
    print_ttt_table({"x": [0, 2, 4, 6, 8], "o": [1, 3, 5, 7]})
    print("This is Tic Tac Toe Game.")
    print("1 - Single player\n"
          "2 - Two player\n"
          "0 - Exit")


def print_ttt_table(x={"x": [], "o": []}, winner=(0,)):  # winner(0-1, who win, win items)
    # Print x or o in tic tac toe table
    # If empty print index number

    # Create an empty table
    y = {"x": [], "o": [], "empty": [0, 1, 2, 3, 4, 5, 6, 7, 8]}

    # Update table according to x
    y.update(x)
    for i in range(9):
        if i in y["x"] or i in y["o"]:
            y["empty"].remove(i)
    # print(y)

    # Create a list for make printing easy
    z = []
    for i in range(9):
        if i in y["x"]:
            z.append("-X-")
        elif i in y["o"]:
            z.append("-O-")
        else:
            z.append(f"[{i}]")
    # print(z)

    # If some win modify z
    if winner[0]:
        for i in winner[2]:
            if z[i] == "-X-":
                z[i] = "*X*"
            elif z[i] == "-O-":
                z[i] = "*O*"

    # Define a row generator for table
    def table(no, values=[]):
        tbl = [
            "|         |         |         |",
            "|    x    |    x    |    x    |",
            "+---------+---------+---------+"
        ]
        if no == 1:
            print(f"|   {values[0]}   |   {values[1]}   |   {values[2]}   |")
        else:
            print(tbl[no])

    # Print table
    table(2)
    for i in range(3):
        table(0)
        table(1, z[i*3:(i*3+3)])
        table(0)
        table(2)

    # Print if winner is here
    if winner[0]:
        print(f" WINNER IS || {winner[1].upper()} || CONGRATULATIONS")


def print_round_status(n):
    # Print round number
    print(f"Round: {int((n/2) + 1)}")

    # Print whose turn
    print(f"Turn for {'X' if n % 2 == 0 else 'O'}")

    # Also return whose turn
    return 'x' if n % 2 == 0 else 'o'


def check_round_status(tbl):
    # For all win situations
    win_list = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # Check for someone won
    for i in tbl:
        for j in win_list:
            for k in j:
                if k not in tbl[i]:
                    break
            else:
                # Someone won the game, Return who and which blocks
                return [1, i, j]

    # Check if table is full
    if len(tbl["x"]) + len(tbl["o"]) == 9:
        return [0]  # Table is full

    return [2]  # keep going


def start_ttt():
    # Initialize table
    print("\nCreating table.\n")
    available_places = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    current_table = {"x": [], "o": []}

    # Lets start
    n = 0
    while True:
        # Print table and status for active user then get user input
        print_ttt_table(current_table)
        active_player = print_round_status(n)
        move = input("Enter number: ")

        # Check if move available then make move and remove it from available places
        if move not in available_places:
            print(f"Invalid or unavailable input. Try again.")
            continue
        current_table[active_player].append(int(move))
        available_places.remove(move)

        # Check status, if game is not over add 1 to n and continue
        status = check_round_status(current_table)
        if status[0] == 2:
            pass
        elif status[0] == 1:
            print_ttt_table(current_table, status)
            break
        elif status[0] == 0:
            print_ttt_table(current_table)
            print("TABLE IS FULL, NO WINNER.")
            break
        n += 1


def start_ttt_single():

    def move_handler():
        from random import choice

        def random_move():
            return choice(available_places)

        def intel_move():
            def my_func():
                x = [
                    [0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]
                ]
                if bot_plays == "x":
                    y = current_table["o"]
                else:
                    y = current_table["x"]
                answer = []
                for j in x:
                    n = 0
                    for i in j:
                        if i in y:
                            n += 1
                    if n == 2:
                        for i in j:
                            if i not in y and str(i) in available_places:
                                answer.append(str(i))
                return answer
            if "4" in available_places:
                return "4"
            if "4" not in available_places and len(available_places) == 8:
                return choice(["1", "3", "5", "7"])
            answer = my_func()
            if len(answer) > 0:
                return choice(answer)
            else:
                return random_move()

        def insane_move():
            def my_func(other=0):
                x = [
                    [0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]
                ]
                if bot_plays == "x":
                    if other:
                        y = current_table["x"]
                    else:
                        y = current_table["o"]
                else:
                    y = current_table["x"]
                answer = []
                for j in x:
                    n = 0
                    for i in j:
                        if i in y:
                            n += 1
                    if n == 2:
                        for i in j:
                            if i not in y and str(i) in available_places:
                                answer.append(str(i))
                return answer
            if "4" in available_places:
                return "4"
            if "4" not in available_places and len(available_places) == 8:
                return choice(["1", "3", "5", "7"])
            answer = my_func()
            answer_other = my_func(1)
            if len(answer_other) > 0:
                return choice(answer_other)
            elif len(answer) > 0:
                return choice(answer)
            else:
                return random_move()

        if bot_difficulty == 0:
            return random_move()
        elif bot_difficulty == 1:
            m1 = random_move()
            m2 = intel_move()
            if m2:
                return choice([m1, m2])
            return m1
        elif bot_difficulty == 2:
            return intel_move()
        elif bot_difficulty == 3:
            return insane_move()
    # Initialize table
    print("\nCreating table.\n")
    available_places = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    current_table = {"x": [], "o": []}
    bot_difficulty = ""  # make different difficulties
    bot_plays = "o"  # X or O

    # Set bot who is starting first
    if input("Do you want to play first or want to bot start?(me/BOT)") not in ["me", "ME", "Me"]:
        bot_plays = "x"

    # Set bot difficulty
    bot_difficulty = input("Difficult?(0-easy, 1-medium, 2-hard, 3-insane)")
    if bot_difficulty in ["easy", "0"]:
        bot_difficulty = 0
        print("Easy bot selected.")
    elif bot_difficulty in ["medium", "1"]:
        bot_difficulty = 1
        print("Medium bot selected")
    elif bot_difficulty in ["hard", "2"]:
        bot_difficulty = 2
        print("Hard bot selected")
    elif bot_difficulty in ["insane", "3"]:
        bot_difficulty = 3
        print("Insane bot selected")
    else:
        bot_difficulty = 0
        print("Default difficult will be selected (easy)")
    # Lets start
    n = 0
    while True:
        # If bot moves make move else print table and status then get user input
        if (bot_plays == "x" and n % 2 == 0) or (bot_plays == "o" and n % 2 == 1):
            move = move_handler()
            current_table[bot_plays].append(int(move))
            available_places.remove(move)
        else:
            print_ttt_table(current_table)
            active_player = print_round_status(n)
            move = input("Enter number: ")

            # Check if move available then make move and remove it from available places
            if move not in available_places:
                print(f"Invalid or unavailable input. Try again.")
                continue
            current_table[active_player].append(int(move))
            available_places.remove(move)

        # Check status, if game is not over add 1 to n and continue
        status = check_round_status(current_table)
        if status[0] == 2:
            pass
        elif status[0] == 1:
            print_ttt_table(current_table, status)
            break
        elif status[0] == 0:
            print_ttt_table(current_table)
            print("TABLE IS FULL, NO WINNER.")
            break
        n += 1


while True:
    print_ttt_banner()
    x = input()
    if x == "0":
        break
    elif x == "1":
        while True:
            start_ttt_single()
            if input("Do you want to play again?(y/N)") in ["y", "Y", "yes", "YES", "yea"]:
                continue
            break
    elif x == "2":
        while True:
            start_ttt()
            if input("Do you want to play again?(y/N)") in ["y", "Y", "yes", "YES", "yea"]:
                continue
            break

print("Exiting...")
