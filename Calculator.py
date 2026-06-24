# Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter +,-,*,/: ")
def calculator(a,b):
    if(c == "+"):
        return a+b
    if(c == "-"):
        return a-b
    if(c == "*"):
        return a*b
    if(c == "/"):
        return a/b

print(calculator(a,b))
        