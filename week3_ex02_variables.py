#Question 1 : Arithmetic and Assignment Operators

x=10
y=5

#Add 3 to x
x +=3

#Multiply y by 2
y *=2

#Divide x by y
result = x/y

#Print result
print ("Result:", result)

#Question 2 : Comparison and Logical Operators

a = 8
b = 4
c = 6

#Conditions
Conditions1 = a>b
Conditions2 = b%2 == 0
Conditions3 = c<=a

#Final Condition
final_condition = Conditions1 or ( Conditions2 and Conditions3 )

#Print result
print ("fonal condition:", final_condition)

#Question 3 : Conditional Statements

#Get user input
score = int(input("Enter your test score(0-100):"))

#Grading System
if score>=90 :
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print grade
print("Your grade is:", grade)

#Question 4 : Combining Operators and Conditionals

#Get inputs

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

# Print Result
print("Result:", result)
    
    




