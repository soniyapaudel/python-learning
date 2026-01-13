""" Create a calculator capable of performing addition, subtraction, multiplication and division
operation on two numbers. Your program should format the output in a readable manner 
 """

num1 = float(input("Enter the first number:"))
print(num1)
num2 = float(input("Enter the Second number"))
print(num2)

print("\nSelect Operation:")

print("1. Add")
print("2. Subtract" )
print("3. Multiply")
print("4. Divide")
print("5. Exponential ")
print("6. Modulus")
print("7. Floor Division")

add = num1 + num2 
subtract = num1 -num2 
multiply = num1 * num2 
divide = num1 / num2 
exponential = num1 ** num2 
modulus = num1 % num2 
floor_division = num1 // num2 

print("\n Result ")
print("Adiition of two numbers: ", add)
print("Subtraction of two numbers:", subtract)
print("Multiplication of two numbers:", multiply )
print("Division of two numbers:", divide)
print("Exponential of two numbers:", exponential )
print("Modulus of two numbers:", modulus)
print("Floor Division of two numbers:", floor_division)
