# Sample Coding Questions 01 Week 01
# Blen Abebe

# 1. Defining Variables
# Define an array variable with the following elements: 1, 4, 7, 9
array = [1, 4, 7, 9]

# 2. Order of Operations
# Define 4 variables a, b, c, d with values 1, 2, 3, 4
a, b, c, d = 1, 2, 3, 4

# Fully-Bracketed Version of: e = a * c - b / d
e = (a * c) - (b / d)

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
# ** is exponentiation, // is floor division, and % is modulus
e = ((a - ((b ** c) // d)) + (a % c))

# 3. Formatting
# Create a variable called “temperature” with the value 32.6
temperature = 32.6
# Print the sentence with formatting
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# 4. Common Functions
# Ask the user to input their age
userAge = int(input("Enter your age: "))
# Add 22 to the userAge
userAge += 22
# Print the sentence with the updated age
print(f"Now showing the shop items filtered by age: {userAge}")
