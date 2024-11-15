# def greetings(name, genre):
#   print(f"Hello {name}!")
#   print(f"Why do you like {genre}?")


# greetings(name=input("What is your name? "),
#           genre=input("Which genre do you like? "))


# Prime Numbers

def prime_number(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
      break
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input("Enter Prime number: "))
prime_number(number=n)