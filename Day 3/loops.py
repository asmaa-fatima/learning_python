# print("this is Loops")

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(fruit)

#Average height using for loop

# student_heights = input("Input a list of student heights \n").split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0

# for height in student_heights:
#   total_height += height

# average_height = total_height/(len(student_heights))

# print(f"Average height is {average_height}.")

#Highest score using for loop

# student_scores = input("Input a list of student scores \n").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# print(student_scores)

# highest_score = 0

# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print(f"The highest score in the class is: {highest_score}")


#Sum of even numbers using for loop

total = 0

for n in range(2, 101, 2):
  total += n

print(total)