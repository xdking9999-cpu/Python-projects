# Version 3 Calculator with Error Handling

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        raise ValueError('Error: Division by zero')

# Example usage
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.subtract(5, 2))
    print(calc.multiply(3, 4))
    print(calc.divide(10, 2))