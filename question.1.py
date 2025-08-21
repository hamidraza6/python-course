# number=[] 
# num=int(input("enter number:"))
# 
# Prompt the user to enter the number of elements they want to add
num_elements = int(input("Enter the number of elements: "))

# Create an empty list to store the numbers
numbers = []

# Use a for loop to iterate for the specified number of times
for i in range(num_elements):
    user_input = int(input(f"Enter number {i + 1}: "))
    numbers.append(user_input)

# Print the resulting list
print("The list of numbers is:", numbers)