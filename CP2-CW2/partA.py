# This program calculates the user's birth_year, handling valueError, prompts the user to enter their name and then uses it in a personalized greeting

# prompts the user to enter their name and stores it in the variable name
name=input('enter your name:')

# Greets the user with a personalized message
print("greetings" +name)

# if the input is numeric, it calculates the birth_year
age=int(input("enter your age:"))
current_year=2024
birth_year=current_year-age
print("you were born in", birth_year)

# handle non-numeric input by showing an aerror message
except ValueError:
print("enter a valid numeric value of your age")
