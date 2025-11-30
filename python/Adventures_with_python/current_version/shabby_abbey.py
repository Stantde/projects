"""
    Shabby Abbey v2: 
    Obtain a command from the player and manipulate it.
    DS
    11-30-2025
"""
# Annotate variable
command: str

# Greet player.
print("Welcome, Adventurer!")

# Obtain the player's command and manipulate it.
command = input("What is your command? ")
print(f"Your command is {command}.")

'''
match expression:
    case pattern1:
        # code block for pattern1
    case pattern2:
        # code block for pattern2
    case _:  # default case
        # code block for no match
'''