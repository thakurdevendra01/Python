def greet():    #function
   print("Hello World!")
greet()

def add(a,b):   #function with argument
    return a+b
print(add(2,3))

def add(a,b=6): #default value
    return a+b
print(add(2))