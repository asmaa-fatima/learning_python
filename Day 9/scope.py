
animals = 2

def increase_animals():
    global animals
    animals += 1
    print(f"the increase animal is {animals}")

increase_animals()

print(animals)