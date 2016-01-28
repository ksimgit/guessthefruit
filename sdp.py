import random

def chooseFruit():
    fruits = [fruit.rstrip('\n') for fruit in open('Fruits.txt')]
    selected_fruit = random.choice(fruits)
    return selected_fruit

def intro(fruit):
    print("Feeling up for a challenge? Lets play 'Guess the Fruit'!")
    num_of_letters = len(fruit)
    print("The fruit you have to guess has " + str(num_of_letters) + " letters")
    print("You have 6 guesses")

def displayGame(fruit):
    display_fruit = fruit.lower()
    display_fruit_temp = list(display_fruit)
##  print(display_fruit_temp)
    guesses = []
    for i in range(6):
        print("This is guess number " + str(i+1))
        guess = input("Enter any letter of the alphabet as your guess: ")
        guesses.append(guess)
        word_length = len(display_fruit_temp)
        blanks = list("_" * word_length)
        for l in range(0, word_length):
            for guess in guesses:
                if guess == display_fruit_temp[l]:
                    blanks[l] = guess
        print(" ".join(blanks))
        guess_word = input("Enter your guessed word in lowercase, or enter 'n' to guess another letter: ")
        if guess_word == 'n':
            continue
        elif guess_word == display_fruit:
            print("You have guessed the word correctly! Congratulations!")
            playAgain = input("Enter y to play again, q to quit: ")
            if playAgain == 'y':
                main()
            elif playAgain == 'q':
                print("You have decided to quit. Exiting the game now...")
                exit()
            else:
                print("Please enter y or q: ")
        else:
            print("Incorrect guess")
            continue
    print("You have used up your guesses")
    print("The secret fruit was " + display_fruit)
    
def main():
    chosen_fruit = chooseFruit()
    intro(chosen_fruit)
    displayGame(chosen_fruit)
    
main()
