# Some programming exercises for iteration

# for loop
# Loop through numbers from 1 to 10 (inclusive of 1, exclusive of 11)
for i in range(1, 11):
    # Print the current number 'i' and its square 'i**2'
    print(i, i**2)
    
    # Check if the current number 'i' is equal to 5
    if i == 5:
        # Exit the loop when 'i' reaches 5
        break




print('__________________')
# Loop through numbers from 1 to 10 (inclusive of 1, exclusive of 11)
for i in range(1, 11):
    # Check if the current number 'i' is equal to 5
    if i == 5:
        # Print a message indicating that 'i = 5' will be skipped
        print("i = 5 is skipped")
        # Skip the rest of the loop iteration for 'i = 5'
        continue
    
    # Print the current number 'i' and its square 'i**2' for all other numbers
    print(i, i**2)


print('__________________')
# Create a list of friends' names
friends = ["ali", "sara", "ava", "pedram", "padra", "parsa", "pouya"]

# Loop through each name in the 'friends' list
for comp in friends:
    # Print a greeting message for each friend
    print("salam", comp)





print('__________________')
# Initialize a counter variable to 0
count = 0

# Create a list of friends' names
friends = ["ali", "sara", "ava", "pedram", "padra", "parsa", "pouya"]

# Loop through each name in the 'friends' list
for comp in friends:
    # Print a greeting message for each friend
    print("salam", comp)
    
    # Increment the counter by 1 after each greeting
    count += 1

# After the loop, print the total number of greetings
print(count, "times of greeting")



print('__________________')
# Ask the user to input a number and convert it to an integer
number = int(input("Please insert a number"))

# Initialize a counter variable to track the number of inputs
count = 0

# Initialize a sum variable to accumulate the total of the numbers entered
sum = 0

# Start a while loop that continues until the user enters -1
while number != -1:
    # Print the current number
    print("number", number)
    
    # Add the current number to the running total (sum)
    sum = sum + number
    # Print the updated sum
    print("sum", sum)
    
    # Increment the counter by 1 to track how many numbers have been entered
    count += 1
    # Print the current count
    print("count", count)
    
    # Ask the user for another number and update the 'number' variable
    number = int(input("Please insert a number"))

# After exiting the loop (when -1 is entered), calculate and print the average of the numbers entered
print('average', sum / count)

