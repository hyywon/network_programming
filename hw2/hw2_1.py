from random import randint

player = 50

while True:
    ans = int(input())
    coin = randint(1,2)
    if ans == coin :
        player += 9
        # print("Correct! Player : {0}".format(player))
    elif ans != coin:
        player -= 10
        # print("Wrong! Player : {0}".format(player))

    if  player < 0 or player == 100:
        break