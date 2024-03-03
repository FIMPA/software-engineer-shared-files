"""
START
Created file called age-quiz to be used to display a variety of responses determined by
the data the user enters.
END

"""
age = input("Please, enter your age: ")            # Prompt the user to enter their age
age_int = int(age)                                 # Change value age to integer

if age_int < 13:
    print("You qualify for the kiddie discount.")

elif age_int == 21:
    print("Congrats on your 21st!")

elif age_int >= 40 and age_int < 65:
    print("Your're over the hill.") 

elif age_int >= 65 and age_int <= 100:
    print("Enjoy your retirement!")

elif age_int > 100:
    print("Sorry, you're dead.")

else:
    print("Age is but a number.")