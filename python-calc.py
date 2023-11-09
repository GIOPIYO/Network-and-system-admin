print("Welcome to the simple calculator")
operation=print("Enter: \n a for addition \n s for subtraction \n m for multiplication \n d for division \n r to find remainder")
operate=input().lower()
a=int(input("Enter the first number: "))
b=int(input("enter the second number: "))

def addition(a,b):
    add=a+b
    print(add)
def subtraction(a,b):
    sub=a-b
    print(sub)  
def multiplication(a,b):
    multi=a*b
    print(multi)
def division(a,b):
    div=a/b
    print(div)    
def remainder(a,b):
    rem=a%b
    print(rem)    

if operate == "a":
   addition(a,b)
elif operate == "s":
    subtraction(a,b)
elif operate == "m":
    multiplication(a,b)
elif operate == "d":
    division(a,b)
elif operate == "r":
    remainder(a,b)
else:
    print("Invalid operation selected")