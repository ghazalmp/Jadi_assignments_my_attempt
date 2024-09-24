#condition (if-elif-else)

# Ask the user to input their first name and store it in the variable 'name'
name = input("please insert your name: ")

# Ask the user to input their family name and store it in the variable 'family_name'
family_name = input("please insert your family_name: ")

# Check if both the first name and family name match specific values
if name == "ghazal" and family_name == "sardari":
    # If both conditions are true, print a special greeting
    print("hello myself")
    
# Check if the first name is "ghazal" but the family name is not "sardari"
elif name == "ghazal" and family_name != "sardari":
    print("hello " + name)

# Check if the first name is not "ghazal" but the family name is "sardari"
elif name != "ghazal" and family_name == "sardari":
   
    print("hello Miss./Mr." + family_name)

# If none of the previous conditions are met (meaning neither name nor family name matches the specified conditions)
else:
    print("hello stranger")
