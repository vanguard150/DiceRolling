import random

if __name__ == '__main__':
    min = 1
    max = 6
    roll_again = "yes"
    print("test github1")
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are ...")
        print(random.randint(min,max))
        print(random.randint(min, max))
        roll_again = input("Roll the dice again? ")

