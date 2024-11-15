import random

print("Welcom to the Banker Roulette \nWho will pay the bill?")

names_input = input(
    "Please enter the names of the people who will be paying the bill, separated by a comma: \n"
)

names = names_input.split(", ")
print(names)

print(names[random.randint(0, len(names) - 1)] + " will pay the bill")
