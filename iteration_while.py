# Iteration -while

# Initialize the variable 'n' with the value 10
n = 10

# Start a while loop that continues as long as 'n' is less than or equal to 10
while n <= 10:
    # Print the current value of 'n'
    print(n)
    
    # Decrease the value of 'n' by 1
    n -= 1
    
    # Check if 'n' is equal to 0
    if n == 0:
        # Print a message indicating that zero has been reached
        print("you reached zero!")
        
        # Exit the loop immediately using 'break'
        break

# Print a message indicating that the loop has ended
print("out of the loop")




# Ask the user to enter their name and store it in the variable 'name'
name = input("what is your name? ")

# Start a while loop that continues until the user types "end"
while name != "end":
    # Print a greeting with the provided name
    print("hello", name)
    
    # Ask for the name again to avoid an infinite loop
    name = input("what is your name? ")  # If this line is missing, the loop will run infinitely


    # Break out of the loop immediately after printing the greeting
    break  # This will stop the loop after the first iteration
