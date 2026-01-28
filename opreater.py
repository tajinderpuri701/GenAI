#
name = input("Enter student name: ")
student_class = input("Enter class: ")
section = input("Enter section: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100  

print("\n----- Student Result -----")
print("Name:", name)
print("Class:", student_class)
print("Section:", section)
print("Percentage:", percentage, "%")

#

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
total = a + b + c
print("Sum =", total)

# 
num = float(input("Enter a number: "))
square = num ** 2
print("Square of", num, "is", square)

#

celsius_str = input("Enter temperature in Celsius: ")
celsius = float(celsius_str)
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature: {celsius}°C = {fahrenheit}°F")

#

num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor): "))
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
  
    quotient = num1 // num2
    remainder = num1 % num2

    print(f"Quotient = {quotient}")
    print(f"Remainder = {remainder}")


#
P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of interest (R) in %: "))
T = float(input("Enter Time period (T) in years: "))

SI = (P * R * T) / 100

print(f"Simple Interest = {SI}")

