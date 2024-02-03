import random
def play(a):
    b=0
    count=0
    while b!=a:
        b=int(input())
        if a>b:
            print("Your guess is too low.")
        elif b>a:
            print("Your guess is too high")
        count+=1
    print(f"Good job, KBTU! You guessed my number in {count}  guesses!")

print("Well, KBTU, I am thinking of a number between 1 and 20.\nTake a guess.")
random_number = random.randint(1, 20)
play(random_number)
