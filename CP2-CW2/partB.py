try:
    favorite_number = int(input("insert your favorite number: ")) 

    # check if the number is odd or even
    if favorite_number % 2 == 0: 
            print("Your favorite number is even")
    else:
        print("Your favorite number is odd")

    #chained and nested conditonals basing on the favorite_number.
    if favorite_number > 10:
        print("Your favorite number is greater than 10.")
    elif favorite_number < 10:
        print("Your favorite number is less than 10.")
    else:
        print("Your favorite number is equal to 10.")

    except ValueError: 
print("enter a valid numeric value")




Testing and Debugging
Error: syntax error 
Let us remove a colon from the if statement on line 5
Result: Python will raise a syntax error.
solution: Add the missing character, save the program and the run it.


Errors:
NameError: Resolved by verifying that variables are well named.
SyntaxError: Resolved by ensuring all syntax is correct.
ValueError: Resolved by try-except blocks.