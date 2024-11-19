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

def calculator():
    number1 = float(input("Enter the first number \n"))

    for symbol in operations:
        print(symbol)

    end_calculation = False

    while not end_calculation:
        choosen_operation = input("Select an operation: ")
        number2 = float(input("What's the next number \n"))
        calculation_function = operations[choosen_operation]
        answer = calculation_function(number1, number2)
        print(f"{number1} {choosen_operation} {number2} = {answer}")
        continue_calculation = input("Type 'y' to continue calculation with: ").lower()
        if continue_calculation == 'y':
            number1 = answer
        else:
            end_calculation = True
            calculator()

calculator()




# answer = calculation_function ????

# answer = operations[choosen_operation](number1, number2)



# choosen_operation = input("Choose another Operation : \n")
# number3 = int(input("Enter the number: \n"))

# calculation_function = operations[choosen_operation]
# answer2 = calculation_function(answer1, number3)

# print(f"{answer1} {choosen_operation} {number3} = {answer2}")

