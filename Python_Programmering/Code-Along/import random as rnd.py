import random as rnd 
# rnd_numb = rnd.randint(1, 101)
rnd_numb = 55
# guess = rnd.randint(1, 100)
low = 1
high = 100
# guess = 0
guesses = 0


while True:
    print(f"Guess a number between 1 - 100: {guess}")
    guess = (low + high) // 2

    if guess > rnd_numb:
        print(f"{guesses}: Guess too high, try again...\n")
        guesses = guesses + 1
        high = guess - 1 
        
    elif guess < rnd_numb:
        print(f"{guesses}: Guess too low, try again...\n")
        guesses = guesses + 1
        low = guess + 1
    else:
        print(f"{guesses}: You won!")
        break