import random

def guess_the_number():
  secret_number = random.randint(1, 100)

  max_guesses = 7

  print("I'm thinking of a number between 1 and 100. You have 7 guesses to find it.")

  guess_count = 0
  while guess_count < max_guesses:
    guess_count += 1
    try:
      guess = int(input("Enter your guess: "))

      if guess < 1 or guess > 100:
        print("Invalid guess. Please enter a number between 1 and 100.")
        continue

      if guess == secret_number:
        print(f"Congratulations! You guessed the number in {guess_count} guesses!")
        break
      elif guess < secret_number:
        print("Too low. Try again!")
      else:
        print("Too high. Try again!")

    except ValueError:
      print("Invalid input. Please enter a number.")

  if guess_count == max_guesses:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")

guess_the_number()
