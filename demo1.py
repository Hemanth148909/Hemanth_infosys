#!/usr/bin/env python3

# This is a simple Python script

def greet(name):
    """Function to greet the user."""
    return f"Hello, {name}!"

def main():
    """Main function to execute the script."""
    print("Welcome to the basic Python script!")

    # Prompt the user for their name
    user_name = input("What's your name? ")

    # Call the greet function and display the message
    greeting = greet(user_name)
    print(greeting)

if __name__ == "__main__":
    main()
