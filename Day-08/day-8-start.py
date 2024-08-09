# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet(user, location):
    """This function greets a user."""
    print(f"Hello {user}!")
    print(f"How are you doing {user}?")
    print(f"What's it like in {location}?")


user = input("Type your name: ")
location = input("Where are you located? ")
greet(user, location)


def greet_with_keyword(user="Mike", location="USA"):
    """This function greets a user."""
    print(f"Hello {user}!")
    print(f"How are you doing {user}?")
    print(f"What's it like in {location}?")


greet_with_keyword()
