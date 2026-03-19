# Version 2 Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    raise ValueError('Error: Division by zero')

# Example usage
if __name__ == '__main__':
    print(add(1, 2))
    print(subtract(5, 2))
    print(multiply(3, 4))
    print(divide(10, 2))