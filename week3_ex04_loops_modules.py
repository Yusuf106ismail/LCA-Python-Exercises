import random
import math_operations


# Question 1: Using a for loop with a list

fruits = ["apple", "banana", "orange", "grape"]

for fruit in fruits:
    print(fruit)


# Question 2: Using a while loop for countdown

count = 5
while count >= 1:
    print(count)
    count -= 1


# Question 3: Using a for loop with range()

for i in range(1, 11):
    print(i * i)


# Question 4: Using the random module

colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(3):
    print(random.choice(colors))


# Question 5: Using a custom module

print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
print(math_operations.multiply(10, 5))
print(math_operations.divide(10, 5))


# Simple calculator using while loop

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", math_operations.add(num1, num2))
    elif operation == "-":
        print("Result:", math_operations.subtract(num1, num2))
    elif operation == "*":
        print("Result:", math_operations.multiply(num1, num2))
    elif operation == "/":
        print("Result:", math_operations.divide(num1, num2))
    else:
        print("Invalid operation")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        break
