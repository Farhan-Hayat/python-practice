import random

# user_input = input("choose one :")

option_display = """
OPTIONS:
1-A
2-B
3-C
4-D
"""


def game():
    # variables
    points = 0
    cond = True
    stage = 1
    max_stage = 20
    # start
    while (stage <= max_stage and cond):
        print("-----STAGE {}-----".format(stage))
        if stage % 5 == 0 and stage > 0:
            print("\nTotal points: {}".format(int(points)), option_display)
            print("You can hit big!!")
            user_input = int(input("choose one option:"))
            big_hit = random.randint(1, 4)
            if user_input == big_hit:
                points = points + (stage * 5)
                print("THERE YOU GO!! a {} point hit!!".format(stage * 5))
            else:
                print("Better luck next time")
                points = points + 10
                stage = stage + 1   

        else:

            wrong_option = random.randint(1, 4)
            print("\nTotal points: {}".format(int(points)), option_display)
            user_input = int(input("choose one option:"))
            if user_input == wrong_option:
                if points < 5:
                    print("you need at least 5 points to keep playing.")
                    cond = False
                else:
                    print("You want to continue! use your points (points:{})".format(int(points)))
                    print("1-Yes      2-No")
                    ans = int(input("Continue?"))
                    if ans == 1:
                        points = points / 2
                    else:
                        cond = False
            else:
                if user_input< 4:
                    points = points + 10
                    stage = stage + 1   
                    
                    
    # end
    return points


points = game()

print("Your Total points are " + str(int(points)))
