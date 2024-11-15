# print("Lists")

# students = ["Maya", "Carol", "Jessica"]

# print(students)

# students.append("James")

# print(students)

# print(students[4])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# print(dirty_dozen[0][3])

row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = position[0]
row = position[1]

map[int(row) - 1][int(column) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
