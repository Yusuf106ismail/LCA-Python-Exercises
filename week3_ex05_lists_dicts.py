# Question 1: Creating and Modifying Lists

# Create a list of fruits
fruits = ["apple", "banana", "orange"]

# Add a fruit to the end of the list
fruits.append("grape")

# Insert a fruit at the beginning of the list
fruits.insert(0, "mango")

# Remove a fruit from the list
fruits.remove("banana")

# Print the modified list
print("Modified fruits list:", fruits)


# Question 2: List Operations

# Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]

# Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# Print the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Sum:", total)
print("Average:", average)


# Question 3: Creating and Modifying Dictionaries

# Create a dictionary of countries and their capitals
countries = {
    "South Africa": "Pretoria",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Add a new country-capital pair
countries["Germany"] = "Berlin"

# Update the capital of an existing country
countries["South Africa"] = "Cape Town"

# Remove a country-capital pair
countries.pop("France")

# Print the modified dictionary
print("Modified countries dictionary:", countries)


# Question 4: Dictionary Operations

# Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Print all the fruits (keys)
print("Fruits:", fruit_colors.keys())

# Print all the colors (values)
print("Colors:", fruit_colors.values())

# Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(fruit, "is", color)

# Check if a fruit is in the dictionary and print its color
fruit_to_check = "apple"

if fruit_to_check in fruit_colors:
    print(f"{fruit_to_check} is {fruit_colors[fruit_to_check]}")
else:
    print(f"{fruit_to_check} not found")
