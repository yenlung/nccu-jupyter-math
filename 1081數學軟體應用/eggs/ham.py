from random import randint

n = randint(1, 100)

cont = True

while cont:
    guess = int(input("你猜哪個數字?"))
    if guess > n:
        print("太大了!")
    elif guess < n:
        print("太小了!")
    else:
        print("太神了!")
        cont = False