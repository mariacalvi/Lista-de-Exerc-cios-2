import random

def generate_random_number():
    random_number = random.randint(1, 10)
    return random_number

random_number = generate_random_number()
print("Random number between 1 and 10:", random_number)
