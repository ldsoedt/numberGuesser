import random # imports the random module which will let you use the random module and all functionality
high = 100
low = 1
r= random.randrange(low,high) # generate a random number between a 100 not inclusive to the 100
print(r)
r= random.randint(low,high) # will generate a random number that will include the 100

user_score = 0
user_guess = input(f"Guess the randomly generated number between {low} and {high}: ") #gets input from the user for their guess
while user_guess != r: # start of while loop
    if user_guess.isdigit(): # checks if the number is a digit
        user_guess = int(user_guess) # converts the guess into a integer if it is a digit

        if user_guess < low or user_guess > high: #checks if the guess is in the range
            print("select an integer within the range") # gives feed back and asks the user to guess again
            user_guess = input(f"Guess the randomly generated number between {low} and {high}: ")
            user_score += 1  # increments the user score up by one for each guess
        elif user_guess > r: # checks if the guess is bigger than r
            print("Too high pick something lower") # gives feed back and asks the user to guess again
            user_guess = input(f"Guess the randomly generated number between {low} and {high}: ")
            user_score += 1 # increments the user score up by one for each guess
        elif user_guess < r: # checks if guess is less than r
            print("Too low pick something higher") # gives feed back and asks the user to guess again
            user_guess = input(f"Guess the randomly generated number between {low} and {high}: ")
            user_score += 1  # increments the user score up by one for each guess
    else: # if the number isn't valid
        print("value is not a valid number pick something else") #will say so and ask the user to pick again
        user_guess = input(f"Guess the randomly generated number between {low} and {high}: ")

user_guess += 1
print(f"you are correct number was {r} you got it in {user_score} guesses") #when the loop ends (number is guessed) it will say correct and pring the number

