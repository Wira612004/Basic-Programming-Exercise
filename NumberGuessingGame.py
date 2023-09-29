# random number guessing  game
# Wira Harsa | TI22I
from random import randint


def user_name():
    name = str(input("what is your name?"))
    return name.upper()


def user_input():
    while True:
        try:
            key = int(input("guess a number="))

        except:
            print("that is not not a valid integer value for limit")
        else:
            return key

# scoring system
def user_score():
    return turns*10

# hints for the player.only if chose to take hints
def hint():
    if turns == 7:
        while True:
            opt = str(input("do you want a hint[y or n]"))
            if opt.upper() == 'Y':
                print(f"the ans lies between {ans - c} and {ans + d}")
                break
            elif opt.upper() == 'N':
                pass
            else:
                print('that is not a valid input')
    if turns == 3:
        while True:
            option = str(input("do you want a hint?[y or n]"))
            if option.upper() == 'Y':
                print(f"the answer lies between {ans - a} and {ans + b} ")
                break
            elif option.upper() == 'N':
                pass
            else:
                print('that is not a valid input')

if __name__ == "__main__":
    Name = user_name()
    #  variables used for hints in the later code
    c = randint(1, 10)
    d = 10-c
    a = randint(1, 5)
    b = 5 - a
    ans = randint(1, 100)
    turns = 10
    print("the guess the number between 1 and 100 ")

    while turns > 0:
        guess = user_input()
        if guess != ans:
            turns = turns - 1
        if guess == ans:
            print(f"congratulations  {Name}, you won the game \n your score is {user_score()}")
            break
        elif (guess - ans) > 5:
            print("you are far away from the answer")
            print(f"you have turns {turns} left ")
        else:
            print("you are near the answer")
            print(f"you have turns {turns} left ")
        hint()
        if guess == ans:
            print(f" you won the game \n your score is {user_score()}")
            break


    if turns == 0:
        print(f'''sorry {Name}, you lost the game
                        better luck next time
                        your score is {user_score()} points''')
        print(f"the answer is {ans}")
