import math


print("  Welcome To Calculator  ")
print("For Adding '+' \nSubtract '-' \nMultiply '*' \nDivid '/' \nResult '=' \nPower '^' \nRoot 'sqrt'")
S = None

while True:
    
    j = input("\nEnter operator:")
    
    if j == "=":
        print("Result is:",S)
        break
    elif j == "sin":
        if S is None:
            print("Enter a number first")
        else:
            rad = math.radians(S)
            print("Converting to radians..........")
            S = math.sin(rad)
            
        
        
    
    try:
        i = float(input("Enter a number: "))
    except ValueError:
        print("Invalid number ❌")
        continue
    
    if S is None:
        S = i
        continue
    
    if j == "+":
        S += i
        
    elif j == "-":
        S -= i 
    
    elif j == "*":
        S *= i
        
    elif j == "/":
        if i == 0:
            print("Divisible by zero is not define........")
        else:   
            S /= i
    
    elif j == "^":
        n = float(input("Enter the power:"))
        S = i ** n
        
    elif j == "sqrt":
        if S is None:
            S = float(input("Enter a number to be rooted:"))
        elif S < 0:
            print("Negetive cannot be rooted.......")
        else:
            S = math.sqrt(S)
    elif j == "sin":
        if S is None:
            print("Enter a number first")
        else:
            rad = math.radians(S)
            print("Converting to radians..........")
            S = math.sin(rad)
            
    
        
    else:
        print("Invalid enter ..... ")