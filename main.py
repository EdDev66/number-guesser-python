import random

print("I'm thinking of a number between 1 and 100")
difficulty = input('Choose a difficulty. Type easy or hard: ')
chosen_number = random.randint(1,100)
lifes = 0
game_over = False

if difficulty == 'easy':
    lifes = 10
elif difficulty == 'hard':
    lifes = 5


while not game_over:
    if lifes == 0:
        game_over = True
        print('Game over!')
        break
    print(f"You have {lifes} attempts remaining to guess the number.")
    guess = int(input('Make a guess: '))
    if guess != chosen_number:

        if guess > chosen_number:
            print('Too high')
            print('Guess again')
        if guess < chosen_number:
            print('Too low')
            print('Guess again')

    if guess == chosen_number:
        print('Correct! You win!')
        game_over = True

    lifes -= 1