class Calculator:

    def __init__(self, number1,number2):
        self.number1 = number1
        self.number2 = number2

    def addition(number1,number2):
        return number1 + number2
        

    def subtraction(number1,number2):
        return number1 - number2

    def multiplication(number1,number2):
        return number1 * number2

    def division(number1,number2):
        return number1 / number2


    def modulusDivision(number1,number2):
        return number1 % number2                           #use % as operator

operation = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulous Division\nPlease enter a number for the operation you would like to perform: ")
number1 = int(input("Please enter in your first number:"))
number2 = int(input("Please enter in your second number:"))

if operation.lower() == "1" or "Addition":
    print("The sum of",number1,"and", number2, "is", Calculator.addition(number1,number2))
elif operation == "2":
    print("The sum of",number1,"and", number2, "is", Calculator.addition(number1,number2))
elif operation == "2":
    print("The sum of",number1,"and", number2, "is", Calculator.addition(number1,number2))
elif operation == "2":
    print("The sum of",number1,"and", number2, "is", Calculator.addition(number1,number2))
elif operation == "2":
    print("The sum of",number1,"and", number2, "is", Calculator.addition(number1,number2))
else:
    print("invalid input. Please retry while choosing one of the available numbers")
    
