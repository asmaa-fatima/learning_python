import calculator_logo

print(calculator_logo.logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1/n2 


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

number1 = int(input("Enter the first number \n"))

for symbol in operations:
    print(symbol)

choosen_operation = input("Select an operation: ")
number2 = int(input("Enter the secound number: \n"))



calculation_function = operations[choosen_operation]
answer1 = calculation_function(number1, number2)

# answer = calculation_function ????

# answer = operations[choosen_operation](number1, number2)

print(f"{number1} {choosen_operation} {number2} = {answer1}")

choosen_operation = input("Choose another Operation : \n")
number3 = int(input("Enter the number: \n"))

calculation_function = operations[choosen_operation]
answer2 = calculation_function[answer, number3]

print(f"{answer1} {choosen_operation} {number3} = {answer2}")

