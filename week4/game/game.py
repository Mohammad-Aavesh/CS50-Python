from random import randint

def main():
    while(True):
        Input = input("Level: ")
        if Input.isdigit() and Input > "0":
            target = randint(1,int(Input))
            Guess(target)
            return

def Guess(target):
    while(True):
        guess = input("Guess: ")
        if guess.isdigit() and guess > "0":
            guess = int(guess)
            if guess > target:
                print("Too large!")
            elif guess < target:
                print("Too small!")
            else:
                print("Just right!")
                return

main()
