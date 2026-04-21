# ask the user for their name
name = input ("Enter your name")
#ask the user for their age
age = input (" Enter your age ")
#print a greeting
print(" Hello" + name + "you are" + age + " years old ")
#ask for length and width ( convert to integers )
length = int ( input( "Enter the length of the rectangle: "))
width = int ( input("Enter the width of the rectangle: "))

#calculate area
area = length * width

#print result
print("The area of the rectangle is:",area)

#ask for temperature in Celsius
celsius = float ( input (" Enter temperature in celsius:"))

#convert to fahrenheit
Fahrenheit = ( celsius * 9/5) + 32

#print to result rounded to 2 decimal places
print (" Temperature in Fahrenheit: ", round (Fahrenheit ,2))

